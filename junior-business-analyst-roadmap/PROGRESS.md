# Трекер прогресса Business/System Analyst

## Статусы

- `not-started` — работа не начата;
- `in-progress` — выполняется практика;
- `review` — артефакт передан на проверку;
- `rework` — требуется корректировка;
- `done` — модуль принят.

## Сводная таблица

| Week | Модуль | Статус | Часы | Знания /100 | Практика /100 | Артефакт /100 | Объяснение /100 | Ссылка |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 0 | Диагностика и рабочий контур | in-progress | 0 | 0 | 0 | 0 | 0 |  |
| 1 | Problem, Goals, KPI, Scope | not-started | 0 | 0 | 0 | 0 | 0 |  |
| 2 | Stakeholders и Elicitation | not-started | 0 | 0 | 0 | 0 | 0 |  |
| 3 | Requirements Engineering и RTM | not-started | 0 | 0 | 0 | 0 | 0 |  |
| 4 | Stories, Use Cases, State Machine, Rules | not-started | 0 | 0 | 0 | 0 | 0 |  |
| 5 | BPMN AS-IS | not-started | 0 | 0 | 0 | 0 | 0 |  |
| 6 | BPMN TO-BE, SLA, Exceptions | not-started | 0 | 0 | 0 | 0 | 0 |  |
| 7 | System Context и C4 | not-started | 0 | 0 | 0 | 0 | 0 |  |
| 8 | ERD и Data Dictionary | not-started | 0 | 0 | 0 | 0 | 0 |  |
| 9 | SQL Fundamentals | not-started | 0 | 0 | 0 | 0 | 0 |  |
| 10 | SQL Advanced и Data Quality | not-started | 0 | 0 | 0 | 0 | 0 |  |
| 11 | REST API, OpenAPI, Postman | not-started | 0 | 0 | 0 | 0 | 0 |  |
| 12 | Integrations, Sequence, Mapping | not-started | 0 | 0 | 0 | 0 | 0 |  |
| 13 | NFR, Security, Observability | not-started | 0 | 0 | 0 | 0 | 0 |  |
| 14 | Testing, UAT, Migration, Release | not-started | 0 | 0 | 0 | 0 | 0 |  |
| 15 | Automation Prototype | not-started | 0 | 0 | 0 | 0 | 0 |  |
| 16 | Final Project and Interview | not-started | 0 | 0 | 0 | 0 | 0 |  |

## Формула оценки

```text
Weekly score = Knowledge × 0.25
             + Practice × 0.30
             + Artifact × 0.30
             + Explanation × 0.15
```

Модуль переводится в `done`, если:

- итоговая оценка не ниже 70;
- обязательный артефакт добавлен в GitHub;
- Jira task закрыта;
- Confluence page содержит согласованную версию или ссылку на неё;
- обучающийся может объяснить решение и ограничения без чтения документа.

## Checkpoints

- **Checkpoint 1:** после Week 3 — problem, stakeholders, requirements, RTM.
- **Checkpoint 2:** после Week 7 — behavior, BPMN, State Machine, System Context и C4.
- **Checkpoint 3:** после Week 11 — ERD, SQL, Data Quality, REST API и Postman.
- **Checkpoint 4:** после Week 16 — полное портфолио, Solution Design, prototype и mock interview.

## Еженедельная ретроспектива

1. Что я теперь могу выполнить самостоятельно?
2. Какой артефакт это доказывает?
3. Как решение связано с requirements и RTM?
4. Где остались противоречия между процессом, данными, API и тестами?
5. Какие assumptions требуют подтверждения?
6. Что я не должен называть production-ready?
7. Какое одно исправление даст наибольший рост качества?

## Правило позиционирования

Учебный результат показывает сформированные навыки и готовность выполнять соответствующие задачи под review. Он не используется как доказательство несуществующего коммерческого или production-опыта.