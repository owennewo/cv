# Experience 3: Leadership

**Requirement:** Ability to lead multidisciplinary teams to successful software delivery project outcomes

## Ideas & Options

*List potential experiences/projects that could work for this requirement:*

- Databricks design, implementation and roll out
- Leading the DNA project which was a multi year project with outside assessments from LSBU
- 

Chosen: databricks rollouto

Scrappy notes
I joined the data team (3 data engineers, 3 machins learning engineers, a data analyst and 2 product managers) as ML Lead.  The existing data engineers (no lead) were struggling with an organically grown analytics platform with Terrabyte of data residing in SQLServer with Azure Data Studio pipelines. It was expensive, difficult to deploy, slow (overnight jobs taking 12hrs) and was not scaling with the rate we were onboarding new trusts.  They knew the architecture they wanted (remove sqlserver, move to lakehouse that uses pyspark/databricks, medalion architecture), however they lacked the time and devops skills to stand this up securely.  At the same time the ML team were consuming data from legacy platform and had no option other than perform most feature engineering in stored procedures.
I championed this strategic move with our product managers and CTO to reach consensus that current impl was unsustainaple and this was strategically important 
I coordinated a 3 day hackathon with the goal of learning how we might move analytics to lakehouse.  The ML Engineers focused on CI/CD pipeline to standup lakehouse in our Azure scratchpad environment, my primary goal was to deeply understand the security aspects as this would be a key part of getting the production environment accepted by the business.  This included secure integration with ADF, SQLServer, AMLS and ADLS, RBAC with AAD integtation over Unity Catalog.  


The Data Engineers focused on the medallion architecture and how to port their scripts to pyspark.  The outcome of the hackathon was a useable scratchpad environment and the knowledge of how to roll this out safely
I prepared a rollout document with heavy emphasis on security that was assessed, revised and accepted by our Data Platform team 

I then developed the Infrastructure as code pipelines that stood up the lakehouse including the security considerations (Managed Identity, KeyVault, Private Endpoints, VPN subnets, etc), again these carefully reviewed and accepted.  Finally I wrote the CI/CD pipepine to test and push pyspark code from Azure DevOps Repos to databricks repos.  


Over the next two months, the data engineer moved their RAW data into the lakehouse with a reduction of overnight processing from 12hrs to 2hrs with estimated reduction in cort of 75%. This also unlocked the ML engineers to use pyspark for feature engineering and significantly improved the velocity of thi whole team.


## STAR Response

### Situation
I joined DrDoctor's data team as ML Lead, inheriting a multidisciplinary team of 11 people (3 data engineers, 3 machine learning engineers, 1 data analyst, and 2 product managers) who were struggling with an organically grown analytics platform. The existing system processed terabytes of data through SQL Server with Azure Data Studio pipelines, but was expensive, difficult to deploy, and critically slow - with overnight jobs taking 12 hours and failing to scale with our rapid NHS trust onboarding rate. The data engineers had no Lead and lacked the DevOps expertise needed to implement their desired lakehouse architecture, whilst ML engineers were constrained to performing feature engineering in stored procedures rather than modern tools.

### Task
As the new ML Lead, I needed to lead this multidisciplinary team through a strategic platform migration from the legacy SQL Server analytics platform to a modern Databricks lakehouse architecture using medallion patterns and PySpark. My challenge was to coordinate team members with diverse skill sets, champion the strategic importance of this migration with senior stakeholders, ensure secure implementation that would pass business security reviews, and deliver measurable performance improvements whilst maintaining ongoing operations for 50+ NHS trusts.

### Action
**Strategic Leadership:** I championed the lakehouse migration with product managers and our CTO, building consensus that the current implementation was unsustainable and securing buy-in for this strategically important transformation.

**Team Coordination & Skill Development:** I organised and led a 3-day hackathon to rapidly upskill the team and prove the concept. I strategically assigned focus areas based on team strengths - ML engineers on CI/CD pipeline development, data engineers on medallion architecture and PySpark migration, whilst I personally focused on security architecture including secure integration with ADF, SQL Server, Azure Machine Learning Services, and ADLS, plus RBAC with Azure Active Directory integration over Unity Catalog.

**Technical Implementation:** Following the successful hackathon, I prepared comprehensive rollout documentation with heavy emphasis on security that was reviewed and accepted by our Data Platform team. I personally developed the Infrastructure-as-Code pipelines that stood up the lakehouse with full security considerations including Managed Identity, KeyVault, Private Endpoints, and VPN subnets. I also created the CI/CD pipeline to test and deploy PySpark code from Azure DevOps Repos to Databricks repositories.

**Change Management:** I guided the team through the six-month migration process, ensuring knowledge transfer and maintaining service continuity for existing NHS trust operations.

### Result
Successfully led the team to deliver a transformational platform migration that reduced overnight processing times from 12 hours to 2 hours (83% improvement) with an estimated 75% reduction in infrastructure costs. The migration unlocked the ML team to use PySpark for feature engineering, significantly improving development velocity of our team and analytics capability across the entire organisation. The secure, scalable architecture successfully supported continued NHS trust onboarding, and the implementation approach became a template for build out of the rest of the medallion architecture. The team emerged more skilled and cohesive, with clear technical leadership and improved cross-functional collaboration.

