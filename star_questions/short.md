##Situation
Project: DrDoctor Insight Hub - AI-powered NHS staff portal serving 50+ NHS Trusts
NHS trusts needed better visibility into patient engagement with digital services and AI-powered tools to help staff take proactive action on patient care. DrDoctor identified an opportunity to create a new "Insight Hub" within their existing staff portal to house advanced analytics and AI applications.
##Task
I was responsible for designing and delivering a full-stack AI solution serving 50+ NHS Trusts and thousands of NHS staff. This included selecting technologies, building a development team, defining requirements with stakeholders, and contributing development work across the entire stack while establishing an AI experimentation culture.
##Action
Technology & Architecture: I implemented a modern stack including Vue.js, .NET 8 with C#, and Azure cloud services. I integrated multiple data sources using GraphQL and REST APIs, implemented Auth0 authentication, and deployed via Azure Container Apps.
Development & Leadership: I maintained active development responsibilities across C#, Python, TypeScript, HTML/CSS, SQL and DevOps YAML while leading the team. I built ML models using Azure Machine Learning Services, Databricks, and integrated OpenAI capabilities. I fostered collaboration through pair programming and worked closely with stakeholders and NHS clients.
##Result
Successfully delivered a comprehensive AI-powered portal serving 50+ NHS Trusts. A key solution was AI-powered appointment confirmations that predicted likely missed appointments and made automated patient calls using neural voice technology. This typically reduces non-attendance rates by 35%, with significant potential savings given that missed appointments cost the NHS £100 each and DrDoctor handles over 10M appointments annually.


##Situation
Project: DrDoctor Smart Centre - AI suite for NHS clinic efficiency with comprehensive DevOps/MLOps
NHS clinics struggle to achieve 100% appointment slot utilisation due to late cancellations and no-shows, creating administrative burden and inefficient resource allocation. As team lead for DrDoctor's AI Team, I was tasked with developing the Smart Centre - a suite of AI applications that would predict patient attendance and recommend interventions to improve clinic efficiency.
##Task
I was responsible for architecting and implementing comprehensive DevOps and MLOps infrastructure ensuring high-quality, secure code releases through repeatable CI/CD processes. This included selecting Azure technologies, coordinating the development team, and establishing robust deployment pipelines for both application code and machine learning models while maintaining production stability across multiple NHS trusts.
##Action
DevOps Infrastructure: I designed and personally wrote approximately 50% of the CI/CD pipelines, including vulnerability scanning, infrastructure-as-code using Bicep, database schema deployment via DACPAC, and comprehensive testing. I established a PR process encouraging "small and often" releases mapped to Jira tasks.
Technology-Specific Pipelines: Each technology layer required its own build, test and deployment process. For example Vue.js frontend used Vite for building, Vitest/Cypress for testing and PostHog for analytics.
MLOps Implementation: I developed specialized ML training, serving, and monitoring pipelines enabling rapid NHS trust onboarding and proactive issue identification being routed to Slack for immediate response.
##Result
Achieved deployment reliability with rollback below 5% and most development tickets completed within 3 days, enabling rapid response to NHS requirements. The infrastructure successfully supported multiple trust onboardings with automated quality assurance.

##Situation
Project: Databricks Lakehouse Migration - Leading 11-person multidisciplinary data team transformation
I joined DrDoctor's data team as ML Lead, inheriting a multidisciplinary team of 11 people (3 data engineers, 3 ML engineers, 1 data analyst, and 2 product managers) struggling with an organically grown analytics platform which processed terabytes of data but was expensive, difficult to deploy, and critically slow - with overnight jobs taking 12 hours and failing to scale with rapid NHS trust onboarding.
##Task
As ML Lead, I guided the team through a strategic platform migration from legacy SQL Server to modern Databricks lakehouse architecture using medallion patterns and PySpark. My challenge was to champion this migration with senior stakeholders, coordinate diverse team members, ensure regulatory security compliance, and deliver performance improvements whilst maintaining operations for 50+ NHS trusts.
##Action
Strategic Leadership: I championed the lakehouse migration with product managers and CTO, securing buy-in for this transformation.
Team Coordination: I organized a 3-day hackathon to upskill the team and prove the concept. I assigned focus areas - ML engineers on CI/CD pipelines, data engineers on medallion architecture, whilst I focused on security architecture including ADF integration, RBAC with Azure Active Directory, and Unity Catalog.
Technical Implementation: I developed IaC pipelines with comprehensive security including Managed Identity, KeyVault, and Private Endpoints. I created CI/CD pipelines for deploying PySpark code from Azure DevOps to Databricks.
##Result
Overnight processing from 12 hours to 2 hours with 75% infrastructure cost reduction. New platform significantly improved development velocity and analytics capability across the organization.