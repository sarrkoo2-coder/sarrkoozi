import os
import logging
import re
from dataclasses import dataclass
from typing import List, Optional

import asyncpg
from aiocache import cached, Cache
from aiocache.serializers import PickleSerializer
from dotenv import load_dotenv

from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    Application, CommandHandler, MessageHandler, ConversationHandler,
    filters, ContextTypes
)

# =================== НАСТРОЙКА ЛОГИРОВАНИЯ ===================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

# =================== ЗАГРУЗКА ПЕРЕМЕННЫХ ОКРУЖЕНИЯ ===================
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_USER_ID = os.getenv("ADMIN_USER_ID")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set in environment")
if not ADMIN_USER_ID:
    raise RuntimeError("ADMIN_USER_ID is not set in environment")

# Конфигурация базы данных
DB_CONFIG = {
    "database": os.getenv("DB_NAME", "courier_bot"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", ""),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "5432")),
}

# Глобальные объекты пула и кэша
pool: Optional[asyncpg.Pool] = None
cache: Optional[Cache] = None

# =================== МОДЕЛЬ ДАННЫХ ===================
@dataclass
class CourierApplication:
    user_id: int
    username: str  # Реальный ник Telegram
    name: str
    age: int
    courier_type: str
    phone: str
    city: str
    schedule: str
    tg_nick_submitted: str  # Введённый пользователем ник

# =================== ЛОКАЛИЗАЦИЯ И ВАРИАНТЫ ===================
TYPE_CHOICES_LANG = {
    "ru": ["Пеший 🚶", "Вело 🚴", "Авто 🚗"],
    "kk": ["Жаяу 🚶", "Вело 🚴", "Авто 🚗"],
    "uz": ["Piyoda 🚶", "Velo 🚴", "Avto 🚗"],
    "tj": ["Пиёда 🚶", "Вело 🚴", "Авто 🚗"],
}

L = {
    "ru": {
        "lang_prompt": "Выберите язык 🌐:",
        "langs": ["Русский", "Қазақша", "O‘zbekcha", "Тоҷикӣ"],
        "start": "Привет! 👋 Я бот для приёма заявок курьеров. Давайте начнём 🚀",
        "ask_name": "Как вас зовут? (Имя/ФИО) ✍️",
        "ask_age": "Сколько вам лет? Введите число, например 23 🔢",
        "age_invalid": "Возраст должен быть числом от 16 до 80. Попробуйте снова ⚠️",
        "ask_type": "Выберите тип курьера или введите свой вариант 🛵",
        "ask_phone": "Укажите контактный телефон в формате +7XXXXXXXXXX (только цифры и +) 📞",
        "phone_invalid": "Некорректный номер. Допустим формат: +77001234567 ❌",
        "ask_city": "Укажите ваш город 🏙️",
        "ask_schedule": "Укажите желаемый график (например: полный день, частичный, смены) 🗓️",
        "ask_tg_username": "Укажите ваш никнейм в Telegram (латиница, цифры, подчёркивание). Можно с @ 📧",
        "username_invalid": "Некорректный никнейм. Пример: @my_courier1 ⚠️",
        "saved": "Спасибо! Ваша заявка принята ✅",
        "summary": "Данные:\n• Имя: {name}\n• Возраст: {age}\n• Тип: {ctype}\n• Телефон: {phone}\n• Город: {city}\n• График: {schedule}\n• Ник (введённый): {nick}\n• Ваш TG: @{real} (id {uid})",
        "admin_notify": "🔔 Новая заявка:\n• Имя: {name}\n• Возраст: {age}\n• Тип: {ctype}\n• Телефон: {phone}\n• Город: {city}\n• График: {schedule}\n• Ник (введённый): {nick}\n• TG профиля: @{real} (id {uid})",
        "no_rights": "Недостаточно прав 🔒",
        "list_empty": "Пока нет заявок 🗂️",
        "list_title": "Заявки 📋:",
        "cancel": "Диалог отменён ❌",
    },
    "kk": {
        "lang_prompt": "Тілді таңдаңыз 🌐:",
        "langs": ["Русский", "Қазақша", "O‘zbekcha", "Тоҷикӣ"],
        "start": "Сәлем! 👋 Мен курьерлердің өтініштерін қабылдайтын ботпын. Бастайық 🚀",
        "ask_name": "Атыңыз кім? (Аты/Т.А.Ә.) ✍️",
        "ask_age": "Жасыңыз қанша? Мысалы, 23 🔢",
        "age_invalid": "Жас 16-80 аралығында сан болуы керек. Қайта көріңіз ⚠️",
        "ask_type": "Курьер түрін таңдаңыз немесе өз нұсқаңызды жазыңыз 🛵",
        "ask_phone": "Байланыс телефонын көрсетіңіз: +7XXXXXXXXXX 📞",
        "phone_invalid": "Нөмір қате. Мысал: +77001234567 ❌",
        "ask_city": "Қай қаладасыз? 🏙️",
        "ask_schedule": "Қалаған жұмыс кестесі (мысалы: толық күн, жартылай, ауысым) 🗓️",
        "ask_tg_username": "Telegram лақап атыңызды жазыңыз. @ қоюға болады 📧",
        "username_invalid": "Жарамсыз лақап ат. Мысал: @my_courier1 ⚠️",
        "saved": "Рахмет! Өтінішіңіз қабылданды ✅",
        "summary": "Мәліметтер:\n• Аты: {name}\n• Жасы: {age}\n• Түрі: {ctype}\n• Телефон: {phone}\n• Қала: {city}\n• Кесте: {schedule}\n• Енгізілген ник: {nick}\n• Сіздің TG: @{real} (id {uid})",
        "admin_notify": "🔔 Жаңа өтініш:\n• Аты: {name}\n• Жасы: {age}\n• Түрі: {ctype}\n• Телефон: {phone}\n• Қала: {city}\n• Кесте: {schedule}\n• Енгізілген ник: {nick}\n• Профиль TG: @{real} (id {uid})",
        "no_rights": "Құқығыңыз жеткіліксіз 🔒",
        "list_empty": "Әзірге өтініш жоқ 🗂️",
        "list_title": "Өтініштер 📋:",
        "cancel": "Сұхбат тоқтатылды ❌",
    },
    "uz": {
        "lang_prompt": "Tilni tanlang 🌐:",
        "langs": ["Русский", "Қазақша", "O‘zbekcha", "Тоҷикӣ"],
        "start": "Salom! 👋 Bu bot kuryer arizalarini qabul qiladi. Boshlaymiz 🚀",
        "ask_name": "Ismingiz kim? (F.I.Sh.) ✍️",
        "ask_age": "Yoshingiz nechida? Masalan, 23 🔢",
        "age_invalid": "Yosh 16-80 oralig‘ida bo‘lishi kerak. Qayta urinib ko‘ring ⚠️",
        "ask_type": "Kuryer turini tanlang yoki yozing 🛵",
        "ask_phone": "Kontakt telefon raqami: +7XXXXXXXXXX 📞",
        "phone_invalid": "Noto‘g‘ri raqam. Misol: +77001234567 ❌",
        "ask_city": "Qaysi shahardasiz? 🏙️",
        "ask_schedule": "Istalgan ish jadvali (to‘liq, qisman, smenali) 🗓️",
        "ask_tg_username": "Telegram nikneymingizni kiriting. @ bilan bo‘lishi mumkin 📧",
        "username_invalid": "Noto‘g‘ri nik. Misol: @my_courier1 ⚠️",
        "saved": "Rahmat! Arizangiz qabul qilindi ✅",
        "summary": "Ma'lumotlar:\n• Ism: {name}\n• Yosh: {age}\n• Turi: {ctype}\n• Telefon: {phone}\n• Shahar: {city}\n• Jadval: {schedule}\n• Kiritilgan nik: {nick}\n• Sizning TG: @{real} (id {uid})",
        "admin_notify": "🔔 Yangi ariza:\n• Ism: {name}\n• Yosh: {age}\n• Turi: {ctype}\n• Telefon: {phone}\n• Shahar: {city}\n• Jadval: {schedule}\n• Kiritilgan nik: {nick}\n• TG profil: @{real} (id {uid})",
        "no_rights": "Huquqlar yetarli emas 🔒",
        "list_empty": "Hozircha arizalar yo‘q 🗂️",
        "list_title": "Arizalar 📋:",
        "cancel": "Suhbat bekor qilindi ❌",
    },
    "tj": {
        "lang_prompt": "Забони муколамаро интихоб кунед 🌐:",
        "langs": ["Русский", "Қазақша", "O‘zbekcha", "Тоҷикӣ"],
        "start": "Салом! 👋 Ин бот аризаҳои курьерро қабул мекунад. Оғоз мекунем 🚀",
        "ask_name": "Номи шумо чист? (Ном/Насаб) ✍️",
        "ask_age": "Синну соли шумо чанд аст? Масалан, 23 🔢",
        "age_invalid": "Синну сол бояд 16-80 бошад. Дубора кӯшиш кунед ⚠️",
        "ask_type": "Навъи курьерро интихоб кунед ё нависед 🛵",
        "ask_phone": "Рақами телефон: +XXXXXXXXXXX 📞",
        "phone_invalid": "Рақами нодуруст. Масалан: +77001234567 ❌",
        "ask_city": "Шаҳри шумо? 🏙️",
        "ask_schedule": "Ҷадвали корӣ (пурра, қисман, навбатдор) 🗓️",
        "ask_tg_username": "Лақаби Telegram-ро ворид кунед. Метавонад бо @ бошад 📧",
        "username_invalid": "Лақаби нодуруст. Масалан: @my_courier1 ⚠️",
        "saved": "Ташаккур! Ариза қабул шуд ✅",
        "summary": "Маълумот:\n• Ном: {name}\n• Син: {age}\n• Навъ: {ctype}\n• Телефон: {phone}\n• Шаҳр: {city}\n• Ҷадвал: {schedule}\n• Лақаби воридшуда: {nick}\n• TG-и шумо: @{real} (id {uid})",
        "admin_notify": "🔔 Аризаи нав:\n• Ном: {name}\n• Син: {age}\n• Навъ: {ctype}\n• Телефон: {phone}\n• Шаҳр: {city}\n• Ҷадвал: {schedule}\n• Лақаби воридшуда: {nick}\n• TG профил: @{real} (id {uid})",
        "no_rights": "Ҳуқуқ кофӣ нест 🔒",
        "list_empty": "Ҳоло аризаҳо нест 🗂️",
        "list_title": "Аризаҳо 📋:",
        "cancel": "Муколама бекор шуд ❌",
    },
}

LANG_KEYBOARD = [["Русский", "Қазақша"], ["O‘zbekcha", "Тоҷикӣ"]]

# =================== УТИЛИТЫ ВАЛИДАЦИИ ===================
age_re = re.compile(r"^\d{1,3}$")
phone_re = re.compile(r"^\+\d{7,15}$")
username_re = re.compile(r"^@?[A-Za-z0-9_]{5,32}$")

def normalize_username(s: str) -> str:
    s = s.strip()
    if not s:
        return s
    return s if s.startswith("@") else "@" + s

def get_lang_code(lang_button: str) -> str:
    if lang_button == "Русский":
        return "ru"
    if lang_button == "Қазақша":
        return "kk"
    if lang_button == "O‘zbekcha":
        return "uz"
    if lang_button == "Тоҷикӣ":
        return "tj"
    return "ru"

# =================== СОСТОЯНИЯ ДИАЛОГА ===================
(
    CHOOSE_LANG,
    ASK_NAME,
    ASK_AGE,
    ASK_TYPE,
    ASK_PHONE,
    ASK_CITY,
    ASK_SCHEDULE,
    ASK_TG_USERNAME,
) = range(8)

# =================== БД И КЭШ ===================
async def init_db(application: Application):
    """Инициализация пула БД и кэша."""
    global pool, cache
    try:
        pool = await asyncpg.create_pool(**DB_CONFIG)
        async with pool.acquire() as conn:
            await conn.execute("""
                CREATE TABLE IF NOT EXISTS applications (
                    user_id BIGINT PRIMARY KEY,
                    username TEXT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    courier_type TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    city TEXT NOT NULL,
                    schedule TEXT NOT NULL,
                    tg_nick_submitted TEXT NOT NULL
                )
            """)
        cache = Cache(Cache.MEMORY, serializer=PickleSerializer())
        logger.info("Database and cache initialized successfully.")
    except Exception as e:
        logger.error(f"Failed to initialize database or cache: {e}", exc_info=True)
        raise

@cached(ttl=60)
async def get_applications() -> List[CourierApplication]:
    """Получает заявки из БД с кешированием."""
    if pool is None:
        logger.error("Database pool is not initialized.")
        return []
    async with pool.acquire() as conn:
        rows = await conn.fetch("""
            SELECT user_id, username, name, age, courier_type, phone, city, schedule, tg_nick_submitted
            FROM applications
            ORDER BY user_id DESC
        """)
        return [
            CourierApplication(
                user_id=row["user_id"],
                username=row["username"],
                name=row["name"],
                age=row["age"],
                courier_type=row["courier_type"],
                phone=row["phone"],
                city=row["city"],
                schedule=row["schedule"],
                tg_nick_submitted=row["tg_nick_submitted"],
            )
            for row in rows
        ]

async def save_application(app: CourierApplication):
    """Сохраняет заявку в БД."""
    if pool is None:
        logger.error("Database pool is not initialized. Cannot save application.")
        return
    async with pool.acquire() as conn:
        await conn.execute(
            """
            INSERT INTO applications (
                user_id, username, name, age, courier_type, phone, city, schedule, tg_nick_submitted
            ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
            ON CONFLICT (user_id) DO UPDATE SET
                username = EXCLUDED.username,
                name = EXCLUDED.name,
                age = EXCLUDED.age,
                courier_type = EXCLUDED.courier_type,
                phone = EXCLUDED.phone,
                city = EXCLUDED.city,
                schedule = EXCLUDED.schedule,
                tg_nick_submitted = EXCLUDED.tg_nick_submitted
            """,
            app.user_id,
            app.username,
            app.name,
            app.age,
            app.courier_type,
            app.phone,
            app.city,
            app.schedule,
            app.tg_nick_submitted,
        )
    # Сброс кеша после сохранения
    try:
        if hasattr(get_applications, "cache") and get_applications.cache:
            await get_applications.cache.clear()
    except Exception as e:
        logger.warning(f"Failed to clear cache after save: {e}")

async def post_shutdown(application: Application):
    """Вызывается при завершении работы бота."""
    global pool, cache
    if pool:
        await pool.close()
        logger.info("Database pool closed.")
    if cache:
        await cache.close()
        logger.info("Cache closed.")

# =================== ХЕНДЛЕРЫ ДИАЛОГА ===================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    kb = ReplyKeyboardMarkup(LANG_KEYBOARD, resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text(L["ru"]["lang_prompt"], reply_markup=kb)
    return CHOOSE_LANG

async def choose_lang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    choice = (update.message.text or "").strip()
    lang = get_lang_code(choice)
    context.user_data["lang"] = lang
    msgs = L[lang]

    await update.message.reply_text(
        msgs["start"] + "\n\n" + msgs["ask_name"],
        reply_markup=ReplyKeyboardRemove()
    )
    return ASK_NAME

async def ask_age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "ru")
    msgs = L[lang]

    name = (update.message.text or "").strip()
    if not name:
        await update.message.reply_text(msgs["ask_name"])
        return ASK_NAME

    context.user_data["name"] = name
    await update.message.reply_text(msgs["ask_age"])
    return ASK_AGE

async def ask_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "ru")
    msgs = L[lang]

    age_text = (update.message.text or "").strip()
    if not age_re.match(age_text):
        await update.message.reply_text(msgs["age_invalid"])
        return ASK_AGE

    age = int(age_text)
    if age < 16 or age > 80:
        await update.message.reply_text(msgs["age_invalid"])
        return ASK_AGE

    context.user_data["age"] = age
    kb = ReplyKeyboardMarkup(
        [[t] for t in TYPE_CHOICES_LANG.get(lang, TYPE_CHOICES_LANG["ru"])],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await update.message.reply_text(msgs["ask_type"], reply_markup=kb)
    return ASK_TYPE

async def ask_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "ru")
    msgs = L[lang]

    courier_type = (update.message.text or "").strip()
    if not courier_type:
        kb = ReplyKeyboardMarkup(
            [[t] for t in TYPE_CHOICES_LANG.get(lang, TYPE_CHOICES_LANG["ru"])],
            resize_keyboard=True,
            one_time_keyboard=True
        )
        await update.message.reply_text(msgs["ask_type"], reply_markup=kb)
        return ASK_TYPE

    context.user_data["courier_type"] = courier_type
    await update.message.reply_text(msgs["ask_phone"], reply_markup=ReplyKeyboardRemove())
    return ASK_PHONE

async def ask_city(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "ru")
    msgs = L[lang]

    phone = (update.message.text or "").strip()
    if not phone_re.match(phone):
        await update.message.reply_text(msgs["phone_invalid"])
        return ASK_PHONE

    context.user_data["phone"] = phone
    await update.message.reply_text(msgs["ask_city"])
    return ASK_CITY

async def ask_schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "ru")
    msgs = L[lang]

    city = (update.message.text or "").strip()
    if not city:
        await update.message.reply_text(msgs["ask_city"])
        return ASK_CITY

    context.user_data["city"] = city
    await update.message.reply_text(msgs["ask_schedule"])
    return ASK_SCHEDULE

async def ask_tg_username(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "ru")
    msgs = L[lang]

    schedule = (update.message.text or "").strip()
    if not schedule:
        await update.message.reply_text(msgs["ask_schedule"])
        return ASK_SCHEDULE

    context.user_data["schedule"] = schedule
    await update.message.reply_text(msgs["ask_tg_username"])
    return ASK_TG_USERNAME

async def finish(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "ru")
    msgs = L[lang]

    nick = (update.message.text or "").strip()
    if not username_re.match(nick):
        await update.message.reply_text(msgs["username_invalid"])
        return ASK_TG_USERNAME

    nick_norm = normalize_username(nick)
    user = update.effective_user

    app_data = {
        "user_id": user.id,
        "username": user.username or "",
        "name": context.user_data.get("name", ""),
        "age": int(context.user_data.get("age", 0)),
        "courier_type": context.user_data.get("courier_type", ""),
        "phone": context.user_data.get("phone", ""),
        "city": context.user_data.get("city", ""),
        "schedule": context.user_data.get("schedule", ""),
        "tg_nick_submitted": nick_norm,
    }

    # Проверка на наличие всех данных
    required_keys = ["name", "age", "courier_type", "phone", "city", "schedule"]
    if not all(app_data.get(k) for k in required_keys):
        await update.message.reply_text("Произошла ошибка: не все данные были собраны. Пожалуйста, начните заново с /start.")
        return ConversationHandler.END

    application_obj = CourierApplication(**app_data)

    try:
        await save_application(application_obj)
        logger.info(f"Application saved for user {application_obj.user_id}")
    except Exception as e:
        logger.error(f"Error saving application for user {application_obj.user_id}: {e}", exc_info=True)
        await update.message.reply_text("Произошла ошибка при сохранении заявки. Пожалуйста, попробуйте еще раз или свяжитесь с администратором.")
        return ConversationHandler.END

    # Сообщение пользователю
    summary_text = msgs["summary"].format(
        name=application_obj.name,
        age=application_obj.age,
        ctype=application_obj.courier_type,
        phone=application_obj.phone,
        city=application_obj.city,
        schedule=application_obj.schedule,
        nick=application_obj.tg_nick_submitted,
        real=(application_obj.username or "—"),
        uid=application_obj.user_id,
    )
    await update.message.reply_text(
        msgs["saved"] + "\n\n" + summary_text,
        reply_markup=ReplyKeyboardRemove()
    )

    # Уведомление админу
    try:
        admin_text = msgs["admin_notify"].format(
            name=application_obj.name,
            age=application_obj.age,
            ctype=application_obj.courier_type,
            phone=application_obj.phone,
            city=application_obj.city,
            schedule=application_obj.schedule,
            nick=application_obj.tg_nick_submitted,
            real=(application_obj.username or "—"),
            uid=application_obj.user_id,
        )
        await context.bot.send_message(chat_id=ADMIN_USER_ID, text=admin_text)
        logger.info(f"Admin notified about new application from {application_obj.user_id}")
    except Exception as e:
        logger.warning(f"Failed to notify admin about application from {application_obj.user_id}: {e}")

    # Очистка состояния и завершение диалога
    context.user_data.clear()
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "ru")
    msgs = L[lang]
    context.user_data.clear()
    await update.message.reply_text(msgs["cancel"], reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

async def list_apps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msgs = L["ru"]

    if update.effective_user.id != ADMIN_USER_ID:
        user_lang = context.user_data.get("lang", "ru")
        await update.message.reply_text(L[user_lang]["no_rights"])
        return

    applications = await get_applications()
    if not applications:
        await update.message.reply_text(msgs["list_empty"])
        return

    lines = []
    for i, app in enumerate(applications, start=1):
        summary = msgs["summary"].format(
            name=app.name,
            age=app.age,
            ctype=app.courier_type,
            phone=app.phone,
            city=app.city,
            schedule=app.schedule,
            nick=app.tg_nick_submitted,
            real=(app.username or "—"),
            uid=app.user_id,
        )
        lines.append(f"*{i}*.\n{summary}")

    full_text = msgs["list_title"] + "\n\n" + "\n\n".join(lines)
    for i in range(0, len(full_text), 4096):
        await update.message.reply_text(full_text[i:i + 4096], parse_mode='Markdown')

# =================== РЕГИСТРАЦИЯ И ЗАПУСК ===================
if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).post_init(init_db).post_shutdown(post_shutdown).build()

    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHOOSE_LANG: [MessageHandler(filters.TEXT & ~filters.COMMAND, choose_lang)],
            ASK_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_age)],
            ASK_AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_type)],
            ASK_TYPE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_phone)],
            ASK_PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_city)],
            ASK_CITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_schedule)],
            ASK_SCHEDULE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_tg_username)],
            ASK_TG_USERNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, finish)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        allow_reentry=True,
    )

    app.add_handler(conv)
    app.add_handler(CommandHandler("list", list_apps))

    logger.info("Bot is starting...")
    app.run_polling()
