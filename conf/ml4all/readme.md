# 2018-05-28 ML4ALL

https://ml4all.org/schedule.html

## Suz Hinton - Machine Learning for Accessibility

Sara Hendren
- Redesigned handicap icon
- more active icon

xss + xml project
- provide ML generated alt descriptions of images on instagram
- https://github.com/noopkat/insta-caption
- using microsoft endpoint
- https://eastus.api.cognitive.microsoft.com/vision/v1.0/analyze?visualFeatures=description

**use existing API for ML products**

live closed caption injection

[twitch stream](https://www.twitch.tv/noopkat)
- live coding and oss maintenance

[Accessible Images AIMS](https://link.springer.com/article/10.1007/s10209-017-0607-z)

## Ricky Hennessy - Using Machine Learning to Increase Health Insurance Coverage

- export data to csv
- load into pandas
- feature engineering: 

## Kaleo Ha'o - Jump or Not to Jump: Solving Flappy Bird with Deep Reinforcement Learning

ML generaly requires lots of data

Reinforcement Learning doesn't require as much data but needs experience

Quality Function:
`Q(s,a) = r + (Y * SUM(Y^(n-1) * r(n), n))`
- s = scenario
- a = action
- r = reward
- Y (gamma) = discount factor

`Q(s,a) = r1 + Y^1 * r2 + Y^2 * r3 + Y^3 * r4...`
- add/subract every reward scenario
- e.g. Harry Potter Wizard Chess. Ron sacrificing himself is -100 but leads to checkmate which is +1000

`Q(s,a) = r1 + Y(max) * Q(s(next), a(next))`
- we use Y(max) assuming we "try" to maximize future rewards despite discount factor

Error Function `Error = GMF - Q(actual)`
- GMF = Giant Mathematical Function

http://github.com06kahao
- improved Deal Learning

Also see [Gogole DeepMind](https://deepmind.com)

## Clair J. Sullivan - A Machine Learning Win at GitHub ...and So Can You!

Github Repo Recommendations

Recommendation Engines

Find quality data e.g.
- Quality of repo
- repos you watched/starred
- repos watched/starred by people you follow
- repos that are trending
- repos that are popular

Quality of Repo:
- using 30 metrics
- 2 most important: does readme exist & how responsive is repo

:bangbang: http://www.gharchive.org/

https://en.wikipedia.org/wiki/Random_forest


## Lightning Talks - A series of short 5min talks. Sign-up at the registration desk!

https://cloud.google.com/bigquery/public-data/

## Paige Bailey - Kill (Deep) Math!

Fourier Tranforms: breaking a signal into consituent parts
- e.g. taking an audio sample with a micropone
	- consituent parts e.g. bpm, frequency, etc
- e.g. fruits in a smoothie

To find te energy at a particulary frequency, spin your signal around a circle
at that frequency, and average a bunch of points along that path

[Project Magenta](https://magenta.tensorflow.org/)

Cheese Quality using metrics e.g. H2S, Acetic, Lactic
- Linera regression can be used
- Deep Learning wit additional *hidden layers* for more accurate Taste

e.g.
- Acetic = 4.543
- H2S = 3.135
- weight = 1
- Hidden layer = 7.678 = 4.543 * 1 + 3.135 * 1
- Output = 15.356 = HL1 + HL2 = 7.678 + 7.678

* Actual score was 12.xxx wich != 15.356
- use **activation functions**
- industry standard is [ReLu](https://en.wikipedia.org/wiki/Rectifier_%40neural_networks%41)

As we add more inputs we get more *bias* and *weight* per layer

A 1024x768 pixel image would have 800k input nodes (complexity grows)

For every single node: `SIGMA(w1a1 + w2a2 + ... + b)`
- w = weights
- b = bias
- a2 = 
- SIGMA = activation function

Check out [TensorFlow playground](https://playground.tensorflow.org/)

:bangbang: look up her "sources and ispirations"
- chris Olahs' Blog
- Bret Victor's Kill Math
- 3 blue 1 brown

## Igor Dziuba - Teach Machine To Teach: Personal Tutor For Language Learners

Code samples for image recognition: cat vs dogs

## Jon Oropeza - ML Spends A Year In Burgundy

Find ML libraries in your language

Learn some ML before using MLaaS

## Manuel Muro - Barriers To Accelerating The Training Of Artificial Neural Networks



## Poul Petersen - From Zero to Machine Learning for Everyone

Use https://bigml.com/ for easy ML

Housing data from Redfin: check download link

:bangbang: Paper: Do We Need Hundreds of Classifiers to Solve Real World Classification Problems?

:bangbang: look up the "Choosing the Algorithm" slide from presentation

Use [OptiML](http://stanford-ppl.github.io/Delite/optiml/) to predict best algorithm
