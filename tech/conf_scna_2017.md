# 2017-10-27 SCNA 2017 

## Software Craftsmanship and the Safety Critical World - Phil Markgraf

"Regulators expect waterfall" e.g. IEC62304

[Book: Extreme Programming Explained](https://www.amazon.com/Extreme-Programming-Explained-Embrace-Change/dp/0321278658/ref=sr_1_1?ie=UTF8&qid=1509214428&sr=8-1&keywords=extreme+programming)

Applying XP for Medical Devices
- Can apply practices while still meeting regulatory requirements

S/W hazard analysis for all the ways devices can fail

Document "Why" and what can't be inferred from code

Continuous delivery mindset even if we don't actually "ship" daily
- What would it take to be shippable anytime

Utilize Chaos Monkey

Quality first approach
- Avoid many features, half done
- Bug fixing should be higher priority than new features
- Start with system tests that drive unit tests

Bugs have a quantifiable business cost

## Mob Programming - Woody Zull

The idea that the team mobs around a single monitor/keyboard
- requires a pair at the helm: driver/navigator

"for an idea to go from someone's head into the computer it must go through someone else's hands"

My thoughts: Interesting idea, not sure how it works practicaly

Addendum: did a couple of mob programming sessions the next day at code retreat. Felt less than ideal in practice
- some folks were getting disengaged
- pace was slow
- even though there was supposed to be only 1 navigator, there was multiple backseat drivers 

Issues above were probably due to it being new to everyone involed other than Woody, but I still noticed
a tendency for the "extroverts" to take over and drive direction. Definitely not ideal for all personality types.

## Computational Thinkig w/ Sara Aslanisfar

Ran experiments on her 6 & 4 yr old kids :)

Taught them to think in algorithms using games such as Cubetto and merge sort with playing cards.

## System Architecture as Network Data w/ Bobby Norton

- Complex != complicated
- how do we structure complex system so they are understandable/visualizable

Worked with Dr. Sri Sarma on Electrocorticography app to monitor brains of epilepsy patiets
- mapped network of neurons that are affected during an epilepsy

Wanted to apply same mapping technique to code

Agile == risk management vs responsiveness

Whitepaper: Improving Systems Architecture with DSM -- Bobby Norton 

Wrote lein/topology to map code and parse dependencies

[Book: Design Structure Matrix Method and Applications](https://www.amazon.com/Structure-Methods-Applications-Engineering-Systems-ebook/dp/B00LG92JIK/ref=sr_1_2?ie=UTF8&qid=1509215133&sr=8-2&keywords=design+structure)

Quantify coupling and cohesion

Used Cytoscape for network visualization

"What if we had a Google Map for our code"

Measure a modularity score; Edge of Betweenness algorithm

When writing tests, don't go for 100% unit test coverage, but try to achieve
100% interface coverage at module boundaries

[Network visualization applied to Game of Thrones](http://got.testedminds.com/)

## Is the Best Software Written Alone - Elizabeth Engelman

Pair programming is not ideal for everyone all the tie

Teamwork is hard!
- even when you have clear common goals and general styles mesh

Pair mismatches due to:
- personality types
- learning style
- experience/expertise etc

"Personality Types" such as Myers Briggs are oversimplified and misapplied but
they provide a vocabulary which is valuable

e.g. using VARK, an auditory learner might just be thinking out loud which could be perceived as backseat driving but that's not their intent. That's just how they think through a problem.

[I think she referenced this thesis on Effects of Pair Programming](https://users.aalto.fi/~vanhanen/pubs/licthesis_vanhanen.pdf)

[Book: The ABCs of How We Learn](https://www.amazon.com/ABCs-How-Learn-Scientifically-Approaches/dp/0393709264/ref=sr_1_1?s=books&ie=UTF8&qid=1509215630&sr=1-1&keywords=ABC+of+learning)

## Teal Organization in Development w/ Amanda Laucher

Different organization profiles are better for different purposes. e.g. Command & Control for the Sopranos

"Teal" is from [Book: Reinventing Organizations](https://www.barnesandnoble.com/p/reinventing-organizations-frederic-laloux/1118591311/2678212595706?st=PLA&sid=BNB_DRS_Core+Catch-All,+Low_00000000&2sid=Google_&sourceId=PLGoP79700&gclid=EAIaIQobChMIpt6E1PqT1wIVEpF-Ch0mFw9MEAYYASABEgKuTPD_BwE)

Books
- [An Everyone Culture]()
- [Ego is the Enemy]()
- [Nonviolent communication]()

## Next Day: Code Retreat (Game of Life)

