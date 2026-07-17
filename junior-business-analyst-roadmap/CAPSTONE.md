# Итоговый проект NovaDesk

## Сценарий

NovaDesk — интеграционная система обработки клиентских обращений из:

- email;
- Telegram;
- веб-формы;
- CRM.

Текущая обработка разрознена: сообщения переносятся вручную, единый идентификатор отсутствует, статусы расходятся, повторные события создают риск дублей, SLA и технические ошибки контролируются непоследовательно.

Цель итогового проекта — показать полный цикл работы Business/System Analyst: от проблемы и требований до архитектуры, данных, API, интеграционных контрактов, NFR, тестирования, внедрения и небольшого работающего прототипа.

## Scope прототипа

Работающий прототип Week 15 реализует только вертикальный сценарий:

```text
Telegram → n8n → FastAPI → PostgreSQL → n8n → Telegram
```

Он подтверждает intake, валидацию, persistence, idempotency, correlation ID и базовую обработку ошибок. Полная интеграция email, web-form и CRM остаётся аналитически спроектированной, но не обязана быть реализована в коде.

## Обязательная структура портфолио

```text
portfolio/
├── README.md
├── 00-baseline.md
├── 01-discovery/
│   ├── problem-scope-kpi.md
│   ├── stakeholder-register.xlsx
│   ├── raci.xlsx
│   ├── elicitation-plan.md
│   ├── interview-notes/
│   └── assumptions-open-questions.md
├── 02-requirements/
│   ├── requirements-catalog.xlsx
│   ├── traceability-matrix.xlsx
│   ├── glossary.md
│   ├── backlog.csv
│   ├── acceptance-criteria.md
│   ├── use-case-diagram.drawio
│   ├── use-cases.md
│   ├── business-rules.xlsx
│   ├── decision-table.xlsx
│   └── ticket-state-machine.drawio
├── 03-processes/
│   ├── as-is-level-1.drawio
│   ├── as-is-registration.drawio
│   ├── process-issues-register.xlsx
│   ├── to-be-level-1.drawio
│   ├── to-be-intake.drawio
│   ├── sla-ola-matrix.xlsx
│   └── gap-analysis.xlsx
├── 04-architecture/
│   ├── system-boundary.md
│   ├── c4-context.drawio
│   ├── c4-container.drawio
│   ├── component-responsibilities.xlsx
│   ├── solution-design.md
│   └── adr/
├── 05-data/
│   ├── novadesk-erd.drawio
│   ├── data-dictionary.xlsx
│   ├── crud-matrix.xlsx
│   ├── schema.sql
│   ├── seed.sql
│   ├── queries-basic.sql
│   ├── queries-advanced.sql
│   ├── data-quality-checks.sql
│   ├── reconciliation-report.md
│   └── explain-notes.md
├── 06-api/
│   ├── openapi.yaml
│   ├── api-design-notes.md
│   ├── error-model.md
│   └── postman/
│       ├── novadesk.postman_collection.json
│       └── environment.example.json
├── 07-integrations/
│   ├── integration-catalog.xlsx
│   ├── sequence-diagrams/
│   ├── data-mapping.xlsx
│   ├── retry-idempotency-policy.md
│   └── integration-errors.xlsx
├── 08-nfr/
│   ├── nfr-catalog.xlsx
│   ├── security-role-matrix.xlsx
│   ├── audit-log-spec.md
│   ├── logging-spec.md
│   ├── monitoring-alerts.xlsx
│   ├── threat-review.md
│   └── runbooks/
├── 09-testing/
│   ├── test-strategy.md
│   ├── test-cases.xlsx
│   ├── uat-plan.md
│   ├── uat-signoff-template.md
│   ├── migration-mapping.xlsx
│   ├── release-checklist.md
│   └── rollback-plan.md
├── 10-prototype/
│   ├── README.md
│   ├── app/
│   ├── sql-or-migrations/
│   ├── n8n/
│   ├── tests/
│   ├── docker-compose.yml
│   ├── .env.example
│   └── demo-evidence/
└── 11-final/
    ├── final-presentation.pdf
    ├── demo-script.md
    ├── interview-questions.md
    ├── final-skills-matrix.md
    └── next-12-weeks.md
```

## Минимальные функциональные области

### Epic 1. Omnichannel Intake

- получение Telegram update;
- получение веб-формы;
- приём email-сообщения;
- импорт или событие из CRM;
- нормализация данных в canonical model;
- проверка обязательных полей;
- защита от повторной доставки.

### Epic 2. Ticket Lifecycle

- создание обращения;
- классификация и приоритет;
- назначение исполнителя;
- статусные переходы;
- ожидание ответа клиента;
- закрытие и повторное открытие;
- история изменений.

### Epic 3. CRM Integration

- поиск или создание клиента;
- передача обращения;
- синхронизация ключевых статусов;
- хранение external IDs;
- reconciliation;
- обработка недоступности и ошибок CRM.

### Epic 4. SLA and Notifications

- расчёт SLA;
- предупреждение о риске просрочки;
- эскалация;
- уведомления клиенту и оператору;
- контроль OLA внутренних команд.

### Epic 5. Operations and Control

- audit trail;
- structured logs;
- integration metrics;
- alerts и runbooks;
- data quality checks;
- ручная очередь необрабатываемых ошибок.

## Обязательные цепочки трассировки

Итоговая RTM должна позволять пройти минимум по пяти цепочкам:

```text
Problem → KPI → Business Requirement → FR/NFR
→ BPMN/Use Case → Architecture/API/Data
→ Test Case/UAT → Prototype evidence
```

Обязательные примеры:

1. защита от дублей;
2. создание обращения из Telegram;
3. синхронизация с CRM;
4. контроль первой реакции;
5. аудит изменения статуса.

## Требования к Solution Design

Итоговый документ должен включать:

1. контекст и цели;
2. scope и ограничения;
3. stakeholders;
4. ключевые требования и Business Rules;
5. BPMN TO-BE;
6. C4 Context/Container;
7. State Machine;
8. ERD и ownership данных;
9. API contracts;
10. integration flows и Sequence Diagrams;
11. mapping;
12. timeout/retry/idempotency/error handling;
13. NFR, security, audit и monitoring;
14. testing/UAT;
15. migration/release/rollback;
16. trade-offs, risks и open questions;
17. границы прототипа.

Рекомендуемый объём: 10–15 страниц без учёта приложений.

## Требования к защите

За 10–12 минут объяснить:

1. какую проблему решает NovaDesk;
2. где проходят границы системы;
3. почему выбрана такая целевая архитектура;
4. как обращение проходит от канала до PostgreSQL и CRM;
5. как предотвращаются дубли;
6. как обрабатываются timeout и ошибки;
7. как ERD, API и State Machine согласованы;
8. какие NFR являются критичными;
9. как решение тестируется и принимается;
10. как выполняются release и rollback;
11. что реально реализовано в прототипе;
12. какие ограничения требуют production-опыта.

## Оценка итогового проекта

| Блок | Вес |
|---|---:|
| Problem, KPI, Scope, Stakeholders | 10% |
| Requirements, Business Rules, RTM | 15% |
| BPMN, Use Cases, State Machine | 15% |
| System Context, C4, Solution Design | 15% |
| ERD, Data Dictionary, SQL, Data Quality | 15% |
| API, Sequence, Mapping, Integration Policies | 15% |
| NFR, Security, Observability, Testing, Release | 10% |
| Prototype and defence | 5% |

## Ограничения позиционирования

Итоговый кейс можно указывать как учебный или pet project. Нельзя представлять его как коммерческое внедрение или заявлять production-результаты, которые не были получены.