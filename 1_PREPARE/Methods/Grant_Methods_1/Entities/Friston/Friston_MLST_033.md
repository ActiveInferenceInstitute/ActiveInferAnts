https://www.youtube.com/watch?v=KkR24ieh5Ow
#033 Karl Friston - The Free Energy Principle
00:00:00 Show teaser intro 
00:16:24 Main formalism for FEP 
00:28:29 Path Integral 
00:30:52 How did we feel talking to Friston? 
00:34:06 Skit - on cultures
00:36:02 Friston joins 
00:36:33 Main show introduction 
00:40:51 Is prediction all it takes for intelligence? 
00:48:21 Balancing accuracy with flexibility 
00:57:36 Belief-free vs belief-based; beliefs are crucial  
01:04:53 Fuzzy Markov Blankets and Wandering Sets  
01:12:37 The Free Energy Principle conforms to itself  
01:14:50 Useful false beliefs 
01:19:14 Complexity minimization is the heart of free energy
01:23:25 An Alpha to tip the scales? Absolute not! Absolutely yes!  
01:28:47 FEP applied to brain anatomy  
01:36:28 Are there multiple non-FEP forms in the brain? 
01:43:11 A positive connection to backpropagation  
01:47:12 The FEP does not explain the origin of FEP systems  
01:49:32 Post-show banter 
Welcome back to the Machine Learning Street Talk YouTube channel and podcast. Today we have an incredibly special guest, Professor Karl Friston. It was one of the most fascinating conversations we've ever had on Street Talk. This is an old school professor; he went to Cambridge in 1980 and he's one of these kind of eccentric polymath types that you know sits on the old kind of Chesterfield chair with all of the springs coming out and you know smoking a pipe or something like that. Professor Friston is most well known certainly in the machine learning domain for his Free Energy Principle or Active Inference, which is a kind of reinforcement learning flavor of that if you like, but he's got an incredible background. He is an expert in psychiatry and cognitive neuroscience and physics and Bayesian statistics. It's so strange just to have all of this knowledge embodied in one person so it really was quite an interesting conversation actually.
Now the Free Energy Principle has been called a postulate, a natural law, an imperative, an unfalsifiable principle. It's been called many things. It aims to give an almost universal understanding between the mind, life and the environment. So how did the Free Energy Principle come about?
The Free Energy Principle as you have just described it started really when I was a student aspiring to put together maths and psychologies and gets back to mathematical formalisms, the principles that underlie the sentient behavior with which we are gifted and the product of that was the Free Energy Principle. The Free Energy Principle sets the foundation for planning as inference by explicitly modeling the world and its states as beliefs. It balances accuracy with entropy which maintains the flexibility needed to continually adapt to future outcomes and explorations. But the more interesting game is I think better cast in terms of planning as inference enabling you to roll out much further into the future and ask well what would happen if I did that, what would my beliefs be about the state of the world in the long term future. So I think prediction in its full and glorious anticipatory sense really takes center stage.
Features of reality itself such as self-organized behavior and even quantum, they seem to require some kind of probabilistic Bayesian belief update on world states. For example, the path integration formalism from Richard Feynman, it essentially averages over many probabilistically weighted paths. In other words, functions over beliefs and has proven crucial to the subsequent development of quantum electrodynamics. That's what happened to understand the first principles underlie sentient behavior. You have to understand the dynamics of self-organization in particular self-organization of systems that are open to the environment. That comes in through Feynman's path integral formulation and thinking not just about the flow of the dynamics of self-organization at this point in time but trajectories into the future and the probability distributions over those trajectories and particularly the states that act upon the outside. And then things get much more interesting. You can interpret this in terms of inferring the most likely paths basically as resting upon a prediction of states of the world in the future conditioned upon a particular sequence of actions or policy.
The heart of the Free Energy Principle and what sets it apart from alternatives is the strict balance between accuracy and simplicity, evidence and entropy. One of the things that I think is very interesting about the Free Energy formulation is that prediction is half the story. So getting accurate predictions about the future while very important is juxtaposed with keeping your options open, keeping a flexible mind, keeping a high entropy model of the world so that as you encounter perhaps new situations it has the flexibility to adapt. In the central role of relative entropies in this sort of variational construct I think that your formerly that is so important in minimizing the free energy you're also trying to maximize the entropy. It seems sometimes counterintuitive but it is exactly that which is really mandated by things like Occam's principle and very practically relevant. So if you don't do that, if you don't put that uncertainty into the games then you're going to run into things like sharp minima and you're going to be searching for resolutions of that in terms of broadening your uncertainty flattening that free energy landscape just to try and secure those flat minima where you can be more reasonably assured that you've got some global minima say in standard deep learning or a machine learning context.
So this led Friston to believe that goal-directed behavior essentially planning based on goals is insufficient. We need to have a more sophisticated system that can reason about the uncertainty of our beliefs. We see echoes of this in machine learning. We spoke to Kenneth Stanley recently about novelty search and in his formalism he explicitly avoids objectives and he thinks that we should use novelty because of the inherent deception in objective search. Similarly in classic machine learning we use regularization to stop the machine learning algorithm overfitting the training set. Friston argues that the Free Energy Principle combines all of these different paradigms.
We're getting quite close to the center of the bullseye here and we're talking about the dichotomy between belief-free and belief-based methods. You know you said in your papers that goal-directed behaviors is fine for learning kind of basic habitual policies. Of course normally there's this value function that needs to be either computed directly in the non-stochastic setting using the Bellman equations or or some other method but but your approach is a stark departure away from having this value function.
Again you've said everything that I could possibly say so I'll send you on my next lecture tour that'll take the pressure off me. Yeah absolutely and of course I forgot to just to highlight this sort of exploitation exploration dilemma that has done 20th century thinking minimizing this mixture that just is the expected free energy. You've got exploration and exploitation solved for free in the right order so you normally see this food in the fridge before you start preparing your meal you don't do it the other way around. And but you said it you said that the Bellman optimality principle is only fit for purpose if there exists a value function of states that will ensue if I connect to that action.
Let's talk about Markov blankets. Markov blankets are probably the one piece of jargon which you're going to hear today more than any other term. We have an innate common sense notion of things and the boundaries that separate them. However capturing this mathematically is more difficult than we might expect. The Markov blanket concept formalizes these notions and underpins the Free Energy Principle. One of the pivotal concepts in the Free Energy Principle is Markov blankets. Tell us about them.
They're relatively straightforward. If you imagine here on our screen we're showing an image and if every single one of these little disks that you see there was a state and if you have a system that can be partitioned then the red dots that are in the middle are the thing itself, the blue dots that are outside are the universe at large, the external environment, and the yellow and orange dots in between form the Markov blanket. And what the Markov blanket requirements are is that the red is able to interact with orange, okay orange is able to interact with yellow and yellow is able to interact with the blue but what we don't have is we don't have blue being directly affected and vice versa by red. So we don't have this. So instead we have this, these boundary sets. We partitioned all the state space into an internal group the red ones, an external group the blue, in these blanket states that sit in between the two and facilitate the interaction between external and internal. And why these are important for the Free Energy Principle is they set up these conditional independencies which say that the blue states as long as I know yellow and orange they're independent informationally from the red states and likewise the red states so long as I know the blanket states are independent of the external ones.
And yet future conceptions might rely on even more general concepts that allow for Markov blankets like for example wandering sets. I'd like to explore that as you put it maliciously engineered false dichotomy a little bit further but in a different context and someone of the Markov blanket for example you were with Sean Carroll long ago and I think he asked does a hurricane have a Markov blanket and he said well no it doesn't and that's that's quite annoying actually if it's enough of a boundary enough of a blanket if you will I can still think about in useful ways is that true I mean do we really need an exact Markov blanket or is it flexible enough that it can be quite a fuzzy boundary?
There's an excellent question and the honest answer is I I don't really know at this stage but what is known and in not knowing that I mean that in a positive way that this is a future challenge I think people will contend with in the next few years. So in an idealized formulation the Markov blanket exists at non-equilibrium steady state so it exists in eternity in a very crisp and well-defined way that there are specific conditional independences that allow for a vicarious coupling between the inside and the outside. So it's the device that gets you out of 20th century equilibrium physics that we're not talking about closed systems anymore we're talking about non-equilibrium steady states. So we're really in the sort of the things that people like Sean Carroll a lot of other people are contending with at the moment the physics of open systems and self-organizing systems and a Markov blanket plays an incredibly crucial role here in demarcating the edge of the system as it were that allows you to identify something stuff on the inside. The Markov blanket has to have a kind of synchrony with stuff on the outside and in virtue of those conditional dependencies that stipulatively define the Markov blanket you can now treat the internal states as parameterizing probability distributions or belief distributions about external states. So there's quite a fundamental bit of information geometry that you bring to the table when you have a Markov blanket that suddenly you can interpret the machinations on the inside in your computer or your variational auto encoder or your brain as having beliefs of a Bayesian sort about what caused these data what's going on the outside. So the Markov blanket is absolutely central everything inherits from the Markov blanket.
So to move on to your more challenging question does a hurricane or the eternal flame have a Markov blanket and strictly speaking no it doesn't because you've got this fuzzy leaking. It is from the point of view somebody's wanted to simplify things as a physicist very irritating but of course it's also incredibly important and challenging. So where would you go to try and understand these fluctuating blankets where you have exchanges and I worry about this every time I cut my fingernails or have my hair cut at what point did my Markov blanket become an external state. So there's clearly there's clearly a bit of work to be done mathematically to accommodate Markov blankets as themselves dynamically random objects. My guess is that you're going to probably go back to the work of Irkov who was this one of the key intellectual architects of ergodic theory in ergodic theory and he was at one point occupied by the notion of wandering sets. So if we think of the Markov blanket as a partition of all the states of the universe into lots and lots of particles that comprise the internal states and their Markov blankets and if you consider that partition into particles as a partitioning into subsets and then you bring wandering sets into play you can now start to see a mechanics and a mathematics where you can now actually explain things like hurricanes and candles. 3D printers printing themselves is a species of 3D printers one big Markov blanket or do I drill down and just say Markov that only really exists for the lifetime of the 3D printer. So all of these issues I think speak to exactly what you're drilling down on which is how can you accommodate fluctuations and if you like physics of non-equilibria not of states of a universe but of the blanket or the partitions that define the other Markov blankets.
Does the Free Energy Principle conform to itself if we can imagine into the future maybe and if in the spirit of the Free Energy Principle we maintain uncertainty about the Free Energy Principle? Yeah that's very clever yes yeah so I often say in moments of vanity and pride that the Free Energy Principle is one of the very few principles that conforms to itself. It's trying to provide an accurate but minimally complex explanation for everything and the only other thing that I know that conforms to itself is the principle of natural selection in the sense that the theories of natural selection themselves evolved from Perry and third world and in that sense this notion that the Free Energy Principle should accommodate a judicious amount of uncertainty about itself is absolutely right yeah that's a great very clever observation.
Friston would argue that certain states of the world and certain states of knowledge would kind of transform themselves conforming to probability theory. The Free Energy Principle implies that non-equilibrium steady-state systems must directly model such states of knowledge and maintain them according to the rules of probable inference in order to continue existing. In other words survival fitness requires inference.
We had this very interesting point from Conor about there may be game theoretic pressures let's say to drive down accuracy in in some sense. The Free Energy Principle is a lot about the idea of we want to gain information to create a better more accurate model of the world around us but there are situations in game theory and decision theory where that's actually not fitness enhancing. You might not want to learn the face of your kidnapper because he's more likely to kill you.
Yeah that's a fascinating area and I I see those those sort of themes in many different contexts I never heard that before about not wanting to know the face of your kidnapper but that's a beautiful example. It really does tell you that objective functions have to be about beliefs and the consequences of belief states not states of the world. So if there's one example that tells you you're not going to serve up with the Bellman optimality principle that's going to be it but it also tells you that many of these real world problems have to contend with the fact that the kind of external states that you are dealing with are composed of sentient creatures like you and that they also have beliefs.
Keith why don't we talk about the main formalism for the Free Energy Principle?
Sure so the Free Energy Principle comes down to the equation that we're showing here on on the screen which is that the free energy is the summation of of two important pieces the energy which is a measure of how well your model fits the observations or the evidence that you're observing and then the second piece which in a lot of ways is really the more important piece of the free energy is the entropic contribution and so that's the KL divergence if you will between your model of the world and then the actual hidden model of the world and the divergence between those two. It has two important pieces to it and I want to kind of call out I want to highlight one here which let's circle right there that's purely the model entropy okay so that's actually the negative of the model entropy and the in the KL divergence and so as the model gains greater and greater entropy and note that that's a positive quantity there okay then up in the free energy it's being subtracted from the free energy so the higher the entropy of your model the lower the free energy. So as you're trying to minimize free energy you've got two competing criteria one is to fit observations better and better but that will require more and more complex models which will have lower and lower entropy and therefore they will be subtracting less from the free energy. So what you're trying to do is find the model that fits the data well while also maintaining a high entropy and the reason why that's important for survival is that if you have a higher entropy model it's maintaining greater flexibility to adapt to incoming information.
So if you recall log evidence and any associated bands like free energy or an ELBO Edwin slow bound in machine learning can be written as a as the accuracy minus the complexity and the complexity is just the divergence between your posterior and your prime belief distributions. So that is a really and possibly the more important part of the free energy. The accuracy is well understood but doing it in a minimally complex and maximally compressed way that that's the heart of it. So recall the complexity is just the relative entropy between the prior and the posterior. It is the degree to which you change your mind in the face of this new data or this new sensory evidence.
The Free Energy Principle equally weights accuracy and complexity. Might it be the case that we need to have a temperature parameter like a kind of knob to tweak the relative contribution between accuracy and complexity? Would such a parameter be useful? I'm wondering is in the Free Energy Principle term with the complexity I'm wondering if maybe there should be a multiplier there like an alpha something like a Boltzmann constant that allows me to tweak the relative balance between accuracy and complexity.

welcome back to the machine learning street talk youtube channel and podcast so today we have an incredibly special
guest professor carl fristan it was one of the most fascinating conversations we've ever had on street
talk this is an old school professor he went to cambridge in 1980 and
he's one of these kind of um eccentric polymath types that you know sits on the the old
kind of chesterfield chair with all of the springs coming out and you know smoking a pipe or something like that
professor fristen is most well known certainly in the machine learning domain for his free energy principle or active
inference which is a kind of reinforcement learning flavor of that if you like but he's got an incredible
background he is an expert in psychiatry and cognitive neuroscience and
physics and bayesian statistics it's so strange just to have
all of this knowledge embodied in one person so it really was quite an interesting
conversation actually now the free energy principle has been called a postulate a natural law
an imperative an unfalsifiable principle it's been called many things it aims to
give an almost universal understanding between the mind life and the environment so how did the
free energy principle come about the free energy principle as you have just described it
started really when i was a student aspiring to put together maths and psychologies
and gets back to mathematical formalisms the you know the principles that underlie
the sentient behavior with which we are gifted and the product of that was the free energy principle the free
energy principle sets the foundation for planning as inference by explicitly
modeling the world and its states as beliefs it balances accuracy with
entropy which maintains the flexibility needed to continually adapt to future outcomes and explorations but
the more interesting game is i think better cast in terms of planning as inference enabling you to roll out
much further into the future and ask well what would happen if i did that what would my beliefs be about the state of the world in the
long term future so i think prediction in its full and glorious anticipatory
sense really takes center stage features of reality itself such as self-organized behavior and even quantum
they seem to require some kind of probabilistic bayesian belief update on world states
for example the path integration formalism from richard feynman it essentially averages over many
probabilistically weighted paths in other words functions over beliefs and has proven crucial
to the subsequent development of quantum electrodynamics
that's what happened to understand the first principles underlie sentient
behavior you have to understand the dynamics of self-organization in particular
self-organization of systems that are open to the environment that comes in through
fyman's path integral formulation and thinking not just about the flow of the dynamics of
self-organization at this point in time but trajectories into the future
and the probability distributions over those trajectories and particularly the states that act upon the outside
and then things get much more interesting you can interpret this in terms of inferring the most likely
paths basically as resting upon a prediction of states of the world
in the future conditioned upon a particular sequence of actions or policy the heart of the free energy
principle and what sets it apart from alternatives is the strict balance between
accuracy and simplicity evidence and entropy one of the things that i think is very interesting about the
free energy formulation is that prediction is half the story so getting accurate predictions about
the future while very important is juxtaposed with keeping your options open keeping a
flexible mind keeping a high entropy model of the world so that as you encounter perhaps
new situations it has the flexibility to adapt in the central role of relative entropies in this sort of variational
construct i think that your formerly that is so important in minimizing the free energy you're
also trying to maximize the entropy it seems sometimes counterintuitive but it is exactly that
which is really mandated by things like occam's principle and very practically relevant so if you
don't do that if you don't put that uncertainty into the games then you're going to run into
things like sharp minima and you're going to be searching for resolutions of that in terms of
broadening your uncertainty flattening that free energy landscape just to try and secure those
flat minima where you can be more reasonably assured that you've got some global minima
say in standard deep learning or a machine learning context so this led fristen to believe that
goal-directed behavior essentially planning based on goals is insufficient
we need to have a more sophisticated system that can reason about the uncertainty of our
beliefs we see echoes of this in machine learning we spoke to kenneth stanley recently about novelty search
and in his formalism he explicitly avoids objectives and he thinks that we should use novelty
because of the inherent deception in objective search similarly in classic machine learning we use regularization
to stop the machine learning algorithm overfitting the training set fristen argues that the
free energy principle combines all of these different paradigms we're getting quite close to the center of the
bullseye here and we're talking about the dichotomy between belief-free and belief-based methods you know you
said in your papers that goal-directed behaviors is fine for learning kind of basic habitual policies
of course normally there's this value function that needs to be either computed directly in the non-stochastic
setting using the bellman equations or or some other method but but your approach is a stark departure
away from having this value function again you've said everything that i could possibly say so
i'll send you on my next lecture tour that'll take the pressure off me yeah
absolutely and of course i forgot to just to highlight this sort of exploitation exploration dilemma that
has done 20th century thinking minimizing this mixture that just is the the expected free energy you
you've got expiration and exploitation sold for free in the right order so you
normally see this food in the fridge before you start preparing your meal you don't do it the other way around
and but you said it you said that the bellman authority principle is only fit for purpose
if there exists a value function of states that will ensue if i connect to that action let's talk
about markov blankets markov blankets are probably the one piece of jargon which you're going to hear today more than any other
term we have an innate common sense notion of things and the boundaries that separate
them however capturing this mathematically is more difficult than we might expect the
markov blanket concept formalizes these notions and underpins the free energy principle
one of the pivotal concepts in the free energy principle is markov blankets
tell us about them they're relatively straightforward if you imagine um here on our screen we're showing an
image and if every single one of these little disks that you see there was a state and if you have a system that can
be partitioned then the red dots that are in the middle are the thing itself the blue dots that
are outside are the universe at large the external environment
and the yellow and orange dots in between form the marcotte blanket and what the
markov blanket requirements are is that the red is able to interact
with orange okay orange is able to interact with yellow and yellow is able
to interact with the blue but what we don't have is we don't have
blue being directly affected and vice versa by by red so we don't have this so instead
we have this these boundary sets we partitioned all the state space into an internal
group the red ones an external group the blue in these blanket states that sit in between the
two and facilitate the interaction between external and internal and why these are important
for the free energy principle is they set up these conditional independencies which say that the
blue states as long as i know yellow and orange they're independent
informationally from the red states and likewise the red states so long as i know
the blanket states are independent of the external ones and yet future conceptions might rely on
even more general concepts that allow for markov blankets like for example wandering sets
i'd like to explore that as you put it maliciously engineered false dichotomy a little bit further but
in a different context and someone of the marcotte blanket for example you were with uh sean carroll
uh long ago and i think he asked does a hurricane have a markov blanket and
he said well no it doesn't and that's that's quite annoying actually if it's enough of a boundary enough of a
blanket if you will i can still think about in useful ways is that true i mean do we really need an
exact markov blanket or is it flexible enough that it can be quite a fuzzy boundary
there's an excellent question and the honest answer is i i don't really know at this stage but what is known uh and in not knowing
that i mean that in a positive way that this is a future challenge i think people will contend with in the next few years so in an idealized
formulation the markov blanket exists at non-equilibrium steady state so it exists in eternity
in a very crisp and well-defined way that there are specific conditional independences that allow for
a vicarious coupling between the inside and the outside so it's the device that gets you out of
20th century equilibrium physics that we're not talking about closed systems anymore we're talking about uh non-equilibrium steady states
so we're really in the sort of the things that people like sean carroll a lot of other people are contending with at the moment the
physics of open systems and self-organizing systems and a markup plan kit plays a incredible
incredibly crucial role here in demarcating the edge of the system as
it were that allows you to identify something stuff on the inside the markov blanket
has to have a kind of synchrony with stuff on the outside and in virtue
of those conditional dependencies that stipulatively define the markov blanket you can now treat the internal states as
parameterizing probability distributions or belief distributions about external states so there's quite a
fundamental bit of information geometry that you bring to the table when you have a markov blanket that
suddenly you can interpret the machinations on the inside in your computer or your variation auto encoder or your
brain as having beliefs of a bayesian sword about what caused these data what's
going on the outside so the markup blanket is absolutely central everything inherits from the markov
blanket so to move on to your more challenging question does a hurricane or the eternal flame
have a mark of black and strictly speaking no it doesn't because you've got this fuzzy leaking it
is from the point of view somebody's wanted to simplify things as a physicist very irritating but of course it's all
also incredibly important and challenging so where would you go to try and
understand these fluctuating blankets where you have exchanges and i worry about this
every time i cut my fingernails or have my hair cut at what point did my
mark or blanket become an external state so there's clearly there's clearly a bit of
work to be done mathematically to accommodate markov blankets as themselves
dynamically random objects my guess is that you're going to probably go back to the work of
irkov who was this one of the key intellectual architects of ergot history in ergolic theory and
he was at one point occupied by the notion of wandering sets so if we think of the markov blanket as a partition
of all the states of the universe into lots and lots of particles that comprise
the internal states and their mark of blankets and if you consider that partition into
particles as a partitioning into subsets and then you bring
wandering sets into play you can now start to see a mechanics and a mathematics where you
can now actually explain things like hurricanes and candles 3d printers printing themselves is a
species of 3d printers one big mark of blanket or do i drill down and just say markup that only
really exists for the lifetime of the 3d printer so all of these issues i think speak to
exactly what you're drilling down on which is how can you accommodate fluctuations and
if you like physics of non-equilibria
not of states of a universe but of the blanket or the partitions that define the other markov blankets does the free
energy principle conform to itself if we can imagine into the future maybe and if in the spirit of
the free energy principle we maintain uncertainty about the free energy principle
yeah that's very clever yes yeah so i often say in moments of vanity and
pride that the free energy principle is one of the very few principles that conforms to itself
it's trying to provide an accurate but minimally complex explanation for everything and the only other thing that i know
that conforms to itself is the principle of natural selection in the sense that the theories of natural
selection themselves evolved from perry and third world and in that sense this notion that the free energy
principle should accommodate a judicious amount of uncertainty about itself is absolutely right yeah
that's a great very clever observation fristen would argue that certain states of the world and certain states of
knowledge would kind of transform themselves conforming to probability theory the free energy principle implies
that non-equilibrium steady-state systems must directly model such states of knowledge and maintain them
according to the rules of probable inference in order to continue existing in other words survival fitness requires
inference we had this very interesting point from conor about there may be game theoretic pressures
let's say to drive down accuracy in in some sense the free energy principle
is a lot about the idea of we want to gain information to create a better more accurate model of the world around us
but there are situations in game theory and decision theory where that's actually not fitness enhancing you might not want to
learn the face of your kidnapper because he's more likely to kill you yeah that's a fascinating area and i i
see those those sort of themes in many different contexts i never heard that before about not
wanting to know the face of your kidnapper but that's a beautiful example it really does tell
you that objective functions have to be about beliefs and the consequences of belief states not states of the world so if there's
one example that tells you you're not going to serve up with the bellman optimality principle that's going to be it but it also tells
you that many of these real world problems have to contend with the fact that the
kind of external states that you are dealing with are composed of sentient creatures like
you and that they also have beliefs keith why don't we talk about the main formalism for the free energy
Main formalism for FEP
principle sure so the free energy principle comes
down to the equation that we're showing here on on the screen which is that the free energy
is the summation of of two important pieces the energy which is a measure of
how well your model fits the observations or the evidence that you're observing and then the
second piece which in a lot of ways is really the more important piece of the free energy is the entropic
contribution and so that's the kl divergence if you will between
your model of the world and then the actual uh hidden model of the world and the
divergence between those two it has two important pieces to it and i want to kind of call out i want to highlight
one here which let's circle right there that's purely the the model entropy okay
so that's actually the the negative of the model entropy and the in the kl divergence
and so as the model gains greater and greater entropy and note that that's a positive quantity
there okay then up in the free energy it's being subtracted from the free
energy so the higher the entropy of your model the lower the free energy so as you're
trying to minimize free energy you've got two competing criteria one is to fit observations
better and better but that will require more and more complex models which will have lower and lower entropy
and therefore they will be subtracting less from the free energy so what you're trying to do is find the
model that fits the data well while also maintaining a high entropy and the reason why that's
important for survival is that if you have a higher entropy model it's maintaining greater flexibility to
adapt to incoming information so if you recall log evidence and any associated bands
like free energy or an elbow edwin slow bound in machine learning can be written as a as the accuracy
minus the complexity and the complexity is just the divergence between your posterior and your prime
belief distributions so that is a really and possibly the more
important part of the free energy the accuracy is well understood but doing it in a minimally complex and
maximally compressed way that that's the heart of it so recall the complexity is just the relative entropy
between the prior and the first year it is the degree to which you change your mind in the face of this new data or this new
sensory evidence the free energy principle equally weights accuracy and complexity might it be the
case that we need to have a temperature parameter like a kind of knob to tweak the relative contribution
between accuracy and complexity would such a parameter be useful i'm wondering is in the free energy
principle term with the complexity i'm wondering if maybe there should be a multiplier there like an alpha
something like a boltzmann constant that allows me to tweak the relative balance between accuracy
and complexity there are two answers to that question
first of all absolutely not the whole the whole point of
dissolving that exploration exploitation dilemma the whole point of putting the information gain in the
same space and in the same currency and on the same footing as your log prior preferences your reward your
utility your belmonesque like imperatives is that there is a seamless
exchange in terms of gnats natural units between the decomposition of your
expected free energy in terms of this intrinsic value and this extrinsic utilitarian
pragmatic value the other answer is absolutely yes but in order to in order to
acknowledge that if you're just trying to explain
the necessary properties dynamics of systems that self-organize to some
non-equilibrium steady state you are saying nothing about the nature of that city state other than it is at
steady state so it could be very high entropy steady state it could be very low entropy steady state it could be very hot it
could be very cold you haven't really committed to any kind of steady state which means that
it's slightly disingenuous to say that the imperative for everything is to minimize
say a free energy functional and if you parameterize up with a particular parameter and we'll call it alpha
as a not to your question then suddenly you really do need this alpha and this alpha gets in
exactly as you say as a knob on the expected complexity versus the
expected accuracy or ambiguity that's not in the literature so there are ongoing debates amongst the
younger people who love the maths of this about whether we just need a generic kale divergence
or whether we need to exclude bits to get to expected free energy you have to really think about the
relative importance for this steady state of technically the risk and the ambiguity
and the sensory entropy so that's again that's a bit of an open question which i'm hoping will be
resolving about a year's time at which point your alpha will occur and i'll try to call it alpha in your honor
one of the previous guests to our show dr hari valpola the ceo of curious ai and a
computational applied neuroscientist he centers in a couple of questions for fristen actually and the answer was quite interesting but the
crux of it is the brain is highly specialized right and is the free energy principle an
oversimplification for what's going on in the brain if you take a young child around nine
months old the critical period for learning the phonemes of your mother tongue and you play some speech from the radio
the result is nothing but if you play the same speech during a social interaction
the child will learn to discriminate the phonemes in the speech structure matters structures of the
brain being very finely attuned to and adapted to the context in which
they're that they're making their inferences what would normally cast that in terms
of structure learning also known as bayesian model selection so this notion speaks to a simple
understanding of evolution or as nature's way of doing natural
bayesian model selection i.e natural selection where you operationally associate the adaptive
fitness with the probability this phenotype exists which is just the evidence that
it is there the probability of finding that phenotyping place you know but it is on some reading provably true
that for any system or agent to regulate its environment it has to embody or be a
good model of that environment what does that mean its structure must somehow recapitulate the structure of the
environment generating that it has to control or it has to engage with
so it is hardly unsurprising that the delicate deep hierarchically
structured connectivity we find in their brain and in a variation auto encoder
is a natural thing that has emerged from the evolution of these architectures
that all are conforming with the principle of free energy minimization what about daniel kahneman's system one
and system two of cognition do those fit into the free energy principle he cites kahneman system one and system
two of thinking there's this famous test where if you give monkeys a sequence of cards with a hidden pattern on
which need to be classified into two classes humans suddenly click they see the hidden rule
because their system two kicks in and they start getting 100 accuracy very quickly but you don't see that
with monkeys so valpolia was saying that he doesn't see how that phenomenon could be explained
by the free energy principle recent thinking about the cerebellum is that it plays the role
of actually a supervisor so it may well be the case that the cerebellum plays a
role in the amortization of carefully acquired skilled
movements that become increasingly skilled as the cerebellum watches the cortex
in that sense the cerebellum can i think be very usefully understood in terms of
being involved in supervised learning but i'd actually turn it on its head and basically say it's been supervised
by the cortex but in a way that allows the cerebellum to tell the cortex well normally you do it like that
do we do our belief updating and a bit of planning as inference or do we just do what we've always done
habitually respond quickly and efficiently by harnessing something that has already
been amortized and that i think is a really interesting interpretation of habitization
versus deliberative thinking which from the point of view of a neuroscientist would be the equivalent of
system one versus versus system two in that sort of edge between machine learning
and reinforcement learning sometimes referred to as model-free versus model-based so it's the bread and butter of a
jobbing neuroscientist certainly a systems neuroscientist to understand the computational architectures and the
nature of message passing implied by either belief updating or predictive
coding or variational message passing how it is enacted physiologically on a
neuroanatomy that has a deep structure connor asked fristen about predictive coding
there has been a paper that says that predictive coding can approximate back propagation in
arbitrary graphs i'm sure a friend of mine has contributed that and if there's any sense that prop has been demeaned as
something which is not that's really central to everything then i think that's probably wrong
so from my perspective it is in very the case that the
gradients with respect to anything of variation free energy can be written down as an a prediction
error which means that if you believe that the universe of interesting things is performing a
gradient flow on a variational free energy functional then you also believe that they are
by the chain rule minimizing their prediction error i think that's one of the first times
that premier scientists actually say something positive about backdrop and does the free energy principle tell us anything about the origin of life
for example abiogenesis if we take for granted that the free energy principle explains a great deal about
how certain systems of the kind we've been elucidating will function does it explain the origin
of those systems is it almost unavoidable that we will end up with these deeply
structured delicate markov blanketed systems that become increasingly rich and have
longer longer information lengths and more itinerant dynamics as the universe unfolds it would be
great to know the answer to that and to have a tractable mathematical formulation of that i'm afraid that the free energy
principle in its vanilla form as it currently stands does not give you that no all it says is
if that thing has evolved these are the properties that it must possess but at least it can tell us
we should continue exploring and looking around to address that uncertainty yes cover yes of course some better
better free energy principle next we're going to talk about richard feynman's path integral this is
Path Integral
something that fristen referred to many times during the session today
yeah so path the path integral formulation let's say of which is essential for
quantum electrodynamics for one thing is quite interesting and actually it should be familiar
in in one sense to to let's say bayesians or people who do a lot of conditional probability theory because
they may recall that the probability of say a particular event
is actually equal to the summation of the probability of that of that event
given like let's say some other state of the world okay over all possible states of that a
in other words this is marginalization or the marginal probability if you have a bunch of possible worlds
what you have to do is sum over all possible worlds and when that's applied to physics
say in the case of quantum electrodynamics what it's saying is that if you have many possible ways in which
let's pretend the photon could come from a and end up over b it could travel along
any one of these many paths here that if you're considering the total
probability of that actually happening you have to sum over all these possible states waiting
by their amplitude and that's a very beautiful consequence because in some real essence we don't
think that the photon say travels every one of those possible paths but it's as if it did and why this is
important in the free energy principle is that when we live in a universe where
you have to perform this summation over all possible worlds that means that inherently we need a
system that can model probabilities and can transform those probabilities
accurately according to the laws of probability theory and another interesting consequence of
it is that if we're playing this repeated game where we're trying to survive over time and we're getting in new information all
the time about these many possible future paths we have to model the world in a flexible
way we have to keep an entropic model a model that has a high entropy that's able to adjust
as new information comes in about those probable paths how did he find it talking to uh
How did we feel talking to friston?
professor fristen oh i i really i have to say i very much enjoyed talking to professor
fristen when i went into the preparation for this call some weeks back
i would say i was probably more skeptical of the free energy principle than i am now but as we've learned a lot
over the last few weeks and then really having a chance to pose some questions uh to professor
fristen and hear his answers uh yeah i think this is a very interesting principle
uh and i think it's i think we'll find increasingly as we become more sophisticated with both
the modeling of the principle and the application of the principle that we are going to find many systems
that that conform to it so i find it quite interesting and completely enjoyed talking to him i wish
i lived next door to him i'd probably hop over there once in a while to have a sherry and just discuss
deep topics he has such an intuitive understanding of deep topics that
it's sometimes hard to keep pace but if you can it's it's very fun yeah because if you look
at the free energy principle on wikipedia it even says at the top of the article that
it's very complicated even experts in the field just have trouble getting their heads wrapped around it and when you listen to
professor fristen talk he clearly is a polymath he has deep knowledge of so many different
fields and it's really interesting to have all of that embodied in one person because the level of cross-pollination
is really quite impressive but by the same token there's so much jargon and he's diving
into so many different areas that it does make it quite difficult to follow what he's talking about
i think that wikipedia has got it wrong that it's complicated i think that we often make the mistake
of thinking that things that are hard to understand are inherently complicated and i think that's wrong i think
simple and easy are very very different concepts it's possible for
simple concepts to be very difficult to understand and indeed to take human civilization thousands of years to
discover and i think this i think the free energy principle falls under the category of
simple but very difficult to understand very deep deep concepts almost like some of the
concepts that rest at the foundation of mathematical logic or probability theory you know when you
start to think about puzzles like this sentence is false right or if you
think about what is the meaning of probability is is it a frequency is it a degree of rational belief
why or why not you know these are very deep concepts at the end they can be expressed relatively simply
on paper but still be very difficult to understand thank you very much they're very
informed questions i got a sense you knew the answers before you asked them that's how i felt
anyway we really hope you've enjoyed the episode today we've had so much fun making it remember to like comment and subscribe
we love reading your comments and we'll see you back next week the like new yorkers are rude
Skit - on cultures
and blunt you know they're they're they're very direct and they'll be about it well germans are polite but blunt like
germans will very politely tell you your code is completely unacceptable but they'll be very polite about it
that's kind of slightly similar to uh southern culture or classic southern
culture in the us it's very polite but straightforward like they don't like beating around the bush you know but i would say they don't
go as far to the rude spectrum while being blunt like they still are straight forward but politely i've i'm
super sensitive to people beating around the bush yes that's it that's why i was funny that when you told me you were like a
traitor in new york i was like yeah this makes a lot of sense like straightforward and polite i love germans i worked with a few of
them in my lab and in graduate school and i like i also like how rule-based they are like there are rules
and you follow the rules when you open the door you close the door you close it you don't leave it half open
it's like i love it that's true it's true it's both a blessing and a curse i used to work
with some radioactive dyes and i disposed of one in the wrong container so i disposed of like
the betas in the alpha container or something and it caused like a cost like a couple hundred dollars or
something the german postdoc there was so like pissed at me but polite he's like
just keeps going on and on about how can you put a in the b container right that's just
not how it happens that should have never happened i don't know what we should do about this
but something needs to happen to make sure you never do that again yeah that is such a german thing i i've
heard that exact conversation with people before he would keep just wouldn't let this go i'm like yeah i'm sorry i screwed up you
know it wasn't a good enough explanation it was like what is broken that we need to fix so
this never happens again that's the most german thing i've ever heard hello hello
Friston joins
hi there hello hello professor fristen great to meet you nice to see you fantastic now i'm not an
expert on etiquette is it dr fristin or professor fristen which is more correct in england it would be professor pristin
okay in the states i think i've heard that teachers are called professors so they prefer to be called
doctors right in the uk it's a professor gotcha and tech industry is first names only
[Laughter] welcome back to the machine learning
Main show introduction
street talk youtube channel and podcast with my two compadres connor leahy
and mit phd dr keith duggar now today we have a very special guest
professor fristen he is a british neuroscientist at university college london and an authority on brain imaging he
studied natural sciences physics and psychology at the university of cambridge in 1980
and completed his medical studies at king's college hospital in london a strong indicator of
professor fristen's illustrious career is that he's been cited over 206 thousand
times with an aged index of 239 in 2016 he was ranked the most
influential neuroscientist on semantic scholar and carl fristan pioneered and developed
the single most powerful technique for analyzing the results of brain imaging studies
he's currently a welcome trust principal fellow and scientific director of the welkin trust center for
neuroimaging his main contribution to theoretical neurobiology is the variational free energy principle
also known as active inference in the bayesian brain the free energy principle is a formal statement
that the existential imperative for any system which survives in the changing world can
be cast as an inference problem the probability of existing as the
evidence that you exist if you will you can always interpret anything which exists as being separate
to the environment it exists in carl asserts that existence is a kind of interface
between the interior and the exterior so the free energy principle which is
closely related to the bayesian brain hypothesis is a simple postulate with complicated
implications any adaptive change in the brain or indeed any system which exists
will minimize surprise or free energy as cold puts it this minimization could be on any time
scale or on any system which resists a tendency to disorder from single cell organisms
to social networks the bayesian brain hypothesis states that the brain is confronted with
ambiguous sensory evidence which it interprets by making inferences about the hidden states which
caused the sensory data so is the brain an inference engine the key
concept separating fristen's idea from traditional stochastic reinforcement learning methods and even bayesian
reinforcement learning methods is moving away from goal directed optimization
belief based updating combines the ambiguous information with prior beliefs about the nature of the world the
missing information problem is something which dogs many areas of machine learning as we discussed on our gpt3 episode last
week implementing the bayes rule directly is often computationally intractable and computer scientists drew inspiration
from the physics world for creating approximate inference techniques called variational bayesian methods
and carl's active inference method uses these techniques to great effect anyway professor fristen it's an
absolute honor to have you on the show welcome and how did you come up with this exciting principle
well first of all let me congratulate you on that beautiful introduction you said everything that i could possibly say in the next hour and a half
so i'll just try and recapitulate what you said the road to the free energy principle as you have
just described it started really when i was a student aspiring to put together maths and psychology so
in those days it would have been known as mathematical psychology nowadays computational neuroscience
and leading of computational neuroscience into machine learning so from the start that was the ambition
more practically though as your brief resume indicated i got a bit distracted by becoming
a doctor and then a psychiatrist in you know out of clinical compassion but also
partly out of an interest in understanding how the brain works and then inevitably one gets back to
mathematical formalisms the the the principles that underlie the sentient behavior with which we are
gifted and the product of that was the the free energy principle or active inference in a sort of more cognitive neuroscience
setting i'd like to ask you about two kind of related topics that have interested in machine learning
Is prediction all it takes for intelligence?
lately is i was interested if you were familiar with the work of jeff hawkins from numenta who
is a unsung hero among machine learning inspirations and he had a quote saying it is the
ability to make predictions about the future that is the crux of intelligence and recently with uh machine learning
progress such as with gpt3 which you know is a better and better predictive model and some would argue
including myself also becomes more and more intelligent in a meaningful way so my question is prediction
really all it takes for intelligence or is there more to it i think prediction figures very centrally in the sort of
dynamics that we're talking about can answer that question from two perspectives often cast in terms of
the high road and the low road to that formal understanding of things like active imprints
so that the low road would really be a bottom-up approach thinking what does the brain do and on that view or on that approach
the the big move in the 21st century has been towards predictive processing and it
started with predictive coding as a nice metaphor for message passing in the brain now
generalized to subsume action and decision-making and choices and epistemic foraging
and so andy clark coined the the phrase predictive processing to it to accommodate that and in that sort of formulation of
sentient behavior prediction is absolutely essential at two levels and from the point of view of predictive
coding obviously it's baked into the title that you're you're trying to predict
what you will see under some belief about the sort of latent states generating some
data or you could formulate that in terms of compression minimizing message length and efficient
making sense of data or unpacking data the prediction in that sense is i think
not quite the kind of prediction that you're asking about which is uh which has this sort of temporal
aspect sort of the forecasting or anticipatory aspect of prediction however once you
move predictive coding into a sort of bayesian filtering setting and
you put dynamics in play then when you're trying to predict the trajectories in the moment you are
implicitly predicting a short-term future so i think sort of prediction in the dynamical the temporal
sense starts to bite again beyond that there is in the
neurosciences an appreciation that that's not the end of the game you can get a long way
on this low road of understanding in terms of understanding how we act and perceive and how action
is in the service of perception vice versa through treating motor behavior responses
of an embodied brain in terms of reflexes and this would be very much a predictive coding explanation of the action perception
cycle essentially equipping predictive coding with reflexes of this sort of in the moment sort yeah you
could write down in terms of differential equations or kalman bc filter but the more
interesting game is i think better cast in terms of planning as inference so actually including
what i'm doing as a random variable in your inference problem and enabling you to
roll out much further into the future and ask well what would happen if i did that what would my beliefs
be about the state of the world in the long term future and that gives a very different
aspect to prediction that you're predicting the consequences of any move on the world of any data that you might want to
sample how will that reduce my uncertainty what information will i gain what relevance does that have
for the kinds of preferred outcomes that characterize me as a goal-directed creature so
i think prediction in its full and glorious anticipatory sense really takes center stage and when
people talk about active imprints that sort of implicitly they're talking about this sort of
fuller deep temporal approach to inferring
what should i do next and then from those inferences selecting the next move to to make so in that sense the
other sort of the hierarchical temporal models that dalip and jeff hawkins have have been
talking about for you know decades as well and i can remember reviewing as a handling editor the first publication plus computational
biology on the on this work and it was refreshing and i think that that's exactly
uh the kind of hangers inference in the future consequent on or conditioned upon the
different kinds of policies or sequential uh sequences of actions that i could entertain bringing time for center stage
in into the inference problem the high role i should just add so using a completely different language now
that i would use as a physicist to promote the importance of prediction it takes a slightly different view it
says well to understand the first principles that underlie sentient behavior
you have to understand the dynamics of self-organization in particular self-organization of systems that are
open to the environment to their eco niche to their heat bath their heat reservoir and when
one does that you can use uh dynamics and random dynamical systems to say
the kind of moves and and changes of the systemic states must
have this form of predictive coding or bayesian or kalman like filtering in
the moment and that's relatively straightforward to show and there was a hint
of the requisite mathematical apparatus you needed to make those assertions in
the introduction and specifically mark off blankets that separate me from not me so that would be grade one if you like
uh prediction it's just that we have dynamics and the dynamics required a self-organization to non-equilibrium
steady state require some in the moment kind of prediction so where is the sort of the the higher
end anticipatory of dynamics well that that comes in through fyman's path integral
formulation and thinking not just about the flow of the dynamics
of self-organization at this point in time but trajectories into the future and the
probability distributions over those trajectories and particularly the states that act upon the outside
the if you like formally characterize what we do over extended periods of time so when
you bring the path integral uh formalism to bear on these non-equilibrium steady state
distributions then you can sort of say what kinds of policies as i move into the future
are more likely and which are less likely and then things get much more interesting and we talk about sort of ambiguity and
risk and what the imperatives are for long-term behaviors and underneath all that there is an interpretation
that i'm really trying to predict or you can interpret this in terms of inferring the most likely
paths basically as resting upon a prediction of states of the world in the future
conditioned upon a particular sequence of actions or policy one of the things that i think
is very interesting about the free energy formulation is that prediction is half the story so getting accurate
balancing accuracy with flexibility
predictions about the future while very important is juxtaposed with keeping your options open keeping a
flexible mind keeping a high entropy model of the world so that as you encounter perhaps
new situations it has the flexibility to adapt more quickly that incoming information and that
because it's a repeated game you're not just trying to optimize the very next step only but
the entire trajectory of your existence if you will and and that's captured in the free energy principle inside the kl
divergence part of that is the entropy of my model of the world and the larger that is
the lower the free energy is this interesting interplay and you also point out in a
video too that when it's this repeated game it's related in a way to what in other fields
is called the exploration versus exploitation kind of trade-off like in the multi-armed bandit
world where i can take an action that's maximally exploited but but i may not learn very
much and then on the other hand i can take an action that's purely just to learn about the world but may not
achieve much of my other objective and what i love about that is it explains why we're always so tempted to push the
button why people always want to press the button and see what happens or go out and explore
even if there's no immediate benefit and it has so many connections to things like novelty search and multi-arm
banded analysis it's quite interesting yeah you bring so many fascinating points there yeah
and under robotics intrinsic motivation and robotic artificial curiosity and the schmidt hoover-like sensor which
itself all comes back down to this minimizing the complexity and paradoxically and celebrating
uncertainty so if you allow me you've made so many good points there i i can't resist just
highlighting the first of all predictions only half the story absolutely i mean why are we predicting
we're predicting in order to infer what to do next so the doing the action the inactive aspect really becomes
essential thing in terms of well things that are written into the description like self-organization how i
organize myself how what i do and if you're in data science that would be basically
how do i optimally update a mine can i find asian optimum design principles
written into the formalism the variational formalism that the free energy principle so i think
just saying that perception is great if you're just studying the visual cortex
or you're interpreting some given pixelated image but the real challenge
is really how do you go and take that picture and how do you move your eyes around and sample that information that's going
to make much more sense in the world so it's all in the service of what i'm going to do you mentioned that the kl
divergence the central role of relative entropies in this sort of variational construct
i think that your for me that is so important so a very simple perspective on free
energy which i think is useful certainly for students is it just to remind them that the free energy is some expected potential some expected
utility if you like and complemented by the entropy and in minimizing the free energy you're
also trying to maximize the entropy we've seen sometimes counter-intuitive but it is exactly that
which is really mandated by things like occam's principle and very practically relevant so if you
don't do that if you don't put that uncertainty into the game so you don't commit to a very precise explanation for these
data then you're going to run into things like sharp minima and you're going to be searching for
resolutions of that in terms of broadening your uncertainty flattening that free energy landscape just
to try and secure those those those flat minima where you can be more reasonably assure
that you've got some global minima say in standard deep learning or a machine learning context
you know that would be a story you could tell just about the composition of why free energy rests upon entropies and
relative entropies but you took us um straight to the heart of the sort of deeper in time
inference that comes along with the active inference which is this sort of this implicit imperative to reduce
uncertainty that can often be described in terms of responding to salience or epistemic affordance to say if i did
that what would happen what would i know what information would i gain novelty you mentioned so
technically what we tend to do is to talk about the resolution of uncertainty or the information
gain that is formally described by kl divergence between my beliefs about states of the world
with and without those sensory samples or observations that i would get if i
did that so that kl divergence can be applied to unknown states the world and that would
be driving behaviors like looking over there to make sure that my hypothesis that was a butterfly or a
bird or a candle was the best explanation for these sort of peripheral visual sensations
but you've also got unknowns for example in a deep learning scenario the the connection strengths
you know in the brain parameters that underwrite our brain connectivity that encode the lawful contingencies and
statistical regulations of likelihood mappings or probability transition matrices
so these don't change quickly in time but this still are equipped with a posterior belief or
some some stochastic representation about which you can reduce uncertainty and we call that novelty so if you can
get yourself into a situation where you reduce your uncertainty about
the contingencies and the parameters of your generative model then you're responding to their again an
epistemic affordance there is exactly this a resolution of
uncertainty formally we would write that down as an expected free energy i don't know if this helps
but one way i find useful to think about this and indeed explain to
to students is free energy is a bound on log evidence simply the probability
of some data under a model of how i thought those data were generated
and you can always split that into accuracy and complexity so if i have a statistician and i wanted to minimize my physics
free energy or maximize my machine learning free energy which is because it's just an evidence
lower bound and so you'd find in a variational auto encoder what am i doing
if i decompose the log evidence into accuracy and complexity what i'm trying to do
is minimize the complexity of my accurate expectations and then we
get back to minimum description lengths the underlying say you know monograph like complexity
formulations of your most efficient coding and the like so you've got this
way of looking at self-evidencing in the sense of just forming good beliefs
of how my data were generated in terms of providing the simplest
but at most accurate explanations or accounts of the data at hand so if we come back to this to the
previous discussion about what would happen in the deep future so i did a deep research
over all the sequences of moves that i could make what would the expected accuracy and the
expected complexity look like and if you write that down they come out as things like risk and
ambiguity so the expected accuracy or more precisely expected inaccuracy the
negative accuracy the negative probability of your data under beliefs
about their causes becomes ambiguity becomes the conditional uncertainty if you like
about the observations if you knew them and the the expected complexity becomes risk
or it has exactly the same form that you'd find in kl control theory or risk sensitive control in economics
it's just the relative entropy or the divergence between what you think will happen if you did that
and what a priori you think is going to happen which normally people treat as a sort of the
preferred outcome the kind of things that a creature or a system or an agent like me
would normally encounter so that ambiguity is actually the thing that you were talking about the reason why we push
that button or open that door or go on that trip or go into that google page you know it
is written into it is if you like the homolog of our aspirations for accurate accounts
of all the sensory and other data that we have to assimilate
when we consider the expectation in the future conditioned on what would actually do
we're getting quite close to the center of the bullseye here and we're talking about the dichotomy between belief-free
belief-free vs belief-based; beliefs are crucial
and belief-based methods so you've been sketching out this really interesting idea that we can take subsequent actions
by maximizing the expectation over a a generative model of states in distribution and subsequent
policies but the alternative is so-called goal-directed behavior now you've said in your papers that
goal-directed behaviors is fine for learning kind of basic habitual policies but you cite this wonderful example with an
owl you say that an owl doesn't necessarily know where the mouse is in in the field there might be
some ambiguity there might be some uncertainty and using a simple goal directed policy the hour would just go straight to the
mouse and and try and eat the mouse now it's quite interesting to contrast your approach to other forms of let's
say bayesian reinforcement learning or traditional stochastic reinforcement learning of course normally there's this value
function that needs to be either computed directly in the non-stochastic setting using the bellman equations or
or some other method but but your approach is a stark departure away from having this value
function again you've said everything that i could possibly say so
i'll send you on my next lecture tour that'll take the pressure off me yeah
absolutely and of course i forgot to just to highlight this sort of exploitation exploration dilemma that has dog 20th century
thinking of course that just dissolves in the 21st century because you know risk and ambiguity sometimes
you can exchange the the terms in this expected free energy formulation uh and re-express that as an intrinsic
um and extrinsic value where the intrinsic value is something that people in robotics artificial curiosity would
recognize as that's of epistemic information gain uh part and the extrinsic value is just the
expected utility of the expected reward and in minimizing this mixture that just
is the expected free energy you you've got exploration and exploitation sold for free in the right order so you
normally see this food in the fridge before you start preparing your your meal you don't do it the other way around
so that's you know what you were hinting at in terms of the owl opening its fridge and searching it's
slightly disingenuous of me i think to use such a stark
contrast dialectic between what is in essence a whole bunch of things
predicated on the bellman optimality principle and contrasts that with another way of doing
it which is the which is essentially a variational hamilton's principle station reaction so
the free energy principle inherits from the physics of non-equilibrium that you will find
from thyman's path integral formulation of quantum electrodynamics right through to hamilton's equations of
your motion so there are these this is the variational principle that is the first principle that we were mentioning
before so the question is do you choose between variational principles of station
reaction or do you go for optimality principles and in that choice what's the big commitment you're making
and you said it you said that the bellman optimality principle is only fit for purpose
if there exists a value function of states that will ensue if i commit to that action whereas
the variational principles of least action being a path integral of an energy and an energy being a log
probability of a probability distribution immediately tells you that the objective function if you want
to cast it in terms of normative theories of optimization the objective function
is a function of a probability distribution so it has to be belief based a problem if
you if read a probability distribution is a bayesian belief so if you allow me to talk about beliefs
simply as uh conditional probability distributions in the sense of belief propagation or bayesian beliefs
then we know that the the from physics the objective function the
lipoon off function the cost function has to be a functional function of bayesian beliefs
so that comes back to your point that if you go down the bellman route the rl route the optimal control route
then you are predicting everything on a value function of states if on the other hand
you go down a variational or a physics route then your objective function has to be a
functional of beliefs about states and that's where you get the resolution of uncertainty that's
where searching gets into the mix because to search is to resolve uncertainty but
uncertainty and surprise and all of these other attributes
of belief updating are all attributes of probabilistic beliefs probability
distributions so you know you have to have a function of probability distributions in order to account
for sentient behavior and i would say including goal directed behavior why is
that disingenuous well it's disingenuous because of course what you can do
is take this more general formalism this variational formalism and take out of it all the uncertainty
and then you can get back to the bellman optionality principle so really there's not a dialectic here it's just
that the optimality principle deals with a special but very ubiquitous and pragmatically very important case where
you can discount various sources uncertainty so common examples here let's ignore the partially observed
aspect of a problem let's assume that our observations tell us everything we need to know about
latent states causing data or latent states of the plant that i'm trying to try to control
so that takes ambiguity out of the expected free energy before before you do anything what
you're left with where you're left with the expected risk what's that's the unexpected complexity
so that's just a probabilistic measure relative entropy measure of the distance probabilistically
between your prior preferences your goals your your rewarding states
and what you think will happen so if you say look now let's assume for simplicity
that it doesn't matter every which way that i can do this the uncertainty about what's going to
happen is not going to change that means that risk now doesn't play
any role anymore other than to um score the expected
um utility or the expected log of your prior preferences that just is bay's bayesian decision
theory so you can get quite easily back to what was a deliberate but maliciously engineered
dichotomy you can sort of dismiss that just by acknowledging that you only need to worry about uncertainty
and epistemics when you put uncertainty and not knowing
your into the mix i'd like to i'd like to explore that as you put it maliciously engineered
Fuzzy Markov Blankets and Wandering Sets
false dichotomy a little bit further but in a different context and it's one of the marcotte blanket for
example you were with uh sean carroll not long ago and i think he asked does a hurricane have a markov blanket
and and he said well no it doesn't and that's that's quite annoying actually that it doesn't have a conv or maybe the
eternal flame is sort of the the nemesis because it doesn't we get to this when is a pile
of sand a pile of sand what i'm curious about is does the concept of a markov blanket
for the purposes of uh contemplating the free energy principle can it be a fuzzy marcotte
blanket so you know just for an inanimate example i can imagine a markov blanket around the
moon and one around the earth but on the other hand they gravitationally interact but i don't
think that precludes me from thinking about dimensions of the free energy principle
even if even if there are interactions that maybe i that pierce the boundary if you will but
still if it's enough of a boundary enough of a blanket if you will i can still think about in
useful ways is that true i mean do we really need an exact markov blanket or is it
flexible enough that it can be quite a fuzzy boundary there's an excellent question and the
honest answer is i i don't really know at this stage what what is known uh and in not knowing
i mean that in positive way that this is a future challenge i think people will contend with in the next few years and i'll and i'll
try to explain why that's important from my perspective the the crisp and clear consequences of
having a markov blanket is when one unpacks it right through to the path integral formulation the implications for the
good trajectories in terms of minimizing expected free energy really do rest upon
that being a well-defined markov blanket which as you say is the mechanism that
allows for these connections and influences at a distance that would
keep the moon in orbit around the earth for example whilst at the same time accommodating
the conditional independences that enable me to distinguish the moon from something else
so in an idealized formulation the markov blanket exists at non-equilibrium
steady state so it exists in eternity in a very crisp and well-defined way that there are specific
conditional independences that allow for a vicarious coupling between the inside
and the outside so it's the device that gets you out of 20th century equilibrium physics so
we're not talking about closed systems anymore we're talking about uh non-equilibrium steady states so
we're really in the sort of the things that people like sean carroll a lot of other people are contending with at the moment and
the physics of open systems and self-organizing systems and a markup plan plays a incredible
incredibly crucial role here in demarcating the edge of the system as
it were and it allows you to identify something so anything has to have a markov blanket strictly
speaking for a particular period of time just as an aside
what happens when you do that is stuff on the inside the markov blanket
has to have a kind of synchrony with stuff on the outside and in virtue of those conditional
dependencies that stipulatively define the markov blanket you can now treat the internal
states as parameterizing probability distributions or belief distributions about
external states so there's quite a fundamental bit of information geometry that you've
been to the table when you have a markov blanket that suddenly you can interpret
the machinations on the inside in your computer or your variation auto encoder or your
brain as having beliefs of a bayesian sort about what caused these data what's
going on the outside so that's absolutely crucial for the whole sort of active inference
and certainly representational or realist or anti-realist sort of philosophical interpretations so the
markup blanket is absolutely central everything inherits from the markov blanket so everything else was in play
before we have the vodka plank equation we have the scrolling wave equation we have variational principles of stationary
action and pathetical formulations that's all there all you need to do is to drop the markov
blanket in and then you get active inference so to move on to your more challenging question
does a hurricane or the eternal flame have a mark of black blanket well strictly speaking no it doesn't
because you've got this fuzzy leaking it is from the point of view somebody's wanted
to simplify things as a physicist very irritating but of course it's all also incredibly important and
challenging so where would you go to try and understand these fluctuating blankets where you
have exchanges so just technically you've got external states and then you've got blanket
states that intervene between the internal states and the external states and yet with something like a candle
flame or a hurricane you seem to have this exchange that what was once an external state becomes in a
blanket state and what was once a blanket state becomes an external state and i worry about this every time
i cut my fingernails or have my hair cut at what point did my mark or blanket become
an external state so there's clearly there's clearly a bit of work to be done mathematically to
accommodate markov blankets as themselves dynamically random objects
my guess is that you're going to probably go back to the work of irkov who was one of the key
intellectual architects of ergot history and ergodic theory and he
was at one point occupied by the notion of wandering sets so if we think of the markov blanket as a partition
of all the states of the universe into lots and lots of particles that comprise
the internal states and their mark of blankets and if you consider that partition into
particles as a partitioning into subsets and then you bring
wandering sets into play you can now start to see a mechanics and a mathematics
where you do actually can now actually explain things like hurricanes and candles and just for interest
literally a couple of weeks ago there was a nice paper in frontiers treating the biosphere as a markov blanket
so you know that there is practical and important sort of you know pressures in order to formalize what are the
markov blankets of these large-scale structures and my guess is that the notion of
wandering sets and the time scales over which internal states exchange with external states and
internal states external states exchange with blanket states are going to be going to be an important issue and i say
that because of course we develop what point when i i'm born and what point am i die
does my can i what happens to my mark off blanket reproduction 3d printers printing
themselves is a species of 3d printers one big markov blanket or do do actually drill down and just say
markup only really exists for the lifetime of the 3d printer so all of these issues i think speak to
exactly what you're drilling down on which is how can you accommodate fluctuations and
if you like physics of non-equilibria
not of states of a universe but of the blanket or the partitions that define the other markov blankets if we can
imagine into the future maybe and if in the spirit of the free energy principle we maintain uncertainty about the free
The Free Energy Principle conforms to itself
energy principle it may be the case that is we extend it to say wandering sets with wandering points we
may develop a mathematics of more of a distance metric this cloud of points is currently this
distance from a particular wandering point and they're orbiting around and there may be some
dynamics in there and then if we follow a similar analysis we might end up back at the free energy principle plus
another term for example like there may be an extra term over there which could be important would that be kind of a
fair speculation of what might happen well yeah that's very clever yes yeah so i often say
in moments of vanity and pride that the free energy principle is one of the very few
principles that conforms to itself it's trying to provide an accurate but minimally complex explanation for
everything and the only other thing that i know that conforms to itself is the principle of natural selection in
the sense that the theories of natural selection themselves evolved for perry and third world and in that
sense this notion that the free energy principle should accommodate a judicious amount of
uncertainty about itself is absolutely right yeah that's a very very clever observation in
terms of the form i think that's probably right as well i mean you're asking me to think about you
know where we might be in in say 10 years time and so this is just hand waving but certainly one could
imagine variational principles of stationary action applied not to probability distributions over
states but probability distributions over over partitions uh and sets and getting into some things
like category theory and the like so one can see a sketch or an image of the future kind of maths that there
might be that might conserve the relatively simple principles that
underwrite the free energy principle but now applied at some one level up as it were so not to the actual system itself but
to the probabilistic configurations and the partitions that define that principle if i can zoom
out a little bit here so the free energy principle is a lot about the idea of we want to gain information
useful false beliefs
to create a better more accurate model of the world around us and but there are situations in game
theory and decision theory where that's actually not fitness enhancing so a few examples here you might not
want to learn the face of your kidnapper because he's more likely to kill you and there's the other thing where you
might so this is an information you don't want to gain and sometimes it's also useful to have false beliefs for example it can be
useful to think you're smarter than you actually are or more confident than you actually are because that will help you in social situations yeah that's a fascinating
area and i see those those sort of themes in many different contexts wishful thinking
deliberately avoiding certain sources of information not wanting to open a letter that tells
you whether you've passed your exams or a letter from the doctor that contains your the results of your
recent scan for cancer for example there are things that we don't want to know so we're talking about very metacognitive things in a sense
that i never heard that before about not wanting to know the face of your kidnapper but that's a
a beautiful example it really does tell you that objective functions have to be about beliefs and the consequences of
belief states not states of the world so if there's one example that tells you you're not going to serve up with the bellman
optimality principle that's going to be it but it also tells you that many of these real world problems
have to contend with the fact that the kind of external states that you are dealing with are composed of
sentient creatures like you and that they also have beliefs so now you get into the game
of putting lots of active inference agents together and multi-agent scenarios and
how you infer the degree of sophistication with which you infer
the intentions of others and the belief states of others and all all that gets into these very deep and
enriched generative models that themselves now represent the belief states of other
active inference uh your optimization machines as it were one other level i think that
you can understand these sometimes paradoxical or counterintuitive expressions of
optimality is just to acknowledge that
the whole of the bayesian brain hypothesis the whole basis of indeed free energy
principle is a statement about prior beliefs
and as such prior beliefs are going to be in the context of
self-evidencing necessarily optimistic so if you remember before i was reading
prior beliefs about the outcomes consequent on the behavior as preferences and the only reason i say
preferences is because if those are the kind of states that i typically find myself in so if i'm a
physicist though the attracting set of my non-equilibrium steady state then it looks as if i will always be
working towards these prior states so they look literally mathematically
attracting in the sense of being an attracting set but also psychologically attractive and valuable and therefore the preferred
states that i worked towards so baked into a bayesian reading of the information
theoretic imperatives for choice is an optimism you're always moving
towards or trying to solicit evidence that confirms that you are an eternal
immortal well-loved warm creature so it has to be like it can't be any
other way manifestations of that i always find appealing because they're just statements of the fact it couldn't be
any other way i have to believe myself to be an expert in this or very proficient in that
in order to realize those preferred fantasies through action to
actually secure the evidence yes i am that kind of thing without those priors without those optimistic priors
you would not get the kind of active inference that underwrites our existence to come back
you know to some of the phrases that tim was using to introduce their free energy
we had this very interesting point from conor about there may be game theoretic pressures let's say to
complexity minimization is the heart of free energy
drive down accuracy in in some sense there could also be and i'm not sure if this strays outside the free energy
principle or not but implementation factors so the lesson is back to maxwell's demons
and and all the very sophisticated kind of information engine analysis that people have done
from then until now has shown that the actual recording and computation of information
is an entropic process it generates entropy and so even though the free energy principle does have a term in there
which is the entropy of my model per se i'm not sure if that captures
the entropy associated and i mean the thermodynamic entropy if you will associated with actually maintaining and
operating that model so it may be the case for example that you reach a point where
increasing my intelligence a little bit more cost me much more to operate and maintain than it actually
buys me an improved accuracy for example where do you see that trade-off does or
doesn't fit into the free energy principle i think the trade-off fits very neatly
in fact you could say that was you know in large part constituent of the free energy
principle in the following sense and again you preempted everything that i might have said about this but i'll say
it again so the complexity that we were talking about so if you recall
log evidence and any associated bands like free energy or an elbow edmond slower bound in machine
learning can be written as a as the accuracy minus the complexity and the complexity
is just the divergence between your posterior and your prime belief distributions now that is a complexity cost it's also
exactly the the cost that underwrites uh salon off and universal computation computational
formulations of generalized or universal intelligence it is the thing that drives compression
in predictive coding or engineering applications of it it is the thing that jurgen smith uber would emphasize if he were
part of our conversation that sort of complexity minimization so
that is a really and possibly the more important part of the free energy the accuracy is well
understood but doing it in a minimally complex and a minimally maximally compressed way that that's the heart of it that's
important because by landauer's principle and the janinsky equality that also
directly one to one dictates the number of jewels that you'll expend in belief updating when you move from
your prior to the posterior so recall the complexity is just the relative entropy between the prior
and the posterior it is the degree to which you change your mind in the face of this new data or this new
sensory evidence and therefore is exactly the changing of the erasure of bits of
information that can be measured in gnats in natural units of using natural logarithms
that via landauer's principle has an exact thermodynamic cost in joules so when
we're talking about informationally efficient complexity minimizing schemes compression schemes from my perspective
anything that minimizes variational free energy or belief updating the minimizes
variational free energy you are also exactly talking about the most efficient way of doing it
thermodynamically so what that means is if you want to build the best kind of computer one simple way
of scoring how good your computer is is to take two machines that have the same accuracy
and the one that uses less electricity is the best one and that will also by definition provide
the least complex um account and thereby minimize its uh minimize its free energy
so i think it's a really important practical observation that what we're aspiring to here are really cheap and cheerful machines
that can that can do do their sort of their synthesis just to make it a bit more concrete what
An Alpha to tip the scales? Absoute not! Absolutely yes!
i'm wondering is in the free energy principle term with the complexity because i completely agree and get the point
that's the crux that's the most important term i'm wondering if maybe there should be a multiplier there like an alpha
something like a boltzmann constant that allows me to tweak the relative balance between accuracy
and complexity yeah oh a temperature parameter yeah that's a great question
there are two answers to that question first of all absolutely not the whole the whole point of
dissolving that exploration exploitation dilemma the whole point of putting the information gain in the
same space and in the same currency and on the same footing as your log prior preferences your
rewards your utility your bellman-esque like imperatives is that there is a
seamless exchange in terms of gnats natural units between the
decomposition of your expected free energy in terms of this intrinsic value and
this extrinsic utilitarian pragmatic value one of the benefits of removing the
alpha or beta or temperature coefficient on the the complexity versus the the
accuracy that for the expected free energy now becomes risk and ambiguity is that now you can talk about
reward in terms of gnats you can talk about how rewarding information is because they're just some arbitrary carving up
of a single expression they expected for energy that seems to me important
because that is if you like the sort of in terms of a dimensional or unitary unit analysis
that is a thing that truly does dissolve the expiration exploitation dilemma and puts the value of
information alongside the value of a money or the value of a fruit
drop if you're doing animal experiments so absolutely not you really want to totally avoid any temptation to start
adding ad hoc hyper parameters like temperature to this beautiful construct which explains everything the other
answer is absolutely yes that in order to in order to
acknowledge that if you're just trying to explain
the necessary properties dynamics of systems that self-organize to some
non-equilibrium steady state you are saying nothing about the nature of that city state other than it is at
steady state so it could be very high entropy steady state it could be very low entropy steady state it could be very hot it
could be very cold you haven't really committed to any kind of steady state which means that
it's slightly disingenuous to say that the imperative for everything is to minimize
say a free energy functional it's not that's why very carefully said hamilton's principles stationary action
is just keeping it flat at steady state it could be very high it could be very low and that starts to beg the question what
kinds of steady states are non-equilibrium are we really interested in simulating
reproducing describing and if you get behi under the hood in terms of
the relative entropies and the mutual informations that shape these steady states and in
particular the the distributions over this markovian partition into inside and outside the
blanket states it turns out that one important attribute or description of the state
depends upon the way in which the active states increase mutual information between the internal
and the external and if you parameterize up with a particular parameter and we'll call it
alpha as a not to your question then suddenly you really do need this alpha and this
alpha gets in exactly as you say as a knob on the expected complexity versus the
expected accuracy or ambiguity so what that means is in a more general formulation of the
of the free energy principle or certainly its application to understanding active inference
there would be this extra parameter that really tells you you're dealing with systems that are exquisitely structured in the sense that
they are they occupy a very small number of states they could occupy
in a particular way that is active that they actively construct their mutual information between the
inside and the outside at the moment that's not in the literature so there are ongoing debates
amongst the younger people who love the maths of this about whether we just need a generic kale divergence
or whether we need to exclude bits to get to expected free energy in by acknowledging there are different
kinds of non-equilibrium steady states and in so doing you have to really think
about the relative importance for this steady state of technically the risk and the
ambiguity and the sensory entropy so that's again that's a bit of an open question which i'm hoping will be
resolving about a year's time at which point your alpha will occur and i'll try to call it alpha in your honor
awesome maybe i should have gone with omega that way it's the last parameter we ever need
but thank you appreciate it absolutely fascinating there's been a lot of emphasis on a single
FEP applied to brain anatomy
all-encompassing learning principle this grand unified theory of the brain or indeed any system now um i've been
speaking to one of our friends on the show he's given us two questions this guy is dr hari valpola he's an applied
theoretical neuroscientist and he's the ceo of curious ai which is a reinforcement learning based startup and
he's a very accomplished scientist actually and and he says it does make sense to claim that there's
a unified cortical algorithm and anatomically the cortex is very uniform and although there are
adaptations to specific tasks they seem to be variations of a single unified template and in biology
function follows form however he says that to claim that everything follows
from free energy minimization is just overly simplistic in his view he says it's obvious that for the core text
goal-orientated learning and perception is crucially important he says the cortex isn't just learning
and perceiving all the structure and information it receives from the senses learning is heavily modulated by task
demand and attention and so is perception itself so he gives this example he says
if you take a young child around nine months old the critical period for learning the phonemes of your mother tongue and you
play some speech from the radio the result is nothing but if you play the same speech during a social
interaction the child will learn to discriminate the phonemes in the speech i think it's an excellent observation
and it takes us into a sort of world which we haven't really been discussing so far which is
the different flavors of free energy minimization and how it might be manifest
and so just coming back to the point that structure matters structures of the brain being very
finely attuned to and adapted to the context in which they're
that they're making their inferences one would normally cast that in terms of structure learning if i was
a statistician there are at least three if not four levels of maximizing model evidence i.e
minimizing variational free energy also known as marginal likelihood i can
make inferences to reduce my uncertainty about states that change
with time i can do learning which is reducing uncertainty
or increasing the marginal likelihood of the parameters of my generative model
i could also think about the hyper parameters that encode that usually cast in terms of precision
or neg entropy of various distributions and that interestingly and speaks to ignoring things that we're
talking about previously with conor sometimes it's best to ignore in a base optimal sense if you've got very inconsistent and
compatible information that's you know one base optimal explanation for ignoring and that speaks
to sort of intermediate temporal scale of free energy minimization but the one i want to get to beyond that
is structure learning also known as bayesian model selection so if i was a statistician i wanted to
score the quality of my generative model my hypothesis my
convolution model whatever it was then i would score it with a free energy
approximation or bound on the marginal likelihood of the model evidence now take another model another
hypothesis and i would compare the adequacy of these two hypotheses
using procedural bayesian model comparison and that is formally identical to choosing
the hypothesis with the least free energy so the free energy scoring the evidence for this hypothesis
of that hypothesis so you have now a mathematical description of what in cognitive signs would be
known as structure learning optimizing the very structure of your model does it have three layers
as my deep network fit for purpose should i add another layer how many units do i
have in each layer do i have a more sparse connectivity do i use linear rectifying all of these
structural aspects can in principle be evaluated in terms
of the the free energy or the marginal of the underlying marginal likelihood or the evidence
so you have this world of structure learning now that world itself can proceed at different time skills it
can proceed in terms of the development of a particular architecture
or phenotype if you're a developmental psychologist you would understand this structure learning from a neurodevelopmental point
of view as the brain grows experience dependent learning that is driven or can be at least
described by free energy minimization or self-evidencing or maximizing model
evidence increa increasing through the addition of different connections different cortical layers and cortical
areas or bringing them online through changes in connectivity that can actually progress
right through until the early 20s in your development you would see that or you could describe
that in terms of structure learning over somatic time but the exactly the
same principles apply at an evolutionary time scale so this notion of free energy minimization as bayesian model selection
speaks to a simple understanding of evolution or as nature's way of doing natural
bayesian model selection i.e natural selection where you operationally associate the
adaptive fitness with the probability this phenotype exists which is just the evidence that
it is there the probability of finding that phenotype in place and i should also
say that all of these different expressions of free energy minimization at different spatial and temporal
scales are all exactly consistent with some of the fundamental cybernetics and
inception of theories of self-organization such as for example the regulator theorem you know that it is on
some reading provably true that for any system or agent to regulate
its environment it has to embody or be a good model of that environment what does that mean its structure must somehow
recapitulate the structure of the environment generating that it has to control or it has to
engage with so what does that tell you it tells you that the structure including all those canonical micro
circuits including those visual hierarchies of our brains for example or the multiple hierarchical
layers in a deep neural network have to be there if it is the case
that the world that they're trying to model has a deep structure if things are
hierarchically generated and we know that the case for us because most of our world is caused by
other creatures like us as we're currently witnessing so we know that there is that there is a
hierarchical and dynamical aspect to it where the hierarchy say interpersonal
interactions transcends just individuals but also groups of people con specifics families societies
political affiliations theological affiliations or geographical hierarchical structure
so it is hardly unsurprising that the delicate deep hierarchically
structured connectivity we find in a brain and in a variation auto encoder
is a natural thing that has emerged from the evolution of these architectures
that all are conforming with the principle of free energy minimization it really resonates with a lot of the
Are there multiple non-FEP forms in the brain?
things that we've been speaking about on on our podcast here because in machine learning we of course there are inductive priors built into
models even the neural network has this kind of hierarchical organization which is an inductive prior but we've
spoken a lot about meta learning as well when this thing that you're saying that there's a structurally relevant inductive pathway which could be learned
but the last question from hari is he wants to know about the cerebellum for example he said there's plenty of
evidence that it learns by supervised learning and can perfectly well handle regulation tasks without any
models and he cites innate reflexes which train a complex feed-forward controller without any internal models i mean
as a bit of a side thing here that valpolo is is in a way implying that the free energy principle is is kind of
unsupervised that's the way he's talking about which there might be some truth to that but we'll come back to that but he also cites the basal ganglia the
hippocampus the amygdala and the superior caliculus each of them learns and their
learning algorithms definitely don't seem to have much to do with the free energy minimization in his opinion and he says that the basal ganglia is a
kind of reinforcement learning and the hippocampus is a one-shot learning and the amygdala and the superior
caliculus are supervised learning for specific tasks and this is super interesting right because he cites kahneman system 1 and
system 2 of thinking there's this famous test where if you give monkeys a sequence of cards with a hidden pattern on
which need to be classified into two classes humans suddenly click they see the hidden rule
because their system two kicks in and they start getting a hundred percent accuracy very quickly but you don't see that
with monkeys so valpolo was saying that he doesn't see how that phenomenon could
be explained by the free energy principle right again a whole raft of really
interesting points there all of those things can be explained by the free energy principle and indeed
there's a small literature on all of those things if people are interested you can get
into the literature i have to say because the literature may not be the familiar literature for people in
machine learning it's really he's asking some fundamental questions about functional anatomy
and probably more specifically the computational anatomy that we can ascribe to various structures and
hierarchies and connectomes in the brain so for example recent thinking about the cerebellum is
that it plays the role of actually a supervisor so it may well
be the case that the cerebellum plays a role in the amortization of carefully acquired skilled
movements that become increasingly skilled as the cerebellum watches the cortex and
in particular the pre-motor cortex supplementary motor area and the motor cortex per se
hierarchically exchange messages all prescribing those predictions for that reflexive kind of predictive coding
we're talking about before that are delivered to the spinal cord and the motor reflex arcs but of course that
sort of low level description of motor control does rest upon this one deeply structured and informed
hierarchy of predicting what am i going to do next because the cerebellum can watch that
it can watch the cortex learning how to compose particular movements and if it can
therefore learn how to do that then it can amortize it so i miss i'm assuming that we all know what amortization is
um but what i what i mean here is that we can offset or defer the cost of the bayesian
belief updating that we've talked about before is entails a computational complexity and
therefore also a thermodynamic cost by actually hardwiring and learning the mappings
from certain beliefs to certain sort of predictions say that drive murder reflexes in that sense the
cerebellum can i think be very usefully understood in terms of being involved in supervised
learning but i'd actually turn it on its head and basically say it's been supervised
by the cortex but in a way that allows the cerebellum to tell the cortex well normally you do
it like that why don't you just do it quickly and efficiently and bake in those mappings
without having to worry about the the actual belief updating and converging to dynamically on a gradient flow to
converging to a free energy minimum and that story i think can also be used
to explain the particular role of say the dorsal and ventral striatum
and the basal ganglia in arbitrating between whether we do a sort of system one versus a system
do we think about stuff do we do our belief updating and a bit of planning as inference or do we just do
what we've always done habitually respond quickly and efficiently by harnessing something that has already
been amortized and that i think is a really interesting interpretation of habitation
versus deliberative thinking which from the point of view of a neuroscientist would be the equivalent of system one versus versus
system two in that sort of edge between machine learning and reinforcement learning sometimes
referred to as model free versus model based and i would not subscribe to that in the
sense that the the habit has to be learned from the the good old-fashioned belief updating and
learning you can't you're not given habits you're given reflexes but to learn a habit
to learn this is the kind of thing that i usually do in this situation and if i just do it i can dispense with
the computational cost thereby minimizing the path integral free energy by doing the habit
i noticed that slipped in there that because it's a principle of least action that entails a
path integral so the amount of time it takes to minimize your free energy or get to your conclusion matters which
means you have to do it quickly to minimize the action you've got to do it quickly which means there's a natural pressure
to habitize and amortize in the service of minimizing free energy and i could go
on in terms of telling you what i know about the functional anatomy of the amygdala but perhaps it's best just to say that
there's a glorious game to be played here in fact it's the bread and butter of a jobbing neuroscientist
sonya systems neuroscientist to understand the computational architectures and the nature of
message passing implied by either belief updating or predictive
coding or variational message passing how it is enacted physiologically on a
neuroanatomy that has a deep structure so this is our job and it really started scratching the
surface in the past decades with brain imaging and other tools at our disposal
this is a very machine learning bias i'm not sure if you're familiar with this recently there has been a paper that
a positive conneciton to backpropagation
says that predictive coding can approximate back propagation in arbitrary graphs do you have any take on this yes it is
i'm sure a friend of mine has contributed to that yeah yes no absolutely
by coincidence i think we're having a an eurips workshop on saturday that sort of
affords different perspectives on backprop i have to say from my perspective that's
completely unsurprising and if there's any sense that prop has been demeaned as something
which is not that's really central to everything then i think that's probably wrong
so from my it is invariably the case that the
gradients with respect to anything of variation free energy can be written down as an a prediction
error which means that if you believe that the universe of interesting things that basically
is performing a gradient flow on a variational free energy functional
then you also believe that they are via the chain rule minimizing their prediction error
so it's for me backprop is just if you like a a nice linearized chain rule-esque way
statement of things that work flow on free energy gradients that can
always be written down with the back propagation of prediction errors it doesn't surprise me the slight
is that predictive coding belongs to this class of algorithm as does propagation of errors
and i would actually submit everything that works should be should be described in along
those lines i think that's one of the first times i've heard neuroscientists actually say something positive about backprop
so that's really fascinating so i have a second question and that is in your own personal opinion what has been the most interesting progress in
systems neuroscience you've seen since you first proposed the free energy principle whether it's directly related to it or not
standing back from a non-personal point of view the whole pragmatic term towards
embodiment we've seen in the 10th century in cognitive science has really been a very big thing that has been
underwritten and also has been lent momentum by theoreticians like ourselves
within that the role of predictive processing that's become a meme now so you can't write a paper in cognitive
neuroscience now without a nod to predictive processing at some level of an inactive and embodied situated
contextualized sword so that's been a slow and really important shift which is
presenting all sorts of really interesting issues in terms of exciting developments
in the neurosciences an increasing quest for understanding the nature
of these epistemic affordances which drive us in particularly in terms of social neuroscience echo niche
construction communication with others and how we forage for information you know
that seems to be in the context of usually social interactions
also touching upon an understanding of feelings and emotion and how resolving uncertainty about
bodily states in my world that will be interceptive inference gets into this game as an integral part of these deep hierarchical
models that try to explain everything what role do literally gut feelings have in my
propositional beliefs about where i am or who i am and how i should be behaving so challenging questions that are now
starting to address key aspects of intelligence
from the point of view of neuroscience such as the emergence of selfhood and
what underpins it and self in relation to others so we're now talking about cultural economic construction and
multi-agent interactions so that's been very exciting so i guess maybe to end the show i'd
The FEP does not explain the origin of FEP systems
like to ask you on potentially a controversial question i don't know i've been trying to find your official answer on this and i haven't
been able to find it but if we take for granted that the free energy principle explains a great deal about how certain
systems of the kind we've been elucidating will function does it explain the origin of those
systems so does the free energy principle for example have anything to say about abiogenesis
on earth on the origin of life on earth that first spark that created systems which can then
follow a trajectory guided by the free energy principle or is that outside of its scope
i'm sorry to add on a deflationary though but i'm afraid it's outside of its scope i say that sort of in in a rigorous way
because remember all of the interesting math and all this sort of physics of sentience all this bayesian
mechanics all inherits from the assumption of a non-equilibrium steady state
that entails a markov blanket as such where it's only about steady states it's
not where that steady state came from so there's lots of there are lots of really interesting questions
there's a great paper by kate jeffries and there's lots of work by people at los alamos around the world
trying to say is it almost unavoidable that we will end up with these deeply
structured delicate mock-off-blanketed systems that become increasingly rich and have
longer longer information lengths and more itinerant dynamics as the universe unfolds it would be
great to know the answer to that and to have a tractable mathematical formulation of that i'm afraid that the free energy
principle in its vanilla form as it currently stands does not give you that no all it says is
if that thing has evolved this is the property these are the properties that it must possess
but at least it can tell us we should continue exploring and looking around to address that uncertainty yes clever yes of course
some better better free energy principle professor fristen thank you very much for joining us this evening it's been an
absolute honor to have you on the show wonderful talking to you thank you very much indeed
thank you so much thank you truly a pleasure thank you very much they're very informed questions i got a sense you
Post-show banter
knew the answers before you asked them but that's how i felt
i'm going to be honest with you after talking to him myself i think he has a very intuitive
understanding of very deep topics and a massive depth of knowledge and
therefore when he tries to communicate that i think he just what's the right way to
say this he leaves behind a trail that's a little bit hard for us to follow because he's just moving at a very
kind of deep and fast rate in my opinion he was trying to help us understand just operate on such a high
level that it's not always easy to follow tell them that that's just the result of externalized intelligence
oh bad you might get your alpha constant i would have called it something like
kappa after my first name alpha's good i mean start with the first one like why why do we need to go
that's good it's the maximally ambiguous answer that still fits the data
