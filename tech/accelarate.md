# Accelerate: The Science of Lean Software and DevOps: Building and Scaling High Performing Technology Organizations

## Nicole Forsgren PhD, Jez Humble, and Gene Kim

    If I am a senior leader and my team doesn’t feel comfortable sharing risks,
    then I will never truly know reality. And, if I’m not genuinely curious and
    only show up when there’s a failure, then I am failing

## QUICK REFERENCE

MEASURES OF DELIVERY PERFORMANCE
- **delivery lead time**
- **deployment frequency**
- **time to restore service**
- **change fail rate**

CAPABILITIES TO DRIVE IMPROVEMENT
- Continuous delivery 
- Architecture 
- Product and Process 
- Lean Management and Monitoring 
- Cultural

![Figure A.1: Overall Research Program](media/accelerate.png)

![High-Performance Team, Management, and Leadership Behaviors and Practices](media/accelerate_practices.png)

### CONTINUOUS DELIVERY CAPABILITIES 
- Version control: Chapter 4 
- Deployment automation: Chapter 4 
- Continuous integration: Chapter 4 
- Trunk-based development: Chapter 4 
- Test automation: Chapter 4 
- Test data management: Chapter 4 
- Shift left on security: Chapter 6 
- Continuous delivery (CD): Chapter 4 

### ARCHITECTURE CAPABILITIES 
- Loosely coupled architecture: Chapter 5 
- Empowered teams: Chapter 5 

### PRODUCT AND PROCESS CAPABILITIES 
- Customer feedback: Chapter 8 
- Value stream: Chapter 8 
- Working in small batches: Chapter 8 
- Team experimentation: Chapter 8 

### LEAN MANAGEMENT AND MONITORING CAPABILITIES 
- Change approval processes: Chapter 7 
- Monitoring: Chapter 7 
- Proactive notification: Chapter 13 
- WIP limits: Chapter 7 
- Visualizing work: Chapter 7 

### CULTURAL CAPABILITIES 
- Westrum organizational culture: Chapter 3 
- Supporting learning: Chapter 10 
- Collaboration among teams: Chapters 3 and 5 
- Job satisfaction: Chapter 10 
- Transformational leadership: Chapter 11

## CHAPTER 1 ACCELERATE

### FOCUS ON CAPABILITIES, NOT MATURITY

The key to successful change is measuring and understanding the right things
with a focus on capabilities—not on maturity.

Importance of focusing on capabilities is due to four factors.

First, maturity models focus on helping an organization “arrive” at a mature
state and then declare themselves done with their journey, whereas technology
transformations should follow a **continuous improvement** paradigm.

Second, maturity models are quite often a “lock-step” or linear formula,
prescribing a similar set of technologies, tooling, or capabilities for every
set of teams and organizations to progress through.
- Maturity models assume that “Level 1” and “Level 2” look the same across all
  teams and organizations,
- capability models are **multidimensional and dynamic**, allowing different
  parts of the organization to take a customized approach to improvement, and
  focus on capabilities that will give them the most benefit based on their
  current context

Third, capability models focus on key outcomes and how the capabilities, or
levers, drive improvement in those outcomes—that is, they are **outcome based**.
- maturity models simply measure the technical proficiency or tooling install
  base in an organization without tying it to outcomes.

Fourth, **maturity models define a static level** of technological, process, and
organizational abilities to achieve.

### EVIDENCE-BASED TRANSFORMATIONS FOCUS ON KEY CAPABILITIES

High performers understand that they **don’t have to trade speed for
stability** or vice versa, because **by building quality in they get both**.


Yellow highlight | Location: 447
## CHAPTER 2 MEASURING PERFORMANCE

### THE FLAWS IN PREVIOUS ATTEMPTS TO MEASURE PERFORMANCE

First, they focus on outputs rather than outcomes.

Second, they focus on individual or local measures rather than team or global
ones.
- three examples: lines of code, velocity, and utilization.

Queue theory in math tells us that **as utilization approaches 100%, lead times
approach infinity—in other words**, once you get to very high levels of
utilization, it takes teams exponentially longer to get anything done.

### MEASURING SOFTWARE DELIVERY PERFORMANCE

A successful measure of performance should have two key characteristics.

First, it should focus on a global outcome to ensure teams aren’t pitted
against each other.
- classic example is rewarding developers for throughput and operations for
  stability:
- contributor to the “wall of confusion” in which development throws poor
  quality code over the wall to operations, and operations puts in place
  painful change management processes

Second, our measure should focus on outcomes not output:
- shouldn’t reward people for putting in large amounts of busywork that doesn’t
  actually help achieve organizational goals.
- measures of delivery performance that meet these criteria, we settled on
  four: **delivery lead time, deployment frequency, time to restore service, and
  change fail rate**.

### LEAD TIME

Lead time is the time it takes to go from a customer making a request to the request being satisfied.
- two parts to lead time: the time it takes to design and validate a product or feature, and the time to deliver the feature to customers.
- design part of the lead time, it’s often unclear when to start the clock, and often there is high variability.
- the “fuzzy front end”
- delivery part of the lead time—the time it takes for work to be implemented, tested, and delivered—is easier to measure and has a lower variability.

**Design vs. Delivery**

Product Design and Development 
- Create new products and services that solve customer problems using
  hypothesis-driven delivery, modern UX, design thinking.
- Feature design and implementation may require work that has never been
  performed before.
- Estimates are highly uncertain.
- Outcomes are highly variable.

Product Delivery (Build, Testing, Deployment)
- Enable fast flow from development to production and reliable releases by
  standardizing work, and reducing variability and batch sizes.
- Integration, test, and deployment must be performed continuously as quickly
  as possible. 
- Cycle times should be well-known and predictable.
- Outcomes should have low variability.

Shorter product delivery lead times are better since they enable faster feedback

Short lead times are also important when there is a defect or outage

measure product delivery lead time as the time it takes to go from code committed to code successfully running in production

### DEPLOYMENT FREQUENCY 

Batch size is hard to measure and communicate across contexts as there is no
visible inventory.

Therefore, we settled on deployment frequency as a proxy

### MEAN TIME TO RESTORE

How quickly can service be restored for the primary application or service they
work on when a service incident (e.g., unplanned outage, service impairment)
occurs, offering the same options as for lead time (above).

### CHANGE FAIL RATE            

Finally, a key metric when making changes to systems is what percentage of
changes to production (including, for example, software releases and
infrastructure configuration changes) fail.

### Software Delivery Perofrmance for 2017

High Performers:
- Deployment Frequency: On demand (x time per day)
- Lead Time for Changes: Less than 1 hour
- MTTR: Less than 1 hour
- Change Failure Rate: 0-15%

Medium Performers:
- Deployment Frequency: 1-4 times per month
- Lead Time for Changes: 1 week to 1 month
- MTTR: Less than 1 day
- Change Failure Rate: 0-15%

Low Performers:
- Deployment Frequency: 1-4 times per month
- Lead Time for Changes: 1 week to 1 month
- MTTR: 1 day to 1 week
- Change Failure Rate: 31-45%

Note: Lower performer were lower on average but had the same median as medium

Note: There is no tradeoff between improving performance and achieving higher
levels of stability and quality.

### THE IMPACT OF DELIVERY PERFORMANCE ON ORGANIZATIONAL PERFORMANCE

Survey respondents were asked to rate their organization’s relative performance
across several dimensions: profitability, market share, and productivity.
- This measure of org perf has been found to be highly correlated to measures
  of return on investment (ROI),
- high-performing organizations were consistently twice as likely to exceed
  these goals as low performers.
- high performers were also twice as likely to exceed objectives in quantity of
  goods and services, operating efficiency, customer satisfaction, quality of
  products or services, and achieving organization or mission goals.

The fact that software delivery performance matters provides a **strong
argument against outsourcing the development of software that is strategic** to
your business, and instead bringing this capability into the core of your
organization.

In contrast, **most software used by businesses** (such as office productivity
software and payroll systems) **are not strategic** and should in many cases be
acquired using the software-as-a-service

## CHAPTER 3 MEASURING AND CHANGING CULTURE

### MODELING AND MEASURING CULTURE

**Westrum**'s typology of organizational cultures
- Pathological (power-oriented)
- Bureaucratic (rule-oriented)
- Generative (performance-oriented)

Three characteristics of good information:
- It provides **answers** to the questions that the receiver needs answered. 
- It is **timely**. 
- It is presented in such a way that it can be **effectively** used by the
  receiver.

Additional insight from Westrum was that **this definition of organizational
culture predicts performance outcomes**.

Table 3.1 Westrums Typology of Organizational Culture.

    |                   | Pathological (Power oriented) | Bureaucratic (Rule oriented)  | Generative (Performance oriented) |
    | --                | --                            | --                            | --                                |
    | Cooperation       | Low                           | Modest                        | High                              |
    | Messengers        | "shot"                        | neglected                     | trained                           |
    | Responsibilities  | shirked                       | narrow                        | shared                            |
    | Bridging          | discouraged                   | tolerated                     | encouraged                        |
    | Failure leads to  | scapegoating                  | justice                       | inquiry                           |
    | Novelty           | crushed                       | leads to problems             | implemented                       |

### MEASURING CULTURE

In order to measure the culture of organizations, we take advantage of the fact
that these types form “points on a scale . . . a `Westrum continuuam`

Likert-Type Questions for Measuring Culture (1-7 scale from strongly disagree
to strongly agree)
- Information is actively sought
- Messengers are not punished when they deliver news of failure or other bad
  news
- Responsibilities are shared
- Cross functional collaboration is encouraged and rewarded
- Failure causes inquiry
- New ideas are welcomed
- Failures are treated primarily as opportunities to improve the system

Calculate the **mean** across all questions and perform **statistical analysis** on the responses as a whole.

Culture enables information processing through three mechanisms.
- First, in organizations with a generative culture, **people collaborate**
  more effectively and there is a higher level of trust both across the
  organization and up and down the hierarchy.
- Second, generative culture emphasizes the mission, an emphasis that allows
  people involved to put aside their personal issues and also the departmental
  issues that are so evident in bureaucratic organizations. The **mission is
  primary**.
- Third, generativity encourages a **‘level playing field,’** in which
  hierarchy plays less of a role”

Bureaucracy is not necessarily bad.
- goal of bureaucracy is to “ensure fairness by applying rules to
  administrative behavior.
- rules would impose efficient structures and processes while guaranteeing
  fairness and eliminating arbitrariness”

### WHAT DOES WESTRUM ORGANIZATIONAL CULTURE PREDICT?

Westrum’s theory posits that **organizations with better information flow function more effectively**.

First, a good culture requires trust and cooperation between people across the
organization, so it reflects the level of collaboration and trust inside the
organization.

Second, better organizational culture can indicate higher quality
decision-making. Not only is better information available for making
decisions, but those decisions are more easily reversed if they turn out to be
wrong

Finally, teams with these cultural norms are likely to do a better job with
their people, since problems are more rapidly discovered and addressed.

### CONSEQUENCES OF WESTRUM‘S THEORY FOR TECHNOLOGY ORGANIZATIONS

Google started a two-year research project to investigate what made teams
effective,
- expected to find a combination of individual traits and skills that would be
  key
- instead found **who is on a team matters less than how the team members
  interact, structure their work, and view their contributions**

In other words, it all comes down to **team dynamics**.

### HOW DO WE CHANGE CULTURE?

Our research shows that **Lean management**, along with a set of other technical
practices known collectively as continuous delivery (Humble and Farley 2010),
do in fact impact culture,

## CHAPTER 4 TECHNICAL PRACTICES

### WHAT IS CONTINUOUS DELIVERY?

Five key principles of CD:
- Build quality in.
- “Cease dependence on inspection to achieve quality.
- Work in small batches.
- Relentlessly pursue continuous improvement.
- Everyone is responsible.

A key goal of continuous delivery is changing the economics of the software
delivery process so the **cost of pushing out individual changes is very low**.

    Computers perform repetitive tasks; people solve problems.

In order to implement continuous delivery, we must create the following
foundations:
- Comprehensive configuration management.
- Continuous integration (CI).
- Trunk based development
- branches short-lived (less than one day’s work) and integrate them into
  trunk/master frequently.
- Continuous testing.
- Automated unit and acceptance tests
- Testers should be performing exploratory testing continuously
- Testers work alongside developers to evolve tests

### THE IMPACT OF CONTINUOUS DELIVERY

- Teams can deploy to production (or to end users) on demand,
- Fast feedback on the quality and deployability of the system is available to everyone on the team,
- A loosely coupled, well-encapsulated architecture
- Teams that can choose their own tools

Teams that did well at continuous delivery achieved the following outcomes:
- Strong identification with the organization
- Higher levels of software delivery performance (lead time, deploy frequency, time to restore service)
- Lower change fail rates
- A generative, performance-oriented culture

## CHAPTER 5 ARCHITECTURE

High performance is possible with all kinds of systems, provided that
systems—and the teams that build and maintain them—are **loosely coupled**.

### FOCUS ON DEPLOYABILITY AND TESTABILITY

These characteristics of architectural decisions, which we refer to as
testability and deployability, are important in creating high performance.  

Whether teams can:
- Make large-scale changes to the design of their system without the permission
  of somebody outside the team
- Make large-scale changes to the design of their system without depending on
  other teams to make changes in their systems or creating significant work for
  other teams
- Complete their work without communicating and coordinating with people
  outside their team
- Deploy and release their product or service on demand, regardless of other
  services it depends upon
- Do most of their testing on demand, without requiring an integrated test
  environment
- Perform deployments during normal business hours with negligible downtime
- architecture and teams are loosely coupled.
- ensure delivery teams are cross-functional, with all the skills necessary

“organizations which design systems . . . are constrained to produce designs
which are copies of the communication structures of these organizations”
(Conway 1968).

**Inverse Conway Maneuver** which states that organizations should evolve their
team and organizational structure to achieve the desired architecture.

Architectural approaches that enable this strategy include the use of **bounded
contexts** and **APIs** and the use of **test doubles** and **virtualization**

A loosely coupled architecture enables scaling: As the number of developers
increases, we found: Low performers deploy with decreasing frequency. Medium
performers deploy at a constant frequency. High performers deploy at a
significantly increasing frequency.

### ALLOW TEAMS TO CHOOSE THEIR OWN TOOLS

- Upsides of delegating tool choice to teams may outweigh the disadvantages.
- There is a place for standardization, particularly around the architecture
  and configuration of infrastructure.
- teams that build security into their work also do better at continuous
  delivery.
- ensuring that information security teams make preapproved, easy-to-consume
  libraries, packages, toolchains, and processes available for developers and
  IT operations to use

### ARCHITECTS SHOULD FOCUS ON ENGINEERS AND OUTCOMES, NOT TOOLS OR TECHNOLOGIES

Discussions around architecture often focus on tools and technologies. Research shows that these are **wrong questions to focus** on.

## CHAPTER 6 INTEGRATING INFOSEC INTO THE DELIVERY LIFECYCLE

### SHIFTING LEFT ON SECURITY

First, security reviews are conducted for all major features, and this review
process is performed in such a way that it doesn’t slow down the development
process.

Second aspect of this capability: information security should be integrated
into the entire software delivery lifecycle from development through
operations.

Finally, we want to make it easy for developers to do the right thing when it
comes to infosec. This can be achieved by ensuring that there are
**easy-to-consume, preapproved libraries, packages, toolchains, and
processes**.

Shift from information security teams doing the security reviews themselves to
**giving the developers the means to build security in**.

High performers were spending 50% less time remediating security issues than low performers.

### THE RUGGED MOVEMENT

Rugged DevOps is the combination of DevOps with the Rugged Manifesto.

## CHAPTER 7 MANAGEMENT PRACTICES FOR SOFTWARE

### LEAN MANAGEMENT

- Limiting work in progress (WIP), and using these limits to drive 
  - process improvement and 
  - increase throughput 
- Creating and maintaining visual displays 
  - showing key quality and productivity metrics and 
  - the current status of work (including defects), 
  - making these visual displays available to both engineers and leaders, and 
  - aligning these metrics with operational goals
- Using data from application performance and infrastructure monitoring tools
  to make business decisions on a daily basis

WIP limits on their own do not strongly predict delivery performance. It’s only
**when they’re combined** with the use of visual displays and have a feedback
loop from production monitoring tools back to delivery teams or the business
that we see a strong effect.

### IMPLEMENT A LIGHTWEIGHT CHANGE MANAGEMENT PROCESS

Approval only for high-risk changes was not correlated with software delivery performance.

Teams that reported no approval process or used peer review achieved higher software delivery performance.

Finally, teams that required approval by an external body achieved lower performance.

Our recommendation based on these results is to use a lightweight change
approval process based on peer review, such as pair programming or intrateam
code review, combined with a deployment pipeline to detect and reject bad
changes.

## CHAPTER 8 PRODUCT DEVELOPMENT

- Building and validating prototypes from the beginning, 
- working in small batches, and 
- evolving or “pivoting” products and the business models behind them early and
  often.

### LEAN PRODUCT DEVELOPMENT PRACTICES

- The extent to which teams slice up products and features into **small
  batches** that can be completed in less than a week and released frequently,
  including the use of MVPs (minimum viable products). 
- Whether teams have a good understanding of the **flow of work** from the
  business all the way through to customers, and whether they have
  **visibility** into this flow, including the **status** of products and
  features. 
- Whether organizations actively and regularly seek **customer feedback** and
  **incorporate** this feedback into the design of their products. 
- Whether development teams have the **authority** to create and change
  specifications as part of the development process without requiring approval.

Figure 8.1: Components of Lean Product Management

    Work in Small Batches
    Make Flow of Work Visible
    Gather & Implement Customer Feedback
    Team Experimentation

**Team Autonomy**: The ability of teams to try out new ideas and create and
update specifications during the development process, without requiring the
approval of people outside the team.

### EFFECTIVE PRODUCT MANAGEMENT DRIVES PERFORMANCE

The virtuous cycle of increased delivery performance and Lean product
management practices drives better outcomes for your organization

## CHAPTER 9 MAKING WORK SUSTAINABLE

### DEPLOYMENT PAIN

We found that where code deployments are most painful, you’ll find the poorest
software delivery performance, organizational performance, and culture.

Fundamentally, most deployment problems are caused by a complex, brittle
deployment process.

- First, software is often not written with deployability in mind.
- Second, the probability of a failed deployment rises substantially when
  manual changes must be made
- Finally, complex deployments often require multiple handoffs between teams,
  particularly in siloed organizations

In order to reduce deployment pain, we should: 
- Build systems that are **designed to be deployed easily** into multiple
  environments, can detect and **tolerate failures** in their environments, and
  can have various **components of the system updated independently** 
- Ensure that the **state of production systems** can be reproduced (with the
  exception of production data) in an **automated** fashion from information in
  version control 
- Build **intelligence** into the application and the platform so that the
  deployment process can be as simple as possible

### COMMON PROBLEMS THAT CAN LEAD TO BURNOUT

Six organizational risk factors that predict burnout (Leiter and Maslach 2008):
-  **Work overload**: job demands exceed human limits.
-  **Lack of control**: inability to influence decisions that affect your job.
-  **Insufficient rewards**: insufficient financial, institutional, or social
   rewards.
-  **Breakdown of community**: unsupportive workplace environment.
-  **Absence of fairness**: lack of fairness in decision-making processes.
-  **Value conflicts**: mismatch in organizational values and the individual’s
   values.

Most organizations try to fix the person and ignore the work environment, even
though her research shows that **fixing the environment has a higher likelihood
of success**.

## CHAPTER 10 EMPLOYEE SATISFACTION, IDENTITY, AND ENGAGEMENT

### EMPLOYEE LOYALTY

employees in high-performing organizations were 2.2 times more likely to
recommend their organization as a great place to work,

### MEASURING NPS

Single **question**: How likely is it that you would recommend our
company/product/service to a friend or colleague?
- Customers who give a score of 9 or 10 are considered promoters.
- Those giving a score of 7 or 8 are passives.
- Score from 0 to 6 are detractors.

In our study, we asked two questions to capture the employee Net Promoter
Score: Would you recommend your ORGANIZATION as a place to work to a friend or
colleague? Would you recommend your TEAM as a place to work to a friend or
colleague?

Employee NPS was significantly correlated with the following constructs:
- The extent to which the organization collects **customer feedback** and uses
  it to inform the design of products and features
- The ability of teams to **visualize and understand the flow** of products or
  features through development all the way to the customer
- The extent to which **employees identify** with their organization’s values
  and goals, and the **effort they are willing to put in** to make the
  organization successful

### CHANGING ORGANIZATIONAL CULTURE AND IDENTITY

We asked people the extent to which they agreed with the following statements
(adapted from Kankanhalli et al. 2005):
- I am glad I chose to work for this organization rather than another company.
- I talk of this organization to my friends as a great company to work for.
- I am willing to put in a great deal of effort beyond what is normally
  expected to help my organization be successful.
- I find that my values and my organization’s values are very similar.
- In general, the people employed by my organization are working toward the
  same goal.
- I feel that my organization cares about me.

Used a Likert-type scale to measure agreement or disagreement with these
statements.

What this tells us is a sense of identity can help reduce burnout by **aligning
personal and organizational values**

In contrast to the way many companies still work: requirements are handed down
to development teams who must then deliver large stacks of work in batches. 

In this model, employees feel little control over the products they build and
the customer outcomes they create, and little connection to the organizations

### DIVERSITY IN TECH-WHAT OUR RESEARCH FOUND

Research shows that teams with more diversity with regard to gender or
underrepresented minorities are smarter (Rock and Grant 2016), achieve better
team performance (Deloitte 2013), and achieve better business outcomes (Hunt et
al. 2015).


It is also important to note that diversity is not enough. Teams and
organizations must also be inclusive. An inclusive organization is one where
“all organizational members feel welcome and valued for who they are and what
they ’bring to the table.’

### WOMEN IN DEVOPS

research linking the presence of women in leadership positions to higher
financial performance (McGregor 2014), stock market performance (Covert July
2014), and hedge fund returns (Covert January 2014).

Teams with more women tended to fall above average on the collective intelligence scale (Woolley and Malone 2011).

## CHAPTER 11 LEADERS AND MANAGERS

A **good leader** affects a team’s ability to deliver code, architect good
systems, and apply Lean principles to how the team manages its work and
develops products.
- Establishing and supporting generative and **high-trust cultural norms**
- Creating technologies that **enable developer productivity**, reducing code
  deployment lead times and supporting more reliable infrastructures
- Supporting team **experimentation and innovation**, and creating and
  implementing better products faster
- Working across organizational silos to achieve **strategic alignment**

(Rafferty and Griffin 2004).  According to this model, the five characteristics
of a transformational leader are:
- **Vision**. Has a clear understanding of where the organization is going and
  where it should be in five years.
- **Inspirational communication**. Communicates in a way that inspires and
  motivates, even in an uncertain or changing environment.
- **Intellectual stimulation**. Challenges followers to think about problems in
  new ways.
- **Supportive leadership**. Demonstrates care and consideration of followers’
  personal needs and feelings.
- **Personal recognition**. Praises and acknowledges achievement of goals and
  improvements in work quality; personally compliments others when they do
  outstanding work.

Measured transformational leadership using survey questions adapted from Rafferty and Griffin (2004). My leader or manager: 
- (Vision) 
  - Has a clear understanding of where we are going?
  - Has a clear sense of where he/she wants our team to be in five years?
  - Has a clear idea of where the organization is going. 
- (Inspirational communication)
  - Says things that make employees proud to be a part of this organization?
  - Says positive things about the work unit?
  - Encourages people to see changing environments as situations full of opportunities. 
- (Intellectual stimulation)
  - Challenges me to think about old problems in new ways?
  - Has ideas that have forced me to rethink some things that I have never questioned before?
  - Has challenged me to rethink some of my basic assumptions about my work. 
- (Supportive leadership)
  - Considers my personal feelings before acting?
  - Behaves in a manner which is thoughtful of my personal needs?
  - Sees that the interests of employees are given due consideration?
- (Personal recognition)
  - Commends me when I do a better than average job?
  - Acknowledges improvement in my quality of work?
  - Personally compliments me when I do outstanding work?

Managers, in particular, play a critical role in **connecting the strategic
objectives** of the business to the work their teams do.

### TIPS TO IMPROVE CULTURE AND SUPPORT YOUR TEAMS

Enable cross-functional collaboration by:
- Building trust with your counterparts on other teams.
- Encouraging practitioners to move between departments.
- Actively seeking, encouraging, and rewarding work that facilitates collaboration.

Help create a climate of learning by:
- Creating a training budget and advocating for it internally.
- Ensuring that your team has the resources to engage in informal learning and the space to explore ideas.
- Making it safe to fail.
- blameless postmortems
- Creating opportunities and spaces to share information.
- weekly lightning talks or offer resources for monthly lunch-and-learns,
- Encourage sharing and innovation by having demo days and forums.

Make effective use of tools:
- Make sure your team can choose their tools.
- Make monitoring a priority.

## CHAPTER 12-15 THE RESEARCH

    Lots of good stuff here

## CHAPTER 16 HIGH-PERFORMANCE LEADERSHIP AND MANAGEMENT

Case study of ING’s New Agile Organizational Model 
- Has No Fixed Structure
— It Constantly Evolves.

## APPENDIX A CAPABILITIES TO DRIVE IMPROVEMENT

### CAPABILITIES TO DRIVE IMPROVEMENT

Five categories: 
- Continuous delivery 
- Architecture Product and process 
- Lean management and monitoring 
- Cultural capabilities

### CONTINUOUS DELIVERY CAPABILITIES

- **Version control for all production** artifacts.
  - including application code, application configurations, system configurations, and 
  - scripts for automating build and configuration of the environment
- **Automate deployment** process.
- Continuous integration (**CI**)
- **Trunk-based development** methods.
  - fewer than three active branches
  - short lifetimes (e.g., less than a day)
  - never having “code lock”
- **Test automation**
  - developers should be primarily responsible for creation and maintenance of automated test suites.
- **Test data management**: Effective practices include 
    - having adequate data to run your test suite,
    - the ability to acquire necessary data on demand, 
    - the ability to condition your test data in your pipeline, 
    - the data not limiting the amount of tests you can run. 
    - We do caution, however, that teams should minimize, whenever possible, the amount of test data needed to run automated tests.
- **Shift left on security**
  - Integrating security into the design and testing phases
  - conducting security reviews of applications, 
  - including the infosec team in the design and demo process for applications, 
    - using preapproved security libraries and packages, 
    - and testing security features as a part of the automated testing suite.
- Implement continuous delivery (**CD**).
  - Fast feedback on the quality and deployability
  - fixes are made quickly.
  - system can be deployed to production or end users at any time, on demand.

### ARCHITECTURE CAPABILITIES

- **loosely coupled architecture**.
  - allows your teams to work independently, 
  - without relying on other teams for support and services,
- Architect for **empowered teams**.
- **Team chooses which tools** to use

### PRODUCT AND PROCESS CAPABILITIES

- Gather and implement **customer feedback**.
  - actively and regularly seek customer feedback and incorporate this feedback
- Make the **flow of work visible** through the value stream.
  - Teams should have a good understanding of and visibility into the flow of work from the business all the way through to customers, including the status of products and features.
- Work in **small batches**.
  - slice work into small pieces that can be completed in a week or less.
  - enables short lead times and faster feedback loops.
- Foster and enable **team experimentation**.

### LEAN MANAGEMENT AND MONITORING CAPABILITIES

- **lightweight change approval processes** based on peer review
- **Monitor across application and infrastructure** to inform business decisions.
  - goes beyond paging people when things go wrong.
- **Check system health proactively**.
  - Monitor system health, using threshold and rate-of-change warnings, to enable teams to preemptively detect and mitigate problems.
- Improve processes and manage work with work-in-process **(WIP) limits**.
- **Visualize work** to monitor quality and communicate throughout the team.

### CULTURAL CAPABILITIES

- Support a **generative culture** (as outlined by Westrum).
  - measure include good information flow, high cooperation and trust, bridging between teams, and conscious inquiry.
- Encourage and support **learning**.
- Support and facilitate **collaboration among teams**.
  - reflects how well teams, which have traditionally been siloed, interact in development, operations, and information security.
- Provide resources and tools that **make work meaningful**.
  - work that is challenging and meaningful, and being empowered to exercise your skills and judgment.
- Support or embody **transformational leadership**. Five factors: 
  - vision
  - intellectual stimulation
  - inspirational communication
  - supportive leadership
  - and personal recognition.
 

