## Experience 1: Digital Service Development

**Requirement:** Demonstratable experience of digital service development using one or more programming languages, frameworks or application platforms

**Project:** DrDoctor Insight Hub - AI-powered NHS staff portal serving 50+ NHS Trusts

### Situation
NHS trusts needed better visibility into patient engagement with digital services and required AI-powered tools to help staff take proactive action on patient care. DrDoctor identified an opportunity to create a new "Insight Hub" within their existing staff portal to house advanced analytics and AI applications that could transform how NHS staff manage patient interactions.

### Task
As Technical Lead, I was responsible for designing and delivering a full-stack AI solution that would serve 50+ NHS Trusts and thousands of NHS staff. My task included selecting appropriate technologies, building a high-performing development team, working with stakeholders to define requirements, and personally contributing to development across the entire stack while establishing an experimentation culture for AI innovation.

### Action
**Technology Selection & Architecture:** I selected and implemented a modern technology stack including Vue.js with TypeScript for the frontend, .NET 8 with C# for the backend, and Azure cloud services for scalable deployment. I integrated multiple data sources using GraphQL and REST APIs, implemented secure authentication via Auth0, and deployed using Azure Container Apps.

**Hands-on Development:** While leading the team, I maintained active development responsibilities, regularly committing code in C#, Python, TypeScript, and HTML/CSS, SQL and DevOps YAML. I built ML models using Azure Machine Learning Services, Databricks, and integrated OpenAI capabilities for advanced automation features.

**Team Leadership & Collaboration:** I fostered a collaborative development approach through pair programming sessions when team members needed support and delegated effectively to leverage each team member's strengths. I worked closely with both internal stakeholders and NHS clients to ensure the solution met real-world needs.

**Innovation Culture:** I established an experimentation process that allowed us to test how new AI technologies could automate repetitive administrative tasks, which was later rolled out as a framework for other development teams to follow.

### Result
Successfully delivered a comprehensive AI-powered portal serving 50+ NHS Trusts and thousands of NHS staff. An example of an end-to-end solution is the AI-powered appointment confirmations worklist/automated process which predicted patients that are likely to miss their appointment and made outbound phone calls with a next-gen neural voice in order to confirm their appointments. This type of targetted intervention typically reduces DNA rates by 35% for NHS Trusts, and the automated calls provides scale beyond what is possible by stretched booking teams. Given that a single missed appointment costs the NHS £100 and DrDoctor handles over 10M outpatient appointments a year, the potential savings and reduction to the 7.5M appointment waiting list is massive

---

## Experience 2: Modern Development and Deployment Practices

**Requirement:** Experience of working with modern development and deployment practices and agile methodologies to build, test, deploy and manage services and applications

**Project:** DrDoctor Smart Centre - AI suite for NHS clinic efficiency with comprehensive DevOps/MLOps

### Situation
NHS clinics struggle to achieve 100% appointment slot utilisation due to late cancellations and no-shows, creating both administrative burden and inefficient resource allocation. As team lead for DrDoctor's newly formed AI Team, I was tasked with developing the Smart Centre - a suite of AI applications that would predict patient attendance and recommend interventions to improve clinic efficiency through targeted communication and evidence-based overbooking strategies.

### Task
As Lead Engineer, I was responsible for architecting and implementing a comprehensive DevOps and MLOps infrastructure that would ensure high-quality, secure code releases through repeatable CI/CD processes. This included selecting appropriate Azure technologies, coordinating the development team, and establishing robust deployment pipelines for both traditional application code and machine learning models. I fostered a development process that supported rapid iteration while maintaining production stability across a complex multi-layered architecture serving multiple NHS trusts.

### Action
**DevOps Infrastructure:** I designed and personally wrote approximately 50% of the CI/CD pipelines, including vulnerability scanning with Snyk, infrastructure-as-code using Bicep templates, database schema deployment via DACPAC, and comprehensive unit and system testing. I established a PR process encouraging "small and often" releases mapped to well-defined Jira tasks.

**Technology-Specific Pipelines:** Each technology layer (frontend, backend, operational db, analytical db, feature engineering, ML model) required its own build, test and deployment process. For example, for our Vue.js frontend, I implemented Vite for building, Vitest for unit testing, and Cypress for end-to-end testing, with pre-commit hooks for linting. Our CI process included vulnerability testing and end-to-end tests against packaged applications, with deployment to Azure Static Web Apps. We instrumented our applications using PostHog for product analytics, session replay and root cause analysis.

**MLOps Implementation:** I developed specialized ML training, serving, and monitoring pipelines that enabled rapid onboarding of new NHS trusts and proactive identification of model issues before production deployment. Pipeline failures were automatically routed to Slack channels for immediate team response. Incidents responses were often resolved before our clients became aware of the issue.

**Agile Methodology:** We adopted a lightweight scrum process with 10-minute daily standups, sprint planning and ad-hoc refinement meetings. We tried to keep it fresh by regularly tweaking the process and rotating the sprint facilitator. Each two-week sprint ends with a team retro and a cross-team review to share progress with stakeholders (product demos, metrics and highlights!)

### Result
Achieved exceptional deployment reliability with rollback rates below 5% due to unforeseen issues, demonstrating the effectiveness of our automated testing and quality gates. Most development tickets were completed within 2-3 days, enabling high deployment frequency and rapid response to NHS trust requirements. The robust MLOps infrastructure successfully supported multiple trust onboardings with automated quality assurance, whilst the established development practices were adopted as a template for other teams within the organisation.

---

## Experience 3: Leadership

**Requirement:** Ability to lead multidisciplinary teams to successful software delivery project outcomes

**Project:** Databricks Lakehouse Migration - Leading 11-person multidisciplinary data team transformation

### Situation
I joined DrDoctor's data team as ML Lead, inheriting a multidisciplinary team of 11 people (3 data engineers, 3 machine learning engineers, 1 data analyst, and 2 product managers) who were struggling with an organically grown analytics platform. The existing system processed terabytes of data through SQL Server with Azure Data Studio pipelines, but was expensive, difficult to deploy, and critically slow - with overnight jobs taking 12 hours and failing to scale with our rapid NHS trust onboarding rate. The data engineers had no Lead Engineer and lacked the DevOps expertise needed to implement their desired lakehouse architecture, whilst ML engineers were forced to write overly complicated feature engineering in stored procedures for lack of modern tools.

### Task
As the new ML Lead, I guided this multidisciplinary team through a strategic platform migration from the legacy SQL Server analytics platform to a modern Databricks lakehouse architecture using medallion patterns and PySpark. My challenge was to champion the strategic importance of this migration with senior stakeholders, coordinate team members with diverse skill sets, ensure implementation is in line with internal and regulatory security standards, and deliver measurable performance improvements whilst maintaining ongoing operations for 50+ NHS trusts.

### Action
**Strategic Leadership:** I championed the lakehouse migration with product managers and our CTO, building consensus that the current implementation was unsustainable and securing buy-in for this strategically important transformation.

**Team Coordination & Skill Development:** I organised and led a 3-day hackathon to rapidly upskill the team and prove the concept. I strategically assigned focus areas based on team strengths - ML engineers on CI/CD pipeline development, data engineers on medallion architecture and PySpark migration, whilst I personally focused on security architecture including secure integration with ADF, SQL Server, Azure Machine Learning Services, and ADLS, plus RBAC with Azure Active Directory integration over Unity Catalog.

**Technical Implementation:** Following the successful hackathon, I prepared comprehensive rollout documentation with heavy emphasis on security that was reviewed and accepted by our Data Platform team. I personally developed the Infrastructure-as-Code pipelines that stood up the lakehouse with full security considerations including Managed Identity, KeyVault, Private Endpoints, and VPN subnets. I also created the CI/CD pipeline to test and deploy PySpark code from Azure DevOps Repos to Databricks repositories.

**Change Management:** I guided the team through the six-month migration process, ensuring knowledge transfer and maintaining service continuity for existing NHS trust operations.

### Result
Successfully led the team to deliver a transformational platform migration that reduced overnight processing times from 12 hours to 2 hours (83% improvement) with an estimated 75% reduction in infrastructure costs. The migration unlocked the ML team to use PySpark for feature engineering, significantly improving development velocity of our team and analytics capability across the entire organisation. The secure, scalable architecture successfully supported continued NHS trust onboarding, and the implementation approach became a template for build out of the rest of the medallion architecture. The team emerged more skilled and cohesive, with clear technical leadership and improved cross-functional collaboration.

---

## Summary

All three experiences demonstrate comprehensive technical leadership capabilities across:

- **Digital Service Development**: Full-stack AI solutions serving 50+ NHS trusts
- **Modern Development Practices**: DevOps/MLOps with <5% rollback rates and 2-3 day delivery cycles  
- **Leadership**: Successfully leading 11-person multidisciplinary teams through complex platform migrations

Each project delivered measurable improvements to NHS healthcare services whilst establishing scalable, secure technical foundations for continued growth.