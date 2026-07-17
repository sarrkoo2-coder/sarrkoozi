# Факультативы

Факультативы не входят в обязательные Week 0–16. Они выполняются после основных модулей или параллельно, если не снижают качество обязательных артефактов.

# Факультатив A. Power BI для operational analytics

## Цель

Построить dashboard NovaDesk на основе PostgreSQL/CSV и проверить согласованность KPI с требованиями и SQL.

## Темы

- Power Query;
- star schema;
- relationships;
- calculated column vs measure;
- DAX: COUNTROWS, DISTINCTCOUNT, CALCULATE, DIVIDE;
- SLA compliance, backlog, integration error rate;
- filters, drill-through и dashboard storytelling.

## Практика

1. Подключить данные tickets, channels, agents, status history и integration events.
2. Создать календарную таблицу.
3. Построить меры минимум для 8 KPI.
4. Сверить результаты с SQL.
5. Создать dashboard для руководителя поддержки и отдельную technical view.
6. Описать три решения, принятые на основании данных.

## Артефакт

`facultatives/power-bi/novadesk-dashboard.pbix` и screenshots.

## Done

- модель данных объяснима;
- KPI совпадают с SQL;
- measures не подменены ручными расчётами;
- dashboard отвечает на конкретные управленческие вопросы.

## Примечание для macOS

Для полноценного Power BI Desktop требуется Windows-среда: виртуальная машина или удалённый Windows-компьютер.

---

# Факультатив B. ELMA365 и BPMSoft

## Цель

Понять перенос аналитической модели NovaDesk в корпоративную low-code/BPM-платформу без привязки всей архитектуры к конкретному вендору.

## Темы

- application, entity, form, workflow, role, permission;
- executable process;
- timer, task, notification;
- integration connector и REST API;
- environments и configuration management;
- platform constraints;
- vendor lock-in;
- criteria-based platform comparison.

## Практика

1. Выбрать ограниченный процесс: регистрация → назначение → работа → закрытие.
2. Сопоставить BPMN, сущности, формы, роли и Business Rules с возможностями ELMA365.
3. Создать прототип или configuration specification.
4. Изучить материалы BPMSoft и выполнить gap analysis.
5. Сравнить платформы минимум по 15 критериям: process engine, data model, API, security, deployment, monitoring, skills, cost assumptions.
6. Подготовить recommendation memo без заявления о полном внедрении.

## Артефакт

`facultatives/low-code/platform-mapping.xlsx`, `prototype-evidence/`, `comparison-memo.md`.

## Done

- бизнес-требования не подгоняются под интерфейс платформы;
- факты отделены от предположений;
- ограничения платформ зафиксированы;
- выбор основан на критериях.

---

# Факультатив C. AI Automation

## Цель

Спроектировать безопасное использование LLM в NovaDesk как дополнительный управляемый компонент, а не как замену основного бизнес-процесса.

## 1. LLM API и границы применения

### Теория

- LLM API request/response;
- system/user messages;
- tokens и context window;
- deterministic vs probabilistic behavior;
- подходящие и неподходящие задачи;
- fallback и graceful degradation.

### Практика

Выбрать один сценарий: классификация темы обращения, черновик ответа или извлечение структурированных полей. Описать business value, risks и fallback.

## 2. Structured Output

### Теория

- JSON schema;
- constrained/structured output;
- validation;
- retry after invalid output;
- confidence и reason codes.

### Практика

Спроектировать schema:

```json
{
  "category": "billing",
  "priority": "normal",
  "summary": "...",
  "requires_human_review": true,
  "reason_codes": ["customer_mentions_payment"]
}
```

Создать минимум 20 тестовых обращений и проверить валидность результата.

## 3. Human-in-the-loop

### Теория

- approval step;
- confidence threshold;
- escalation;
- override;
- audit trail;
- feedback collection.

### Практика

Построить BPMN/Sequence flow, где LLM предлагает классификацию, а человек подтверждает критичные случаи. Описать, что происходит при недоступности модели.

## 4. RAG Overview

### Теория

- retrieval;
- chunking;
- embeddings;
- vector search;
- grounding;
- citation;
- freshness и access control.

### Практика

Создать концептуальный RAG design для базы знаний NovaDesk. Реализация vector database не обязательна. Указать источники, ownership, обновление и права доступа.

## 5. Quality Evaluation

### Теория

- golden dataset;
- precision/recall для классификации;
- factuality/groundedness;
- rubric-based evaluation;
- offline и online evaluation;
- regression testing.

### Практика

Создать golden dataset минимум из 30 примеров. Определить acceptance threshold, error categories и ручную процедуру review.

## 6. Security и Cost Control

### Теория

- prompt injection;
- data leakage;
- PII redaction;
- model/provider access;
- retention;
- token budget;
- rate limits;
- caching;
- model routing;
- cost monitoring.

### Практика

1. Создать AI risk register минимум из 12 рисков.
2. Подготовить data handling policy.
3. Определить cost model: requests/day, average tokens, model cost assumption, monthly budget threshold.
4. Описать kill switch и fallback.

## Итоговый артефакт факультатива

```text
facultatives/ai-automation/
├── ai-use-case.md
├── structured-output-schema.json
├── hitl-bpmn.drawio
├── ai-sequence.drawio
├── rag-overview.md
├── golden-dataset.csv
├── evaluation-plan.md
├── ai-risk-register.xlsx
├── security-policy.md
└── cost-control.xlsx
```

## Критерии Done

- AI use case имеет измеримую ценность;
- structured output валидируется;
- критичные решения не принимаются моделью без контроля;
- fallback не блокирует основной процесс;
- качество оценивается на dataset, а не по отдельным примерам;
- PII, security и cost controls описаны до реализации;
- результат не называется production-ready без production-проверки.