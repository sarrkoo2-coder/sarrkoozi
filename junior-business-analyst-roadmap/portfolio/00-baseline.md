# Week 0 — Baseline диагностика Business/System Analyst

Дата начала: 17 июля 2026

## Правило заполнения

Описывайте только подтверждённый опыт. Можно указать работу с автоматизацией, Bitrix24, AS-IS/TO-BE, API, SQL, n8n и подразделениями, но нельзя добавлять несуществующие масштабы, обязанности, роли или production-результаты.

# 1. Текущая профессиональная база

## 1.1 Подтверждённые задачи

Для каждого примера укажите:

- контекст;
- вашу конкретную задачу;
- что вы сделали самостоятельно;
- какие системы или данные использовали;
- какой артефакт или результат можно показать;
- что вы не делали.

| Пример | Контекст | Моя работа | Инструменты | Доказательство | Ограничения |
|---|---|---|---|---|---|
| 1 |  |  |  |  |  |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |

## 1.2 Самооценка навыков

Шкала:

- 0 — не знаком;
- 1 — понимаю назначение и термины;
- 2 — выполняю по примеру;
- 3 — выполняю самостоятельно и объясняю;
- 4 — нахожу противоречия, сравниваю решения и улучшаю результат.

| Навык | 0–4 | Доказательство или пример |
|---|---:|---|
| Problem Statement, KPI, Scope |  |  |
| Stakeholders и Elicitation |  |  |
| BR/SR/FR/NFR |  |  |
| Requirements Traceability |  |  |
| User Stories и Acceptance Criteria |  |  |
| UML Use Case |  |  |
| Business Rules |  |  |
| UML State Machine |  |  |
| BPMN AS-IS/TO-BE |  |  |
| System Context и C4 |  |  |
| ERD и Data Dictionary |  |  |
| SQL SELECT/GROUP BY |  |  |
| SQL JOIN/CTE |  |  |
| HTTP/REST/JSON |  |  |
| OpenAPI/Postman |  |  |
| Webhooks и Integration Patterns |  |  |
| UML Sequence |  |  |
| Data Mapping |  |  |
| Timeout/Retry/Idempotency |  |  |
| NFR и Security |  |  |
| Logging/Monitoring/Audit |  |  |
| Test Cases/UAT |  |  |
| Migration/Release/Rollback |  |  |
| n8n/FastAPI/PostgreSQL |  |  |
| Jira/Confluence |  |  |
| Solution Design и защита |  |  |

# 2. Диагностический кейс NovaDesk

NovaDesk принимает обращения из email, Telegram, веб-формы и CRM. Единого intake и внутреннего идентификатора нет. Часть данных переносится вручную, статусы могут расходиться, SLA контролируется непоследовательно, а повторная доставка события может создать дубль.

Выполните задания без использования готового решения курса.

## 2.1 Problem Statement

Сформулируйте проблему в 3–5 предложениях без выбора конкретной технологии.

> Заполнить.

## 2.2 Stakeholders

Назовите минимум 8 заинтересованных сторон и их интересы.

| Stakeholder | Интерес | Влияние | Вопросы к нему |
|---|---|---|---|
|  |  |  |  |

## 2.3 Elicitation

Подготовьте 12 вопросов:

- 4 бизнесу;
- 4 IT/владельцу CRM;
- 2 безопасности;
- 2 эксплуатации.

1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 
9. 
10. 
11. 
12. 

## 2.4 Requirements

Напишите:

- 2 Business Requirements;
- 2 Stakeholder/User Requirements;
- 3 Functional Requirements;
- 2 Non-functional Requirements.

Для каждого укажите ID, rationale и verification method.

> Заполнить.

## 2.5 Backlog и Acceptance Criteria

Создайте:

- 1 Epic;
- 3 User Stories;
- Acceptance Criteria для одной истории в Given–When–Then.

> Заполнить.

## 2.6 Business Rules и State

1. Напишите три Business Rules.
2. Перечислите предполагаемые состояния обращения.
3. Укажите два недопустимых перехода.

> Заполнить.

## 2.7 AS-IS

Текстом опишите текущий процесс от поступления сообщения до закрытия. Укажите минимум:

- 3 process issues;
- 2 data issues;
- 2 integration risks.

> Заполнить.

## 2.8 System Context

Текстом определите:

- что входит в NovaDesk;
- какие системы являются внешними;
- кто является human actor;
- какая система предположительно является source of truth для клиента и обращения.

> Заполнить.

## 2.9 Data Model

Предложите минимум 6 сущностей и их ключевые связи.

| Entity | Назначение | Key | Связи |
|---|---|---|---|
|  |  |  |  |

## 2.10 REST API

Опишите один endpoint создания обращения:

- method;
- path;
- request JSON;
- success status;
- два error responses;
- idempotency approach.

> Заполнить.

## 2.11 Sequence

Текстом перечислите шаги сценария:

```text
Telegram → orchestration → API → database → confirmation
```

Добавьте ветку повторной доставки события и ветку недоступности API.

> Заполнить.

## 2.12 SQL

Даны таблицы:

```text
tickets(ticket_id, channel_id, status, created_at, first_response_at)
channels(channel_id, code)
integration_events(event_id, ticket_id, source, external_event_id, status)
```

Напишите:

1. запрос количества закрытых обращений по каналам;
2. запрос событий интеграции без связанного обращения;
3. кратко объясните выбор JOIN.

```sql
-- Заполнить
```

## 2.13 NFR и Testing

1. Напишите три измеримых NFR.
2. Напишите пять test cases, включая negative и duplicate delivery.
3. Укажите один UAT-сценарий.

> Заполнить.

# 3. Самооценка после диагностики

- Что выполнено без поиска:
- Что потребовало поиска:
- Где термин знаком, но решение объяснить не удалось:
- Какие пять навыков требуют наибольшего развития:
- Какие навыки уже подтверждаются реальными задачами:
- Какие навыки подтверждены только учебной практикой:
- Что нельзя указывать как production-опыт:

# 4. Ссылки и время

- Commit:
- GitHub Issue:
- Jira task:
- Confluence page:
- Потрачено часов:
