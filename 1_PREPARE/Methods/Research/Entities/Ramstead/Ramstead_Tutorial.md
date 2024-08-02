https://www.youtube.com/watch?v=WzFQzFZiwzk
Maxwell Ramstead — A tutorial on active inference



so just I just want to express my gratitude to everyone who's come today
thank you for coming so my name is Maxwell ramstad I am a postdoctoral
fellow here at the Jewish general I work with Lawrence and I work mainly on this
approach called active inference that I'll be presenting today so my talk appropriately is called a tutorial on
active inference from the predictive brain to socio-cultural regimes of expectation and the talk basically is
going to come in for part four parts yeah so the the first is basically a motivation of the problems that that
we're trying to address using active inference so I'll present on the one
hand the problems per se that active inference addresses like the the space
of problems in which active inference lives and then I'll move on to a few
more specific motivations about why an approach like this might be interesting then I'll turn to its what's known in
the literature as predictive processing which is basically this active inference
scheme applied to the brain then I'll I'll move to active inference per se
these two sections will kind of come together I mean the the predictive processing part is just the application
of this framework to the brain so they're not all that distinct although you know if you get into the more
technical debates there there are some distinctions that we can return to that and finally if time allows all I'll
discuss some of the multi scale extensions of active inference so going
beyond models of brains and cells to like this kind of integrated view of systems of systems of systems that are
nested the ones within the others and the kind of together thanks to this act of inference
framework so first I guess a discussion of the motivation and problems so
basically the problem I think that active inference helps us solve most
clearly is a problem of multi scale systems so this is a picture of McGill
University in slightly warmer times so McGill University is a is a complex
system it's a system that's composed of several different parts right some of which are living some of which are not
right so the the faculty the student body the support staff right but also
all those are living and and some some things that arguably are not right like
the the building's right the rest of the physical infrastructure labs and so
forth well if you zero in on one one component of this the living ones right so say the student body in McGill is
itself composed of bodies right and bodies as we know are composed of cells and cells make up organ networks right
that eventually make up organisms organisms themselves interact in social groups and eventually make up social
networks one of which may be the most evil I've posted the image of right here
so systems within systems within systems right we are systems within systems within systems that's kind of the
takeaway of this slide so if you look at the structure of the brain the brain
structure in a sense recapitulates the structure of the environment in which it's encapsulated so if you look at the
brain structure the structure of the brain this is from a paper by a park and frisson what you'll notice is basically
a repeated encapsulation of networks within networks within networks right so
you know dendritic formation at one level you know and if you zoom out a bit
you have networks of neurons and then if you zoom out even more you have brain regions interacting with brain regions
and so forth and what we what we notice is that there's a there's a a segregation in
a kind of spatial temporal segregation of the interactions between brain
regions that in a sense corresponds to and captures the regularities of the
kind of statistical segregation that we see out in the out in the world around us right things change in relevant ways
at different scales at different spatial and temporal scales so this is something that we'll return to and so you know up
until very recently this was lacking in a literature but suppose we wanted to study all these levels you know together
in an integrated fashion you know recognizing the interest and dignity of all these levels right so suppose we
wanted to construct a framework that was able to address you know I've plotted here this is from a paper that I wrote
with Carl for soon and Paul Badcock a while back I've plotted spacial dimensions on the y-axis and temporal
dimensions on the x axis so we would like is a theory that can in an
integrated fashion offer an explanation for the way that systems behave from the
subcellular level through to the cellular level the the level of tissues organs and organ networks to organisms
all the way eventually to speciation the construction of specifically design Mischa's and from from it this is from
the spatial point of view but from the temporal point of view we would also like an account that's able to account
for the the variety of temporal scales that are involved in the phenomena of
interest right so from mechanistic processes occurring over milliseconds all the way to you know phylogeny and
adaptive radiation which span you know hundreds of thousands if not millions of years so so that's one that's the
motivation of the problem how would we how would we address all these different spatial and temporal scales in a
principled way what kind of framework would be able to enable that okay so
that's the problem one motivation for thinking about active inferences particular in particular is a it's an
observation it's that most self-organizing systems in nature tend to dissipate
right so from galaxies and stars to lightning bolts and tornadoes almost all
really like all and I mean that in a very strong sense almost all systems that self organize in nature self
organized to equilibrium so does this mean if we had to unpack it in a kind of
basic way well first first we should note that these self-organizing systems can consume the gradients around which
they organize right so if for instance you think of a lightning bolt lightning
bolt self-organizes around a charge gradient right and in striking the lightning bolt consumes the gradient
around which it's self-organized effectively leaving the entire system at equilibrium so the same could be said
for tornadoes although although now it's not a charge gradient it's a temperature gradient and a weather system but the
the main takeaway is that for almost all systems in nature self-organization serves to increase entropy so in this
context entropy is a measure of spread you can think about it roughly as a quantification of how many different
configurations the system could be in right so if you think of a gas versus
say a crystal or water or a solid in a gas the Constituent particles could be
in any number of different configurations right like this this one that I'm pointing to at the end of my finger this little molecule of gas might
be at the other end of the room in like you know 20 minutes there there's there's less constraint as to where the
the the little particle will end up or is if you think of a crystal well the
the kind of regular leti structure and a crystal means that there are only ever local interactions and that you can
predict with a high degree of reliability what any different when any any given particle what state it will be
in right so high entropy means a high number of available configurations low
low entropy means a low number of available configurations so so back to
this most systems in nature right self-organized to equilibrium they they
dissipate they increase and but other systems a self-organized and
do not write bunny rabbits and tigers and you know I don't want to make
assumptions about you but I assume you as well don't self organize to equilibrium right you we self organize
to the this regime of states that's in effect very far from equilibrium right i
I don't exist at room temperature my core body temperature is about thirty-six and a half degrees Celsius I
imagine yours is roughly the same you know so we we we manage to stay far away
from equilibrium and the question is well how how do we manage to do this so
here is gonna be my first kind of technical excursus I'm gonna present to you a the state space formalism from
dynamical systems and this will help us think a bit more formally about what I just said so a state space description
is something borrowed from dynamical Systems Theory and the idea is to
construct an abstract space that represents all possible states of a system right so it's it's literally that
we're just constructing a state space right so like a a mathematical object
with dimensions that you can kind of move around in right and this space is going to represent all the possible
states that our system can be in and so how do we do this well basically for every way that the system can change
right aka for every variable in the system what we're gonna do is plot one
dimension in this space so we're gonna say okay this this variable corresponds to a dimension in this space that we're
constructing so suppose you have a very simple physical system with a
temperature and a size right then you might represent it this way right one of the dimensions corresponds to
temperature the other dimension corresponds to size and so what you'll notice already from this set up is that
a point in this space here is already a complete description of the system that
we're interested in right just so to recap the argument every dimension in this space corresponds to a variable in
the system therefore every point in the system corresponds to assigning a value
to every variable so essentially a position along the dimension right and so that might
seem like a banal observation but it allows us to to say interesting things about which you might call the intrinsic
geometry of a system in terms of its phase space so for example you might want to say well in in the whole space
of possible states that the system could be in there's this particular region that has these particular properties
that when you're in this area something interesting happens right so as an example here again I'm just using the
same thing right plotting the temperature on the x axis and size on the y axis well you might say well most
living things that exist exist in this sub region of that space right most living things exist somewhere between 0
and 100 roughly degrees Celsius and most living things are somewhere between uh
how did I put like 10 centimeters and 100 meters if you're looking at like
these very large colonies of cloning trees and stuff like so this is the kind
of thing that you can say using the state space formalism and one of the
interesting things is that you can do with this is described trajectories over the phase space right so this is sort of
like you know literally drawing a trajectory over this phase space and saying okay well the system starts here
and then some perturbation moves the system towards another state and then the system has to cycle back so for
example I wake up in the morning I'm a bit hungry right this is somehow related
in an interesting way to my you know making coffee and breakfast and then I
eat and then I'm satiated and then I moved to another area of the phase space that is me satiated right but you know I
I consume sugar you know as I as I for example give this talk so sure enough
I'll be hungry later today so then I'm back where I was and then this you know so the phase space
description allows us to say something about the dynamics of a system it allows
us to say something about the way that a system States evolved over time so basically the reason I'm talking
about this is that active inference is a theory of provides and mechanics of or
tells us how living systems are able to do this right so we we all exist as
living things in a bounded set of states right we we don't self organize to
dissipation like these things right we self organize to a very well-defined set
of states the question is how do we how do we do this an active inference provides a an answer to that question
active inference tells us about how things can stay away from basically you
know states that they they want to avoid and stay in a regime of states that are compatible with their existence okay
second motivation which you might call the animals perspective or the Bayesian room so if you really really really want
to caricature the position that organisms are in basically organisms are
in what you might call the Bayesian room chris elias smith has called this the animals perspective so the the idea of
the bayesian room is that organisms only ever have access to their sensory input right and this sensory input isn't
always very reliable the for those of you who do neurophysiology you'll know that you know the sensory motor channels
that we deal with are just intrinsically noisy they have to deal with movement and variance and there are varying
trustworthiness as well that's kind of context dependent so you know I spent a
lot of time in London last year and there's a lot of fog so you learned for example not to trust your eyes as much and to listen more than you would for
example in Canada when there's very little fog so this kind of this kind of
problem that the organism has to solve is a reverse inference problem in the
sense that it has access only to its sensory input and it needs to determine
what caused its sensory input so you know you might hear I've got a a Spock
ear connected to a brain right a very simple sensory system as as occur in nature frequently right
so suppose my Spock ear system here's a snap a crack of some kind right well the
what caused the snap is you know relevant right sometimes for the
survival of my the Spock ear organism in this case it may be it was just the wind
moving you know the branches of trees and a twig snapped maybe it was a tiger right and the difference is relevant
because the brain we mustn't forget its main function is to coordinate movement
in a I forget what the the animal is there there's a there's a very simple
animal that lives in water and it has a nervous system for the first phase of its life it moves around and in a
metaphor for tenure what it does when it reaches maturity is it attaches to a rock and it digests its nervous system
it's the first thing it does when it doesn't have to have to generate
movement right when you don't have to coordinate movement anymore you don't really need a nervous system so yeah so
out of multiple possibilities for action the brain has to determine well so what exactly caused the sensation was that a
tiger or was it just the twig and has to coordinate action you know the in an
adaptive way as a function of its inferences so this is another motivation
right active inference is useful because it tells us how this happens okay that
was the motivation introduction bit we can now move to predictive processing
unless there are questions about that opening part are we good all right
okay so predictive processing is a theory of how the brain works and it's
essentially a an instantiation of active inference applied to the dynamics of the
brain and it's it's a good starting point to understand active inference in
part because historically this is how the sequence kind of originated right these approaches were developed in
theoretical and computational neuroscience ha's and only recently through the work I mean
you know our group at McGill and and the work of others has been extended to to
model social and cultural phenomena so we'll start with the brain so you know
neuroscience 101 the traditional view of cognitive processing that you'll learn in any neuroscience class is that the
brain is essentially an aggregate of bottom-up feature detectors so we'll unpack this sequentially the brain is
first of all the feature detector meaning that the the more sensory areas
of the brain that are supposed to be like lower down on the processing hierarchy what they do is essentially
detect features right so in the primary visual area for example you're sensitive to bars and then as you ascend the
cortical hierarchy you and this is the other key word aggregate right these statistical features together until you
arrive at something like a complex percept so two things to note about the
traditional view on the traditional view the bottom-up signal is the one that's driving the show right essentially what
the brain is kind of cast as in this on this view is a kind of passive collector
of sensations right that yet combined
aggregated together and yield you know the arced world of experience right
another thing to note is that on this view the the descending connections
right that descend from so-called higher areas like the prefrontal cortex back
down to the sensory areas these are seen as modulation or feedback right so the
so on this view the brain is a passive organ it receives sensations it
aggregates them and the top-down stuff is just feedback so there are a few
weird things about this for people who study the brain in more detail one thing
to note for example is that roughly 80% of the brain's connections are doing this feedback thing right are descending
so in a sense it would sort of be surprising that 80% of the brain's energy budget goes to something that's
just feedback so I mean another at for someone trained
in philosophy like myself another very important problem is like where is meaning supposed to emerge from this
right so somehow I'm supposed to be aggregating geometric features of
stimuli and then meaning is supposed to pop out of that somehow it's not clear how that's supposed to happen as is
often the case in neuroscience we we give a nice little name to our ignorance
essentially we it's called the binding problem in cognitive neuroscience so how is this information bound together to
produce a meaningful stimulus I mean it you know what we think is that this is
maybe just the wrong way to look at the problem that maybe no answer is forthcoming
so the predictive processing viewer the active inference view flips this on its
head and says ok well maybe maybe this top-down thing is what the brain is mainly engaged in maybe that's the main
activity that the brain is busying itself with so from this point of view
the the main activity of the brain is essentially to produce these kind of top-down predictions about what it
should expect to sense next right and what flows up right so it's
traditionally thought of as the signal right is is what we call a prediction
error so it's essentially the difference between what was predicted at a given
moment and what is actually sensed I'll return to this in a second like in a lot of detail but a few things to note first
I guess the most important is that really conceptually it flips the traditional view of like how the brain
works on its head because what we're basically saying is well the the top-down activity is the main driver and
essentially sensory information is feedback right the the feedback is not
what we thought it was in a sense so it's it's sort of like moving from a conception of the brain is a passive
collector of data and a combiner of you know geometric or statistical
information moving from that to a view of the brain as a kind of query machine
right it's sort of a perception is like a Google search right you you you ask a question and you get an answer this is
so you know a visual cicada is as asking the world a question essentially so perception is an answer to that question
so it's a completed version of the received view in that sense so now we're
gonna get a bit more technical so how does this work it works via this broad framework that
we we can call generative modeling you're gonna see this a lot in the following slides the scheme is always
basically the same you have two things to its so when I say the active inference is simple i I mean it you can
essentially explain it with two circles on the line as I'll try to do now so the two circles here represent on the one
hand data right the data that's available to to us so observations
things that are capable of registering observations or measurements on the one hand and on the other the hidden or
latent factors that actually cause the data that we're observing right so in
this graph causality flows from left to right right you have states in the world
that cause the blue arrow the data that we're observing on on the right here and
so what we want to do if we go back to this problem that I presented of you know the the brain having to you know
solve this inference problem right is it a tiger is it a twig so basically the
brain the brain according to active inference at least what the brain is busy doing is kind of reversing this
arrow right so the the arrow of causality goes from hidden States to data and what we want to do is move from
the data that we have to an inference of what the most likely causal factors are
that caused the data right so this is I say data in a kind of broad sense
because it's important to keep in mind the historical context in which the methods were initially developed my
mentor at UCL Carl Kristen developed these generative modeling techniques for
fMRI initially so in fMRI which you have is a bold signal and which you want to
infer is the underlying neurobiological activity that caused the bold signal so
just by show of hands how many of you are familiar with neuroimaging and like more technically okay so a fair bit of
you just as a refresher for those of you who don't know when you do fMRI you're
not directly measuring brain activity right you these fancy heat maps of the
brain that you see are not direct measurements of brain activity what we measure is a is a proxy for brain
activity right so it's a it's a basically a measure of this this bold
signal stands for blood oxygenation level dependent signal it essentially consists in putting someone you know in
a brain scanner which is basically a big magnet and then you measure essentially a byproduct of oxygen consumption by
neurons in the brain right so what you what you're measuring is an effect of the neural activity that you really find
interesting and so what you would like to do then is from this signal right
from these from this data you want to infer the most probable neurobiological
activity that caused the data so this is the technique that was pioneered than
the 90s by Michael Forrest in in the 90s they were using statistical parametric
mapping which I won't get into very much but essentially for reasons that I'll we'll be able to see a bit later these
techniques allow us to move from this data to a model of of the essentially
the connectivity of the brain that the most likely connectivity that would have
generated the data that we're interested in explaining right active inference and it's more familiar format for those of
you who work on it comes in at a second level what happens when the data that we want
to explain is literally the sensory signals that the brain is receiving all
the time how does that change the general scheme well it changes it in the
what we're doing now is constructing a model not just of the underlying neurobiological activity that caused a
signal that we measured but rather constructing a model of what's what
causes the sensory signals of an organism so you know the the the the
major part of what causes our sensory experience is us acting in the world in
various ways right think I'll think only of the visual saccades that you're performing many times a second right you
we are we are as embodied agents are the main causal driver of our phenomenology
in a sense so active inference per se is about characterizing this right the it's
about characterizing a model of how our sensory data were generated so I'll
return to that in a lot of detail later I just want to quickly say that there's a new kind of tier of active inference
that that's being developed right now this is probably the least explored most cutting-edge application of this this
framework what does it look like when the data that we're trying to explain is outcomes of the diagnostic process right
so like the data that I'm trying to explain for example is a schizophrenia
diagnosis or a depression diagnosis right so then the model that we're writing is a model of the process that
generated the diagnostic classification per se and for me as a philosopher this
is really interesting because this is where it gets really meta right like this is where we are part of the model
in a sense we as clinicians and researchers really are represented in
the model that generates the data if the data is psychiatric diagnosis anyway the
so the point of generative modeling the way that it's it's been used for for a
few decades now is this kind of very simplified pipeline we're on the one hand you have an experimental
that generates data that you want to explain and on the other you have a computational setup that is effectively
a model of the process involved in your experimental setup so then you get this
kind of circular relation going where your experimental setup provides data
you can essentially model or create
models of the most probable causal process to have generated your data that
in turn can be used to refine your hypotheses and your methodology right
that you're using in your experimental setup and so there's this kind of circular motion between modeling work
and computational work that we capitalize on and essentially in the generative modeling paradigm okay so
what is a good model a good model is a model that generates a a small amount of
error so we'll see what that looks like in the brain the way that so remember I gave this kind of general framework to
understand what's going on like in the brain in terms of active inference if we wanted to unpack it a bit more at any
layer of cortical activity or really of any neural activity according to this
framework what's what's happening is that at layers above and at the same layer any unit is receiving predictions
about what it should sense right and basically what's going on is a constant
comparison between what the brain expects to perceive and what it actually
does perceive and the discrepancy between these two signals is what gets shuffled up the hierarchy in this kind
of fashion right so I mean interestingly this happens as early as the retina so I
mean I won't get into the into the neurobiology too much but the there
there's reason to think that this predictive architecture stuff happens everywhere at every level that really
there's no prediction free layer of cognitive active
yeah as early as the retina like I was saying so if we want to think about it metaphorically but we're sort of moving
towards a formalism here like what it means then to minimize this error
quantity is basically you have a cloud of data that you're trying to explain right and you're constructing a model of
how that data was was generated like what and therefore what you should
expect of that data so in what you're essentially doing is fitting a curve to
a cloud of data and the prediction error per se is is this distance here it's
this distance between the value that the model predicted and the value that you're actually perceiving so there's a
there's a story to tell about thermodynamics and information theory that I'm going to skip over but we can
return to later if you're interested so essentially according to active inference / the predictive processing
there are two ways to minimize this this quantity right this this discrepancy between what I expected and what I
perceived the first is to change your model I think it's the most obvious right if if there's a discrepancy
between what you predicted and what you perceived the simplest way to reduce the discrepancy is just to change what you
predicted so we just change the model we'll see what that means a bit later we
adopt a different model and this model generates less prediction error than the original one right which means that it's
better it means that it's more reliably you know explaining the variance in your
data of course it's always possible to overfit so I mean this is just a brief
mathematical excursus but for those of you who have done statistics you'll know that like if you have n data points you
can always arbitrarily construct a polynomial function of degree n plus 1
that'll go by all of the points that you're interested in but capture none of the trends that you're trying to explain
right so it I just ad hoc you know I probably can't tell right because it's so gracefully traced but I ad hoc
constructed a function here which I assure you very rigorous one and it passes by all
of the data points as you'll notice but what you'll also notice is that there is a trend in the data and that the this
function isn't capturing it anymore so you might think that if the brain does something like that in overfits data
then it on the long term it's going to generate a lot of prediction error and so you know some disorders you might
think of delusional ideation and this kind of thing is have been understood in terms of overfitting so overall you're
better with a slightly simpler model that generates some error right but that
on average sticks to the the trend and the data better so this also speaks to a
more general more I guess philosophical point here is that in this framework the
error is your signal right when we say like minimizing prediction error we
don't want zero prediction error because that would mean having zero signal so
one way to think about this is your model has to be simpler than the reality that you're modeling right so think of a
map right a model is basically a map a one-to-one scale map would be completely
useless right like if I had a you know the a map of this room would be like you
know I wouldn't be able to to look at it and it wouldn't it wouldn't contain you
know information in a way that could be used in a useful fashion right the model
has to be simpler than the data this means that just by construction there will always be prediction error right
just that's how it works you need prediction error because it's your signal okay so first way to
minimize prediction error is to change your model second way to minimize
prediction error is to change the world right so if there's this discrepancy right you know you might want to make
your model more like the world but you might also just want to make the world more like your prediction and so
inactive inference / predictive processing action itself is understood as a form of self-fulfilling prophecy in
the following sense you start off with a prediction of action and you're not moving right so I
don't know like I don't have a prop handy I usually do but suppose I had a
glass of water handy and I wanted to reach for it well the way that it's unpacked in the predictive processing framework is I
produce a prediction of movement but I'm not moving right so it's so facto if I'm
not moving and I expect to move that induces a prediction error right and so the cool thing about using a prediction
error as your signal is that it updates over time in real time right so I
basically initiate movements that in real time reduce this prediction error
so it can be used as a kind of knowledge driven real-time signal you know that
enables adaptive motor behavior so this is just what I said
you generate an action prediction you're not moving therefore a prediction error is induced and that can be used to guide
online motor behavior okay so now I'd
ask you to buckle in really tightly because we're gonna do some math so
we're gonna look at the generative models themselves I've talked a lot about the models etc so what are these
models so remember the general flavor of this is we have data and we're trying to
infer the the most probable latent States that cause the data that we're
trying to explain right so causality flows in this direction inference flows in that direction okay so how exactly do
you quantify you know how well a model explains your data so the way that you
typically will do this is by constructing several alternative models right the that are each each encode a
different hypothesis about how the data might have been caused and then you evaluate how well that model accounts
for the variance in your data so if you want to compress that algorithm into
like a quantity what you get is this spooky variational free-energy thing
which you know you might also just call the model evidence or abound on the model evidence basically this
variational free-energy thing is a measure of how much evidence is provided by the data for a given model of the
process right so it's important to stress this the free-energy isn't an energy in the sense of thermodynamics
right it's a it's a measure of how well your model explains the variance in your
data so that I think that's an important takeaway you know to like understand
what is going on here right it the let
me repeat the variational free energy is just basically a measure of how well your model explains the data the
variance in your data yes yeah okay well
so the the model evidence itself if you actually try to compute it usually just
for calculation reasons you won't be able to do it typically it's because these always involve a normalization
term you kind of have to divide by this term and this term calculating it
involves summing over an infinite set of states so basically you can't do it
analytically and so what you do instead is you construct this quantity of the
variational free energy which which is basically an upper bound on the model evidence what that means is that like
the model evidence the your variational free energy basically tells you you at
least have this much evidence right you might have a bit more but you at least
have that much evidence from your model for your model right so so just to
rehearse this again right so always the same formula you have some data you're trying to construct the most probable
model of the process that caused the data and you get added through inference
so and so this is what the models typically look like and Florence once
told me that just presenting these models is basically an act of intimidation
this one is very consoling and comforting thank you so so rather than
the engage in this act of violence all I'll try to unpack a bit what what these
models are right so the most basic generative model is this thing here and
this thing here is just this thing here right everyone sees right you have your
data you have your most probable causal states and a relation of inference
between them all right so here you have it's just flipped here you have your data right the most probable causal
state that caused your data that you're trying to infer and now what we're doing is just adding a bit of mathematical
niceties mainly we're parameterizing these relations right so this a thing is
just a likelihood mapping and basically what it does is specify for every state
if this state was actually the case right what kind of data would I expect
to see right so for example if it is night I would expect it to be dark outside this is the kind of thing that
this a characterizes so one important distinction to make sense of these graphs is that the circles are either
your data or the quantities that you're trying to infer right and the squares are essentially parameters of the
relations between these circles right so that they characterize the arrows between so like I was saying S is just
your state that you're trying to infer oh is your data a is your likelihood
mapping from your state's to your observations basically like I said assuming that this state is the case
what what is the probability of observing this or that and D is just your prior beliefs over States so like
independently of any observations that you might make what what do you think the state is right so just I'll run
through some of the math right so if you see on the left hand side here s equals
D is just saying well my guess about the state independent of any data is just my
prior about the state right pretty simple this o equals a s thing again
it's just describing this relation that the likelihood mapping has right your your outcome just is a combination of
this mapping between your states and observations and the your beliefs about states and here to the right what you
see in a mathematical form that I won't get into too much is that your the state
that you predict right your posterior estimate over States is equal to some combination that I won't get into too
much of your prior beliefs and what you learn from your observations from the
data and how that relates to states right so these look very intimidating at
first but like we can unpack them in the way that's okay so these were the models
up into that we were using up until 2015 roughly and in 2014 15 16 what happened
was that we started considering temporal depth and temporality so here we're
adding and it looks a bit more complicated but we're really just stacking the first layer model right
does everyone see that like see this thing here is just this right so
basically the only thing that we've added here is this B matrix and the B
matrix specifies your beliefs about the way that states transition over time again independently of the observations
that you're making this is very clear from the equations here to the left so
it just says your state at time T plus 1 is a combination of this B matrix right
that captures your beliefs about the way states transition and the state at time T all right not nothing exorbitant or a
complicated and again the posterior thing is just telling you okay your your posterior belief about a state is just
equal to some combination of your state and B in the past your state and B in
the future and what you're seeing in the present right so again it looks
intimidating but it's actually less complicated than it is I I know it has
been all 2020 this is this presentation
of the material is was developed by one of my close collaborators and friend
friends Kasper Hesse at the University of Amsterdam this is from a paper that
we've pre printed now called deeply-felt effect which I mean besides articulating
emotional inference using the active inference framework also presents a
tutorial of the more formal kind of package that underwrites active
inference so if you're interested I can send you the paper okay so so so far
we've talked about perception at from time from moment to moment right this this relation between o and s mediated
by a then if you consider it you know the the sequence of states what you're
doing is introducing beliefs about the way the world transitions States evolve over time independently of your
observations you'll notice that your prior here has effectively disappeared from these steps here because your prior
just feeds in your first kind of estimation and then it kind of goes on so you're really just using s2 as your
new prior for the next time sorry s1 is your prior for the the next time step and so on okay but so far this this
could have just been a tutorial on reinforcement learning active inference does something special which is this so
again don't panic this is just what we've just seen all I did here was add a
circle or which is this policy selection thing this pie thing here so inactive
inference the way that action selection is implemented is essentially by
choosing transition matrices by choosing your beliefs about the way that the
world changes over time so again we have these B matrices that we just discussed
here right these beliefs about the way the states in the world transition well what this
policy thing this policy selector does up here is effectively choose a series
of B matrices right so to act is to have
beliefs about the way you think the world should evolve in in this kind of self confirming way that we discussed
earlier and all the stuff that the top does is just like put the variational
free-energy thing into into the loop so this is definitely beyond the level of
mathematical discussion that I had in mind for today but essentially you have
this G thing G is just your expected free energy right so it's it's the amount of free energy that you expect
for every possible action that you could take and essentially what this thing is doing is selecting the action that leads
to the lowest free energy right so again it's just this action selection thing
that leads to you know prediction error minimization or that runs on prediction error minimization which you'll notice
is that PI again is a circle it's one of these quantities that we have to infer
so contrary to you know more traditional schemes in motor control where you just
program a command and it's affected inactive inference your little agent is effectively trying to infer well what am
i doing right no but really like oh well
on the basis of your prior beliefs right and on the data that you're receiving from your sense is what is it that I
must be doing right so I'm this again
contains a lot of weird math that I'm not going to go into but I just wanted to show you this because it's cool so here you have your generative process
here you have your generative process so this is just a basically a model of like
a model in the sense of we are modeling just the process that actually generates
the data that's sort of like invisible invisible to us right so this is sort of
like it's hidden to us but like there is a process that generates our data and this is a poor
knee style factor graph representation of the generative model that I just showed you it's it's all the same terms
right you've got your bees your DS and your eyes and all that I won't get into how you go from one from one to the
other because it's a little complicated I was just putting this slide up because I wanted you to notice two things well
it's the same thing but it's it has two elements where the process that generates our data and the model of our
data like where they meet is it two points you have these you things up here
which are the actual actions that you're performing right and this these the O's
your your observations so basically the model the generative model and the
generative process meet at action and observation like that's that's sort of the two connective points I mean this is
complicated and we can return to it then this is the last technical thing I wanted to show you like where we're at
now with the modeling is that we we introduce a new layer of States into the model that are about States at the lower
layer so in our new worker working on metacognition emotional content and kind
of self-control mindfulness meditation and this stuff so what we did here is
connect a layer of states at the top here with their own transition matrices and everything two states at the lower
level so what we've begun doing is treating States oops is treating states
at the lower level here as observations so like we're treating the results of
inference as new data right that the system can can then use to make
inferences about itself and basically how well it's doing so I told you this paper is called deeply-felt effect
because we use this kind of layered structure to account for basically
beliefs about oneself right and eventually self-control in this kind of
thing for the sake of people who may get a little lost when the discussion is too
abstract anymore if you could think of a couple concrete examples without technical
language going beyond something like oh here's how a monkey something more like
how did you help make sense of human emotions and moods for example how sure
checking in with oneself okay well so
this bottom part of the model you can make it do you can make it do whatever you're interested in making it do right
so you could have a model of I don't know a con for having a conversation right so in this kind of model of having
it might be simpler to explain that bit just with this so you know the data that you have to explain might be you know
configurations spatial configurations a you know of expression in someone's face you know the the auditory sensations
that you're registering right so for each of these modalities you have an a matrix that specifies the way that the
you believe these sensations are typically related to the states that cause them right and you have this
policy selection thing that affects beliefs about the way that states evolves right so in a conversation for
example right you would be resolving that continuously I would be inferring these lower-level states like what is
Sam telling me now right and I would be selecting a policy that you know that
facilitates this interaction that ideally gets us like to some kind of coupled point where were able to
interact so the the point of adding these additional layers is that now I can make inferences about my inferences
I can be like well am I sure that Sam feels good today you know like he I don't know like he he seems tired or
something or I don't know like yeah it's
it's things to do with for example confidence in your own judgments how well am i doing you know how how do I
feel about these inferences that I'm making this kind of thing so inferences
about our inferences and you the reason why this is important I think just generally for for humans is that'll
you know I'm telling this to you you know in particular most of human thinking is thinking through other minds
right it's thinking about right other minds the way you're describing it now
it seems like there may be two things conflated or maybe just one part of them
being I'm talking to you and I'm thinking I'm thinking something about
the nature of our conversation and that's a kind of self-consciousness if I'm thinking right I wonder if I'm
making a good impression right so what what it brings to mind is
is there a generic self-consciousness like you just have lots of those thoughts because this version is just
very specific I just have one question right have one hypothesis but in real life these things come in bundles it
ends with a whole and and that's what we would then call an effective stance let's see yeah absolutely I mean uneasy with you
so I'm engaging with the lots of alternative so so how would you model
that in other words it's not simply one thing one bit of metacognition or rate
of reflection on the nature of interaction it's a different I would describe it informally again it's like a different stance or a different one
important thing is that we can entertain more than one different model right so there's some interesting work by ezel
Mora I think who essentially implements like a simple and these are very simple
toy systems for now what we're doing now is scaling them up to human systems but it's basically a bird simulation and
it's it's it listens to eight different birds and it recognizes them essentially
because it entertains eight different models that might correspond to this or that so the capacity to simultaneously
entertain different models might help
different if I say okay I'm uncertain where I stand with Brett and so I have
to entertain many different models versus I'm just having one policy okay
so you're right well the thing to note about is that the thing to note about
this is that this top level of inference makes this bottom level accessible to the system right so basically inferences
at at this bottom level just happen right so they they guide action but in
an implicit sense whereas these states are literally about the states below so
attentional States for example exist at this level right States about my sensory
states that helps right which then has
destructive effect let's say on my attention of state versus having one that is coherently great sort of
reinforcing the particular anyway I guess know that you what you're seeing
is is that that's that's really like I think an important point I mean and in in work that we have in that I'm not
going to be presenting today which is basically like where we're at right now we've got a three layer system going to
explain mindfulness meditation this is a work by Lars Lars Sam Ted Smith in
particular that we're doing with Karl for student at UCL we're basically on top of this we have an addition yet an
additional layer make the attentional states opaque to the system this is already there kind of
implicitly right look we have a B matrix that that links these different things so we already have beliefs about the way
that these higher-order mental states are transitioning what would it look like if we implemented policy selection
there because you can it's a B matrix so why not just like hook these up to a higher level pie you could you could and that's what we
end up doing in the anyway so I guess I'll be putting this on YouTube policy
is a sequence of B matrices okay right because that's what it is to select an action under this framework
is to change your beliefs about the way that states are supposed to evolve right
yeah it's a well it's it in the Morse
well because in in the most simple case it's just a series of B matrices but
what if you're considering counterfactual depth right like yeah then you have like trees of B matrices
and so forth can create a network yeah there's feedback between different contexts
well let me try to just finish I have about like ten minutes left of material pointed you'll come back to because for
me the so it's appealing again that you get these harder to the levels and it seems like you're getting more however
the more layers you add it seems to me you don't say have more data do you so exactly a problem of like your
complexities back to the overfitting whatever having way more complexity modeling actually I mean that's a really
good question and we struggled really hard you know last time I was in London a lot of what we did was ask well do we
really need a third level it can't we just do policy selection at the second level but the key thing is this opacity
thing is that to make these states of inference accessible to the system to to
allow the system to use them as data for further information
I mean we've sort of seen it before but basically Bayes Bayes rule is just a way
to combine prior probabilities with your likelihoods to get posterior probability
so yeah Bayes is important so I put it on a little crap so your prior
probability is just the probability of some event before any evidence is taken into account your likelihood is the
likelihood of some event the probability of some event given some evidence that
should be probability of some of that given some evidence so just to illustrate the difference if Houdini magics away an elephant on stage well
you know there's a high likelihood that the elephant is gone you can even go on stage and collect more data the elephant
clearly is gone right but we know that there's a low prior probability that elephants just D materialized because elephants are solid
objects and right those don't typically D materialized so Bayes rule is just a
way to combine these quantities optimally so basically the cool thing
about this is that you can always use your posterior at one step so the result of combining your
prior and your likelihood as your new prior at the next step so there's this nice kind of bootstrapping thing that
you can do and the way that this relates to what we've been talking about is basically the descending connections
right they carry your priors and your prediction error is basically always
integrating the data that you're that you're generating so it's it's essentially a likelihood and the
Bayesian brain says okay well this is what the brain essentially looks like right you've got likelihoods flowing up
in the form of unexplained prediction error and prior probabilities flowing down right in the form of neural
prediction these these schemes are typically hierarchical I hinted at this
earlier the reason why they are is that as you mystically as you go up the
hierarchy the things that are represented are more stable over time and as you go towards the more sensory
and things change faster right so for those of you who are familiar with
Fourier analysis basically you can take any image and decompose it into
frequency bands right so high spatial frequency and low spatial frequency
information right which which you'll notice so high spatial frequencies to the right here low spatial frequencies
to the left here and what you'll notice is that in a conversation hi-spec high spatial frequency information changes
much faster than low spatial frequency information I mean unless you're someone like myself you know moves around the
face and like makes funny expressions like typically most people like you know
that their lips move faster than the rest of their face right so you might
think that this is implemented in the hierarchies that the brain encodes
the the hierarchies of information that the brain encodes and according to the
predictive processing framework this is precisely what we see so I'll skip over
that all right so yeah so you have hierarchies of information that encode
regularities that are time sensitive and you have prediction error minimization going across the this hierarchy and it
essentially explains the way that the brain reacts to stimuli
alright so that was predictive processing we can scale this up is what
I submit to you now so I have this winter is coming just to talk about my
favorite example of active inference it's like well when I get cold I don't know about you but I put on a parka
especially like in Canada it's cold right so that we can cast this as active inference as well I think so the the
point for the next two slides is basically going to be it's not just the brain that engages in active inference
it's every cell in your body every organ system in your body and effectively
maybe social groups as well and this is what we you know we work on ok the last
bit of math that I want to introduce to you I think is simpler than the rest it's called a Markov blanket and what I
want to submit to you is the rock cells organs animals social groups basically
anything that exists at all has a Markov blanket so a Markov blanket is just a
way to use statistics to answer what is traditionally a philosophical question right the philosophical question being
what does it mean to exist what does it mean to exist as a thing right what does it mean to be a thing so I mean if you
ask a philosopher they'll tell you like a story about metaphysics and you know like type token and identity theory and
whatever we've issued all of this for something much more simple which is to
say okay well if we're interested in a system right so suppose the system that we're interested in is the brain right
because we've talked about it and we want to differentiate it from the environment and which Siachen in which
it is embedded what we'll do essentially is introduce or define a third set of
states that mediates the causal relations between the system that were interested in defining and its
environment so these are known as sensory and active States so these are
metaphors of course the the way that they're defined is by their connectivity
right so sensory states cause internal States but are not caused by internal states
and active states caused that are not caused by external states so I mean the
point of doing this is to say okay to exist is to be endowed with some degree
of conditional independence relative to your environment right so if you
consider this massive gas right here it's not a system because it'll just dissipate right like there's no robust
sense in which it's independent of its environment in any sense like you know it's gone right so a Markov blanket is a
way of saying conditioned on the existence of this set of states the sensory in the active States the
internal states of the system are independent of the external states of the world is that clear to everyone okay
so active inference then is a story about how internal states that which encode our model right and the active
States which are like our skeletal muscles and so forth change to minimize
free energy and the end effect is to allow this inference process to happen
right so the the inference here meaning that the free energy or prediction error
diminishes right so making the internal states more like the external States and vice versa again this is just this story
right it's just that as we've seen inference also occurs through action so
basically like you have the state estimation bit going on here where we're
kind of inferring what should be going on in the world you have the policy selection bit here but this is just the
story that we told right but just now presented in terms of like the existence
of the system I'm gonna skip through that so so yeah this is a drawing by the
famous physicist Huygens and yellow Brandenburg has it in one of papers on
this like an important point is that like an advantage of using active inference over other frameworks is that
it just it comes from physics right so you solve this inference problem but using using a framework that basically
says well inference is sort of like a rock falling down a cliff you're just falling to an an energy minimum right so
the the reason it's called variational free energy is with an app is analogous
is with analogy to the thermodynamic quantity free energy right in thermodynamics free energy is the amount
of energy left in a system that can perform work right in the information theoretic context the variational free
energy is basically the amount of wiggle room you still have on your parameters to get a better representational grip of
the situation right it's like yeah how much room is left on your parameters to
do work to do representational work okay last thing basically that I'll be
talking about today so here's our Markov blanketed system again I submit to you
that all of the components of this system are also systems right this is the observation that we started with I'm
a system I'm an organism but I'm made of networks of organs that are themselves systems and the organs themselves are
systems of cells and so forth so every component of a Markov blanket is itself Markov blanketed so in this 2015 paper
by Carl Kristen which i think is the
first and literature to do this they effectively connected two levels of description so what they showed is that
on the assumption that what you see here first is I think seven eight cells eight
cells that share a generative model and over time reach a target configuration
so it's basically a little creature with a head and a tail everyone sees that and so what you have plotted here is
basically the beliefs of each cell about what kind of cell they are essentially
and so you have your free energy plotted here and so what you see is all of these
cells share the same generative model so basically they're able to infer their place relative to other cells so long as
they're able to commute with other cells because we all have the same expectations right we all expect to sense the same kinds of things so
basically the the little units start off and there's free energy spikes because
they're trying to figure out what's going on but then as they communicate the the free energy starts to go down
until it reaches a minimum value and when it's reached its minimum value here
the simulation reaches its target configuration right so that for me this
was like an eye-opening moment where I kind of you know with Carl realized that
you know this is how you effectively connect levels of organization right units at one level sharing a generative
model are able to enact a target morphology so from there we generalized this is from our one of our physics of
life reviews papers we're essentially just telling the story of how at any Markov blanketed system itself is
composed of Markov blanketed systems so you have this kind of recursively nested
systems of systems of systems of systems approach which you might think of as a a
vertical stack of systems I say vertical because there are two dimensions to this
system really there's a vertical stack where like cells compose organs which compose organ networks and so on and so
on but there's also a horizontal stack where at any scale of interest like the
the relevant actors like cells for example are also in the process of niche
construction they're they're constructing an environment for themselves and they're effectively sharing a physical environment yeah
so this kind of gets us here right where we started at least I hope I've made the
point that you know via active inference there's at least the possibility for something like an integrated science of
culture mind and brain that takes all of these levels seriously right and I'm
just going to skip through this right to the thank you slides yeah so that's what
I wanted to share today thank you for your attention thank you to my hungers special thanks
to the people listed particularly those of you who came and yes thanks for your
