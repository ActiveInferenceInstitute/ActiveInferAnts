"Physics as Information Processing" ~ Chris Fields ~ Lecture 2
https://www.youtube.com/watch?v=WkWIqpxWRM4



it's June 15 2023 we are here in lecture
two of Chris Fields course physics as information processing so thank you
Chris looking forward to the lecture oh thank you Daniel
um and yes welcome to this session uh this section is titled why quantum
physics and if you will recall from the first session
we reviewed the history of physics and and some of the history of mathematics and computer science
or I'll the end from the end of the 19th century through to the beginning of the 21st
Century and discuss the the slow development
from classical thermodynamics of quantum information Theory
and uh specifically characterizing Quantum information Theory
as a new kind of physics that
describes systems that are exchanging finite amounts of discreetly encoded
information across some intervening boundary and
so we use this very conventional graphical notation
of two agents or physical systems
Alice and Bob A and B that are exchanging energy and
information across some boundary and I always use a
blue ellipse like this to indicate the boundary that separates Alice from Bob
and this new approach to physics is entirely topological it's not
geometric so it doesn't assume a particular background space time
so it doesn't assume that Alice and Bob are spatially separated
and so this this makes it a very different kind of theory from classical
information Theory in that the channel uh that separates
Alice from Bob this boundary is a boundary in state space it's not a
boundary in some geometric embedding space and in particular it's not a
boundary or a channel that's embedded in a three-dimensional space that separates
Alice from Bob that's what we talked about last time
Quantum Theory
and today what I want to discuss is how quantum
theory in particular makes this idea of physics is a theory
of communication simple than obvious and
quantum theory of course has a terrible reputation uh of being abstruse and mathematically
incredibly complicated and counter-intuitive and difficult to
understand and this is one quotation among many
of from leading physicists pointing out that that quantum mechanics is just
difficult and uh as as you probably know there's
an entire philosophical industry of interpretations of quantum theory
that try to make sense of its ontology and so what I don't want to do today is try
to introduce quantum mechanics uh we're not doing uh any of this
Quantum Mechanics
some of you will recognize this as the table of contents the first part of the
table of contents of the famous textbook by Landau and lift sheds
oh but if you've studied quantum theory in undergraduate or graduate school
you've probably dealt with a textbook structured much like this one and you've
probably been introduced to quantum mechanics as it was traditionally conceived as essentially a mechanical
Theory a theory of motion uh with wave functions and and particle
representations and on and on and on so we're not going to try to do that
this uh what we're going to do instead is take a completely
information theoretic approach uh and we're going to characterize
um information transfer in a Quantum theoretic way without any assumptions
about mechanics or space-time or any of that so instead of this
Simple Questions
we're going to ask a simple question uh a simple by a simple question I mean
a question with just a yes no answer or a binary answer so let's use up or down
as our example question and to ask this question we need three
things first we need an action we need a way of asking it
uh for example making a sound or writing something down
um second we need to a thing that we can ask the question of
uh we need an environment or a friend or the rest of the world or an experimental
apparatus or some system or other that we're going
to act on to ask this question and the third thing that we need to to
ask this question is a shared language and it's the shared language that's
often neglected in in models based in physics
um and I think the importance of the shared language was became clear and classical information Theory and it's
it's become clear again of course in Quantum information Theory but this has only happened over the last few decades
so what I want to do today is to construct in a step-by-step fashion a
formal representation of these three things that we need to ask a simple question
and what we'll find is that that formal representation is in fact quantum theory
so it's quantum theory that provides us with a formal representation of asking
these simple binary questions and of course if you can ask a binary question you can ask any finite number of binary
questions so you can construct and arbitrarily complex finite decision tree
that ends up formulating an arbitrary an arbitrarily complex but
still finite question so this really is a general model of
communicative interactions between agents
Action
so let's go about this and and talk first about the action of asking a
question and so the first thing I want you to do is is actually say out loud
up or down actually ask a question
and then note two things about what just happened uh the first thing to note is that it
took some time to do that that that action actually we required to find that amount of time
um a couple of seconds not very long but it's not zero it it always takes
time to ask a question and the second thing to note is that it took energy
to to actually say up or down it requires a little bit of exertion
to ask a question so let's put those two together
and Define a word we're going to define the word action
to mean some energy that's spent in some time so asking a question is an action
and it qualifies as an action because it requires spending some energy in some
finite amount of time and so we can write this as action equals energy times time or I'll
sometimes use the abbreviation E times t um
and action is is always required when when
there's some interaction or two-way action
between systems so whenever we talk about physical interaction we're always
talking about two systems doing something to each other that requires both energy and time
so let's define another concept a concept of a minimum action needed to
ask a question and specifically a question with a binary answer
and we'll just pick a symbol to stand for that minimum action and the symbol
we'll use because it's conventional as h and it turns out that this h
is Planck's constant the number that Planck came up with
when he was trying to solve the black body problem back in 1900 that we talked
about last time and recall that was the problem of characterizing the spectrum of radiation
emitted by some physical system that was hot how much energy comes out as a function
of temperature and if you assume that the spectrum of
energy coming out is continuous you get predictions that are wrong and plank got predictions that were
correct by assuming that that Spectrum was discrete and that that this h
uh represented the minimum amount of energy that could be emitted in a
particular time so it represented the minimum energy times time or action
so let's look at an example of that and here's an example that may be
Example
familiar it's the example of your own visual system
so in the retinal the cells of your retinas
uh there are many many molecules that are rhodopsins of one variety or other
that respond to different wavelengths of visible light and they have some efficiency for
capturing light and let's just assume that they're optimally efficient that there is
efficient as they could possibly be and that means that they require the
minimum amount of energy to change shape which is what they do
when they're impacted by light to capture the the energy and hence the
information that's available in the light and the minimum energy to do anything
that records one bit of information so yes or no up or down
uh is 0.7 so log 2 um
of of Boltzmann's constant times the temperature
and again we saw this last time uh this is from roughly 1875.
and was then built into classical information Theory by Shannon and then by landauer uh in
the mid 20th century so what we're doing is is assuming that
since rhodopson's optimally efficient all it requires is this amount of energy to change shape
and it's known experimentally that rhodopsin takes about 200 femtoseconds to change shape so that's 200 times 10
to the minus 15 seconds so it's a very very fast reaction chemical reaction
so we can just calculate what the action is and at 37 degrees Centigrade so human
body temperature KT is about 4.3 times 10 to the minus 21
Joule my joules just the standard unit of energy
and so we can multiply everything together um KT times 0.7 times this response time of
200 femtoseconds of multiplied together gives you an action
of about 6 times 10 to the minus 34 Joule seconds
and if you're familiar with quantum mechanics you'll instantly recognize that number because it's very close to
the value of Planck's constant uh which is 6.6 times 10 to the minus 34 Joule
seconds so this says that rhodopsin is very near to Optimal
um the the best it would be able to do would be Planck's constant that's the
minimum action that can be undertaken um so rhodopsin is clearly doing very
well it can't be as efficient as we're assuming it to be
uh but it's pretty efficient so this number Planck's constant is and
this idea of a minimum action is not something we just pulled out of the air it's something that one can observe when
you're looking at what real biological systems in particular do in other
physical systems too so let's think about the the second
What to be asked
component of of this project of asking a question and that's
the thing to be asked and we want to ask a very simple question we want to have a theory of
asking very simple questions so let's define the simplest thing that
we can ask a binary question too and let's say this is the thing that we
can ask a binary question of using just this minimum action h
so we're going to ask for the minimal thing that it's possible physically to ask a question of
and this thing needs a name so let's call it a qubit and that word is a
contraction or Quantum bit and we can draw it like this a little
sphere with an arrow through it Ah that's called a block sphere and we use this symbol q and that
notation with the bar and the angle bracket uh
is called a bra notation and it originates with Dirac so it's a
traditional way of writing inner products actually in quantum theory
[Music] um to indicate the state of Q so we'll we'll this this thing called a
qubit uh only responds to Binary questions so it clearly can have only
two states the state that answers yes and the state that answers no and conventionally we we draw the arrow
going up if the answer is yes and the arrow going down if the answer is no
and so those are the two states that the qubit can be in when it's answered a
question so now let's draw a picture for the act
of asking a question of Q in the state q and let's draw it like this
uh this curviero is the action of asking the question and getting the answer back
and we're asking it of this minimum system the qubit
and let's call this this entire Act of H
and right at H acting on Q by this expression HQ
so again we're developing the the notation of quantum theory which uh all
of you who know the theory already will find familiar
so the third thing that we have to to build into this picture and into the theory
Shared language
is the shared language so we have to know uh what we mean by up
or down if we're going to ask the question up or down and we have to I'll have some
representation of of what it means for the qubit to distinguish up or down
so let's say that to us oh up and down mean this little diagram
with an arrow that's labeled up on one end and down on the other end so we're
defining up and down in a very simple way as just opposites we don't know
anything else about them except that they're opposites so this is a stripped down one bit
question we could have called them one and minus one we could have called them A and B we could have called them
anything uh we're just indicating that up and down are two opposing Concepts
and so this object that we've used to make this definition of the relationship between our two
words up and down is called a reference frame uh it's it's a
a physical object that encodes a concept or a meaning
and if you think about using language using English for example you can
understand me speaking in English uh because your brain has the right
sorts of neural circuits to allow you to understand English and produce English
uh using your your hand in your mouth and those neural circuits are reference
frames in your brain uh for understanding and producing English and
they encode the relationships between different words so you all know about chat GPT you can
think of all of the weights on uh all of the 10 to the
19th or however many parameters there are in gpd4 as a reference frame
that describes the relationships between words and phrases in English and many
other languages so this idea of a reference frame is an instance of of Land hours
principle which is is often summarized as saying that information is physical
what that means is that information always has to have some encoding
and that encoding that object can always be thought of as a reference
frame so let's put all this stuff together
Hamiltonian operator
what we have now is a reference frame that defines the difference between up
and down we have an action that we've labeled h and the action acts on this object of
the qubit uh which is in some state and what we've drawn here now is an
experiment and you can think of the incoming part of the arrow that goes from the
reference frame to the qubit as a preparation of the qubit so you can
think of it as I'm doing something to the qubit to put it in a particular
State like up because that's the state I want it to be
in and I can think of this returning part of the arrow
as a measurement of the state that the qubit is actually in
so if the qubit's actually in this state with Europe pointing up
uh then I'm going to get back the answer up when I act on the qubit to measure
its state so now we can recognize this this action
h as the hamiltonian operator in quantum
theory which always takes some time which we represent by an interval DT
to act on some State and in particular this binary state q so this is this
whole picture depicts the action of a very simple hamiltonian operator
um and again I want to emphasize that we've just defined the qubit as the
simplest thing that we can ask a binary question of
so how does this H work uh we can use h
to prepare this qubit in one of two states which we're going to label one
and minus one of the state one uh corresponds to the up Direction
and the State minus 1 corresponds to the down Direction
and doing this to Q so preparing Q in one of
these two states takes energy and we know how much uh boltzmann told
us back in 1875 that the minimum energy to reduce the the entropy of the
universe by one bit is log 2 of KT we saw that earlier when
we were thinking about rhodopsin so we can say that acting with h always
requires some number times KT where that number is bigger than the log of 2. and
remember the log of 2 is just in there to get units of bits of binary questions
uh as opposed to units of gnats which are questions that have
e answers where e is the exponential base the natural exponential base but we
want to use units of bits so we have to always have this factor of log 2.
so this lets us write H in a particular way we can take out this this energetic
term that vaultzmann tells us we have to include uh beta times KT
and what's left over is is in a sense the pure representation of the action
stripping out the energy requirement and we're going to call that M because m
is the standard symbol to use in quantum theory for a measurement operator
and M is is now dimensionless H uh has units of energy KT
is in energy and M has no units at all so it's h
without the energy so now we can ask what is this operator M that we've defined as the the simplest
possible action on a qubit but abstracting away the amount of energy that we have to use
to act on the qubit well what M does is just encode a bit or
Operator M
decode a bit so we can use this operator M to say uh
I want Q to have the value 1 I want it to be up so I can sort of reach out with
my operator M and grab q and turn it so that its arrow is pointing up
and that's what the the operation that's called preparation in physics it's what
it means to prepare an experimental apparatus for example you you actually grab hold of the apparatus and you twist
some knobs and flick some switches to prepare it to be in some state
and you can use M to measure a state that isn't known so I can
use M to grab a hold of Q and look at it and determine whether it's in state 1 or
-1 and I can represent these as just a cycle that starts with measuring and
then prepares or that starts with preparing and then measuring and if I represent it that way
uh what I see is is m having a value which is either the value
I want to encode or the value that I have measured and Q
and M acts on that value and Q to produce a particular state of Q to put Q
in a particular state or to realize that Q is in that state
and so m is actually an identity acting on some value and Q so it Maps
one and Q to 1 and Q and it Maps minus 1 and Q two minus 1 and Q
if you do the whole cycle of preparation and then measurement and that makes
sense it's actually an axiom in some formulations of quantum theory that if I measure the state of some
object what I'm doing is also preparing it in that state so if I immediately measure
it again I'll see the same value and that makes sense physically if I you
know put my coffee cup on the table and then I look for it it's likely going to be on the table unless something else
intervenes well what does this mean it means that we can do a little bit of algebra
um it means that we can write this original expression
of acting on cue with our hamiltonian in this somewhat more explicit form of
using the energy beta KT and our operator M on Q
and what I get out of that is the energy beta KT multiplied by Q
so HQ equals EQ that's the Schrodinger equation
so that's one of the central equations of quantum theory what it says is that
this operator h is the total energy operator on a system
its eigenvalues are the total energies of the system and we can now see where that energy is
coming from in this very very simple strip down kind of of representation of an action
the energy is the thermodynamic energy that has to be spent to determine one
binary outcome up or down
now if you're familiar with quantum mechanics uh you will have seen exponentiated operators uh like the the
next line here of algebra this operator P which is time dependent
and which is the exponential of H uh multiplied by i t over H bar
is called the propagator it's the unitary operator in quantum theory the
operator that conserves probability or conserves information
and so using the representation of H
as beta KT we can see that that this operator p is just e to the minus beta m
uh if we recall the wick rotation from the first session of this strange equivalence of i t over
H bar with 1 over KT that wasn't discovered until 50 years after the
invention of quantum theory um and that's still a very debated uh
thing I mean people worry about what this what this equation really means
but one thing that it means in this setting where H has this particularly
simple form is that the propagator is now just
the exponential of a number multiplied by this very simple strip down operator
that um encodes a bit or decodes a bit
but we know something about the exponential propagator just by looking at its form if you're again familiar
with these sorts of exponential operators you know that they're wave equations
and we can make sense of that using the diagram up above what m is doing is just
performing a cycle uh it's just mapping 1 and Q back to
itself or minus 1 and Q back to itself so we
can think of of M as just taking this object and flipping
it back around until it's uh until it gets itself again
and that kind of cycle can always be turned into a wave equation
and e to the I over H Bar times h t is a canonical form of a wave equation where
the the horizontal axis here on the wave is time or if you look at the little
cycle that I've drawn as a circle with an arrow it's it's the time of the thing spinning around like this which
is exactly the same thing as a wave traveling through time
so that tells us something very important it tells us that that this equivalent
expression e to the minus beta m is also a wave equation so it tells us that this operator m
has built into it some sense of time
um it's the sense of time of this prepare measure cycle
and that's implicit in m right we've used the wick rotation to
get rid of the the kind of what what I'll end up calling the external time T
the objective time t and we'll see in July uh
where this internal time comes from uh in terms of the wick rotation
but we can say now that it's an agent specific time it's an internal time
reference frame that's built into the our idea of this
system Alice that can act on the world and it represents the time that's required to ask this question
okay Chris uh can I ask a question at this point yes uh so on this slide uh
with the operator um I'm curious that's how can the agent deploy in the operator m
tell the difference or break the Symmetry between preparation and measurement or are they just completely dual
pictures um yeah they're completely dual so the agent the agent never breaks the
Symmetry the agent can't actually distinguish the act of preparing from the act of measuring
every preparation is a measurement and every measurement is a preparation right
that's that's in fact what this Axiom of of
measuring a state leaves the particle in the measured
State means right so yeah mathematically they're duals
thank you okay so let's let's now use this theory
Alice and Bob
that we've developed to describe the interaction between Alice and Bob and let's think of this situation in
which Alice prepares a qubit that Bob then measures
and then Bob prepares the very same qubit and that Alice measures it
so Alice acts with her hamiltonian operator which will label h a
and Bob acts with his hamiltonian operator that we label HB
and let's say that Alice prepares the qubit as in-state up
and uh Bob can then measure the qubit in state up and say oh the qubit is now up
and if Bob then prepares the Cuban State down uh Alice can measure the qubit in state
down and say oh the qubit switch from the up that I prepared to down so Bob
must have prepared it is down so what's happened here uh Alice and Bob have actually shared a
bit flip right Alice said uh up and and Bob said
down so and Alice heard him say down so they've they've shared this idea of
change by interacting with each other now this works as long as they mean the
same thing by up and down so we've implicitly assumed in talking
about them communicating that they both have this reference frame
that distinguishes up from down and this is actually a completely
General model of what I'll call a noiseless one qubit
channel now what does that mean it's noiseless because there's nothing else
in the picture right there's nothing else in the picture that can jiggle the qubit when
else and Bob aren't looking Alice and Bob are the only systems we're talking about and they share this qubit and there's
nothing else in the picture so there's no kind of third party or environment or
heat bath or anything like that that's going to mess with the qubit and disrupt their interaction so that's
a noiseless channel and it's a one qubit channel because they just have one qubit
that they're interacting with and they're alternately preparing and measuring at state
now clearly if if they can interact using one qubit they can interact using any finite number of qubits
so here's a picture of an in qubit Channel that uh Alice and Bob which here I've
labeled A and B because I took this figure from a paper are sharing
and uh Alice and Bob both have n operators one
for each of the N qubits that they share and they just do this prepare and
measurement cycle on all in qubits so you can think of Alice preparing the in
qubits Bob measuring the in qubits and then Bob preparing an ALICE measuring
and that allows them to to exchange in-bit messages and we can make n as
large as we want and so they can exchange messages of arbitrary
complexity and if they share the meaning of up and down then they can exchange these
messages with no noise so they can communicate and we now have our theory of two
communicating agents that are that are sharing arbitrary uh finite information
now I've labeled uh q1 through qn in this picture uh a holographic screen
and in fact that's exactly what it is I'll recall from Session One this slide
holographic principle
illustrating the holographic principle um
Shannon made this point that a bit of information is an answer to a yes no question
and so we can write down a number of possible States
we can write down an entropy um and
the limiting case of that entropy is the entropy of a black hole the densest
possible uh encoding of information in space
or on a boundary and this holographic principle allows us
to see any boundary as we discuss in session one as an encoding of bits
so the previous boundary of these in qubits we can think of as a holographic
screen now why is that important
um it's important because it allows us to use this idea of holography
and this idea of fixed encoding of a message or a fixed
encoding of an observable entropy at some density
that was developed in cosmology to talk about arbitrary Quantum
communication channels so we can import a whole bunch of theory that was done someplace else
into Quantum information Theory and see that it works perfectly because it
describes exactly the same situation what does this tell us
philosophically it tells us that Alice and Bob can learn
about each other at most in bits per communication cycle
so the maximal amount of information that they can get from an observation is
the in bits that the other one wrote on the screen
so this tells us something very important that when an agent is looking at their environment which is this other
agent Bob the amount of information that can be extracted from the environment is
actually proportional to the size in bits of the boundary
and the holographic principle just makes that size finite in space
and I said early on that there's no embedding space time in this theory that
Alice and Bob are not thought of as separated in space but as soon as we use the holographic
principle we can think of the boundary between them as having a spatial coordinate even though they don't have a
spatial coordinate so uh we'll get back to this point in
September when we talk about theories of emergent SpaceTime but all of these
theories of emergent space-time come back to this idea that boundaries can
have spatial extent even though the systems that they separate don't have
any natural spatial description or natural spatial degrees of freedom
okay so now let's recall another picture from
unitary evolution
Session One uh we talked a little bit about
feynman's theory of scattering and the the origin of Feynman diagrams
and the idea that if Alice prepares some
system in some initial state and then measures the state later
if we want to calculate what the new state is we have to take into account all of the
possible paths that join the initial state that Alice prepared to the final state that Ellis
measured so what does that mean I mean here effectively if we think of
suppose I'm Alice and the boundary is my screen
I'm talking to the screen and then later on I'm going to measure
the screen and between my preparation actions and
my measurement actions a bunch of stuff happens on the other side of the screen
and if I want to predict what's going to happen on the other side of the screen
I've got to take into account every possible thing that could happen
and uh I have to give some weight to those possible things that could happen
and quantum theory in fact tells you how to assign those weights to things that could happen in order to make a
measurement given some theory of the mechanism that makes things happen
but the fact that all of the paths have to be counted as what unitary Evolution means this in this this Evolution that
preserves information that doesn't take any away it doesn't add any it just
represents it in different ways so if you look at the screen
and imagine that Alice is interacting with her boundary and then she's interacting with her
boundary again it looks just like the previous screen and the way they read arrows are what's
happening inside Bob the wavy red arrows are a representation
of what's going on inside Bob as he measures his side of the screen and then prepares
his side of the screen so what Feynman is representing here is just the action of the environment or
the action of the system uh while Alice isn't looking
between Alice's preparation stage and her measurement stage while Bob is is
doing his measurement in preparation so this diagram is actually completely
symmetrical we could have drawn an arrow where the the wavy red things are and
drawn wavy red things where we've talked about Alice and we'd have the same picture just from Bob's point of view
we can also think of this of course as Alice communicating with her first future self by writing a memory record
someplace in the world and then coming back and reading it and if Alice writes a memory on the
world and then comes back later on and reads it she actually has to take into account
some theory of all of the things the world might have done to her memory while she wasn't looking
um so this picture of feynman's actually tells us a lot about memory
and when we think about organisms running around in the world uh doing
things like we do all the time um we tend to think of memories as
things that are are persistent and unchanging and all of that but we know that that's not true
we know that memory is degrade in various ways uh we know that uh adversarial third
parties can come and and change what we've done so that they fool us into
thinking that we've remembered something that we haven't and so on and so forth
that whole picture of memory is actually encoded in in this picture
that Feynman Drew in the late 50s to represent scattering of particles
summary
so what we've done here is started with this simple idea of asking questions
and we've actually constructed a fair amount of quantum theory we constructed the Schrodinger equation we constructed
the unitary propagator we constructed the idea of a reference frame which we'll talk about intensely next
time in July so we can sum this up by saying that
quantum theory simply is a theory of communicating agents and that quantum mechanics
of the theory that Feynman was complaining about in that earlier slide
the quantum mechanics generates this problem that seems intractable of how to
understand measurement because the theory is in fact about measurement it's not about mechanical
motion at all so Quantum Theory actually tells us nothing about ontology
and this is why the interpretations of quantum theory the the many worlds interpretation where you have all these
branching universes uh and so forth are not really science
they're philosophy their attempts to understand an ontology
of that's generated by a theory that doesn't talk about ontology it talks
about communication between agents but we've left something very important
out we've left out a consideration of what happens when Alice and Bob don't
mean the same thing by up and down and we've left out the famous phenomenon
of entanglement uh spooky action at a distance as Einstein
called it and it turns out these things that we've left out are very very closely related
free choice of reference frames
and we're going to see why in July and I'm going to give you a brief preview now
so what happens when Alice and Bob actually mean different things by up and down what if their reference frames
aren't aligned well the first thing to note is that nothing in the theory says they have to
be aligned so we have to consider the possibility that they're not
and in fact both Alice and Bob have to have what's called free choice of
reference frame when Alice prepares her her instrument she has to be able to
prepare it any way she wants to in order to do an experiment
and uh when Bob makes up a sentence to tell Alice uh he has to be able to
choose any language he wants to use he's a he's a free agent in this way
and if they don't have that freedom it turns out they're entangled so reference frame non-alignment and entanglement are
very very closely coupled now misalignment of reference frames is
Superpositions
what produces superpositions of outcomes so if Alice makes her measurements with
her up and down arrow arranged vertically for example but Bob prepares his qubit with his up
and down Arrow arranged at 90 degrees to Alice's Alice
is not going to have any idea what Bob did I mean she can't see distinctions in the
left right direction she can only see distinctions in the up and down Direction
so all she can do is flip a coin if she wants to know what uh Bob
prepared it's 50 percent likely he prepared up for her what she calls one
and it's fifty percent likely that he prepared what's down for her she can't
tell oh now if Bob if Bob's reference frame is pointing at
about 45 degrees so up for him means 45 degrees off of Alice's up
then she can sort of tell what he did if if he's pointing 45 degrees from Up
then uh she's probably going to measure up and if he's putting 45 degrees from town
she's probably going to measure down so her outcomes are 75 percent for one
and 25 percent for minus one if he prepares uh at this 45 degree angle
so we can write this in a particular way we can say that the value that Alice gets acting with
her M on a qubit that Bob prepared is some number times what she measures
is up plus some other number plus times what she measures as minus one
where those numbers the squares of those numbers add to one so why do they have to add to one well
they add to one because of the Pythagorean theorem oh
one is the distance the total distance between the two outcomes
and um a squared plus b squared are the other two sides of that triangle so
um another way to think of it is that the metric distance
of [Music] impossibility space is one
and a squared and B squared are just the euclidean distance components again euclidean distance is based on the
Pythagorean theorem so this is the born rule in quantum theory uh it's the rule that tells us what
happens when we're trying to measure a superposition and it tells us where these superpositions come from uh
we have a mismatch in in reference frames between two agents that are
communicating so if we go back to the free energy
principle which is what uh this whole active inference class is about
and we formulated in quantum theory we get a very simple idea of what the free
energy principle is the fep and quantum theory just says that interacting systems are going to
behave in a way that aligns their reference frames and that makes their communication as
good as it can be uh but since aligning reference frames
perfectly leads to entanglement of the free energy principle drives
systems asymptotically toward entanglement
well the principle of unitarity says that all systems will approach
entanglement asymptotically so we can see the fep is actually a
classical statement of the principle of unitarity and what we'll see in the next session
is why this is the case why active inference when we think of a Quantum
mechanically is a way of talking about the principle of unitarity which is the
deepest Axiom of quantum theory and we'll also see that this question of
alignment becomes more and more complex as the complexity of the messages of the
CIS that the systems are trying to communicate to each other increases
and the message complexity correlates with system complexity
so that aligning complicated systems is very hard although aligning very simple systems is
fairly easy if you think about uh what's the what's the simplest
possible theory in science it's particle physics because you're dealing with these very
simple things that interact in extremely simple ways and the really difficult parts of
science are things like sociology where you're dealing with uh incredibly
complicated systems like humans that interact in incredibly complicated ways and all we have are very vague kind of
folk theories of how that works but we know from that example that
aligning complex systems is extremely difficult um
it's what humans don't get along very well so the second session uh well the second
Conclusion
discussion section which Andrew will be leading is on Saturday the first of July a couple of weeks from now
the third lecture session will be on July 13th and uh I hope you all will contribute to
the interactive question and answer session on the web and uh show up for the discussion on
Saturday the 1st of July and join us again in July for the discussion of
quantum reference frames and reference Frame Alignment so thank you very much