# Business/System Analyst: Automation & Integration Track

Практический курс развития в направлении **Business/System Analyst уровня Junior+ / Middle-track**.

Фокус курса:

- автоматизация бизнес-процессов;
- корпоративные системы;
- требования и трассируемость;
- BPMN и UML;
- системный контекст и C4;
- ERD, PostgreSQL и расширенный SQL;
- HTTP, REST, JSON, OpenAPI и Postman;
- webhooks, mapping и интеграционные паттерны;
- NFR, безопасность, аудит и observability;
- тестирование, UAT, migration, release и rollback;
- небольшой работающий прототип на n8n, FastAPI, PostgreSQL и Telegram.

## Позиционирование

Курс рассчитан на специалиста, у которого уже есть опыт автоматизации, Bitrix24, AS-IS/TO-BE, API, SQL, n8n и взаимодействия с подразделениями.

Он не гарантирует автоматическое достижение уровня Middle. Цель — систематизировать существующую практику, расширить её в сторону системного и интеграционного анализа, собрать доказательное портфолио и определить дальнейший разрыв до Middle.

## Формат

- Подготовительный этап: **Week 0**.
- Основная программа: **16 недель**.
- Нагрузка: **8–10 часов в неделю**.
- Соотношение: **30% теории и 70% практики**.
- Сквозной кейс: интеграционная система обработки обращений **NovaDesk**.
- Рабочая среда: GitHub + сквозные Jira/Confluence.

## NovaDesk

NovaDesk принимает обращения из email, Telegram, веб-формы и CRM. В ходе курса проектируются единый intake, нормализация данных, дедупликация, статусная модель, SLA, CRM-синхронизация, API/webhooks, аудит, мониторинг, тестирование и безопасный релиз.

## Карта курса

| Week | Тема |
|---:|---|
| 0 | Диагностика и рабочий контур |
| 1 | Problem, Goals, KPI, Scope |
| 2 | Stakeholders и Elicitation |
| 3 | Requirements Engineering и RTM |
| 4 | User Stories, UML Use Cases, State Machine, Business Rules |
| 5 | BPMN AS-IS |
| 6 | BPMN TO-BE, SLA и Exceptions |
| 7 | System Context и C4 Architecture |
| 8 | ERD и Data Dictionary |
| 9 | SQL Fundamentals |
| 10 | JOIN, CTE, Window Functions и Data Quality |
| 11 | REST API, OpenAPI и Postman |
| 12 | Integrations, Sequence Diagrams и Mapping |
| 13 | NFR, Security, Audit, Logging и Monitoring |
| 14 | Testing, UAT, Migration, Release и Rollback |
| 15 | Automation Prototype |
| 16 | Final Project, Portfolio и Interview |

## С чего начать

1. Прочитать [`COURSE.md`](COURSE.md).
2. Завершить Week 0 и заполнить [`SKILLS_MATRIX.md`](SKILLS_MATRIX.md).
3. Для каждой недели создавать Jira task и Confluence page.
4. Складывать финальные версии в GitHub по структуре [`CAPSTONE.md`](CAPSTONE.md).
5. Обновлять [`PROGRESS.md`](PROGRESS.md) и `data/progress.csv`.
6. После обновления CSV запускать:

```bash
python3 scripts/progress.py
```

## Критерий завершения

- завершён Week 0 и обязательные Week 1–16;
- средняя оценка не ниже 70/100;
- обязательные артефакты собраны и связаны через RTM;
- прототип работает end-to-end в ограниченном scope;
- проект можно защитить за 10–12 минут;
- сформулирован реалистичный дальнейший план развития.

## Факультативы

Обязательная программа не зависит от Power BI, ELMA365 или BPMSoft. Они перенесены в [`FACULTATIVES.md`](FACULTATIVES.md), куда также добавлен трек по AI-автоматизации.

## Структура

- [`COURSE.md`](COURSE.md) — детальная программа;
- [`CAPSTONE.md`](CAPSTONE.md) — итоговый проект и структура портфолио;
- [`FACULTATIVES.md`](FACULTATIVES.md) — Power BI, BPM/low-code и AI Automation;
- [`SKILLS_MATRIX.md`](SKILLS_MATRIX.md) — матрица компетенций;
- [`PROGRESS.md`](PROGRESS.md) — правила оценки;
- [`data/progress.csv`](data/progress.csv) — трек динамики;
- [`templates/`](templates/) — шаблоны аналитических артефактов.