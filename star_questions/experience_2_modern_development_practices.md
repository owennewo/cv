# Experience 2: Modern Development and Deployment Practices

**Requirement:** Experience of working with modern development and deployment practices and agile methodologies to build, test, deploy and manage services and applications

## Ideas & Options

*List potential experiences/projects that could work for this requirement:*

- DrDoctor Smart Center.  A suite of AI applications to improve NHS clinic efficiency.
- Focus on ML Ops side of things e.g. Dna model
- 

Chosen: Smart Centre

scrappy notes

The DrDoctor Smart Center was a new initiative for the newly formed AI Team of which i was team lead.  NHS clinics aim to fill 100% of their appointment slots, however this is difficult to achieve (late cancels, no shows) and admin intensive.
The new initiative aimed to predict patient attendance and intervene through additional communication/confirmations targetted at likely no-show patience.  In addition, if statistical evidence supported that a clinic could be overbooked then the system would recommend adding additional slots to the clinic.

My role as lead engineer was to identify the Azure technologies to use and to coordinate the team to develop a devops process that ensured high quality and secure code releases were enforced through repeatable CI/CD processes for both infrastucture and code.  I wrote ~50% of these pipelines incl vulnerability checks, bicep templates, DACPAC (schema deployment) and unit / system tests and a sensible PR process that encourages "small and often" releases which mapped to well defined jira tasks.
Each layer of the architecture required its own build, test and deploy consideration e.g for front end (Vue js), we used vite, vitest, cypress with pre-commit hooks for linting/unit testing.  CI would include snyk test for vuln and ? + end to end tests, CI process would package the app and run e2e against it. Our apps were instrumented using posthog, which was used to replay events before errors in users browser to find the root cause. CD would deploy to azure static app.  Both CI and CD used Azure devops templates
In addition to the standard DevOps processes, I helped develop our MLOps training, serving and monitoring pipelines. These allowed us to onboard new trusts quickly and identify and resolve issues with Trust Models before they were put into production. The ML pipelines push pipeline failures to a slack channel so that the team can respond quickly. 
The team used a light wait process with standard ceromonies: daily 10min standup, sprintly planning and retro with adhoc refinement meetings with a sprintly cross team review to share progress. We used a rota to decide who facilitated the events.

The overall process protected the team from regressions which meant that rollbacks due to unforseen issues were rare (<5%).  Most tickets could be completed in 2-3 days and this reflected in our deployment frequency.


## STAR Response

### Situation
NHS clinics struggle to achieve 100% appointment slot utilisation due to late cancellations and no-shows, creating both administrative burden and inefficient resource allocation. As team lead for DrDoctor's newly formed AI Team, I was tasked with developing the Smart Centre - a suite of AI applications that would predict patient attendance and recommend interventions to improve clinic efficiency through targeted communication and evidence-based overbooking strategies.

### Task
As Lead Engineer, I was responsible for architecting and implementing a comprehensive DevOps and MLOps infrastructure that would ensure high-quality, secure code releases through repeatable CI/CD processes. This included selecting appropriate Azure technologies, coordinating the development team, and establishing robust deployment pipelines for both traditional application code and machine learning models. I needed to create a development process that supported rapid iteration while maintaining production stability across a complex multi-layered architecture serving multiple NHS trusts.

### Action
**DevOps Infrastructure:** I designed and personally wrote approximately 50% of the CI/CD pipelines, including vulnerability scanning with Snyk, infrastructure-as-code using Bicep templates, database schema deployment via DACPAC, and comprehensive unit and system testing. I established a PR process encouraging "small and often" releases mapped to well-defined Jira tasks.

**Technology-Specific Pipelines:** Each technology layer (frontend, backend, operational db, analytical db, feature engineering, ML model) required its own build, test and deployment process. For example, for our Vue.js frontend, I implemented Vite for building, Vitest for unit testing, and Cypress for end-to-end testing, with pre-commit hooks for linting. Our CI process included vulnerability testing and end-to-end tests against packaged applications, with deployment to Azure Static Web Apps. We instrumented our applications using PostHog for product analytics, session replay and root cause analysis.


**MLOps Implementation:** I developed specialized ML training, serving, and monitoring pipelines that enabled rapid onboarding of new NHS trusts and proactive identification of model issues before production deployment. Pipeline failures were automatically routed to Slack channels for immediate team response. Incidents responses were often completed before our clients became aware of the issue.

**Agile Methodology:** This followed a lightweight scrum process with standard events including 10-minute daily standups, sprint planning, retrospectives and ad-hoc refinement meetings. We tried to keep it fresh by regularly tweaking the process and rotating the sprint facilitator. Each two-week sprint ends with a team retro and a cross-team review to share progress with stakeholders (product demos, metrics and highlights!)

### Result
Achieved exceptional deployment reliability with rollback rates below 5% due to unforeseen issues, demonstrating the effectiveness of our comprehensive testing and quality gates. Most development tickets were completed within 2-3 days, enabling high deployment frequency and rapid response to NHS trust requirements. The robust MLOps infrastructure successfully supported multiple trust onboardings with automated quality assurance, whilst the established development practices were adopted as a template for other teams within the organisation.
