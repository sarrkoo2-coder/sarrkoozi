# Курс Junior Business Analyst: 16 недель

## Как проходить курс

На каждую неделю планируйте 8–10 часов: 2–3 часа теории, 4–5 часов практики, 1 час оформления артефакта и 1 час самопроверки. Каждая неделя завершается результатом, который можно показать на собеседовании.

## Неделя 0. Диагностика и рабочая среда

**Результат:** определён исходный уровень, создана структура портфолио и зафиксирован учебный ритм.

**Теория:** роли Business Analyst, System Analyst, Product Manager, Project Manager и QA; задачи BA в SDLC; артефакты анализа; repository, commit, branch, issue и README.

**Искать:** `business analyst role in SDLC`, `business analyst vs system analyst`, `GitHub learning tracker`.

**Практика:** оценить себя по `SKILLS_MATRIX.md`, создать `portfolio/`, описать кейс NovaDesk без предложения решения и закрепить время обучения в календаре.

**Артефакт:** `portfolio/00-baseline.md`.

**Связь:** GitHub хранит доказательства развития, baseline позволяет сравнить старт и итог.

**Done:** есть честная диагностика, расписание на четыре недели и первый commit.

---

## Неделя 1. Проблема, цели и стейкхолдеры

**Результат:** проблема отделена от решения, определены цели, KPI, границы и участники.

**Теория:** problem statement, business need, outcome/output, SMART-цели, KPI, stakeholder register, power/interest matrix, RACI, scope, assumptions, constraints, risks, context diagram.

**Искать:** `problem statement business analysis`, `stakeholder power interest matrix`, `RACI IT project`, `in scope out of scope`.

**Практика:** для NovaDesk создать problem statement, 3 цели, 5 KPI, реестр минимум 8 стейкхолдеров, RACI и границы MVP.

**Артефакты:** problem statement, goals/KPI, stakeholder register, RACI, context diagram.

**Связь:** цели станут основанием требований, KPI попадут в Power BI, стейкхолдеры станут источниками требований.

**Done:** проблема не содержит готового решения; цели измеримы; KPI связаны с целями; роли RACI непротиворечивы.

---

## Неделя 2. Выявление и управление требованиями

**Результат:** собран и структурирован первичный каталог требований.

**Теория:** интервью, workshop, observation, document analysis, survey; открытые вопросы и 5 Why; BR, UR, FR, NFR, business rules; atomic, unambiguous, feasible, testable, traceable; MoSCoW; glossary; assumptions/decision log.

**Искать:** `requirements elicitation techniques`, `functional non functional requirements`, `requirements quality checklist`, `MoSCoW prioritization`.

**Практика:** смоделировать интервью с оператором, руководителем поддержки, клиентом и IT-администратором. Создать каталог минимум из 25 требований.

**Артефакты:** interview guide, notes, requirements catalog, glossary.

**Связь:** требования будут преобразованы в backlog, BPMN и Acceptance Criteria.

**Done:** у каждого требования есть ID, тип, источник, приоритет и способ проверки.

---

## Неделя 3. Agile, Scrum, Kanban и команда полного цикла

**Результат:** понятна логика поставки ценности и выбран способ организации работы NovaDesk.

**Теория:** Agile mindset; Scrum roles/events/artifacts; Sprint Goal и Increment; Kanban flow, WIP, pull, lead time, cycle time; discovery–delivery–support; Definition of Ready и Definition of Done.

**Искать:** `Scrum Guide Russian`, `Kanban WIP lead time cycle time`, `cross functional product team`, `Definition of Ready Done`.

**Практика:** сравнить Scrum и Kanban по 8 критериям, выбрать подход и описать путь одной функции от идеи до эксплуатации.

**Артефакт:** `03-delivery-model.md`.

**Связь:** выбранный подход определит Jira-доску, workflow и метрики.

**Done:** выбор основан на характере работы; описана роль BA на каждом этапе; подготовлены DoR и DoD.

---

## Неделя 4. Epics, User Stories и Acceptance Criteria

**Результат:** требования преобразованы в управляемый backlog.

**Теория:** product goal, Epic, feature, User Story, task, bug, spike; story mapping; вертикальная декомпозиция; INVEST; Given–When–Then; MoSCoW, value/effort, dependencies.

**Искать:** `user story mapping`, `INVEST user stories`, `Given When Then acceptance criteria`, `epic feature story hierarchy`.

**Практика:** создать 3–5 Epics, минимум 12 User Stories и критерии приёмки для регистрации, классификации, SLA, эскалации, ответа и закрытия.

**Артефакт:** backlog в XLSX/CSV.

**Связь:** backlog импортируется в Jira; Acceptance Criteria становятся основой тестирования; Story связывается с requirement ID.

**Done:** истории дают ценность, имеют разумный размер и проверяемые критерии.

---

## Неделя 5. Jira и Confluence

**Результат:** создано единое пространство управления работой и документацией.

**Теория:** Jira projects, issue types, workflow, statuses, fields, components, links, filters, dashboards; Scrum/Kanban board; Confluence spaces, page tree, templates, decisions, meeting notes, specifications; traceability.

**Искать:** `Jira free Scrum tutorial`, `Jira workflow best practices`, `Confluence requirements template`, `link Jira Confluence`.

**Практика:** создать проект NovaDesk, типы Epic/Story/Task/Bug/Spike, загрузить backlog, настроить доску и структуру Confluence: Overview, Stakeholders, Requirements, Processes, Decisions, Meetings, Releases.

**Артефакты:** screenshots, Jira export, Confluence export/link.

**Связь:** Jira показывает поток реализации, Confluence хранит контекст, решения и спецификации.

**Done:** статусы отражают реальный поток; Story связаны с Epic и requirement ID; документы легко найти.

---

## Неделя 6. BPMN 2.0: основы и AS-IS

**Результат:** построена корректная модель текущего процесса.

**Теория:** process, pool, lane, events, task, subprocess, gateway, sequence flow, message flow, data object; уровни детализации и читаемость.

**Искать:** `BPMN 2.0 pools lanes gateways`, `BPMN AS IS example`, `BPMN modeling mistakes`, `draw.io BPMN tutorial`.

**Практика:** построить AS-IS обработки обращений NovaDesk из разных каналов до закрытия.

**Артефакт:** `.drawio` и PNG/PDF.

**Связь:** проблемы AS-IS создадут требования и изменения TO-BE.

**Done:** участники разделены; message flow используется корректно; шлюзы имеют условия; схема читается без устных пояснений.

---

## Неделя 7. BPMN 2.0: TO-BE, исключения и SLA

**Результат:** спроектирован целевой процесс и объяснён эффект изменений.

**Теория:** timer, message, error, escalation events; boundary events; event-based gateways; happy/alternative/exception flows; SLA; bottleneck; handoff; process KPI.

**Искать:** `BPMN timer boundary event`, `BPMN escalation`, `AS IS TO BE gap analysis`, `process KPI SLA`.

**Практика:** создать TO-BE с автоматической регистрацией, маршрутизацией, SLA-таймерами, эскалациями и контролем закрытия; подготовить gap analysis.

**Артефакты:** TO-BE diagram и gap analysis.

**Связь:** шаги TO-BE связываются с FR, User Stories, ролями, Jira и low-code-прототипом.

**Done:** обработаны минимум три исключения; SLA отражён таймерами; каждое изменение связано с проблемой или KPI.

---

## Неделя 8. Excel для бизнес-аналитика

**Результат:** исходные данные очищены, проанализированы и представлены в отчёте.

**Теория:** Excel Tables, structured references, IF/IFERROR, SUMIFS, COUNTIFS, date/text functions, VLOOKUP/XLOOKUP, Data Validation, conditional formatting, Pivot Table и Pivot Chart.

**Искать:** `Excel VLOOKUP exact match`, `Excel XLOOKUP`, `pivot table business analyst`, `SUMIFS COUNTIFS examples`.

**Практика:** создать или сгенерировать 300 обращений; очистить данные; добавить справочники; рассчитать время реакции, SLA и повторы; построить сводный отчёт.

**Артефакт:** `08-support-analysis.xlsx`.

**Связь:** те же данные используются в SQL и Power BI, KPI должны совпасть с неделей 1.

**Done:** исходные и расчётные данные разделены; формулы не содержат ручных подстановок; есть сводные таблицы, диаграммы и выводы.

---

## Неделя 9. SQL: основы

**Результат:** данные извлекаются из реляционной БД без ручной обработки.

**Теория:** table, row, column, primary/foreign key, NULL; SELECT, DISTINCT, aliases, WHERE, IN, BETWEEN, LIKE, ORDER BY, LIMIT, GROUP BY, HAVING, COUNT/SUM/AVG/MIN/MAX.

**Искать:** `SQL SELECT WHERE GROUP BY beginner`, `primary foreign key`, `SQL NULL`, `aggregate functions exercises`.

**Практика:** создать БД с таблицами tickets, clients, agents, categories, status_history и выполнить минимум 15 бизнес-запросов.

**Артефакты:** `schema.sql`, `seed.sql`, `queries-basic.sql`.

**Связь:** модель данных поддерживает требования, Power BI и low-code-сущности.

**Done:** ключи осмыслены; каждый запрос отвечает на бизнес-вопрос; результат сверён с Excel.

---

## Неделя 10. SQL JOIN и аналитические запросы

**Результат:** объединяются связанные таблицы и проверяется целостность данных.

**Теория:** INNER/LEFT/RIGHT/FULL JOIN; cardinality; дубликаты после JOIN; subquery; базовый CTE; CASE WHEN; COALESCE; data quality checks.

**Искать:** `SQL JOIN visual`, `INNER vs LEFT JOIN`, `duplicates after join`, `SQL CTE CASE WHEN`.

**Практика:** создать минимум 12 JOIN-запросов: нагрузка агентов, SLA по категориям, повторные обращения, записи без истории, среднее время по этапам.

**Артефакт:** `queries-joins.sql` и `sql-findings.md`.

**Связь:** результаты становятся источником Power BI и проверяют соответствие данных BPMN-процессу.

**Done:** объяснён выбор JOIN; проверено число строк; найдены проблемы качества данных; запросы связаны с KPI.

---

## Неделя 11. Модель данных и Power BI

**Результат:** создана корректная модель и первый интерактивный dashboard.

**Теория:** fact/dimension, star schema, relationships, cardinality, filter direction; Power Query import/merge/append/cleanup; calculated column vs measure; DAX COUNTROWS, DISTINCTCOUNT, CALCULATE, DIVIDE; KPI, slicer, drill-through.

**Искать:** `Power BI star schema`, `Power Query merge`, `DAX measure vs column`, `CALCULATE beginner`.

**Практика:** подключить данные NovaDesk, создать календарь и меры: количество обращений, SLA compliance, среднее время реакции, backlog, повторы, нагрузка.

**Артефакт:** `.pbix` и screenshots.

**Связь:** dashboard визуализирует KPI, использует SQL/Excel и показывает эффект TO-BE.

**Done:** модель близка к star schema; меры отделены от исходных столбцов; фильтры работают; есть минимум три вывода.

---

## Неделя 12. PowerPoint, Visio и MS Project

**Результат:** решение можно представить руководителю и спланировать внедрение.

**Теория:** storytelling «проблема → данные → решение → эффект → риски → следующий шаг»; executive summary; cross-functional flowchart; task, duration, dependency, milestone, baseline, resource, critical path; risk register.

**Искать:** `business analyst presentation`, `Visio cross functional flowchart`, `MS Project critical path`, `ProjectLibre Gantt tutorial`.

**Практика:** собрать презентацию 8–10 слайдов; календарный план пилота на 6–8 недель; risk register; перенести одну схему в формат, близкий к Visio.

**Артефакты:** PPTX/PDF, MPP или ProjectLibre, risk register.

**Связь:** презентация объединяет BPMN, backlog, данные и архитектуру; план задаёт порядок внедрения.

**Done:** решение понятно вне проекта; сроки следуют зависимостям; критический путь объяснён; у рисков есть owner и response.

---

## Неделя 13. Low-code и BPM-архитектура

**Результат:** понятно, как аналитическая модель превращается в приложение и исполняемый процесс.

**Теория:** low-code/no-code/custom; application, entity, record, form, process, rule, role, permission; BPM engine, process instance, timer, notification; API/webhook; master data; dev/test/prod; vendor lock-in, performance, security, governance.

**Искать:** `low code architecture entities forms workflows`, `BPM engine process instance`, `low code governance`, `API webhook integration`.

**Практика:** сопоставить TO-BE NovaDesk с сущностями, формами, процессами, ролями, правилами, интеграциями и отчётами.

**Артефакт:** solution design и logical data model.

**Связь:** требования, BPMN и ER-модель становятся спецификацией low-code-конфигурации.

**Done:** у автоматизаций есть trigger/result; права описаны по ролям; интеграции имеют error handling; ограничения зафиксированы.

---

## Неделя 14. ELMA365: учебный прототип

**Результат:** собран минимальный исполняемый прототип.

**Теория:** workspace/application, data types, forms, statuses, roles, process designer, tasks, gateways, timers, notifications, access rights, test instances.

**Искать:** `ELMA365 создание приложения`, `ELMA365 бизнес процесс`, `ELMA365 таймер SLA`, `ELMA365 обучение аналитик`.

**Практика:** в демосреде реализовать путь «регистрация → классификация → назначение → работа → ожидание клиента → закрытие» и добавить SLA-таймер с эскалацией.

**Артефакты:** screenshots/video, configuration map, test protocol.

**Связь:** прототип проверяет выполнимость BPMN, требований и модели данных.

**Done:** процесс проходит end-to-end; права ролей проверены; таймер протестирован; расхождения возвращены в требования.

---

## Неделя 15. BPMSoft и сравнение платформ

**Результат:** сформировано независимое от вендора понимание low-code и критерии выбора.

**Теория:** CRM/BPM-контур BPMSoft; объектная модель, процессы, роли, интеграции, аналитика; product fit, total cost, implementation complexity, ecosystem, support, compliance; RFP criteria.

**Искать:** `BPMSoft школа low-code аналитик`, `BPMSoft бизнес процессы`, `ELMA365 BPMSoft сравнение`, `low code platform selection`.

**Практика:** по учебным материалам и демо сравнить ELMA365 и BPMSoft минимум по 15 взвешенным критериям и подготовить recommendation memo.

**Артефакт:** comparison matrix и memo.

**Связь:** бизнес-требования превращаются в критерии платформы, а не подгоняются под знакомый продукт.

**Done:** отделены факты, предположения и вопросы к вендору; учтены масштаб, бюджет, интеграции и компетенции команды.

---

## Неделя 16. Итоговый кейс, портфолио и собеседование

**Результат:** готов цельный кейс Junior BA для работодателя.

**Теория:** portfolio case structure; STAR/CAR; объяснение перехода в BA через выполняемые функции и результаты; типовые вопросы интервью.

**Искать:** `business analyst portfolio case study`, `junior BA interview questions`, `STAR method project`, `traceability matrix interview`.

**Практика:** собрать структуру `CAPSTONE.md`; проверить цепочку problem → KPI → requirements → BPMN → backlog → data → dashboard → prototype; записать защиту 7–10 минут; подготовить 20 вопросов/ответов; обновить резюме.

**Артефакты:** final README, presentation, demo video, interview notes, final skills matrix.

**Связь:** финал показывает не отдельные инструменты, а сквозную работу аналитика.

**Done:** нет противоречий между артефактами; отсутствуют конфиденциальные данные; кейс понятен без пояснений; readiness score не ниже 70.

# Контрольные точки

## После недели 4

Объяснить роль BA и SDLC, провести учебное интервью, оформить качественное требование, декомпозировать Epic и защитить выбранный Agile-подход.

## После недели 8

Показать Jira/Confluence, объяснить AS-IS/TO-BE, связать BPMN с требованиями и backlog, показать Excel-анализ.

## После недели 12

Написать JOIN-запрос, объяснить модель данных, показать Power BI, представить план внедрения и риски.

## После недели 16

Защитить сквозной кейс, пройти пробное интервью, опубликовать портфолио и составить план закрытия пробелов.