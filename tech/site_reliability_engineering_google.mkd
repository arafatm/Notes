# Site Reliability Engineering: How Google Runs Production Systems by Betsy Beyer, Jennifer Petoff, Chris Jones, Niall Richard Murphy

## Chapter 1. Introduction

> Hope is not a strategy.

In traditional ops, size of the team necessarily scales with the load generated
by the system.

Traditional operations teams and their counterparts in product development thus
often end up in conflict, most visibly over how quickly software can be
released to production.

SRE is what happens when you ask a software engineer to design an operations
team.

SREs can be broken down into two main categories
- 50–60% are Google Software Engineers, or more precisely, people who have been
  hired via the standard procedure for Google Software Engineers
- The other 40–50% are candidates who were very close to the Google Software
  Engineering qualifications (i.e., 85–99% of the skill set required), and who
  in addition had a set of technical skills that is useful to SRE but is rare
  for most software engineers. By far, UNIX system internals and networking
  (Layer 1 to Layer 3) expertise are the two most common types of alternate
  technical skills we seek.

team of people who (a) will quickly become bored by performing tasks by hand,
and (b) have the skill set necessary to write software to replace their
previously manual work,

Google places a 50% cap on the aggregate “ops” work for all SREs — tickets,
on-call, manual tasks, etc.

Ensuring a Durable Focus on Engineering

When they are focused on operations work, on average, SREs should receive a
maximum of two events per 8–12-hour on-call shift.

enough time to handle the event accurately and quickly, clean up and restore
normal service, and then conduct a postmortem.

**blame-free postmortem culture**, with the goal of exposing faults and
applying engineering to fix these faults, rather than avoiding or minimizing
them.

Pursuing Maximum Change Velocity Without Violating a Service’s SLO

marginal difference between 99.999% and 100% gets lost in the noise of other
unavailability, and the user receives no benefit from the enormous effort
required to add that last 0.001% of availability.

product question, which should take the following considerations into account:
- What level of availability will the users be happy with, given how they use
  the product?
- What alternatives are available to users who are dissatisfied with the
  product’s availability?
- What happens to users’ usage of the product at different availability levels?

SRE’s goal is no longer “zero outages”; rather, SREs and product developers aim
to spend the error budget getting maximum feature velocity.

### Monitoring

Monitoring should never require a human to interpret any part of the alerting
domain.

three kinds of valid monitoring output:
- **Alerts** Signify that a human needs to take action immediately
- **Tickets** Signify that a human needs to take action, but not immediately.
- **Logging** No one needs to look at this information, but it is recorded for
  diagnostic or forensic purposes.

### Emergency Response

Reliability is a function of mean time to failure **MTTF** and mean time to
repair **MTTR** [Sch15]

thinking through and recording the best practices ahead of time in a “playbook”
produces roughly a 3x improvement in MTTR as compared to the strategy of
“winging it.”

### Change Management

roughly 70% of outages are due to changes in a live system. Best practices in
this domain use automation

Implementing progressive rollouts Quickly and accurately detecting problems
Rolling back changes safely when problems arise

### Demand Forecasting and Capacity Planning

steps are mandatory in capacity planning: An accurate organic demand forecast,
which extends beyond the lead time required for acquiring capacity An accurate
incorporation of inorganic demand sources into the demand forecast Regular load
testing of the system to correlate raw capacity (servers, disks, and so on) to
service capacity

### Provisioning

Provisioning combines both change management and capacity planning.

### Efficiency and Performance

paying close attention to the provisioning strategy for a service, and
therefore its utilization, provides a very, very big lever on the service’s
total costs.

Resource use is a function of demand (load), capacity, and software efficiency.

**SRE is a set of principles, a set of practices, a set of incentives, and a
field of endeavor within the larger software engineering discipline.**

## Chapter 2. The Production Environment at Google, from the Viewpoint of an SRE

Part II. Principles

looks at SRE through the lens of risk — its assessment, management, and the use
of error budgets to provide usefully neutral approaches to service management.

Service level objectives

disentangle indicators from objectives from agreements,

Eliminating toil

monitoring

automation,

release engineering

simplicity is a quality that, once lost, can be extraordinarily difficult to
recapture.

## Chapter 3. Embracing Risk

maximizing stability limits how fast new features can be developed

users typically don’t notice the difference between high reliability and
extreme reliability

cannot tell the difference between 99.99% and 99.999%

Managing Risk

incremental improvement in reliability may cost 100x more than the previous
increment.

The cost of redundant machine/compute resources

The opportunity cost

Measuring Service Risk

focus on unplanned downtime.

Equation 3-1. Time-based availability

instead of using metrics around uptime, we define availability in terms of the
request success rate.

Equation 3-2. Aggregate availability

Risk Tolerance of Services

SREs must work with the product owners to turn a set of business goals into
explicit objectives to which we can engineer.

Identifying the Risk Tolerance of Consumer Services

Target level of availability

usually depends on the function it provides and how the service is positioned
in the marketplace.

We set a lower availability target for YouTube than for our enterprise products
because rapid feature development was correspondingly more important.

Types of failures

Which is worse for the service: a constant low rate of failures, or an
occasional full-site outage?

Both types of failure may result in the same absolute number of errors, but may
have vastly different impacts on the business.

Cost

key factor in determining the appropriate availability target for a service.

consider the following cost/benefit for an example service where each request
has equal value: 
- Proposed improvement in availability target: 99.9% → 99.99%
- Proposed increase in availability: 0.09%
- Service revenue: `$1M Value of improved availability: $1M * 0.0009 = $900`

we’ve measured the typical background error rate for ISPs as falling between
0.01% and 1%.

Other service metrics

Examining the risk tolerance of services in relation to metrics besides
availability is often fruitful.

AdWords,

key requirement of the system was that the ads should not slow down the search
experience.

AdSense,

latency goal for AdSense is to avoid slowing down the rendering of the
third-party page when inserting contextual ads.

This means that AdSense ads can generally be served hundreds of milliseconds
slower than AdWords ads.

Identifying the Risk Tolerance of Infrastructure Services

by definition, infrastructure components have multiple clients, often with
varying needs.

Target level of availability

Such services need low latency and high reliability.

These teams tend to be more concerned about throughput than reliability. Risk
tolerance for these two use cases is quite distinct.

One approach to meeting the needs of both use cases is to engineer all
infrastructure services to be ultra-reliable.

such an approach is usually far too expensive in practice.

Types of failures

Success for the low-latency user is failure for the user concerned with offline
analysis.

Cost

to satisfy these competing constraints in a cost-effective manner is to
partition the infrastructure and offer it at multiple independent levels of
service.

we can build two types of clusters: low-latency clusters and throughput
clusters. The

Example: Frontend infrastructure

consists of reverse proxy and load balancing systems running close to the edge
of our network.

Given their critical role, we engineer these systems to deliver an extremely
high level of reliability.

consumer services can often limit the visibility of unreliability in backends,

Motivation for Error Budgets

Product development performance is largely evaluated on product velocity,

SRE performance is (unsurprisingly) evaluated based upon reliability of a
service,

Information asymmetry between the two teams further amplifies this inherent
tension.

following list presents some typical tensions:

Software fault tolerance

Testing

Push frequency

Canary duration and size

Forming Your Error Budget

the two teams jointly define a quarterly error budget based on the service’s
service level objective, or SLO

This metric removes the politics from negotiations between the SREs and the
product developers

Our practice is then as follows:

Product Management defines an SLO, which sets an expectation of how much uptime
the service should have per quarter.

actual uptime is measured by a neutral third party: our monitoring system.

The difference between these two numbers is the “budget” of how much
“unreliability” is remaining for the quarter.

As long as the uptime measured is above the SLO — in other words, as long as
there is error budget remaining — new releases can be pushed.

Benefits

For example, if product development wants to skimp on testing or increase push
velocity and SRE is resistant, the error budget guides the decision. When the
budget is large, the product developers can take more risks.

Key Insights

Managing service reliability is largely about managing risk, and managing risk
can be costly.

100% is probably never the right reliability target:

An error budget aligns incentives and emphasizes joint ownership between SRE
and product development.

## Chapter 4. Service Level Objectives

define service level indicators (SLIs), objectives (SLOs), and agreements
(SLAs).

Service Level Terminology

Indicators An SLI

quantitative measure of some aspect of the level of service that is provided.

request latency

error rate,

system throughput,

measurements are often aggregated:

availability,

(Durability

Objectives An SLO

natural structure for SLOs is thus SLI ≤ target, or lower bound ≤ SLI ≤ upper
bound.

Agreements Finally, SLAs are service level agreements:

explicit or implicit contract with your users that includes consequences of
meeting (or missing) the SLOs they contain.

Whether or not a particular service has an SLA, it’s valuable to define SLIs
and SLOs and use them to manage the service.

Indicators in Practice

What Do You and Your Users Care About?

Choosing too many indicators makes it hard to pay the right level of attention

choosing too few may leave significant behaviors of your system unexamined.

Services tend to fall into a few broad categories in terms of the SLIs they
find relevant:

User-facing serving systems, such as the Shakespeare search frontends,
generally care about availability, latency, and throughput.

Storage systems often emphasize latency, availability, and durability.

Big data systems, such as data processing pipelines, tend to care about
throughput and end-to-end latency.

All systems should care about correctness:

Collecting Indicators

Many indicator metrics are most naturally gathered on the server side, using a
monitoring system

some systems should be instrumented with client-side collection,

For example, concentrating on the response latency of the Shakespeare search
backend might miss poor user latency due to problems with the page’s
JavaScript:

Aggregation

For simplicity and usability, we often aggregate raw measurements. This needs
to be done carefully.

Consider a system that serves 200 requests/s in even-numbered seconds, and 0 in
the others. It has the same average load as one that serves a constant 100
requests/s, but has an instantaneous load that is twice as large as the average
one.

The higher the variance in response times, the more the typical user experience
is affected by long-tail behavior,

User studies have shown that people typically prefer a slightly slower system
to one with high variance in response time, so some SRE teams focus only on
high percentile values, on the grounds that if the 99.9th percentile behavior
is good, then the typical experience is certainly going to be.

Standardize Indicators

Any feature that conforms to the standard definition templates can be omitted
from the specification of an individual SLI, e.g.: Aggregation intervals:
“Averaged over 1 minute” Aggregation regions: “All the tasks in a cluster” How
frequently measurements are made: “Every 10 seconds” Which requests are
included: “HTTP GETs from black-box monitoring jobs” How the data is acquired:
“Through our monitoring, measured at the server” Data-access latency: “Time to
last byte”

Objectives in Practice

Often, what your users care about is difficult or impossible to measure, so
you’ll end up approximating users’ needs in some way.

working from desired objectives backward to specific indicators works better
than choosing indicators and then coming up with targets.

Defining Objectives

SLOs should specify how they’re measured and the conditions under which they’re
valid.

Choosing Targets

Don’t pick a target based on current performance

Keep it simple

Avoid absolutes

Have as few SLOs as possible

not all product attributes are amenable to SLOs: it’s hard to specify “user
delight” with an SLO.

Perfection can wait

better to start with a loose target that you tighten than to choose an overly
strict target that has to be relaxed when you discover it’s unattainable.

Control Measures

Monitor and measure the system’s SLIs.

Compare the SLIs to the SLOs, and decide whether or not action is needed. If
action is needed, figure out what needs to happen in order to meet the target.
Take that action.

SLOs Set Expectations

For instance, a team wanting to build a photo-sharing website might want to
avoid using a service that promises very strong durability and low cost in
exchange for slightly lower availability, though the same service might be a
perfect fit for an archival records management system.

Keep a safety margin

Don’t overachieve

You can avoid over-dependence by deliberately taking the system offline
occasionally

throttling some requests,

designing the system so that it isn’t faster under light loads.

Agreements in Practice

Crafting an SLA requires business and legal teams to pick appropriate
consequences and penalties for a breach.

## Chapter 5. Eliminating Toil

If a human operator needs to touch your system during normal operations, you
have a bug.

There are also administrative chores that have to get done, but should not be
categorized as toil: this is overhead.

Grungy work can sometimes have long-term value, and in that case, it’s not
toil, either. Cleaning up the entire alerting configuration for your service
and removing clutter may be grungy, but it’s not toil.

Toil is the kind of work tied to running a production service that tends to be
manual, repetitive, automatable, tactical, devoid of enduring value, and that
scales linearly as a service grows.

toil) below 50%

Engineering work is novel and intrinsically requires human judgment.

It produces a permanent improvement in your service, and is guided by a
strategy.

It is frequently creative and innovative, taking a design-driven approach to
solving a problem

Software engineering

Systems engineering

Toil

Overhead

Let’s invent more, and toil less.

Googlers record short free-form summaries, or “snippets,” of what we’ve worked
on each week.

## Chapter 6. Monitoring Distributed Systems

Why Monitor?

Analyzing long-term trends

Comparing over time or experiment groups

Alerting

Building dashboards

Conducting ad hoc retrospective analysis

Effective alerting systems have good signal and very low noise.

Setting Reasonable Expectations for Monitoring

better tools for post hoc analysis.

Rules that generate alerts for humans should be simple to understand and
represent a clear failure.

Symptoms Versus Causes

Your monitoring system should address two questions: what’s broken, and why?

“What” versus “why” is one of the most important distinctions in writing good
monitoring with maximum signal and minimum noise.

Black-Box Versus White-Box

black-box monitoring is symptom-oriented and represents active — not predicted
— problems:

White-box monitoring depends on the ability to inspect the innards of the
system, such as logs or HTTP endpoints, with instrumentation.

allows detection of imminent problems, failures masked by retries, and so
forth.

The Four Golden Signals

The four golden signals of monitoring are latency, traffic, errors, and
saturation. If you can only measure four metrics of your user-facing system,
focus on these four.

Worrying About Your Tail (or, Instrumentation and Performance)

the 99th percentile of one backend can easily become the median response of
your frontend.

The simplest way to differentiate between a slow average and a very slow “tail”
of requests is to collect request counts bucketed by latencies

Choosing an Appropriate Resolution for Measurements

As Simple as Possible, No Simpler

maintaining distinct systems with clear, simple, loosely coupled points of
integration is a better strategy

Tying These Principles Together

rules for monitoring and alerting,

Does this rule detect an otherwise undetected condition that is urgent,

Will I ever be able to ignore this alert, knowing it’s benign?

Does this alert definitely indicate that users are being negatively affected?

Can I take action in response to this alert?

Are other people getting paged for this issue, therefore rendering at least one
of the pages unnecessary?

Monitoring for the Long Term

while some team members want to implement a “hack” to allow time for a proper
fix, others worry that a hack will be forgotten or that the proper fix will be
deprioritized indefinitely.

## Chapter 7. The Evolution of Automation at Google

automation is a force multiplier, not a panacea.

just multiplying force does not naturally change the accuracy of where that
force is applied:

The Value of Automation

Consistency

A Platform

Designed and done properly, automatic systems also provide a platform that can
be extended, applied to more systems,

Faster Repairs

If automation runs regularly and successfully enough, the result is a reduced
mean time to repair (MTTR) for those common faults.

Faster Action

humans don’t usually react as fast as machines.

Time Saving

Decoupling operator from operation

The Value for Google SRE

It isn’t appropriate to automate every component of every system, and not
everyone has the ability or inclination to develop automation at a particular
time.

The Use Cases for Automation

Google SRE’s Use Cases for Automation

context for our automation is often automation to manage the lifecycle of
systems, not their data:

higher-level abstractions are easier to manage and reason about, but when you
encounter a “leaky abstraction,” you fail systemically, repeatedly, and
potentially inconsistently.

The evolution of automation follows a path:

1) No automation

Database master is failed over manually between locations.

2) Externally maintained system-specific automation

An SRE has a failover script in his or her home directory.

3) Externally maintained generic automation

The SRE adds database support to a “generic failover” script that everyone
uses.

4) Internally maintained system-specific automation

The database ships with its own failover script.

5) Systems that don’t need any automation The database notices problems, and
automatically fails over without human intervention.

Automate Yourself Out of a Job: Automate ALL the Things!

We graduated from optimizing our infrastructure for a lack of failover to
embracing the idea that failure is inevitable, and therefore optimizing to
recover quickly through automation.

Soothing the Pain: Applying Automation to Cluster Turnups

Automation code, like unit test code, dies when the maintaining team isn’t
obsessive about keeping the code in sync with the codebase it covers.

The most functional tools are usually written by those who use them.

our evolution of turnup automation followed a path: Operator-triggered manual
action (no automation) Operator-written, system-specific automation Externally
maintained generic automation Internally maintained, system-specific automation
Autonomous systems that need no human intervention While this evolution has,
broadly speaking, been a success, the Borg case study illustrates another way
we have come to think of the problem of automation.

Borg: Birth of the Warehouse-Scale Computer

as we move systems up the hierarchy from manually triggered, to automatically
triggered, to autonomous, some capacity for self-introspection is necessary to
survive.

Reliability Is the Fundamental Feature

automation provides more than just time saving,

shipping and iterating rapidly might allow you to implement functionality
faster, yet rarely makes for a resilient system.

Autonomous operation is difficult to convincingly retrofit to sufficiently
large systems, but standard good practices in software engineering will help
considerably: having decoupled subsystems, introducing APIs, minimizing side
effects, and so on.

## Chapter 8. Release Engineering

concisely described as building and delivering software

understanding of source code management, compilers, build configuration
languages, automated build tools, package managers, and installers.

skill set includes deep knowledge of multiple domains: development,
configuration management, test integration, system administration, and customer
support.

The Role of a Release Engineer

safely deploying products and keeping Google services up and running.

release engineers and SREs work together to develop strategies for canarying
changes, pushing out new releases without interrupting services, and rolling
back features that demonstrate problems.

Philosophy

Self-Service Model

to work at scale, teams must be self-sufficient.

best practices and tools that allow our product development teams to control
and run their own release processes.

high release velocity because individual teams can decide how often and when to
release new versions

Release processes can be automated to the point that they require minimal
involvement by the engineers,

Releases are truly automatic, and only require engineer involvement if and when
problems arise.

High Velocity

philosophy that frequent releases result in fewer changes between versions.

Some teams perform hourly builds and then select the version to actually deploy
to production from the resulting pool

Other teams have adopted a “Push on Green”

Hermetic Builds

ensure consistency and repeatability.

build the same product at the same revision number in the source code
repository on different machines, we expect identical results.

build process is self-contained and must not rely on services that are external
to the build environment.

rebuilding at the same revision as the original build and including specific
changes that were submitted after that point in time.

cherry picking.

build tools are themselves versioned based on the revision in the source code
repository for the project being built.

Enforcement of Policies and Procedures

Gated operations include:

Approving source code changes

Specifying the actions to be performed during the release process

Creating a new release Approving the initial integration proposal (which is a
request to perform a build at a specific revision number in the source code
repository) and subsequent cherry picks Deploying a new release Making changes
to a project’s build configuration

Continuous Build and Deployment

automated release system called Rapid.

Building

Engineers use Blaze to define build targets (e.g., the output of a build, such
as a JAR file), and to specify the dependencies for each target. When
performing a build, Blaze automatically builds the dependency targets.

Branching

All code is checked into the main branch

branch from the mainline at a specific revision and never merge changes from
the branch back into the mainline.

Bug fixes are submitted to the mainline and then cherry picked into the branch
for inclusion in the release.

Testing

Release engineering recommends that the continuous build test targets
correspond to the same test targets that gate the project release. We also
recommend creating releases at the revision number (version) of the last
continuous test build that successfully completed all tests.

During the release process, we re-run the unit tests using the release branch
and create an audit trail showing that all the tests passed.

use an independent testing environment that runs system-level tests on packaged
build artifacts.

Packaging

Software is distributed to our production machines via the Midas Package
Manager (MPM)

MPM assembles packages based on Blaze rules that list the build artifacts to
include, along with their owners and permissions. Packages are named (e.g.,
search/shakespeare/frontend), versioned with a unique hash, and signed to
ensure authenticity.

A typical release process proceeds as follows:

Rapid uses the requested integration revision number (often obtained
automatically from our continuous test system) to create a release branch.

Rapid uses Blaze to compile all the binaries and execute the unit tests, often
performing these two steps in parallel.

Compilation and testing occur in environments dedicated to those specific
tasks,

Build artifacts are then available for system testing and canary deployments.

The results of each step of the process are logged. A report of all changes
since the last release

Rapid allows us to manage our release branches and cherry picks; individual
cherry pick requests can be approved or rejected for inclusion in a release.

Deployment

Rapid is often used to drive simple deployments directly.

It updates the Borg jobs to use newly built MPM packages based on deployment
definitions in the blueprint files and specialized task executors.

For more complicated deployments, we use Sisyphus, which is a general-purpose
rollout automation framework

Configuration Management

All schemes involve storing configuration in our primary source code repository
and enforcing a strict code review requirement.

Teams should budget for release engineering resources at the beginning of the
product development cycle. It’s cheaper to put good practices and process in
place early, rather than have to retrofit your system later.

## Chapter 9. Simplicity

exploratory coding — setting an explicit shelf life for whatever code I write
with the understanding that I’ll need to try and fail once in order to really
understand the task I need to accomplish.

Fred Brooks suggests in his “No Silver Bullet” essay [Bro95], it is very
important to consider the difference between essential complexity and
accidental complexity.

Source control systems make it easy to reverse changes, whereas hundreds of
lines of commented code create distractions and confusion

clear, minimal APIs

loose coupling between binaries, or between binaries and configuration,

Versioning APIs allows developers to continue to use the version that their
system depends upon while they upgrade to a newer version in a safe and
considered way.

Part III. Practices

hierarchy, illustrated in Figure III-1

Figure III-1. Service Reliability Hierarchy

Monitoring

Incident Response

balance on-call duties with our other responsibilities.

Postmortem and Root-Cause Analysis

Building a blameless postmortem culture is the first step

outage tracker, that allows SRE teams to keep track of recent production
incidents, their causes, and actions taken in response to them.

Testing

Test suites offer some assurance that our software isn’t making certain classes
of errors before it’s released to production;

Capacity Planning

Development

Product

## Chapter 10. Practical Alerting from Time-Series Data

Monitoring, the bottom layer of the Hierarchy of Production Needs,

At the scale our systems operate, being alerted for single-machine failures is
unacceptable because such data is too noisy to be actionable.

designed to aggregate signals and prune outliers.

Prometheus1 shares many similarities with Borgmon, especially when you compare
the two rule languages. The principles of variable collection and rule
evaluation remain the same across all these tools and provide an environment
with which you can experiment, and hopefully launch into production,

At predefined intervals, Borgmon fetches the /varz URI on each target, decodes
the results, and stores the values in memory.

Borgmon stores all the data in an in-memory database, regularly checkpointed to
disk. The data points have the form (timestamp, value), and are stored in
chronological lists called time-series, and each time-series is named by a
unique set of labels, of the form name=value.

compare the ratio rate of errors to our service level objective (see Chapter 4)
and alert if this objective is missed or in danger of being missed:

white-box monitoring does not provide a full picture

you aren’t aware of what the users see.

queries that never make it due to a DNS error are invisible,

queries lost due to a server crash never make a sound.

Prober, which runs a protocol check against a target and reports success or
failure.

## Chapter 11. Being On-Call

The quantity of on-call can be calculated by the percent of time spent by
engineers on on-call duties.

The quality of on-call can be calculated by the number of incidents that occur
during an on-call shift.

SRE managers have the responsibility of keeping the on-call workload balanced
and sustainable across these two axes.

strive to invest at least 50% of SRE time into engineering:

of the remainder, no more than 25% can be spent on-call, leaving up to another
25% on other types of operational, nonproject work.

multi-site team is advantageous for two reasons:

Night shifts have detrimental effects on people’s health [Dur05], and a
multi-site “follow the sun” rotation allows teams to avoid night shifts
altogether.

Limiting the number of engineers in the on-call rotation ensures that engineers
do not lose touch with the production systems

dealing with the tasks involved in an on-call incident — root-cause analysis,
remediation, and follow-up activities like writing a postmortem and fixing bugs

## Chapter 12. Effective Troubleshooting

troubleshooting is both learnable and teachable.

Every problem starts with a problem report,

effective report should tell you the expected behavior, the actual behavior,
and, if possible, how to reproduce the behavior.

consistent form and be stored in a searchable location, such as a bug tracking
system.

Unpacking the Causes of a Symptom Symptom: A Spanner cluster has high latency
and RPCs to its servers are timing out. Why? The Spanner server tasks are using
all their CPU time and can’t make progress on all the requests the clients
send. Where in the server is the CPU time being used? Profiling the server
shows it’s sorting entries in logs checkpointed to disk. Where in the
log-sorting code is it being used? When evaluating a regular expression against
paths to log files. Solutions: Rewrite the regular expression to avoid
backtracking. Look in the codebase for similar patterns. Consider using RE2,
which does not backtrack and guarantees linear runtime growth with input size.

## Chapter 13. Emergency Response

SREs break our systems, watch how they fail, and make changes to improve
reliability and prevent the failures from recurring. Most of the time, these
controlled failures go as planned,

All Problems Have Solutions

If you can’t think of a solution, cast your net farther. Involve more of your
teammates, seek help, do whatever you have to do, but do it quickly.

Keep a History of Outages

Ask the Big, Even Improbable, Questions: What If…?

What if the building power fails…?

Encourage Proactive Testing

## Chapter 14. Managing Incidents

Several distinct roles should be delegated to particular individuals:

Incident Command The incident commander holds the high-level state about the
incident. They structure the incident response task force, assigning
responsibilities according to need and priority. De facto, the commander holds
all positions that they have not delegated. If appropriate, they can remove
roadblocks that prevent Ops from working most effectively. Operational Work The
Ops lead works with the incident commander to respond to the incident by
applying operational tools to the task at hand. The operations team should be
the only group modifying the system during an incident. Communication This
person is the public face of the incident response task force. Their duties
most definitely include issuing periodic updates to the incident response team
and stakeholders (usually via email), and may extend to tasks such as keeping
the incident document accurate and up to date. Planning The planning role
supports Ops by dealing with longer-term issues, such as filing bugs, ordering
dinner, arranging handoffs, and tracking how the system has diverged from the
norm so it can be reverted once the incident is resolved.

It’s essential that the post of incident commander be clearly handed off at the
end of the working day.

Best Practices for Incident Management Prioritize. Stop the bleeding, restore
service, and preserve the evidence for root-causing. Prepare. Develop and
document your incident management procedures in advance, in consultation with
incident participants. Trust. Give full autonomy within the assigned role to
all incident participants. Introspect. Pay attention to your emotional state
while responding to an incident. If you start to feel panicky or overwhelmed,
solicit more support. Consider alternatives. Periodically consider your options
and re-evaluate whether it still makes sense to continue what you’re doing or
whether you should be taking another tack in incident response. Practice. Use
the process routinely so it becomes second nature. Change it around. Were you
incident commander last time? Take on a different role this time. Encourage
every team member to acquire familiarity with each role.

## Chapter 15. Postmortem Culture: Learning from Failure

Postmortems are expected after any significant undesirable event.

inherent cost in terms of time or effort, so we are deliberate in choosing when
to write one.

common postmortem triggers include:

User-visible downtime or degradation

Data loss of any kind

On-call engineer intervention

A resolution time above some threshold

A monitoring failure (which usually implies manual incident discovery)

reinforce a collaborative postmortem culture through senior management’s active
participation in the review and collaboration process.

Some example activities include:

Postmortem of the month

Google+ postmortem group

Postmortem reading clubs

Wheel of Misfortune

Ease postmortems into the workflow.

Make sure that writing effective postmortems is a rewarded and celebrated
practice, both publicly through the social methods mentioned earlier, and
through individual and team performance management.

Encourage senior leadership’s acknowledgment and participation.

## Chapter 16. Tracking Outages

## Chapter 17. Testing for Reliability

Figure 17-1. The hierarchy of traditional tests

Unit tests

unit test is the smallest and simplest form of software testing.

assess a separable unit of software, such as a class or function, for
correctness independent of the larger software system

employed as a form of specification

Integration tests

integration test on an assembled component

Dependency injection,

System tests

end-to-end functionality of the system.

System tests come in many different flavors:

Smoke tests

Smoke tests, in which engineers test very simple but critical behavior,

Performance tests

Regression tests

Regression tests can be analogized to a gallery of rogue bugs that historically
caused the system to fail or produce incorrect results.

Production Tests

interact with a live production system,

similar to black-box monitoring

Configuration test

Stress test

Canary test

To conduct a canary test, a subset of servers is upgraded to a new version or
configuration and then left in an incubation period.

## Chapter 18. Software Engineering in SRE

Achieving linear team growth in the face of exponential service growth requires
perpetual automation work and efforts to streamline tools, processes, and other
aspects of a service that introduce inefficiency into the day-to-day operation
of production.

## Chapter 19. Load Balancing at the Frontend

Load Balancing Using DNS

balancing with DNS on its own is not sufficient.

Load Balancing at the Virtual IP Address

## Chapter 28. Accelerating SREs to On-Call and Beyond

Figure 28-1. A blueprint for bootstrapping an SRE to on-call and beyond

“trial by fire” method of orienting one’s newbies is often born out of a team’s
current environment; ops-driven, reactive SRE teams “train” their newest
members by making them…well, react!

Put some amount of learning order into your system(s) so that your new SREs see
a path before them.

For example, if your team is responsible for a real-time, user-facing serving
stack, consider a curriculum order like the following: 1) How a query enters
the system Networking and datacenter fundamentals, frontend load balancing,
proxies, etc. 2) Frontend serving Application frontend(s), query logging, user
experience SLO(s), etc. 3) Mid-tier services Caches, backend load balancing 4)
Infrastructure Backends, infrastructure, and compute resources 5) Tying it all
together Debugging techniques, escalation procedures, and emergency scenarios

Targeted Project Work, Not Menial Work

give them a hearty problem to solve!

even a minor sense of ownership in the team’s service can do wonders for
learning.

Reverse Engineering a Production Service

learning everything via Reverse Engineering class techniques, and having the
rest of us correct her/fill in the blanks for whatever she missed or got wrong.

Five Practices for Aspiring On-Callers

A Hunger for Failure: Reading and Sharing Postmortems

Disaster Role Playing

Break Real Things, Fix Real Things

Documentation as Apprenticeship

“on-call learning checklist,”

Shadow On-Call Early and Often

## Chapter 29. Dealing with Interrupts

Pages are most commonly managed by a dedicated primary on-call engineer.

secondary on-call engineer acts as a backup for the primary.

Tickets are managed in a few different ways,

dedicated ticket person who is not on-call.

randomly autodistributed among team members,

Ongoing operational responsibilities are also managed in varying ways.

Factors in Determining How Interrupts Are Handled

Interrupt SLO or expected response time The number of interrupts that are
usually backlogged The severity of the interrupts The frequency of the
interrupts The number of people available to handle a certain kind of interrupt

Cognitive flow state: Creative and engaged

Maximizing the amount of time a person can spend in this state is very
desirable — they’re going to produce creative results and do good work by
volume. They’ll be happier at the job they’re doing.

state of constant interruption, or interruptability. This working environment
is extremely stressful.

On the other hand, when a person is concentrating full-time on interrupts,
interrupts stop being interrupts.

Polarizing time means that when a person comes into work each day, they should
know if they’re doing just project work or just interrupts.

## Chapter 30. Embedding an SRE to Recover from Operational Overload

Once embedded in a team, the SRE focuses on improving the team’s practices
instead of simply helping the team empty the ticket queue.

Phase 1: Learn the Service and Get Context

Identify the Largest Sources of Stress

Identify Kindling

Knowledge gaps

Services developed by SRE that are quietly increasing in importance

Strong dependence on “the next big thing”

Common alerts that aren’t diagnosed by either the dev team or SREs

Postmortems that only have action items for rolling back the specific changes
that caused an outage

Any serving-critical component for which the existing SREs respond to questions
by saying, “We don’t know anything about that; the devs own it”

Phase 2: Sharing Context

Write a Good Postmortem for the Team

Sort Fires According to Type

Phase 3: Driving Change

Start with the Basics

Get Help Clearing Kindling

resist the urge to fix these issues yourself,

Instead, take the following steps:

Find useful work that can be accomplished by one team member.

Clearly explain how this work addresses an issue from the postmortem in a
permanent way.

Serve as the reviewer for the code changes and document revisions.

Explain Your Reasoning

Ask Leading Questions

## Chapter 31. Communication and Collaboration in SRE

Production meetings are a special kind of meeting where an SRE team carefully
articulates to itself — and to its invitees — the state of the service(s) in
their charge, so as to increase general awareness among everyone who cares, and
to improve the operation of the service(s). In general, these meetings are
service-oriented; they are not directly about the status updates of
individuals.

Agenda

Upcoming production changes

Metrics

Outages

Paging events

Prior action items

## Chapter 32. The Evolving SRE Engagement Model

Production Readiness Review (PRR),

The SRE Engagement Model

aspects include the following: System architecture and interservice
dependencies Instrumentation, metrics, and monitoring Emergency response
Capacity planning Change management Performance: availability, latency, and
efficiency

Not all Google services receive close SRE engagement.

Many services don’t need high reliability and availability,

number of development teams that request SRE support exceeds the available
bandwidth of SRE teams

other options for making improvements to production, such as documentation and
consultation.

objectives of the Production Readiness Review are as follows: Verify that a
service meets accepted standards of production setup and operational readiness,
and that service owners are prepared to work with SRE and take advantage of SRE
expertise. Improve the reliability of the service in production, and minimize
the number and severity of incidents that might be expected. A PRR targets all
aspects of production that SRE cares about.

