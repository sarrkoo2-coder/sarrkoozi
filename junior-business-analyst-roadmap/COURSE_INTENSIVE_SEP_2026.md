# Business/System Analyst: Intensive Automation & Integration Track

Активный ускоренный план обучения с завершением основной программы к **30 сентября 2026 года**.

## Формат

- период: 27 июля — 30 сентября 2026;
- Week 0 + 9 основных недель;
- нагрузка: 8–10 часов в неделю, финальная неделя — до 12 часов;
- 30% теории и 70% практики;
- сквозной проект: NovaDesk;
- GitHub — портфолио и версии артефактов;
- Jira и Confluence — обязательные сквозные инструменты;
- курс не гарантирует уровень Middle, а формирует доказуемую готовность к Junior+/Strong Junior и Middle-track задачам под review.

## Сквозная практика Jira и Confluence

Jira изучается не только как интерфейс, а как рабочий контур аналитика:

- issue types: Epic, Story, Task, Bug, Spike;
- backlog, boards, sprints и workflow;
- statuses, priorities, links, dependencies и blockers;
- JQL, filters и dashboards;
- velocity, burndown, cycle time, throughput, predictability;
- Definition of Ready и Definition of Done;
- связь задач с requirement ID, BPMN, API, Test Case и Release.

Confluence используется для Problem Statement, требований, решений, протоколов, спецификаций, API, UAT и Release Notes.

---

# Week 0 — 27–29 июля

## Диагностика, SDLC и рабочий контур

**Темы:**

- различия Business Analyst, System Analyst и Integration Analyst;
- SDLC и enterprise implementation lifecycle;
- работа аналитика с бизнесом, frontend, backend, QA и DevOps;
- GitHub для портфолио;
- Jira: проект, backlog, workflow, board, filters и базовый JQL;
- Confluence: структура пространства NovaDesk;
- диагностика подтверждённого опыта и пробелов.

**Практика:** настроить GitHub/Jira/Confluence, заполнить baseline и матрицу навыков, создать первый Epic NovaDesk и workflow `Backlog → Analysis → Review → Rework → Done`.

**Артефакт:** `portfolio/00-baseline.md`, Jira board, Confluence space.

**Done:** рабочий контур настроен; опыт описан без преувеличений; определены стартовые пробелы.

**Время:** 5–7 часов.

---

# Week 1 — 30 июля–5 августа

## Problem Statement, цели, KPI, Scope, Stakeholders и Elicitation

**Темы:**

- problem statement и business need;
- outcome, output, KPI, baseline и target;
- in scope, out of scope, constraints, assumptions и dependencies;
- stakeholder register, power/interest и RACI;
- интервью, workshop, observation и document analysis;
- работа с внешним заказчиком: вопросы, демонстрации и согласования.

**Практика:** сформулировать проблему NovaDesk, цели и KPI; определить границы; создать реестр минимум из 10 stakeholders, RACI и план интервью; провести учебное интервью.

**Артефакты:** Problem Statement, Goals/KPI, Scope, Stakeholder Register, RACI, Interview Guide и Interview Notes.

**Done:** проблема не содержит готового решения; KPI измеримы; stakeholders и источники требований определены.

**Время:** 8–10 часов.

---

# Week 2 — 6–12 августа

## Requirements Engineering, Traceability, User Stories, Use Cases и постановка разработчику

**Темы:**

- BR, UR/SR, FR и NFR;
- atomic, unambiguous, feasible, testable и traceable requirements;
- MoSCoW и приоритизация;
- Business Rules, Glossary, Assumptions и Decision Log;
- Epic, User Story, Acceptance Criteria и Given–When–Then;
- UML Use Case;
- детальная постановка задачи frontend/backend/QA;
- Requirements Traceability Matrix.

**Практика:** создать каталог не менее 25 требований, минимум 12 Business Rules, 3 Epics и 12 Stories; описать 2 Use Cases; подготовить одну полноценную постановку разработчику с ошибками, ограничениями и Acceptance Criteria; построить RTM.

**Артефакты:** Requirements Catalog, Business Rules Catalog, Backlog, Use Cases, Developer Task Specification и RTM.

**Done:** требования проверяемы и имеют источники; задача понятна разработчику и QA; RTM связывает цели, требования, реализацию и проверки.

**Время:** 9–10 часов.

### Checkpoint 1

Мини-интервью по problem framing, stakeholders, requirements, Jira и постановке задачи. Обновление матрицы навыков.

---

# Week 3 — 13–19 августа

## BPMN AS-IS/TO-BE, SLA, исключения и маршруты документов

**Темы:**

- BPMN events, tasks, gateways, pools, lanes и message flow;
- AS-IS и выявление bottlenecks;
- TO-BE, happy path, alternative flow и exception flow;
- SLA timers, escalation и boundary events;
- document routes и approval workflow;
- ролевая модель и Access Matrix;
- Gap Analysis.

**Практика:** построить AS-IS и TO-BE NovaDesk; отразить email, Telegram, web-form и CRM; добавить SLA, минимум 4 исключения, эскалации, роли и права; составить Gap Analysis.

**Артефакты:** BPMN AS-IS, BPMN TO-BE, Gap Analysis и Access Matrix.

**Done:** BPMN читается без устных пояснений; исключения и SLA отражены корректно; изменения связаны с требованиями и KPI.

**Время:** 8–10 часов.

---

# Week 4 — 20–26 августа

## System Context, C4 и UML архитектурных сценариев

**Темы:**

- границы системы и external systems;
- System Context;
- C4 Context и Container;
- frontend/backend взаимодействие;
- монолит, микросервисы и интеграционный слой;
- UML Sequence Diagram;
- UML State Machine;
- UML Class Diagram на концептуальном уровне;
- Solution Concept и архитектурные ограничения.

**Практика:** построить System Context, C4 Context/Container, минимум 3 Sequence Diagrams и State Machine обращения; описать ответственность компонентов и основные архитектурные решения.

**Артефакты:** System Context, C4 diagrams, Sequence Diagrams, State Machine и Solution Concept.

**Done:** границы системы непротиворечивы; сценарии согласованы с BPMN; ответственность компонентов понятна.

**Время:** 8–10 часов.

---

# Week 5 — 27 августа–2 сентября

## ERD, Data Dictionary, PostgreSQL и расширенный SQL

**Темы:**

- entities, attributes и relationships;
- cardinality, PK, FK, unique и nullable;
- нормализация и справочники;
- ERD и CRUD Matrix;
- SELECT, WHERE, GROUP BY, HAVING и aggregates;
- JOIN, subquery, CASE, COALESCE и CTE;
- базовые Window Functions;
- data quality checks;
- проектирование PostgreSQL schema.

**Практика:** создать ERD NovaDesk и Data Dictionary; реализовать schema.sql и seed.sql; написать минимум 20 SQL-запросов, включая JOIN/CTE и проверки дублей, пропущенных статусов и SLA.

**Артефакты:** ERD, Data Dictionary, CRUD Matrix, `schema.sql`, `seed.sql`, `queries.sql`, Data Quality Report.

**Done:** модель поддерживает BPMN и требования; запросы отвечают на бизнес-вопросы; число строк после JOIN проверено.

**Время:** 9–10 часов.

---

# Week 6 — 3–9 сентября

## HTTP, REST, JSON, XML, OpenAPI, Postman и OAuth 2.0

**Темы:**

- HTTP methods, headers и status codes;
- resources, endpoints и REST constraints;
- request/response JSON;
- XML и CSV как форматы обмена;
- OpenAPI/Swagger;
- Postman collections, environments и tests;
- API key, Basic Auth, Bearer Token и OAuth 2.0 Client Credentials;
- validation, pagination, filtering и error model;
- webhooks и callback security.

**Практика:** спроектировать API NovaDesk; описать OpenAPI; создать Postman Collection; проверить positive/negative cases; описать OAuth flow и webhook signature validation.

**Артефакты:** `openapi.yaml`, Postman Collection, API Error Catalog и Authentication Scheme.

**Done:** спецификация валидна; ошибки и статусы согласованы; API связан с requirements, ERD и Sequence Diagrams.

**Время:** 8–10 часов.

---

# Week 7 — 10–16 сентября

## Интеграции, Data Mapping, Kafka/RabbitMQ и надёжность обмена

**Темы:**

- synchronous и asynchronous integration;
- REST, webhook, file exchange и SFTP;
- producer, consumer, queue, topic и event;
- Kafka vs RabbitMQ на уровне аналитика;
- at-most-once, at-least-once и duplicate delivery;
- acknowledgement, ordering и Dead Letter Queue;
- timeout, retry, exponential backoff и circuit breaker;
- idempotency и correlation ID;
- Data Mapping и canonical model;
- Integration Catalog.

**Практика:** описать четыре интеграции NovaDesk; создать field-level mapping; выбрать sync/async pattern; описать retry, timeout, idempotency, DLQ и reconciliation; смоделировать повторную доставку события.

**Артефакты:** Integration Catalog, Data Mapping, Error Handling Matrix, Event Specification и обновлённые Sequence Diagrams.

**Done:** для каждого обмена определены контракт, инициатор, безопасность, ошибки и восстановление; повторная доставка не создаёт дубль.

**Время:** 9–10 часов.

### Checkpoint 2

Защита System Context, ERD, API и Integration Mapping. Практические вопросы по Jira, SQL, REST и event-driven integration.

---

# Week 8 — 17–23 сентября

## NFR, Security, Linux/logs, Testing, UAT и enterprise release lifecycle

**Темы:**

- performance, availability, scalability и reliability;
- RBAC, least privilege, audit trail и secrets;
- logging, metrics, monitoring и alerting;
- Linux terminal и чтение логов;
- correlation ID и поиск интеграционной ошибки;
- Test Case, Test Scenario и test data;
- API/integration testing;
- UAT и acceptance protocol;
- migration, pilot, rollout, release и rollback;
- опытная и промышленная эксплуатация.

**Практика:** сформировать NFR Catalog; описать logging/monitoring; разобрать учебные логи; создать минимум 15 Test Cases, UAT Plan, Migration Plan и Release/Rollback Plan.

**Артефакты:** NFR Catalog, Security/Access Matrix, Logging & Monitoring Specification, Test Cases, UAT Plan, Migration Plan, Release/Rollback Plan.

**Done:** NFR измеримы; тесты трассируются к требованиям; rollback имеет условия запуска и проверяемый результат.

**Время:** 9–10 часов.

---

# Week 9 — 24–30 сентября

## Automation Prototype, delivery-метрики, Solution Design, портфолио и интервью

**Темы:**

- ограниченный прототип `Telegram → n8n → FastAPI → PostgreSQL → n8n → Telegram`;
- обработка ошибок и idempotency в прототипе;
- Jira delivery metrics: velocity, burndown, cycle time, throughput и predictability;
- blockers, dependencies и release readiness;
- post-release evaluation и проверка KPI;
- Solution Design;
- защита решений бизнесу и технической команде;
- описание проекта в резюме и на GitHub;
- вопросы Junior+/Middle-track интервью.

**Практика:** собрать один работающий end-to-end сценарий; провести demo; обновить RTM; проверить соответствие BPMN, ERD, API, mapping и tests; подготовить Solution Design, README и презентацию; пройти пробное интервью.

**Артефакты:** исходный код прототипа, deployment/runbook, Solution Design, финальная RTM, portfolio README, presentation и resume project description.

**Done:** прототип воспроизводимо запускается; ключевой сценарий демонстрируется; артефакты непротиворечивы; решения объясняются без чтения конспекта.

**Время:** 10–12 часов.

### Final Checkpoint

- ревью полного NovaDesk;
- проверка трассируемости от проблемы до тестов;
- GitHub portfolio review;
- mock interview;
- итоговая оценка готовности к откликам.

---

# Факультатив после 30 сентября

## AI Automation

- LLM API;
- structured output;
- prompt/version management;
- human-in-the-loop;
- RAG overview;
- AI agents overview;
- quality evaluation;
- security, privacy и prompt injection;
- token/cost control;
- интеграция AI-сервиса в корпоративный процесс.

## Платформы и отрасли

- Power BI / Yandex DataLens;
- BPMSoft / Creatio / ELMA365;
- 1С integration overview;
- WMS и складская логистика;
- Order-to-Cash;
- ЭДО и маршруты документов;
- EPC notation.

# Итоговое обязательное портфолио

- Problem Statement, Goals, KPI и Scope;
- Stakeholder Register и RACI;
- Requirements Catalog, Business Rules и RTM;
- User Stories, Acceptance Criteria и Use Cases;
- BPMN AS-IS/TO-BE и Gap Analysis;
- System Context, C4 и UML diagrams;
- ERD, Data Dictionary и SQL;
- OpenAPI и Postman;
- Integration Catalog и Data Mapping;
- NFR, Security, Logging и Monitoring;
- Test Cases, UAT, Migration, Release и Rollback;
- работающий automation prototype;
- Solution Design, презентация и описание для резюме.
