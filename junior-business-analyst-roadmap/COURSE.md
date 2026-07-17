# Business/System Analyst: Automation & Integration Track

Практический 16-недельный курс развития в направлении **Business/System Analyst уровня Junior+ / Middle-track** с фокусом на автоматизацию бизнес-процессов, корпоративные системы, данные и интеграции.

Курс не гарантирует уровень Middle после завершения. Его задача — сформировать системную базу, проектное портфолио и практические навыки, которые позволяют претендовать на Junior+/Strong Junior позиции и последовательно закрывать разрыв до Middle.

## Формат

- Подготовительный этап: **Week 0**.
- Основная программа: **16 недель**.
- Нагрузка: **8–10 часов в неделю**.
- Соотношение: примерно **30% теории и 70% практики**.
- Сквозной проект: интеграционная система обработки обращений **NovaDesk**.
- Рабочая среда: GitHub для версионирования портфолио; Jira и Confluence используются сквозным образом на протяжении курса.

Рекомендуемое распределение времени:

| Работа | Время |
|---|---:|
| Теория и разбор примеров | 2–3 часа |
| Практика | 4–5 часов |
| Оформление артефакта | 1 час |
| Самопроверка и защита решения | 1 час |

## Сквозной кейс NovaDesk

NovaDesk получает клиентские обращения из четырёх источников:

- email;
- Telegram;
- веб-форма;
- CRM.

Сейчас каналы обрабатываются разрозненно. Часть сообщений переносится вручную, идентификаторы обращений не унифицированы, статусы между системами расходятся, SLA контролируется непоследовательно, а повторная доставка события может создать дубль.

В рамках курса необходимо спроектировать целевую интеграционную систему, которая:

1. принимает обращения из разных каналов;
2. нормализует и валидирует данные;
3. создаёт единое обращение и защищается от дублей;
4. синхронизирует ключевые данные с CRM;
5. поддерживает статусную модель и SLA;
6. отправляет уведомления и принимает события через API/webhooks;
7. ведёт аудит, логи и технические метрики;
8. допускает безопасный релиз, миграцию и rollback.

## Сквозное использование Jira и Confluence

Отдельной недели по Jira/Confluence нет. На каждой неделе:

- в Jira создаётся Epic/Story/Task на учебный результат;
- задача связывается с requirement ID или архитектурным решением;
- в Confluence создаётся страница соответствующего артефакта;
- решения фиксируются в Decision Log;
- вопросы и предположения фиксируются в Open Questions / Assumptions Log;
- ссылки на итоговые версии добавляются в GitHub.

Минимальный workflow: `Backlog → Analysis → Review → Rework → Done`.

## Система оценки

После каждого модуля выставляется оценка от 0 до 100:

| Компонент | Вес |
|---|---:|
| Знания | 25% |
| Практическое выполнение | 30% |
| Качество артефакта | 30% |
| Способность объяснить решение | 15% |

```text
Итог = Знания × 0,25
     + Практика × 0,30
     + Артефакт × 0,30
     + Объяснение × 0,15
```

Модуль принимается при результате не ниже 70/100, наличии обязательного артефакта и способности объяснить принятые решения. При результате ниже 70 назначается корректирующая работа.

---

# Week 0. Диагностика и настройка рабочего контура

## Измеримый результат

Определён фактический уровень по бизнес- и системному анализу, создана структура портфолио, настроены GitHub, Jira и Confluence, выбран учебный график.

## Теория

- различия Business Analyst, System Analyst, Integration Analyst и Solution Architect;
- роль аналитика в SDLC;
- уровни требований и архитектурных артефактов;
- Git workflow для аналитической документации;
- базовое место Agile, Scrum и Kanban в delivery-процессе без отдельного углублённого модуля;
- Definition of Ready и Definition of Done для аналитической задачи.

## Профессиональные термины

`Business Analysis`, `System Analysis`, `SDLC`, `Artifact`, `Baseline`, `Repository`, `Commit`, `Issue`, `Definition of Ready`, `Definition of Done`, `Decision Log`.

## Практическое задание

1. Заполнить стартовую матрицу навыков.
2. Описать подтверждаемый опыт в автоматизации, Bitrix24, AS-IS/TO-BE, API, SQL, n8n и взаимодействии с подразделениями — только фактами, без добавления несуществующих обязанностей.
3. Выполнить диагностический кейс NovaDesk: problem statement, 6 stakeholders, 10 вопросов интервью, 9 требований разных типов, 1 Epic, 3 User Stories, текстовый AS-IS и один SQL-запрос.
4. Настроить Jira-проект и Confluence-space NovaDesk.
5. Создать структуру папок портфолио и первый commit.

## Обязательный артефакт

`portfolio/00-baseline.md`, стартовая `SKILLS_MATRIX.md`, ссылки на Jira и Confluence.

## Критерии Done

- диагностика заполнена полностью;
- опыт описан без преувеличений;
- Jira/Confluence настроены;
- учебное расписание зафиксировано;
- первый commit присутствует;
- стартовые пробелы сформулированы конкретно.

## Вопросы для самопроверки

1. Чем Business Analyst отличается от System Analyst?
2. Какие артефакты описывают бизнес, а какие — систему?
3. Что должно быть в DoR аналитической задачи?
4. Почему знакомство с инструментом не равно владению навыком?
5. Как GitHub помогает подтверждать развитие аналитика?

## Типичные ошибки

- занижать или завышать стартовый уровень;
- перечислять инструменты без доказательств применения;
- путать бизнес-анализ с настройкой конкретной системы;
- переносить конфиденциальные данные работодателя;
- считать просмотр материалов завершением модуля.

## Оценка времени

5–7 часов.

---

# Week 1. Проблема, цели, KPI и Scope

## Измеримый результат

Сформулирована подтверждаемая бизнес-проблема NovaDesk, определены цели, KPI, границы продукта и ограничения первой версии.

## Теория

- problem statement и business need;
- симптом, причина и root cause hypothesis;
- outcome и output;
- цели и KPI;
- product/system scope;
- in scope, out of scope, assumptions, constraints, dependencies;
- контекстная диаграмма как ранняя модель границ без преждевременной архитектуры.

## Профессиональные термины

`Problem Statement`, `Business Need`, `Root Cause`, `Outcome`, `Output`, `KPI`, `Scope`, `In Scope`, `Out of Scope`, `Assumption`, `Constraint`, `Dependency`.

## Практическое задание

1. Сформулировать problem statement NovaDesk без выбора технологии.
2. Построить дерево проблем и минимум две root-cause hypotheses.
3. Определить 3–4 цели и минимум 6 KPI: регистрация, первая реакция, доля дублей, SLA compliance, синхронизация CRM, технические ошибки.
4. Описать scope первой версии, явно отделив email, Telegram, web-form и CRM от будущих каналов.
5. Создать список assumptions, constraints и dependencies.
6. Зафиксировать исходные вопросы, на которые пока нет данных.

## Обязательный артефакт

`01-discovery/problem-scope-kpi.md` и простая boundary diagram.

## Критерии Done

- проблема не содержит готового решения;
- KPI измеримы и связаны с целями;
- scope исключает неконтролируемое расширение;
- предположения отделены от фактов;
- ограничения и зависимости не смешаны;
- каждому KPI указан источник данных или способ будущего измерения.

## Вопросы для самопроверки

1. Чем outcome отличается от output?
2. Может ли KPI существовать без источника данных?
3. Почему scope должен включать out-of-scope?
4. Чем constraint отличается от assumption?
5. Как проверить, что problem statement не подменён решением?

## Типичные ошибки

- использовать слова «внедрить» и «разработать» в формулировке проблемы;
- задавать KPI, которые система не сможет измерять;
- включать в MVP все возможные каналы;
- считать гипотезу доказанной причиной;
- смешивать бизнес-цель и системную функцию.

## Оценка времени

8–10 часов.

---

# Week 2. Stakeholders и Requirements Elicitation

## Измеримый результат

Определены заинтересованные стороны, источники требований и проведён структурированный цикл выявления требований по NovaDesk.

## Теория

- stakeholder identification и stakeholder map;
- power/interest matrix;
- RACI и зоны принятия решений;
- интервью, workshop, observation, document analysis, interface analysis;
- открытые, закрытые, уточняющие и проверочные вопросы;
- конфликтующие ожидания;
- фиксация evidence, assumptions и open questions.

## Профессиональные термины

`Stakeholder`, `Sponsor`, `Subject Matter Expert`, `Power/Interest Matrix`, `RACI`, `Elicitation`, `Interview`, `Workshop`, `Observation`, `Evidence`, `Open Question`.

## Практическое задание

1. Создать реестр минимум из 10 stakeholders: клиент, оператор, руководитель поддержки, CRM owner, IT, security, разработчик интеграции, QA, владелец веб-формы, администратор Telegram-бота.
2. Построить power/interest matrix и RACI.
3. Подготовить отдельные гайды интервью для бизнеса, IT и безопасности.
4. Провести четыре симулированных интервью и оформить протоколы.
5. Зафиксировать минимум 8 противоречий или открытых вопросов.
6. Подготовить elicitation plan: источник, техника, ожидаемый результат, owner, deadline.

## Обязательный артефакт

`01-discovery/stakeholder-register.xlsx`, `raci.xlsx`, `elicitation-plan.md`, `interview-notes/`.

## Критерии Done

- у каждого stakeholder указан интерес и влияние;
- вопросы не подталкивают к заранее выбранному решению;
- технические и бизнес-вопросы разделены;
- противоречия не скрыты;
- для открытых вопросов определены owner и срок;
- результаты интервью отражены в Confluence и связаны с Jira.

## Вопросы для самопроверки

1. Почему пользователь системы не всегда является заказчиком?
2. Когда интервью недостаточно и требуется observation?
3. Как фиксировать конфликтующие требования?
4. Чем RACI отличается от stakeholder register?
5. Какие вопросы нельзя считать нейтральными?

## Типичные ошибки

- опрашивать только руководителя;
- принимать мнение stakeholder за факт;
- задавать вопросы о желаемых кнопках вместо процесса и потребности;
- не фиксировать противоречия;
- путать ответственного за процесс и владельца системы.

## Оценка времени

8–10 часов.

---

# Week 3. Requirements Engineering и Traceability

## Измеримый результат

Создан качественный каталог требований NovaDesk и полная начальная трассировка от бизнес-проблемы до проверяемого системного поведения.

## Теория

- уровни BR, stakeholder/user requirements, FR, NFR и transition requirements;
- requirement quality: atomic, unambiguous, feasible, necessary, testable, traceable;
- приоритизация MoSCoW и value/risk;
- атрибуты требования;
- versioning и change control;
- RTM — Requirements Traceability Matrix;
- glossary, assumptions log, decision log;
- связи problem → goal → requirement → design → test.

## Профессиональные термины

`Business Requirement`, `Stakeholder Requirement`, `Functional Requirement`, `Non-functional Requirement`, `Transition Requirement`, `Requirement Attribute`, `Traceability`, `RTM`, `Change Request`, `Baseline`.

## Практическое задание

1. Создать каталог минимум из 35 требований разных уровней.
2. Добавить ID, type, source, rationale, priority, owner, verification method и status.
3. Отдельно зафиксировать минимум 8 NFR-заготовок без детальной проработки — она будет на Week 13.
4. Создать glossary минимум из 30 терминов.
5. Построить RTM, связав проблему, цели, требования и будущие тесты.
6. Провести quality review: найти и переписать минимум 10 слабых требований.
7. Смоделировать один change request и показать влияние на связанные артефакты.

## Обязательный артефакт

`02-requirements/requirements-catalog.xlsx`, `traceability-matrix.xlsx`, `glossary.md`, `change-request-01.md`.

## Критерии Done

- требования атомарны и проверяемы;
- у каждого требования есть источник и rationale;
- RTM не содержит «висячих» обязательных требований;
- NFR не записаны общими словами «быстро» и «безопасно»;
- change request содержит impact analysis;
- каталог имеет версию и baseline.

## Вопросы для самопроверки

1. Чем stakeholder requirement отличается от FR?
2. Что делает требование тестируемым?
3. Для чего RTM нужна после начала разработки?
4. Когда требование следует разделить на несколько?
5. Что должно попасть в impact analysis?

## Типичные ошибки

- писать требования без rationale;
- смешивать несколько функций в одном FR;
- использовать неопределённые слова;
- создавать RTM формально, без реальных связей;
- менять требования без версии и оценки влияния.

## Оценка времени

9–10 часов.

## Checkpoint 1 — после Week 3

Проверяются problem/scope, stakeholders, elicitation, каталог требований и RTM. Мини-интервью включает защиту двух требований, одного конфликта и одного change request.

---

# Week 4. User Stories, UML Use Cases, State Machine и Business Rules

## Измеримый результат

Описано пользовательское и системное поведение NovaDesk через взаимодополняющие модели: backlog, Use Cases, Business Rules и State Machine.

## Теория

- Epic, Feature, User Story, Acceptance Criteria;
- INVEST и вертикальная декомпозиция;
- UML Use Case: actor, system boundary, include, extend, generalization;
- textual Use Case: preconditions, trigger, main flow, alternative flow, exception flow, postconditions;
- Business Rules: constraints, derivations, decisions, eligibility, calculations;
- decision table;
- UML State Machine: state, transition, event, guard, action, terminal state;
- различия User Story, Use Case, Business Rule и State Machine.

## Профессиональные термины

`Epic`, `User Story`, `Acceptance Criteria`, `Use Case`, `Actor`, `Precondition`, `Postcondition`, `Alternative Flow`, `Business Rule`, `Decision Table`, `State`, `Transition`, `Guard`.

## Практическое задание

1. Создать 4 Epics и минимум 14 User Stories.
2. Написать Acceptance Criteria для минимум 8 историй в Given–When–Then.
3. Построить UML Use Case Diagram для клиентов, операторов, CRM и внешних каналов.
4. Описать три детальных Use Cases: регистрация, изменение статуса, синхронизация с CRM.
5. Создать каталог минимум из 15 Business Rules.
6. Построить decision table для определения приоритета и SLA.
7. Создать UML State Machine для обращения, включая ошибки синхронизации, ожидание клиента, закрытие и повторное открытие.
8. Связать все модели с requirement ID в RTM.

## Обязательный артефакт

`02-requirements/backlog.csv`, `use-case-diagram.drawio`, `use-cases.md`, `business-rules.xlsx`, `ticket-state-machine.drawio`.

## Критерии Done

- User Stories описывают ценность, а не технические задачи;
- Use Case boundary соответствует scope;
- include/extend используются осмысленно;
- Business Rules не спрятаны внутри длинных требований;
- State Machine не допускает необъяснимых переходов;
- модели не противоречат каталогу требований.

## Вопросы для самопроверки

1. Когда Use Case полезнее User Story?
2. Чем Business Rule отличается от FR?
3. Что такое guard condition?
4. Почему State Machine нельзя заменить списком статусов?
5. Как Acceptance Criteria связаны с test cases?

## Типичные ошибки

- использовать include/extend как обычные стрелки;
- писать технические компоненты как actors;
- путать состояние и действие;
- создавать Business Rules без владельца;
- дублировать одно поведение в нескольких несогласованных документах.

## Оценка времени

9–10 часов.

---

# Week 5. BPMN 2.0 AS-IS

## Измеримый результат

Построена доказательная модель текущего процесса обработки обращений по всем каналам и выявлены точки потерь, ручные операции и разрывы данных.

## Теория

- process, participant, pool, lane;
- start/intermediate/end events;
- task, subprocess, gateway;
- sequence flow и message flow;
- data object и data store;
- happy path, alternative и exception flow;
- уровень детализации процесса;
- handoff, wait state, bottleneck и control gap.

## Профессиональные термины

`BPMN 2.0`, `Pool`, `Lane`, `Event`, `Task`, `Subprocess`, `Gateway`, `Sequence Flow`, `Message Flow`, `Data Object`, `Handoff`, `Bottleneck`.

## Практическое задание

1. Собрать текстовый narrative текущего процесса.
2. Построить общую AS-IS диаграмму email, Telegram, web-form и CRM.
3. Создать отдельную детальную схему ручной регистрации и передачи обращения.
4. Отметить места, где меняется владелец, копируются данные или теряется идентификатор.
5. Зафиксировать минимум 12 process issues и классифицировать их: process, data, integration, role, control.
6. Связать проблемы процесса с KPI и problem statement.
7. Провести walkthrough диаграммы от лица оператора и IT.

## Обязательный артефакт

`03-processes/as-is-level-1.drawio`, `as-is-registration.drawio`, `process-issues-register.xlsx`.

## Критерии Done

- участники разделены корректно;
- message flow не используется внутри одного pool;
- gateways имеют понятные условия;
- диаграмма отражает фактический, а не желаемый процесс;
- каждая проблема имеет evidence или статус hypothesis;
- схема читается без устного восстановления пропущенных шагов.

## Вопросы для самопроверки

1. Когда нужен отдельный pool?
2. Чем message flow отличается от sequence flow?
3. Как показать ручное ожидание ответа клиента?
4. Что делает AS-IS доказательной моделью?
5. Почему нельзя сразу исправлять процесс на AS-IS диаграмме?

## Типичные ошибки

- рисовать TO-BE под видом AS-IS;
- перегружать одну схему всеми подробностями;
- смешивать систему, роль и подразделение;
- не моделировать исключения;
- фиксировать проблему без связи с последствием.

## Оценка времени

8–10 часов.

---

# Week 6. BPMN TO-BE, SLA и исключения

## Измеримый результат

Спроектирован целевой процесс NovaDesk с автоматизированным intake, синхронизацией, SLA, исключениями и ручными контрольными точками.

## Теория

- TO-BE design и gap analysis;
- timer, message, error и escalation events;
- boundary events;
- event-based gateway;
- compensation concept;
- SLA, OLA и escalation matrix;
- human task и automated task;
- happy, alternative и exception paths;
- связь BPMN с requirements и State Machine.

## Профессиональные термины

`TO-BE`, `Gap Analysis`, `Boundary Event`, `Timer Event`, `Error Event`, `Escalation`, `Event-based Gateway`, `SLA`, `OLA`, `Human Task`, `Service Task`.

## Практическое задание

1. Построить TO-BE Level 1.
2. Детализировать intake и обработку события для каждого канала.
3. Добавить валидацию, дедупликацию, назначение, синхронизацию CRM и уведомления.
4. Смоделировать минимум шесть исключений: неверный payload, недоступность CRM, timeout, повторный webhook, неизвестный клиент, ошибка отправки уведомления.
5. Создать SLA/OLA matrix и escalation rules.
6. Подготовить gap analysis AS-IS → TO-BE.
7. Обновить RTM и backlog по результатам моделирования.

## Обязательный артефакт

`03-processes/to-be-level-1.drawio`, `to-be-intake.drawio`, `sla-ola-matrix.xlsx`, `gap-analysis.xlsx`.

## Критерии Done

- автоматизация не скрывает ручные решения;
- минимум шесть exception paths имеют результат;
- SLA начинается и останавливается по однозначным событиям;
- TO-BE согласован со State Machine;
- изменения привязаны к требованиям и KPI;
- отсутствуют бесконечные циклы повторов.

## Вопросы для самопроверки

1. Когда использовать boundary error event?
2. Чем SLA отличается от OLA?
3. Как BPMN отражает retry?
4. Почему exception flow должен иметь бизнес-результат?
5. Что обновляется в RTM после изменения процесса?

## Типичные ошибки

- моделировать автоматизацию магическим одним блоком;
- не ограничивать количество retry;
- смешивать технический timeout и бизнес-SLA;
- забывать ручную обработку необрабатываемой ошибки;
- создавать TO-BE, не закрывающий проблемы AS-IS.

## Оценка времени

9–10 часов.

---

# Week 7. System Context, границы и C4 Architecture

## Измеримый результат

Определены границы NovaDesk как системы, внешние участники и системы, доверительные зоны и основные контейнеры решения.

## Теория

- system context и system boundary;
- external actor и external system;
- upstream/downstream dependencies;
- C4 Model: Context и Container;
- responsibilities и ownership;
- trust boundary;
- synchronous/asynchronous interaction на концептуальном уровне;
- source of truth;
- architecture decision record — ADR;
- различия business process, system context и container architecture.

## Профессиональные термины

`System Context`, `System Boundary`, `External System`, `Upstream`, `Downstream`, `C4 Context`, `C4 Container`, `Responsibility`, `Source of Truth`, `Trust Boundary`, `ADR`.

## Практическое задание

1. Определить NovaDesk как систему и явно перечислить то, что не является её частью.
2. Построить C4 Context Diagram: клиент, оператор, email provider, Telegram, web-form, CRM, identity provider, monitoring.
3. Построить C4 Container Diagram: channel adapters/orchestration, API service, PostgreSQL, background worker или n8n, notification component, admin interface как optional boundary.
4. Создать responsibility matrix компонентов.
5. Определить source of truth для обращения, клиента, статуса и SLA.
6. Отметить trust boundaries и направления передачи персональных данных.
7. Оформить минимум три ADR: выбор способа intake, хранение данных, синхронность CRM-интеграции.

## Обязательный артефакт

`04-architecture/c4-context.drawio`, `c4-container.drawio`, `component-responsibilities.xlsx`, `adr/`.

## Критерии Done

- Context Diagram не содержит внутренних технических деталей;
- Container Diagram показывает обязанности, а не только технологии;
- boundary согласована со scope;
- source of truth определён для ключевых сущностей;
- внешние зависимости видимы;
- ADR содержит context, decision, alternatives и consequences.

## Вопросы для самопроверки

1. Чем C4 Context отличается от BPMN?
2. Что считается container в C4?
3. Почему технология без ответственности недостаточна?
4. Что такое source of truth?
5. Какие изменения требуют ADR?

## Типичные ошибки

- помещать таблицы и эндпоинты на Context Diagram;
- считать каждую библиотеку отдельным container;
- не определять владельца данных;
- смешивать текущую и целевую архитектуру;
- фиксировать решение без альтернатив и последствий.

## Оценка времени

8–10 часов.

## Checkpoint 2 — после Week 7

Проверяются User Stories/Use Cases/Rules, BPMN AS-IS/TO-BE, State Machine, System Context, C4 Container и согласованность границ. Мини-интервью включает объяснение одного бизнес-исключения и одного архитектурного решения.

---

# Week 8. ERD, Data Modelling и Data Dictionary

## Измеримый результат

Спроектирована логическая модель данных NovaDesk, поддерживающая каналы, статусы, историю, интеграции, аудит и защиту от дублей.

## Теория

- entity, attribute, relationship;
- conceptual, logical и physical data model;
- primary key, foreign key, natural и surrogate key;
- cardinality и optionality;
- normalization 1NF–3NF;
- reference/master/transaction data;
- status history и event history;
- audit fields;
- data dictionary;
- PII и data classification;
- mapping между external и internal identifiers.

## Профессиональные термины

`ERD`, `Entity`, `Attribute`, `Relationship`, `Cardinality`, `Primary Key`, `Foreign Key`, `Surrogate Key`, `Normalization`, `Reference Data`, `Audit Field`, `Data Dictionary`, `PII`.

## Практическое задание

1. Спроектировать ERD минимум из сущностей: tickets, channels, clients, contacts, agents, categories, priorities, ticket_status_history, messages, external_references, integration_events, audit_log.
2. Выбрать ключи и объяснить выбор surrogate/natural keys.
3. Добавить idempotency key, correlation ID, external IDs и timestamps.
4. Определить обязательность и кардинальность связей.
5. Нормализовать модель до разумного уровня и зафиксировать осознанные денормализации.
6. Создать data dictionary: тип, nullable, default, constraints, source, sensitivity, description.
7. Подготовить CRUD matrix по основным Use Cases.

## Обязательный артефакт

`05-data/novadesk-erd.drawio`, `data-dictionary.xlsx`, `crud-matrix.xlsx`, `data-model-decisions.md`.

## Критерии Done

- ERD поддерживает State Machine и BPMN;
- история статусов не перезаписывается;
- внешние идентификаторы отделены от внутренних;
- PII классифицированы;
- data dictionary не противоречит ERD;
- каждая обязательная сущность используется хотя бы одним Use Case.

## Вопросы для самопроверки

1. Когда нужен surrogate key?
2. Почему статусная история должна быть отдельной сущностью?
3. Чем reference data отличается от transaction data?
4. Что показывает optionality?
5. Для чего аналитик фиксирует sensitivity данных?

## Типичные ошибки

- хранить несколько значений в одном поле;
- использовать внешний ID как единственный PK без анализа;
- не моделировать историю;
- путать NULL и пустую строку;
- создавать таблицы, не связанные с требованиями.

## Оценка времени

9–10 часов.

---

# Week 9. SQL Fundamentals для системного анализа

## Измеримый результат

Создана PostgreSQL-схема NovaDesk и набор запросов, проверяющих бизнес-правила и базовые KPI.

## Теория

- DDL и DML;
- CREATE TABLE, constraints и references;
- INSERT/UPDATE/DELETE;
- SELECT, aliases, DISTINCT;
- WHERE, IN, BETWEEN, LIKE, NULL;
- ORDER BY, LIMIT;
- GROUP BY, HAVING;
- aggregate functions;
- date/time operations;
- CASE WHEN и COALESCE;
- transaction basics.

## Профессиональные термины

`DDL`, `DML`, `Constraint`, `Transaction`, `SELECT`, `Filter`, `Aggregation`, `GROUP BY`, `HAVING`, `NULL`, `CASE`, `COALESCE`.

## Практическое задание

1. Создать PostgreSQL schema по ERD.
2. Добавить PK, FK, UNIQUE, CHECK и NOT NULL constraints.
3. Подготовить seed dataset минимум на 300 обращений и связанные записи.
4. Написать минимум 20 запросов на бизнес-вопросы: объём по каналам, backlog, SLA, повторы, категории, нагрузка, ошибки интеграции.
5. Создать запросы для проверки пяти Business Rules.
6. Смоделировать транзакцию создания обращения и первого integration event.
7. Сверить результаты с ожидаемыми значениями.

## Обязательный артефакт

`05-data/schema.sql`, `seed.sql`, `queries-basic.sql`, `expected-results.md`.

## Критерии Done

- схема создаётся с нуля без ручных исправлений;
- constraints соответствуют data dictionary;
- запросы отвечают на сформулированный бизнес-вопрос;
- NULL обрабатывается осознанно;
- агрегаты проверены на контрольном наборе;
- SQL оформлен читаемо и версионируется.

## Вопросы для самопроверки

1. Чем WHERE отличается от HAVING?
2. Для чего нужен UNIQUE constraint?
3. Почему COUNT(*) и COUNT(column) могут дать разный результат?
4. Когда используется transaction?
5. Что должен предотвращать CHECK constraint?

## Типичные ошибки

- рассчитывать целостность только на уровне приложения;
- сравнивать NULL через `=`;
- использовать SELECT * во всех запросах;
- создавать seed без edge cases;
- писать запрос без ожидаемого результата.

## Оценка времени

9–10 часов.

---

# Week 10. SQL JOIN, CTE, Window Functions и Data Quality

## Измеримый результат

Создан набор расширенных аналитических и контрольных запросов, выявляющих нарушения целостности, SLA и интеграционные аномалии.

## Теория

- INNER, LEFT, RIGHT и FULL JOIN;
- cardinality и multiplicative joins;
- subquery и correlated subquery;
- CTE и recursive CTE overview;
- window functions: ROW_NUMBER, LAG, LEAD, SUM/COUNT OVER;
- duplicate detection;
- reconciliation;
- data quality dimensions;
- indexes и базовый EXPLAIN;
- isolation и concurrency overview.

## Профессиональные термины

`JOIN`, `Cardinality`, `CTE`, `Window Function`, `Partition`, `Duplicate`, `Reconciliation`, `Completeness`, `Consistency`, `Uniqueness`, `Index`, `EXPLAIN`.

## Практическое задание

1. Написать минимум 15 запросов с JOIN по нескольким таблицам.
2. Рассчитать время нахождения обращения в каждом статусе через LAG/LEAD.
3. Найти дубли по external ID, payload hash и комбинации полей.
4. Выполнить reconciliation NovaDesk ↔ CRM по external references.
5. Найти orphan records, пропущенные статусы, неотправленные события и нарушения порядка переходов.
6. Создать CTE-отчёт по SLA и повторным обращениям.
7. Добавить 2–3 обоснованных индекса и сравнить EXPLAIN до/после.
8. Оформить data quality report с severity и remediation.

## Обязательный артефакт

`05-data/queries-advanced.sql`, `data-quality-checks.sql`, `reconciliation-report.md`, `explain-notes.md`.

## Критерии Done

- выбор JOIN объяснён;
- количество строк проверяется до и после объединения;
- оконные функции используются по назначению;
- data quality issue имеет правило обнаружения;
- индексы добавлены на основании запросов, а не случайно;
- найденные аномалии связаны с требованиями или Business Rules.

## Вопросы для самопроверки

1. Почему JOIN может умножить строки?
2. Когда LEFT JOIN предпочтительнее INNER JOIN?
3. Чем CTE отличается от временной таблицы?
4. Для чего используется LAG?
5. Какие измерения качества данных важны для NovaDesk?

## Типичные ошибки

- не проверять cardinality;
- устранять дубликаты через DISTINCT без поиска причины;
- создавать индексы на каждое поле;
- смешивать data quality issue и integration error;
- считать reconciliation обычным сравнением количества строк.

## Оценка времени

9–10 часов.

---

# Week 11. HTTP, REST, JSON, OpenAPI и Postman

## Измеримый результат

Спроектирован и проверен REST API NovaDesk для регистрации, получения и изменения обращений, включая ошибки, авторизацию и OpenAPI-спецификацию.

## Теория

- HTTP request/response;
- methods GET, POST, PUT, PATCH, DELETE;
- status codes;
- headers и content types;
- JSON data types и schema;
- REST resource modelling;
- URI, query parameters и path parameters;
- pagination, filtering и sorting;
- authentication vs authorization;
- API versioning;
- OpenAPI 3.x;
- Postman collections, environments, variables и tests.

## Профессиональные термины

`HTTP`, `Request`, `Response`, `Method`, `Status Code`, `Header`, `Payload`, `Resource`, `Endpoint`, `Pagination`, `Authentication`, `Authorization`, `OpenAPI`, `Schema`.

## Практическое задание

1. Спроектировать API resources для tickets, messages и status transitions.
2. Описать минимум 8 endpoints.
3. Создать JSON Schema для создания обращения и ответа.
4. Определить обязательные headers: authorization, correlation ID, idempotency key при необходимости.
5. Описать success и минимум 8 error responses в едином формате.
6. Создать OpenAPI specification с examples.
7. Поднять mock server или использовать FastAPI stub.
8. Создать Postman collection и tests: status, schema, required fields, negative cases.
9. Связать endpoints с Use Cases и RTM.

## Обязательный артефакт

`06-api/openapi.yaml`, `api-design-notes.md`, `postman/novadesk.postman_collection.json`, `error-model.md`.

## Критерии Done

- HTTP methods соответствуют семантике операций;
- status codes используются последовательно;
- request/response schemas согласованы с data dictionary;
- ошибки имеют machine-readable code;
- OpenAPI проходит валидацию;
- Postman содержит позитивные и негативные тесты.

## Вопросы для самопроверки

1. Чем PUT отличается от PATCH?
2. Когда возвращать 201, 202 и 204?
3. Чем path parameter отличается от query parameter?
4. Для чего нужен correlation ID?
5. Что OpenAPI не заменяет в аналитической документации?

## Типичные ошибки

- использовать POST для любой операции;
- возвращать 200 при бизнес- и технической ошибке;
- проектировать payload отдельно от ERD;
- передавать секреты в query string;
- описывать только happy path.

## Оценка времени

9–10 часов.

## Checkpoint 3 — после Week 11

Проверяются ERD, data dictionary, SQL, data quality, OpenAPI и Postman. Мини-интервью включает проектирование одного endpoint, объяснение JOIN и поиск расхождения между API schema и БД.

---

# Week 12. Интеграции, Webhooks, UML Sequence и Data Mapping

## Измеримый результат

Спроектированы интеграционные взаимодействия NovaDesk с каналами и CRM, включая последовательности вызовов, mapping данных, retry, timeout, idempotency и обработку ошибок.

## Теория

- synchronous и asynchronous integration;
- request/response, webhook, polling, messaging overview;
- event-driven interaction;
- webhook signature и delivery semantics;
- timeout;
- retry policy и exponential backoff;
- idempotency;
- at-most-once, at-least-once и exactly-once как практическая оговорка;
- dead-letter queue concept;
- correlation и causation IDs;
- UML Sequence Diagram;
- canonical data model и field mapping;
- transformation, validation, enrichment;
- integration error taxonomy.

## Профессиональные термины

`Webhook`, `Polling`, `Synchronous`, `Asynchronous`, `Event`, `Timeout`, `Retry`, `Backoff`, `Idempotency`, `Delivery Semantics`, `Dead-letter Queue`, `Correlation ID`, `Sequence Diagram`, `Data Mapping`, `Canonical Model`.

## Практическое задание

1. Выбрать паттерн взаимодействия для email, Telegram, web-form и CRM и обосновать решения.
2. Построить минимум четыре UML Sequence Diagrams:
   - Telegram → NovaDesk;
   - web-form → NovaDesk;
   - NovaDesk → CRM;
   - обработка ошибки CRM с retry и ручной эскалацией.
3. Создать integration catalog: source, target, trigger, protocol, frequency, auth, owner, SLA, data classification.
4. Создать mapping source → canonical → CRM минимум для 25 полей.
5. Определить validation и transformation rules.
6. Разработать timeout/retry policy с ограничениями и backoff.
7. Описать idempotency strategy для повторного webhook.
8. Создать error taxonomy и routing ошибок: retry, DLQ/manual queue, reject, alert.
9. Обновить OpenAPI, ERD, BPMN и RTM при найденных противоречиях.

## Обязательный артефакт

`07-integrations/integration-catalog.xlsx`, `sequence-diagrams/`, `data-mapping.xlsx`, `retry-idempotency-policy.md`, `integration-errors.xlsx`.

## Критерии Done

- каждый integration flow имеет owner и trigger;
- Sequence Diagrams показывают ответы и ошибки;
- mapping включает тип, обязательность и transformation rule;
- retry ограничен и не создаёт дубли;
- idempotency имеет конкретный ключ и срок хранения;
- технические ошибки отделены от бизнес-отказов.

## Вопросы для самопроверки

1. Когда webhook лучше polling?
2. Почему retry без idempotency опасен?
3. Чем timeout отличается от SLA?
4. Что должно быть в integration mapping?
5. Для чего нужна dead-letter queue или manual retry queue?

## Типичные ошибки

- считать webhook гарантированной однократной доставкой;
- задавать бесконечный retry;
- рисовать Sequence Diagram без ответов и ошибок;
- сопоставлять поля только по названию;
- не определять владельца интеграционного контракта.

## Оценка времени

9–10 часов.

---

# Week 13. NFR, Security, Audit, Logging и Monitoring

## Измеримый результат

Сформирован измеримый набор нефункциональных требований и operational design NovaDesk, позволяющий обнаруживать сбои, расследовать действия и контролировать качество интеграций.

## Теория

- NFR categories: performance, availability, reliability, scalability, security, maintainability, observability;
- measurable quality attribute scenarios;
- authentication, authorization и RBAC;
- least privilege;
- secrets management;
- encryption in transit/at rest;
- PII, retention и masking;
- audit trail;
- logging levels и structured logs;
- metrics, traces и alerts;
- SLI, SLO и SLA;
- monitoring dashboard и runbook;
- threat modelling overview.

## Профессиональные термины

`NFR`, `Quality Attribute`, `Availability`, `Reliability`, `RBAC`, `Least Privilege`, `Encryption`, `PII`, `Audit Trail`, `Structured Logging`, `Metric`, `Trace`, `Alert`, `SLI`, `SLO`, `Runbook`.

## Практическое задание

1. Переписать NFR из Week 3 в измеримый вид минимум по 8 категориям.
2. Создать role/permission matrix.
3. Определить sensitive fields, retention и masking.
4. Создать audit event catalog: actor, action, object, old/new value, timestamp, correlation ID.
5. Разработать logging specification: event, level, fields, prohibited data.
6. Определить технические и бизнес-метрики: latency, error rate, queue depth, retry count, duplicate rate, SLA compliance.
7. Создать alert matrix с threshold, severity, channel и owner.
8. Описать три runbooks: CRM unavailable, webhook failures, database capacity/error.
9. Провести лёгкий threat review и зафиксировать минимум 8 рисков и controls.

## Обязательный артефакт

`08-nfr/nfr-catalog.xlsx`, `security-role-matrix.xlsx`, `audit-log-spec.md`, `monitoring-alerts.xlsx`, `runbooks/`, `threat-review.md`.

## Критерии Done

- NFR измеримы и тестируемы;
- права следуют least privilege;
- логи не содержат секреты и лишние PII;
- каждый alert имеет действие и owner;
- audit отличается от технического лога;
- SLI/SLO связаны с реальной эксплуатацией.

## Вопросы для самопроверки

1. Чем audit log отличается от application log?
2. Что делает NFR измеримым?
3. Чем SLO отличается от SLA?
4. Какие данные нельзя писать в лог?
5. Почему alert без runbook малоценен?

## Типичные ошибки

- писать «система должна быть быстрой»;
- давать всем ролям полный доступ;
- логировать токены и персональные данные;
- создавать alert на каждую отдельную ошибку;
- путать uptime системы и успешность бизнес-процесса.

## Оценка времени

9–10 часов.

---

# Week 14. Test Cases, UAT, Migration, Release и Rollback

## Измеримый результат

Подготовлен полный пакет приёмки и внедрения NovaDesk: тесты, UAT, migration mapping, release checklist и rollback plan.

## Теория

- verification и validation;
- test level и test type;
- test case, precondition, test data, expected result;
- positive, negative, boundary и integration tests;
- API contract tests;
- traceability requirements → tests;
- UAT scope, entry/exit criteria и sign-off;
- migration strategy: full, incremental, cutover;
- data mapping и reconciliation;
- release plan, feature flag overview;
- rollback criteria и recovery;
- hypercare и post-release monitoring.

## Профессиональные термины

`Verification`, `Validation`, `Test Case`, `Test Data`, `Expected Result`, `Integration Test`, `Contract Test`, `UAT`, `Entry Criteria`, `Exit Criteria`, `Migration`, `Cutover`, `Reconciliation`, `Release`, `Rollback`, `Hypercare`.

## Практическое задание

1. Создать test strategy по NovaDesk.
2. Написать минимум 30 test cases: business process, API, integration, security и data quality.
3. Создать Postman regression subset минимум из 10 автопроверок.
4. Связать test cases с RTM и выявить непокрытые требования.
5. Подготовить UAT plan, сценарии, участников, entry/exit criteria и sign-off template.
6. Спроектировать migration исходных обращений и external IDs.
7. Создать migration mapping и reconciliation checks.
8. Подготовить release checklist, communication plan и rollback plan.
9. Определить go/no-go criteria и hypercare metrics.

## Обязательный артефакт

`09-testing/test-strategy.md`, `test-cases.xlsx`, `uat-plan.md`, `migration-mapping.xlsx`, `release-checklist.md`, `rollback-plan.md`.

## Критерии Done

- тесты покрывают happy, negative и exception flows;
- RTM показывает покрытие требований;
- UAT проверяет бизнес-результат, а не только интерфейс;
- migration включает reconciliation;
- rollback имеет триггеры и ответственных;
- go/no-go criteria измеримы.

## Вопросы для самопроверки

1. Чем verification отличается от validation?
2. Почему UAT не заменяет системное тестирование?
3. Что должно проверяться после миграции?
4. Когда rollback невозможен или ограничен?
5. Как RTM помогает оценить тестовое покрытие?

## Типичные ошибки

- писать тесты только на happy path;
- использовать один набор данных для всех случаев;
- считать UAT демонстрацией продукта;
- мигрировать данные без source-to-target mapping;
- описывать rollback как «вернуть старую версию» без шагов и условий.

## Оценка времени

9–10 часов.

---

# Week 15. Небольшой работающий Automation Prototype

## Измеримый результат

Создан минимальный работающий вертикальный сценарий NovaDesk на **Telegram + n8n + FastAPI + PostgreSQL**, подтверждающий ключевые решения, но не претендующий на production-систему.

## Ограниченный scope прототипа

Реализуется только:

1. пользователь отправляет сообщение Telegram-боту;
2. Telegram update поступает в n8n;
3. n8n нормализует данные и вызывает FastAPI;
4. FastAPI валидирует request, проверяет idempotency key и создаёт ticket в PostgreSQL;
5. API возвращает ticket ID;
6. n8n отправляет пользователю подтверждение;
7. повторная доставка того же события не создаёт второй ticket;
8. ошибки пишутся в структурированный лог.

Не реализуются полный CRM, email, web-form, сложная авторизация, Kubernetes, брокер сообщений и production monitoring.

## Теория

- prototype vs MVP vs production;
- vertical slice;
- FastAPI request validation и OpenAPI;
- PostgreSQL transaction;
- n8n webhook/workflow;
- Telegram Bot API basics;
- configuration и environment variables;
- idempotent create;
- basic structured logging;
- smoke test.

## Профессиональные термины

`Prototype`, `Vertical Slice`, `Webhook`, `Workflow`, `FastAPI`, `Pydantic Schema`, `Environment Variable`, `Database Transaction`, `Idempotency`, `Structured Log`, `Smoke Test`.

## Практическое задание

1. Создать локальную структуру проекта и README запуска.
2. Поднять PostgreSQL через Docker или локальную установку.
3. Реализовать FastAPI endpoints `/health` и `/tickets`.
4. Создать таблицы tickets и integration_events.
5. Реализовать уникальную защиту по source + external_event_id.
6. Настроить Telegram bot и n8n workflow.
7. Передать correlation ID через весь flow.
8. Реализовать понятный error response и обработку ошибки в n8n.
9. Провести минимум 8 smoke/integration tests, включая повторное событие и недоступность API.
10. Сопоставить реализацию с OpenAPI, Sequence Diagram, ERD и NFR; зафиксировать отклонения.
11. Записать короткое demo video или сделать последовательность screenshots.

## Обязательный артефакт

`10-prototype/` с исходным кодом FastAPI, SQL/migrations, экспортом n8n workflow, `.env.example`, Docker Compose при использовании, tests, README и demo evidence.

## Критерии Done

- end-to-end сценарий работает;
- повторное Telegram update не создаёт дубль;
- секреты отсутствуют в GitHub;
- API соответствует основной части OpenAPI;
- база сохраняет source и external event ID;
- ошибки не теряются молча;
- README позволяет повторить запуск;
- ограничения прототипа явно описаны.

## Вопросы для самопроверки

1. Чем prototype отличается от production implementation?
2. Где должна выполняться проверка idempotency?
3. Почему `.env` нельзя коммитить?
4. Что подтверждает vertical slice?
5. Какие решения прототип не способен доказать?

## Типичные ошибки

- расширять прототип до полноценного продукта;
- хранить токены в коде;
- реализовать только happy path;
- допустить расхождение кода и OpenAPI без фиксации;
- считать локальную работу доказательством production readiness.

## Оценка времени

10 часов. При нехватке времени сокращается интерфейс, но не idempotency, persistence и error handling.

---

# Week 16. Final Project, Portfolio и Interview

## Измеримый результат

Собран и защищён цельный кейс Business/System Analyst, показывающий переход от проблемы и требований к архитектуре, интеграциям, тестированию и работающему прототипу.

## Теория

- structure of an analytical case study;
- consistency review;
- architecture and requirements walkthrough;
- trade-off explanation;
- portfolio sanitization;
- interview patterns для Business/System Analyst;
- STAR/CAR для подтверждаемого опыта;
- gap-to-Middle assessment без объявления гарантированного уровня.

## Профессиональные термины

`Case Study`, `Walkthrough`, `Trade-off`, `Consistency Review`, `Portfolio`, `System Design Review`, `Mock Interview`, `Competency Gap`, `Next-step Plan`.

## Практическое задание

1. Собрать итоговую структуру портфолио из `CAPSTONE.md`.
2. Провести consistency review:
   - problem/KPI ↔ requirements;
   - requirements ↔ BPMN/Use Cases;
   - State Machine ↔ ERD/API;
   - API ↔ Sequence/Mapping;
   - NFR ↔ tests/monitoring;
   - RTM ↔ UAT.
3. Исправить все критические противоречия.
4. Подготовить Solution Design на 10–15 страниц.
5. Подготовить презентацию 10–12 слайдов и защиту на 10–12 минут.
6. Записать demo прототипа.
7. Подготовить 30 вопросов и ответов по BA/SA, SQL, API и интеграциям.
8. Пройти mock interview и system walkthrough.
9. Обновить навыковую матрицу и составить 12-недельный план дальнейшего роста.
10. Подготовить формулировки проекта для резюме без выдумывания коммерческого опыта.

## Обязательный артефакт

Итоговый `portfolio/README.md`, `solution-design.md`, `final-presentation.pdf`, demo, заполненная RTM, final skills matrix и `next-12-weeks.md`.

## Критерии Done

- портфолио содержит все обязательные артефакты;
- критические модели не противоречат друг другу;
- решения объясняются через requirements и trade-offs;
- прототип демонстрируется end-to-end;
- конфиденциальные данные отсутствуют;
- итоговая оценка не ниже 70;
- сформулирован реалистичный следующий шаг развития, без заявления о гарантированном Middle.

## Вопросы для самопроверки

1. Как проблема прослеживается до конкретного test case?
2. Где в проекте зафиксированы trade-offs?
3. Как обеспечивается idempotency?
4. Как обнаруживается сбой интеграции с CRM?
5. Какие компетенции до Middle всё ещё требуют production-опыта?

## Типичные ошибки

- показывать набор несвязанных файлов;
- скрывать ограничения проекта;
- называть учебный прототип production-решением;
- заявлять коммерческий опыт, которого не было;
- объяснять инструменты вместо аналитических решений.

## Оценка времени

9–10 часов.

## Checkpoint 4 — итоговый

Проводятся review портфолио, трассировка случайной цепочки requirement → design → test, SQL/API task, анализ интеграционной ошибки, защита Solution Design и mock interview.

---

# Факультативы

Факультативы не входят в обязательные 16 недель и не заменяют основные артефакты.

1. **Power BI:** импорт данных NovaDesk, модель, DAX и dashboard KPI.
2. **ELMA365/BPMSoft:** перенос части TO-BE в low-code/BPM и сравнение платформ по критериям.
3. **AI Automation:** LLM API, structured output, human-in-the-loop, RAG overview, quality evaluation, security и cost control.

Подробная программа находится в [`FACULTATIVES.md`](FACULTATIVES.md).