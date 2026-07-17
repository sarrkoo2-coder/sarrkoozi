# Итоговый проект NovaDesk

## Сценарий

NovaDesk принимает обращения клиентов по email и в мессенджерах. Заявки регистрируются вручную, часть теряется, приоритеты определяются субъективно, SLA не контролируется, руководитель не видит реальный backlog и нагрузку команды.

Нужно спроектировать первую версию управляемого процесса обработки обращений, подготовить требования и аналитическую модель, создать backlog, dashboard и low-code-прототип.

## Обязательные артефакты

```text
portfolio/
├── 00-baseline.md
├── 01-discovery/
│   ├── problem-statement.md
│   ├── goals-kpi.md
│   ├── stakeholder-register.xlsx
│   ├── raci.xlsx
│   └── context-diagram.drawio
├── 02-requirements/
│   ├── interview-guide.md
│   ├── requirements-catalog.xlsx
│   ├── glossary.md
│   ├── assumptions-decisions.md
│   └── traceability-matrix.xlsx
├── 03-processes/
│   ├── as-is.drawio
│   ├── to-be.drawio
│   └── gap-analysis.xlsx
├── 04-backlog/
│   ├── epics-stories.csv
│   ├── acceptance-criteria.md
│   └── jira-export.csv
├── 05-data/
│   ├── source-data.xlsx
│   ├── schema.sql
│   ├── seed.sql
│   ├── queries-basic.sql
│   └── queries-joins.sql
├── 06-bi/
│   ├── novadesk-dashboard.pbix
│   └── dashboard-screenshots/
├── 07-low-code/
│   ├── solution-design.md
│   ├── test-scenarios.md
│   └── demo-screenshots/
├── 08-delivery/
│   ├── implementation-plan.mpp-or-projectlibre
│   ├── risk-register.xlsx
│   └── final-presentation.pptx
└── README.md
```

## Минимальный backlog

### Epic 1. Intake and registration

- Регистрация обращения из email.
- Ручная регистрация оператором.
- Проверка обязательных полей.
- Защита от дублей.

### Epic 2. Classification and assignment

- Категория и приоритет.
- Автоматическое назначение по очереди.
- Ручное переназначение.
- Эскалация сложных обращений.

### Epic 3. SLA and communications

- Таймер первой реакции.
- Предупреждение о риске просрочки.
- Ожидание ответа клиента.
- Ответ, подтверждение и закрытие.

### Epic 4. Management analytics

- Backlog по статусам.
- SLA compliance.
- Нагрузка исполнителей.
- Повторные обращения и категории причин.

## Требования к защите

За 7–10 минут объяснить:

1. Какую проблему решает проект.
2. Кто заинтересован и чего ожидает.
3. Что показал AS-IS.
4. Почему выбран именно такой TO-BE.
5. Как требования связаны с backlog.
6. Как данные подтверждают проблему и эффект.
7. Что реализовано в прототипе.
8. Какие ограничения и риски остались.
9. Что войдёт в следующий релиз.

## Оценка проекта

| Блок | Вес |
|---|---:|
| Problem, scope, stakeholders | 15% |
| Requirements quality and traceability | 20% |
| BPMN AS-IS/TO-BE | 15% |
| Backlog and Acceptance Criteria | 15% |
| Data, SQL and Power BI | 15% |
| Low-code design/prototype | 10% |
| Presentation and ability to defend decisions | 10% |