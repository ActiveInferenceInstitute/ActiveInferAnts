ActInf GuestStream #023.1 ~ Maxwell Ramstead, Dalton Sakthivadivel, et al.

https://www.youtube.com/watch?v=igY9iyowesc

acting lab guest stream number 23.1 with maxwell and dalton we're talking
about rebooting the free energy principle literature and their recent publication
so i'll pass it to the two of you to provide just an initial introduction and
some context for the paper before we jump into some specific parts
maxwell first cool my name is maxwell ramstad
i'm the director of research at the versus research lab
where we specialize in probabilistic approaches to artificial intelligence
um and of late most of my research has been on the physics foundations of the free
energy principle and yeah very very much looking forward to having this
conversation awesome and dalton
sure um okay well i'm dalton uh i'm a mathematician and a physicist
um so right now i'm i'm uh at stony brook university in new york i'm also at the
uh versus lab where we're doing some work on the free energy principle right now my research interests are about
formal approaches to biological physics and mathematical foundations of complex systems and these kinds of questions one
of the most interesting frameworks in this sphere is the free energy principle
and that's uh how i've gotten involved in this literature awesome
so maybe in the same order what brought us to this paper what was
the gap that this paper stepped into and how did this team arise around the paper
and i'll bring it up on the screen as well it's a good question
um well i i think the paper does a bunch of different things um the first i mean
we've presented this as rebooting the free energy principle literature um
i think uh yeah over the last it's been almost two decades now since
uh the fep has been a thing uh i think the first paper was circa 2005 ish
and the framework or the the field of study that
has emerged around the free energy principle has changed a lot over the last two decades
in no small part in terms of the self-understanding that we have
as a community of practitioners working with these techniques and i mean as dalton
pointed out a while back i think the last time that really the fep literature had been surveyed
in a systematic fashion to kind of present where we were at uh where we
where we are currently like the state of the art it was probably carl's uh monograph from 2019 january 2019 um i
mean you know both of you were part of this international physics reading group that we had uh this was not this is not a
simple uh piece to read and uh yeah since then um there hasn't really
been uh basically a summary of where the literature is so on the one hand we were
aiming to uh reboot the literature uh to to basically summarize uh the ways that
the free energy principle had been applied uh in the literature and uh
to also present a lot of the uh progress that had been made over the last three
years a lot of which is due to uh dalton so i think that segues nicely into the
dalton well too generous by far as usual but uh
yeah so um maxwell raises a good point that there uh hasn't been
really an effort to tie together all the different
threads since probably 2019 and uh one of the reasons why
i mean that's that's a long time but it's not overly long however
in the last couple of years there have been some pretty serious advances in the state of the mathematics and the physics
behind the free energy principle so now you know three years later we're in 2022 it's not
a long time but nevertheless there have been big developments that really
beg this kind of a survey to be done and so that was one of the aims at least
of the paper was to draw together all the different threads to unify them make them a bit more cohesive
and and present the free energy principle as we're conceptualizing it today in a very top
to bottom fashion so before we jump into the sections and
the arguments and the claims in the paper which i'm sure will cover a lot of these updates
i'd just love to hear what is the free energy principle what is active inference and how are
they related i mean i i guess in the most general
sense the free energy principle is a statement that says that we can
understand the the dynamics of self-organizing systems as following um
a path of least surprisal in the most general sense and then in that context uh it's good
that you ask the question i think that there are at least two uses of the term active inference in the
literature um the one that i've tended to use is a very broad sense which is just like
active inference is specifying a path of least action um for what are called autonomous states
so like the active and internal states of uh systems that can that are considered things under the free energy
formulation active inference has also been used to refer to uh a class of specific
partially observable markov decision process models um that have been deployed and you know most of the
implement in silico implementations of the free energy principle rely on these
i think this has led to a little bit of confusion in that you know when folks say
active inference is a general theory uh it's able to account for self-organization that they're not talk
they're not saying this specific class of pond vp models is effectively you know repurposable for everything um so
yeah i i would say that this is the first sense that i outlined is the sense in which we say that active
inference is a corollary of the free energy principle um and yeah i mean in its most general form
the free energy principle is just a statement uh an alternative statement or restatement
of the principle of stationary action where the action is defined as a
surprisal in effect great dalton same questions to you
yeah i think um maxwell pretty much um covered it uh so as i mentioned you know my
background is actually not in the free energy principle not originally and it's not even in
machine learning uh so i've come at this literature with a bit of a different um set of
ideas and traditions and tools and so as a result i can't really talk
about active inference and i'm not totally familiar with it but i can talk about the free energy
principle um at length i'll try to be brief um so to me the the free energy
principle is a statement that random dynamical systems
uh do on average unsurprising things and and it's a very simple statement all
it means is that if you have a random dynamical system and it's trying to
get to some place in state space that is not surprising to it
so some preferred region of state space maybe a particular phenotype maybe a
particular morphological blueprint something like this the free energy principle is a statement
of not only that that happens but also a set of tools to model how that happens
how do systems get to these kinds of attractors and there's this very interesting way
in which the the getting to that attractor can be
read as inference and this is where these all these connections in literature appear to um
things like active inference you can talk about how systems actually get themselves to that attractor as a
perception an action problem and you can model it using this very famous uh variational free energy bound and you
can show okay when the system is encoding some sort of belief about its environment and about itself that when
it does this inference you have the minimization of some upper bound on surprisal so so the system is at least
doing unsurprising things at the level of you know it's not exceeding some kind of
intrinsic surprise that's some of the early formulations some of the more recent formulations take it even further and you say the
surprising full stop of of some trajectory of the system is going to be minimized by the system so it's going to
take on average the system is going to do what it expects to do which in this case
is get to some region in the state space that it prefers to inhabit
um what makes that not a tautology and what makes it something that we can
actually operationalize and ask interesting questions about is the fact that there is this nice connection to
inference there are all of these explicit mathematical tools that we can use to talk about surprising
minimization not just as the kind of information theoretic statement of systems that aren't surprising
or systems that aren't surprised due on surprising things it ends up a little bit more nuanced than that and so
so to me the free energy principle is this whole host of results uh about um
random dynamical systems and especially random dynamical systems which are organized or which self-organize
think that is uh how i would think of it and it's and it's got some physics and
uh stuff that that we can actually talk about in that context
awesome thanks both for those great answers i'm pulling up the paper
and so many things in what you said i just wanted to follow up on but let's follow
the main line of the paper and wherever you think there's some dots that could be connected or any questions arising or
areas of future research or the connection to applications that you're working on or other people might think
about getting involved in we can just take those little cul-de-sacs from the main line
so i have the paper up on bayesian mechanics of physics of and
by beliefs the two of you are the first authors there's also connor heinz magnus
kudo barron millage lancelot decosta brandon klein and carl fristen
any just overview notes on again like what led to this team or anything like
that while we're on this first page
um well from my perspective uh you know daldon and i have been talking a lot about this
kind of stuff for the last year year and a half two years um
and uh yeah i i won't i won't try to
i'll try not to be too uh overly generous dalton but like i think
uh yeah uh so some of dalton's work um has i think
changed the way that we uh think about uh the fep uh in particular um
what what dalton did in this great paper towards a geometry and analysis
for bayesian mechanics is to show that the free energy principle and the principle
of constrained axon entropy are actually dual to each other they are two sides of the same coin
and i i you know i've been um i've been following this line of uh work
for uh quite some time and i think it it foundationally changes the way that we think about the fep it moves it from
like this um some might say exotic result from you know theoretical uh
neurobiology to uh you know it connects it back up to
um the foundations of contemporary physics effectively by showing that you know
this thing that we we understand and almost take for granted uh you know maximum entropy inference procedures
turn out to connect up to uh this free energy literature in a non-trivial way so i think the paper
started out and it didn't end this way but i think we started off trying to write a
reader-friendly companion to uh the work that dalton had done um
but by the end of it realized that this was more um i think the dalton's paper towards
geometry and analysis for uh bayesian mechanics pillars
i think it stands uh on its own as a piece of mathematical reasoning so it is
an exercise in a maximum of entropy inference math and it shows that you can
recover uh some of the really core results of the free energy formulation just using the language of constraint
maximum entropy in particular dalton approves the approximate bayesian inference lemma that had uh you know
caused so much discussion in our literature for the last bit
and so you know uh i think the the paper grew out of that um
and yeah the the team is something of a who's who of like the
you know the the core contributors to this literature and just from a strategic point of view it was important
for us to have like you know lance decosta carl fristen you know connor hines and
folks that had been i think contributing to this core formulation and in particular to the
development of uh you know this new framing of the free energy stuff a bayesian mechanics
um so yeah i think that the paper grew out of that and if dalton's paper is this
kind of dalton's stent like the towards the geometry and analysis for bayesian
mechanics is a kind of standalone piece of mathematical reasoning this is more about how this actually fits into the
free energy principle literature so this is very much more a free energy principle literature paper
um and yeah we were hoping to do you know as reader friendly an introduction as we
could uh there are actually two whole kind of introductory sections in the paper um but we ended up doing a lot
of i think important work uh in that paper connecting up to the free energy principle
i hope that helps answer me great answer and welcome lars would you
like to give any overviews or notes before we jump into the sections of the
paper hey thanks thanks for sending me the link there maxwell allow
me on here um no nothing really to add there i'm just here as a spectator i have a few questions as we go down along
and maybe i can throw into the conversation but um yeah thanks for having me on awesome all right
so the abstract begins with a really clear aim the aim of this paper is to introduce a field of study that has
emerged over the last decade called bayesian mechanics and we're going to be
unpacking that claim so suffice to say the abstract very clear and summarizes
some of the core points that we're going to delve into now we're looking now at the contents
so what led to the sections the paper being
this way and in this order what did you feel like it was important
to include what did you feel like it was important to introduce and why
well so if you look i'll i'll actually pull it up in front of me so that we uh we're
all talking about the same thing um give me one second
and it's viewable in in large size on the live stream so yeah feel free to have your own copy up but i'll have
whatever section we're looking at will be very visible on the live stream well uh maxwell is grabbing his copy um
i'll just give a couple of contextual remarks so like maxwell described i mean
originally i had released this set of results about
what we call approximate bayesian inference and the sort of mathematical basis for some
of the key ideas in the fep literature up until that point anyway
um and originally it was meant to be a much shorter paper that just
dissected some of those results and related them back to the fep in a way
that was a little more concrete and a way that people who actually work on the ftp might might care a little more about
um because of course the stuff that i wrote about is um a little far removed from the fep
even though it's an object of inspiration for the results in the in that paper um
there is a reading of that paper where it's formally pretty distinct from the fep
so so originally that was the goal is just give it some extra physics intuition and some extra
connection to the actual fep it became something a little bit different as we were building this out
and we realized okay there are a whole instead of of new results um not only
mine but also from uh carl's tnb group and from others folks
and and they all really should be tied together nicely and part of that is the you know connecting the geometry and
analysis paper to the actual fep part of it is actually talking about
what we would think of the fep as today um
that shaped the table of contents a little bit because a lot of what we then
wanted to go and say is okay we have this theory of the free energy principle
one of the key ideas in the way that we're viewing the free energy principle today
is that it is just a bit of physics it is it is much like classical mechanics
or statistical mechanics um it has a set of mathematical uh
results that sort of hang around it that give it a nice foundation and it applies to specific systems and describes them
in a specific way and and that was why we began with both an overview of
what is mechanics what do we talk about in physics when we say mechanics and also section three is what is the free
energy principle what what have we talked about so far in the literature and and what might we define as bayesian
mechanics so what is what is the physics of beliefs or systems that carry beliefs so that that's sort of
excuse me that's sort of um shaped the the first uh maybe 20 pages of the papers it's just building out the theory
and the context for the theory afterwards is is a bit of a uh
sort of change in um our uh line of attack but
but you'll see it does remain very similar so so i won't uh get too far ahead of myself
great any other notes maxwell or we can carry on i think that that's a
that's a great summary i think uh yeah we we try to keep this as self-contained as
possible as a paper so you know the the two uh you know introductory sections
uh are meant to uh provide some kind of visual uh
intuition for a lot of the more formal results that are discussed in the paper and in you know the the papers that it
builds on um we have uh you know the artistic brilliance of brennan klein uh
that's added uh to this paper so uh you know i think the the illustrations help
um the idea was that you know based on dalton's work we we are formulating basically a geometry and
analysis for the core results and the free energy principle literature so we thought
let's leverage uh the geometric nature of a lot of these intuitions to really illustrate them
and so yeah that i think explains a lot of the structure and the paper ends on
some philosophical considerations and hopefully clarifies some of the
confusions or misunderstandings uh understandable misunderstandings uh
that have arisen um yeah so i think that no that does really address uh i guess the last thing to
point out is uh we we introduced this uh field of study uh in the
last section that we uh we call g theory um which is i think the direction that
we're going to be moving in for a while which uh is um yeah formulating uh
the free energy principle in the bayesian mechanics in terms of maximum caliber so
extending this duality between the density dynamics formulation of the free
energy principle in terms of that probability densities over states and maximum constrained maximum entropy
to path-based uh formulations so path entropy is called caliber and you
can dalton is one of the few world specialists in maximum caliber
uh and yeah maximum caliber is a maximum path entropy so it's the same idea as
maximum entropy but you're considering the entropy of paths and
we have had you know the free energy principle started off as a formulated in terms of paths
after all it is a version of the you know the principle of stationary action it leads us to write down paths of
stationary action and so the uh the ambition now is to connect these things up much more formally so that uh
we can uh we can handle really genuine non-equilibria
uh things like wandering uh markov blankets and uh yeah moving attractors
and all that kind of stuff which find uh you know a home much more naturally in
the language of maximum caliber did you did you want to add anything to that belton you're really the uh max cal
expert um no i think that's uh that's a good account of um one of the key future
directions is you know we spend the first half introducing bayesian mechanics
we spend the second half talking about where bayesian mechanics fits into the
rest of statistical mechanics and uh high energy physics by connecting it to
max end and to gauge theory and this is where some of the geometric stuff comes in
and then the the very last thing we do we sort of cap it off by saying okay now you know
we've talked a lot about bayesian mechanics we've talked a lot about maximum entropy bayesian mechanics
but there is in some sense much more natural formulation of bayesian mechanics in terms of dynamics because
ultimately that's what we're thinking about is dynamical systems and the way that they evolve in time the way that
they flow over their state space and there's there's a sense in which not only is it much more natural
mathematically it just works easier it looks prettier it's so it's much nicer
there's also a sense in which it's it's meaningless to talk about states of a process which is constantly in flux
so limiting ourselves to densities over states as exists in the last
you know couple of years of the literature um which has in fact not always been the
case some of the early stuff is written in terms of generalized coordinates of motion which are nothing
but a particular way of talking about dynamics and therefore paths
um so there's a sense in which the the recent um detour into
states is very limiting not only mathematically but conceptually limiting
and we can see that directly in the way that it is um handling things like non-markovian
processes uh or processes that change with statistics that are out of
equilibrium so so at the very end we say you know we've done all this work um the the
best next step is to take all of this and and all this stuff that we've just
done about maximum entropy basic mechanics and put it in dynamical terms and this necessitates passing to what we
call maximum caliber which is uh also due to jains originally it's the
principle of path entropy um but uh eventually you know the goal is we would
be able to write all of this stuff uh and in particular we'd have to be able to generalize what we have written
into a language that's much more dynamical and and uh and max cal we already know uh has
demonstrated uh an immense uh success in treating non-equilibrium processes so
mathematically i mean there's reason to be very optimistic about what we will gain when we generalize the duality that
we've talked about previously uh and so it really does seem like it's it's the ideal thing to do in the very near
future awesome let's jump into the sections
so section one is the introduction and just one part that uh
i wanted to highlight the footnotes are so informative there's some of these motifs like we set out to make it as
simple as possible and four pages was our limit but then we ended up innovating this way so that's one funny
motif and then the other funny motif that i see is um the super informative footnote
often because maybe it's possible to just make the claim stand alone and
indirect response to somewhere else so that's very exciting and interesting like
footnote 1 covers a lot of the prerequisite fields like dynamical systems theory calculus
probability and information theory so i found that to be very interesting because it helps understand where we can
come from and what kinds of backgrounds we'd want to be learning about and then also a very important
distinction of the two meanings of the word belief in the probabilistic sense of bayesian
statistics or the propositional or folk understanding as you write from philosophy and cognitive science so um
just thought those were two interesting footnotes and and reflected like part of the process and the discourse around the
primary text and how that can be clarified in this format
feel free to make any overall comments on that or that's just getting to page
three um well about the um the prerequisites
it's a it's a difficult um it's a difficult balance to achieve in some sense right because
um we don't want to be academic gatekeepers no one benefits from gatekeeping but these are also highly
technical fields um so you know i've been joking for you know the last
few months if you've never taken a derivative you're gonna have a bad time in this literature it's just not the
kind of thing that lends itself to um you know surface engagement in some sense like
it's very and especially with these um these new developments i mean uh there's
dalton's work uh that basically shows that the free energy principle is dual
to uh maximum entropy maximum caliber so there's this kind of deep connection to
i mean effectively the the core of contemporary physics uh and there's the there are
these new results uh that show that the free energy principle is asymptotically
equivalent to the principle of unitarity from quantum mechanics uh you know there's there are these new
quantum formulations of fep that have uh popped up so
yeah i mean navigating the space comfortably presupposes a lot
and the good news is that it's hard for everyone so there's uh
there's something to learn for everyone uh you know i spent the last uh three years of my life teaching myself like
category theory and gage theory and stuff which turned out to be very useful uh you know connecting up with dalton
and make doing all of this work but now uh we're launching ourselves into quantum
theory which i'm less familiar with so there's something to find difficult for everyone
but um yeah it i i really do think that to fully appreciate
going on here um some technical prerequisites are
important um otherwise we're led to making uh false assertions like i see
this circulate a lot that dynamical systems approaches uh are contradictory to uh information
theoretic approaches which is just nonsense from a formal point of view um yeah information metrics naturally
re-emerge when you're considering for example uh how do you measure distances in
state space effectively it's just yeah so the the more uh mathematical background
one comes with i think the easier it is to integrate into this um
yeah yes well indeed there's a lot of encouraging and good news and hopefully
a community that also values participation and accessibility as well
so agreed important general points there um yeah before we move on i'll say
something really quickly about this second book just because it's it's a remark that's
actually pretty important to me in fact maxwell's the one who wrote it but uh i i didn't even realize but it is an
important um clarification that when we talk about beliefs and an inference
it's it's much more general than just uh an agent or a cognitive
object um the the manner in which we talk about inference and we talk about carrying
beliefs is this this much more general sense of just two random dynamical systems that
are coupled and and therefore reflect the statistics of each other so
it could be a i mean generically this is a system estimating the statistics of an
embedding environment the very important point is any system
with any noise and in fact systems with no noise have statistics and so any
system that estimates or couples to another system with statistics
can be interpreted as mathematical inference that one system performs inference about the other
the the sort of content that you place on that idea of inference is very case dependent so it's not the case that that
stones for instance are cognitive but it is very much the case that stones reflect the statistics of their
environment simply because these two systems are coupled and their statistics reflect each other and so this is what
we mean in the sense of talking about agents that carry beliefs simply it is about objects that do this kind of
statistical estimation which we think of as inference but it's it's certainly much more general than simply something
like a reinforcement learning agent that actually stores representation of its environment um it is a representation
but in a much more trivial sense in the general case i mean i would i would add to that by
pointing out that um you know dalton was saying that we there were there were disadvantages to
focusing on the density dynamics formulation which features markov blankets and the like up so marco
blankets are great and we like them um but i think uh focusing on them so much
in the literature over the last several years has obscured the fact that uh the the free energy principle is at core
a statement about how you know as dalton was uh saying earlier random dynamical systems couple to each other so you know
the markov blanket is not some i often hear and read in the literature um the markov blanket secludes the organism
from its environment but it's not that's not that's not the idea at all uh the markov blanket is the set of
states by which the organism and its environment are coupled and in fact the
you know we made this case in a neat paper on a variational approach to niche construction several years ago
you can basically swap the sensory and active states uh
of your organism and you get sensory and active states of an environment it is fundamentally a story about how uh
systems couple uh and synchronize with each other uh it's not a story about how
uh yeah things that exist or somehow secluded from an environment it's it's really a
story about how yeah we uh we we become a model of our environment
meaning that we are like in tune with engaged with and reflecting the structure of that environment this
becomes very clear by the way when you look at the quantum formulations of the free energy principle
if you take the asymptotic limit of the free energy principle so its behavior is time tends towards infinity um for
classical systems that have space time individuation what you get is something
like the good regulator theorem so i become as much as possible as i can
like my environment uh you know modulo this space time separation i can't be my
environment because i'm here and it's there in some sense and then what you get in that context is statistical
mirroring but in in the quantum context when there is no space like separation between systems the fep tends uh
towards um entanglement so systems that uh are related in an fep
theoretic way at the quantum level uh become entangled that is precisely what the fep does
conforming to the fep means that systems become maximally entangled so it really is not a statement about
you know how organisms are separate from their environment it's a statement about how organisms are
or things in general self-organizing systems individuate and couple
simultaneously to their environments and how that's not a contradiction
excellent um so as we rush through section one and head to section two i just wanted to pull out
two really key quotes you wrote in this paper we discussed the relationship between dynamics mechanics and
principles and then later on page five you write bayesian
mechanics is specialized for particular systems that have a partition of states and go on to describe it more so as we
head towards section 2 an overview of the idea of mechanics and
indeed bayesian mechanics could you unpack a little bit by what you mean
dynamics mechanics and principles sure um so mel andrews uh as everyone i
think in the literature knows now wrote this great paper uh the math is not the territory um which challenged us to be
very clear about what we meant really uh when we're talking about the free energy principle and active inference and in
there i think mel makes a number of contributions but one of their most
important contributions is to differentiate between the fep as an uninterpreted uh formal
structure and the fep as it might figure in applications to
model specific kinds of systems and uh mel points out that you know
the a lot of the confusion in the philosophical literature has to do with the fact that the the primary ftp
literature often doesn't differentiate between the just the mathematical structure of
the theory and then these models interpreted as representing certain features of
a target system that we want to make sense of and that's important because
falsification uh or verification empirical validation more generally um applies to one kind of
thing but not the other right so uh the the free energy principle in so far it
is as it is a mathematical theory i.e like a formal statement is no more falsifiable or subject to
empirical verification than calculus would be right like you wouldn't you wouldn't try to falsify the axioms of calculus they
do or do not apply informatively to certain kinds of systems so there's a level at which the core formal results
of the fpp are have that status their mathematical results
and we can use this to uh you know do some interesting
empirical stuff so uh what we wanted to do is to differentiate between three kinds of uh
formal things in the first class of tools that
mel was outlining namely we distinguish between dynamics
mechanics and principles so the dynamics are descriptive they are basically a
formal description of some systems behavior you might say that like galilean
mechanics is almost entirely dynamics
you know the you needed someone like newton to come around and say well there are uh
general equations of motion that one can write down to account for uh
sort of how these uh how this description plays out in some sense uh so we move
from dynamics to mechanics uh in the same way that we move from
description to explanation from a target phenomenon that is formalized in a
certain way that we would like to have an explanation for to a set of equations of motion that really account for
how those dynamics come to be and then principles if if mechanics tell you how
principles tell you why so usually in physics we appeal to
some symmetry or conservation principle in order to derive the mechanics or the
mechanical theory for the the systems in question so what we're left with is principles
mechanics and dynamics all of which are formal theories and once you have a
mechanics you can apply it to study specific kinds of systems empirically
and that's where empirical verification would come in so principles are not falsifiable they're just bits of math
and you use them to write down mechanical theories which when interpreted in the right context and
when the variables are mapped onto things that are of interest target systems then they become subject to
empirical evaluation so hopefully that um
you know uh clarifies a lot of the model around uh around the fep one of the reasons why we
spent so long you know outlining the idea of mechanics and physics is that this isn't some exotic
way of thinking about things this is really just physics just straight
vanilla reasoning from physics um yeah i'll stop there dalton has probably
some interesting things to add no i think
i think you've covered it um yeah it's it's just that there are important formal differences in physics
between what we would call a mechanical theory for some object and a dynamical description
of some object and so in this tower of things
you get ideas you get theories that sit at different layers in the tower
this hierarchy ends up being useful in clarifying uh
this host of different results in the fep and where one fits into the other so
it was important to take the time to discuss it but that was that and that's the whole point
of section two awesome so to also move quickly through
section two on page nine you write we are concerned here with what we have called bayesian mechanics
and then you launch into an example of mechanical theory operationalizing a mathematical
principle and you provide some classical statistical formulations on
page 10. so could you give us an overview of what the equations on page 10 are showing
like what they do for classical physics and what is the analogy or what is the
connection that this is preparing us to make with bayesian mechanics yes uh well in fact i have an entire
paper uh that's about to come out about this just like building on the analogy um so i'll
uh leave that as an easter egg for the audience watch out for a classical physics for the bayesian mechanic paper
because i think instant classic it might be some interest yeah might be of some interest but yeah so on
page 10 um we are just giving an example of the of this kind of formal difference so
you have um some kind of principle in classical physics it is the principle
that systems um are kind of lazy you know they there is some kind of uh
an amount of energy that it takes to get from a to b and systems don't waste that energy uh
so they take precisely the shortest path from a to b or the path of least energy
in in the more technical sense of the transfer of potential energy into kinetic energy
so if you have some amount of stored energy the transfer of that into energy of motion is minimized along the path
that's a very um [Music] abstract statement and there's not a lot that you can actually do with that
computationally all you can say is you know the systems systems uh try and get from a to b
using the shortest amount of motion possible no extra motion so so if you see in figure one for instance uh there
are these paths that fly off into sort of these these very strange fluctuations in the classical world
those fluctuations don't exist because classical systems take this uh energy minimizing uh parabolic path in the
darker blue what is computational about that is that principle of stationary action so the
principle that you don't waste energy um results in a
mechanical theory a law of motion for the mechanics of classical objects
this is what we would call newton's law newton's second law in particular it's this everyone knows f equals m a it's uh
force equals mass times acceleration so the idea is that
if you are such a system if you minimize the amount of energy that you take
then the acceleration of you must obey precisely the force being applied to you
uh and um and so this is your your law of motion this is a mechanical theory the dynamics that come out of that
are able to be discussed when you start putting in actual details when you plug
in whatever force being applied uh sorry that's a dog you probably heard it
uh what is what is the force being applied to the system what are the initial conditions for the system what is the mass for the system all this
extra data starts giving you trajectories so an actual model of the system which is less explanatory and
more descriptive and this is at the very bottom of the hierarchy where you get this dynamical theory that's got all
this extra data in it so this is this is very quickly an account of the
that hierarchy awesome let's move into section three and figure
two so the caption is three faces of bayesian mechanics
what are the three faces of bayesian mechanics and what is this figure showing
well it's it's often been suggested that there are like 17 000
versions of the free energy principle and that it's not very clear you know
what the current version is and all that stuff and some of this is fair and some of it isn't i think some of it
is fair because it is true that often in the technical papers not sufficient care has been given to
you know ex making very explicit which assumptions we're making about the
systems that we're interested in modeling um so what we tried to do in section
three is to provide a comprehensive survey of all of the ways that the free energy principle has been articulated
in the literature um and so it turns out that there are basically three main ways in which the
fep has been applied which we're representing here so we've already alluded to the first
distinction um the fep can either be formulated in terms of a probability
density over states directly or as a probability density over paths
so over trajectories of states that we write in so-called generalized coordinates um
and those are importantly different um so the the literature over the last i guess like circa 2009
2012 to 2019 focused you know almost exclusively on the uh density
over states formulation and this is where you get um you know the approximate bayesian
inference lemma that's played uh a pretty critical role in a lot of these investigations this is also where you
get uh like states that play the role of markov blankets effectively
um whereas the original formulation of the fep was in terms of a probability
density over paths so you're not you're not really so much interested in in the you know
the the the dynamics of a system just in terms of how probable states are what
you're actually interested in is you know entire trajectories uh that unfold over time
and um the the most general you know paths formulation doesn't make a lot of
the um assumptions that have been criticized over the last little bit so
importantly uh we don't assume that the systems being described are stationary
um we don't assume that uh you know and accordingly we don't assume that the system has a non-equilibrium a
steady state and we're now returning to this formulation because it's less restrictive uh
you know for reasons that uh the dolphin could probably detail uh better than i
can um so then within the density over states
formulation um what you get is this kind of mode tracking or mode matching behavior
where um i mean essentially what we're saying is that a
system that conforms to the free energy principle is such that it looks as if
the average internal state is tracking the average external state or
like matching it and the the relevant difference in that
density over states formulation is that the external mode that the system is
tracking can have dynamics to it or can also not um and it was important to distinguish
these cases because a lot of the formal analysis so for example our colleagues at sussex released this great paper how particular
are the physics of the free energy principle and they come to the conclusion that uh there's
the fep doesn't really have anything interesting to say about the class of systems that they examined
what is the class of systems that they examined they are looking at linear systems uh
that undergo dissipation effectively so uh
physically these are dampened springs right so uh to restate if you take away
the mathematical uh baggage what they're saying is the fep doesn't have anything particularly interesting to say about uh
the behavior of dampened springs so what does a dampened spring do well it starts
off and then it dissipates back to a fixed point if you're burning
right like just due to friction um so the mode
towards which the system is flowing has no dynamics to it it is a fixed point it just dissipates back to a fixed point
and what they're showing is that there's nothing interesting to say from an fep theoretic perspective about
those systems but i mean the the counterpoint is sort of that there isn't interesting anything
interesting theoretically to say about those systems there isn't any interesting uh external
dynamics that uh the internal dynamics would be matching and a lot of these null results uh where
we we use fvp technology to say stuff about a system and there's nothing interesting
to say look at systems that have fixed modes fixed external modes and so you know
the the the idea is that you know the fep applies vacuously to those systems because there's nothing
interesting to say um so yeah to
to summarize my rant um we uh we tried to
summarize the main applications of the fep in the literature we identified three um and strategically uh we point out
where some commentators may have been led astray uh by focusing on one rather than the
other so in particular a lot of this these ideas that the fep can't handle
things like you know systems with moving attractors and uh you know systems that
don't have like a single mode um that this these are understandable characterizations given that basically
since 2000 from 2018 to 2 sorry 2012 to 2019
mostly focused on this middle class of systems so systems that uh we're
describing in terms of the density over states uh that have a dynamic mode so
it's understandable why people would focus their attention on that um but the fep in its most general form doesn't
make you know perhaps problematic assumptions like stationarity um and it yeah it it
also applies interestingly to systems that have interesting external state dynamics um so strategically i think
that's what we were going for in this section um and i i believe this is the only
place in the entire literature where this is reviewed so comprehensively in
terms of this tripartite distinction um so you know i i don't mean to be disingenuous and to suggest that you
know the confusions that have arisen are only due to um you know just
a lack of paying attention these things have not been expressed very clearly the assumptions have not always been stated
very clearly and yeah the the form of uh the path of least
action in each of these things looks very different um so it we can also understand why it might seem like there
are 17 versions of the free energy principle um but there aren't
thank you maxwell as we speed through this section i'll just note that formalism 1 on page 15 is
familiar and has to do with the flow of states in the particular partition and we've also seen the helmholtz
decomposition shown in figure 3 in terms of a decomposition on
into the vertical and the horizontal the gradient pursuing and the solenoidal isocontour aspect of flow those are
reviewed in the citations that are provided here so let's get into the newer stuff
um in section four you're discussing some mathematic mathematical preliminaries on
the maximum entropy principle gage theory and dualization but first yes lars
moving on to section 4 section 3 was incredibly illuminating for me
personally and i think the literature in general and having the separation out and there was a question that arose for
me and working through this that i just wanted to throw out there um i don't want to distract the journey
through the paper too much but in moving to this um you talk about on page
19 um when the ftp is applied to density over states as opposed to path we assume
a non-equilibrium steady state density and then on the next page page 20 you see we can view this
this non-equilibrium study state density is providing a set of prior preference preferences which lead the particular
system um to look like it attempts to enact and bring about these preferences through action if you
then move to the path-based formulation where there is no nest assumption
how do you recover these preferences in in that formulation
or can you not use that formulation to describe systems that are doing actions that look like they have preferences or
is there a piece that i'm missing does that make sense
um i can take that one so um one of the one of the key uh deliverables of this
third section is this three phases type thing right so the idea of the free energy principle
and and the mechanical theory that arises from it is we would want a
mechanical theory a law of motion for bayesian inference or for systems that
do basic inference and what it ends up being is approximate bayesian inference and and this comes in three flavors mode
matching mode tracking or path track this is the the three faces thing so that i mean just like you have
different flavors of classroom mechanics you have things that move continuously like satellites in orbit or you have
things that move and then stop moving like a bull thrown through the air eventually
returns to the ground and things that sit on the ground don't move unless they're acted upon so there are very
different flavors of approximate basin infants and these three are in particular the kinds of things that
we're thinking about so the reason why i give that context is because we can still imagine preferences
on the paths of a system a system must evolve in such a way that
it avoids certain areas of the state space given that it remains a system so uh you
know uh a human can't evolve in such a way that it dips too
far away from its allostatic bounds there are certain set points and certain bounds around those set points
in which i can oscillate but too far outside of those bounds and i'm in trouble
likewise you know i can have something like a stone that kind of
evolves through a state space the stone doesn't have preferences per se but it has
a definition and and so we can read not um preferences but definitions about what a
stone looks like in the same sense as we understand what a human looks like as certain preferences that guarantee
cohesion so things that are definitional of a stone um guarantee that same kind of cohesion
that just there's a type error if you would identify them but but you know
mathematically they end up looking very similar and and what's interesting about that is
now you can talk about preferences or you can talk about definitions along the path of evolution of a system a stone
must stay roughly together it must stay in this sort of crystalline structure
if you start uh hammering away at it you turn it into a powder this is something that we
wouldn't think of as a stone so so in the same sense if a human um
doesn't eat for too long and and maybe starves to death it's a
really grim example but unfortunately um it's one of the better ones you can imagine you know you're you're drifting
too far away from this um this state of being satiated or having
sufficient energy to maintain um cellular uh
processes and the chemical reactions that sustain life and as a result you know
the the preference along your set of paths uh has been violated um so i think yes there is a sense in which even
though we have forgone a nest density per se we still have a density over over
paths not over states that this density still expresses something of a definition for the system or a set of
preferences for the system without which we don't have a conceptualization of that system
that's that's a very long answer to your question but but maybe it satisfies you no that's that's great thank you so much
it was really useful that makes sense you you can kind of think about it as these constraints force systems to
basically pick trajectories that are at the trial of uh you know a preference landscape or
a constraint landscape if you want to think about it so you get the same kind of thing as dalton was saying but it's
not the systems aren't assumed to be stationary so they're not um you know
non-equilibrium steady-state distributions per se but there is something analogous
uh and a lot of the uh future work in g theory is precisely about using the technology of maximum
caliber to really make sense of this formally
um let's move into section four so in section four as noted and as
referenced to the previous publication there's a discussion that the fep is dueled to the constrained maximum
entropy principle and then one of the ways that that's pursued in this section is through the
lens or at least related to gauge theory so we're looking at figure four
what is gauge theory what does category theory duel and how is it being deployed in this situation
um i guess i'll take that one as well uh figure four you said yes
okay illustration of fiber bundles sections the big mega figures
oh yeah okay yeah uh well mega fig i i recognize that name i i believe that's
how we refer to it internally uh yeah well so
if you ask me um because i am a mathematician
primarily uh if you were to ask me or if you were to ask a mathematician what is a gauge
theory you would probably get a response roughly like well gage theory is the
study of a particular geometric space called a fiber bundle
so there is there is a type of space called the fiber bundle in geometry uh it looks exactly like that figure it's a
bunch of fibers pasted onto um something on the bottom uh what we
call a base manifold and uh and studying how do things behave
in a space like this how do they behave in the sort of fibers and how does that
reflect some kind of behavior on the base manifold these are interesting geometric
questions that arise in the study of fiber bundles and hence in what is called gage theory
if you're a physicist i mean it turns out that fiber bundles are the natural space for talking about um classical uh
gauge theories so the theory of certain high-energy particles
um but it's but it's a little bit more general than that uh and so if you're a physicist this is
what you think if you think about um like gauge bosons uh but but this is only
because fiber bundles are very natural way of talking about these things and so it is a little bit more general
what we're talking about in the figure four is this idea that uh in this space of fibers
uh you can kind of trace out um surfaces and that
these surfaces are like probability densities over the base manifold and in fact they aren't just like probability
densities they are so you can formulate probabilities over a state space as an
object in a fiber bundle and therefore if you have all the technology available
to you you can draw this very nice gauge theoretic interpretation of what it means to be
a probability density and therefore because the object of basic mechanics is systems that do
inference and so systems that estimate probability densities there is a nice gauge theoretic interpretation to
bayesian mechanics that hinges pretty much on this picture
what we would call the the gauge in this situation is the uh choice of this j function so
you see you have several different surfaces uh three of them each of which comes with a different choice of j
uh so the the idea of choosing a function in the fibers
and therefore choosing a shape for your surface this is what we would think of as a
gauge theory and and that's why i went down this route in the geometry
and analysis paper because it ends up drawing a very nice picture of what it
might mean to engage in constrained inference
awesome and could i give a pedestrian or so the the bystander
yeah the the more the less technical version of it is uh so gage theories and
dalton correct me whenever i say something that's wildly or even not so wildly inaccurate but gage theories are
basically how one would how one articulates symmetries or conservation laws and
contemporary physics so most physics relies on the idea that
um some transformations that are of interest like the ones uh described by
maxwell's equations uh have some kind of symmetry or or that
concern i think a slightly better way of going about it would be to say that you know modern physics is broken up roughly
into stuff and forces yeah and forces act on stuff
and stuff gets acted on by forces so the interesting thing in gage theory
is you can talk about how a definition of some stuff the shape of some stuff
is intimately dependent on the forces acting on the stuff
and so this is where we get this idea of we have a a particular
shape to our surface we have some you know probabilities over our states but
that this is actually defined by the the the choice of gauge this this j
function so our assignment of probability two states is actually determined not by
probability but it's determined by the constraints on those states certain states are preferable certain states are
not unpreferable states get low probability preferable states get high probability
and our notion of preferability is encoded in the choice of j it's a
function that constrains different states so constraints in this case are like penalties uh so our
assignment of penalties so our choice of force is actually what shapes our assignment of probability that's
ultimately um i think uh well that's a slightly different way of viewing um the geometry
of the situation is gage theory is all about these kinds of what we would call
covariance relationships covariance meaning literally two things varying together if i choose a force i'm i'm
forced to choose some stuff uh and likewise if i choose some stuff
that necessitates uh an underlying choice of force so gauge covariance ends up being very
helpful in situations like this
thanks let's see if we can touch on some of these last figures in figure 5
we see a vector field on a curve that's reminding us of that sort of baseball
diamond shape from earlier with the path of least action and in figure 6 a probability density is
generated by level sets of the constraint function j so either figure five or figure six
whichever you feel fits in best here what is being shown and where were you
going with it how is it connected to alternative phrasings yeah i guess i'll just cut to figure six
which is kind of about this covariance thing so if i choose a
particular functional form for j in this case it's a penalty that is proportional
to distance i would expect my assignment of probability to fall off
roughly like a distance function so it should it should be probability of a state should decrease as the penalty on
a state increases so in this case the probability of a state should decrease as i go away from some central point and
it should do so symmetrically and and so we would expect a gaussian density from
this and it is indeed the case that uh you can understand
the covariance as a kind of projecting down and then lifting back up
and what do you get when you do that well the stuff in the equation the probability uh ends up being defined by
where you take all of the sort of rings on the the j function you project them
down you get circles on the base manifold when you lift them back up they're rings
and so we know a symmetric probability density with a whole bunch of rings is just a gaussian probability
density so so this this figure is kind of capturing um what does this covariance
relationship actually look like how do we actually build stuff out of forces
and and it ends up being the case that it's this very simple recipe of you push everything down
and then you lift it back up and the lift is e to the j so the so you place j on to x
uh that's the first step your second step is then you hit it with this exponential function and e to the minus
x squared is of course a gaussian density so that's all that figure 6 is
depicting it's just zooming in on one of the objects in figure
4. great and i thought um on page 34 also
the striking result that the splitting of the flow of a system into vertical and horizontal components under the
constrained maximum entropy principle is isomorphic to the helmholtz decomposition of the flow of the
autonomous partition of a particular system so for those who are caught up with the way that the helmholtz
decomposition was used for example in the papers that we discussed in live
stream 32 with markov blankets and chaos stochastic chaos this is augmenting it
or transposing it into another formalization um and
moving on again quickly um it's worth pointing out that there is uh
there are some significant advantages to reformulating things in in terms of maximum entropy um
uh i'll i'll let you know delta and speak to the more technical uh
parts of this but i guess one um one thing that pops out to me more
politically is that uh maximum entropy and constrained maximum entropy
i mean they are just core parts of the physicist toolbox
so the fact that we are able to reproduce the helmholtz decomposition in
terms of the way that flow splits up in the gauge theoretic formulation i think is quite significant
it gives us an entirely independent line of reasoning arising at the same results
so uh you know especially due to some some work by martin beale and colleagues
a few years ago we were not we were no longer sure whether some of these results uh
obtained you know the there had been doubt thrown on to the derivations of the approximate bayesian
inference lemma in some papers uh life as we know it from 2013 i believe
is the paper that they targeted uh one way of reading this is that independent of all these analyses and independent of
whether bl and colleagues are correct about their criticism of the 2013 paper this is an independent derivation that
just follows from uncontroversial mathematics and we're able to re-uh re-derive basically the
the main core uh portions of the formal results uh that carl had derived so the
approximate bayesian inference lemma the helmholtz decomposition um and i mean
in some sense the the magic is that we understand now why these arise to begin with
uh there's uh yeah i think they're
the um the maximum entropy interpretation um in some sense especially in the the gauge
theoretic formulation in some sense tells us well why why does approximate bayesian
entrance work just full stop and these sets of results explain you know effectively why this
has to be the case only my facilitator hat prevents me from
being that excited um section 5.4 also explored more in the
previous citation so the four things that i wanted to just touch on as briefly as people wanted as we close are
the three philosophical areas that are introduced in section six and then of course just the appetizer of g theory so
in page 38 section 6 the philosophy of bayesian mechanics
6.1 addresses clarifying the epistemic status of the fep so
what were you aiming to bring people's attention to and address in 6.1 with this philosophical question
well i think this basically summarizes the point about dynamics mechanics and principles that we were making earlier
um you know so the fep has been described variously in various and sometimes very different
ways even by like its core proponents so carl uh introduced the fdp to the world
as a theory of cortical function circa 2005 and then as a unified brain theory um in
2010 which led a lot of people and i think not to um
this is in bad faith it led a lot of people to say well okay so this is a theory and so it should be making predictions
and therefore it should be empirically verifiable uh so i think you know the
the way that we talked about it led to a lot of uh confusion and it's been described as you know a framework
whatever that means by myself included right so meia koopa we called it the active
inference framework for a long time without really being specific as to what that meant we kind of meant all this
this cluster of results that kind of agglomerate around the fep
raja and colleagues have called this a trick uh kind of like a variational auto
encoder trick in machine learning so it's a it's a trick if you can write a markov blanket for a system that you can
make you can write down a model that looks as that says that the system looks as if it's performing bayesian inference
it's also been called a physics a physics of sentient systems a formal ontology
um so the point is to say well everyone is kind of right you know these are all in some sense valid
assessments and mel is really the one who clarified things initially i think by distinguishing formal structures
from interpreted empirically evaluable uh models
and um yeah i think the first part here is to say well we can make sense of this
model by appealing to this tripartite distinction that we've outlined so by distinguishing dynamics
or descriptions formal descriptions of some behavior that we want to get to mechanical theories that explain how
and principles that explain why and then what we're calling i think empirical
applications uh which are basically uh these formal models plus uh an
assignment or an interpretation or evaluation of these models in terms of the features of target systems that we
want to explain um yeah so when they're applied in that way
mechanical theories become empirical theories uh as we write in the ordinary sense
but yeah so hopefully this kind of clarifies everything around falsification how this thing is used and
importantly why this is just standard physics i mean this isn't this isn't all that spooky in terms of
the use of mathematics to make sense of physically relevant aspects of our universe
um so that's what we were trying to do in that section great
really clear 6.1 it reads to me like it's the tip of an iceberg with a nice
landing and take off strip and yes it's a big iceberg but it is an iceberg and
there is a tip that makes sense 6.2 on page 39
elon vital and the fep what does this french linguistics have
to do with the fep maxwell well uh dalton might have some pretty
interesting remarks to make but just briefly i mean um i find it kind of ironic that uh you
know the people who are most critical of fep right now like folks from the inactive tradition and
folks from the ecological tradition sometimes frame their own research is trying to you know
struggle against dualism in some sense but our belief is that they are
intrinsically dualistic frameworks um so elon vitale is a french term
with vitalism i don't know how familiar you are with like the history of biology but before the 20th
century in the uh discovery of dna most serious uh physicists believed in
something like aristotle's entire key so like that you you had to have some kind
of physical mechanism for propositiveness and so ella guitar was this kind of
vital force that uh they believe the vitalists believe animated living
systems and differentiated them from non-living systems like stones and rocks
and we believe that one of the consequences of the perspective that we're adopting here and building on you know especially
the work of mike levin who's done amazing uh made amazing contributions in this field is that it
self-organization and cognition and life and these these things that we like to point out as being distinct from inert
matter are actually are more on a continuum uh the you know the bayesian mechanic
says that um basically anything that's a thing will exhibit some features of what we
think of as cognition um so uh it is a massive massively
deflationary and absolutely resolutely monistic perspective that we're
advancing here uh yeah it was just you know the um
trying to look for the boundary between living and non-living systems is bound to fail in
some sense there is a continuum these processes that we're interested in
are also evidenced by rocks and by tornadoes and by crystals and it is a
question of degree uh to which systems uh act
as cognitive systems um yeah
i'm sure dalton has more interesting things to say about that yes on 6.2 what else would you add there
dalton well maybe not more interesting perhaps more interesting things to say
but uh well yeah i mean i think this section is is mostly just um
a recapitulation of footnote two in a sense um meaning you know we we made this
statement that inference per se representation of some statistics
of something else is this very broad very general thing and any system that is not a closed
system does inference so what that means is you know under the free energy
principle and at least what we've written in that paper was you know what we've worked out
so far uh there isn't uh a way to talk about cognition versus
non-cognition it's more of a spectrum of cognition
there are certain systems that are more competent this is something that carl might call
a temporal depth so there are systems that are very good at planning and executing actions and there are systems
that are not you know so there's a very clear difference between humans and stones for instance but that difference
isn't in one does inference and another doesn't it's that one does a bit more
complicated inference it has uh better or more accurate representations
or more representations full stop maybe uh and it's better at using those representations to to do action but both
stones and humans are estimators of the statistics of the processes around them
simply by mathematical construction and and so there's this very uh
uncontroversial statement or at least it shouldn't be a controversy that systems
things in the very most general sense exhibit this kind of
representation-based inference that we would typically identify
as cognition so that was the motivation for talking about that and then maxwell tied a very
nice bow on it with this uh this great history of a debate around very similar questions uh but yeah it
was this idea of a spectrum of cognition awesome and citation 92 there is the
2018 paper answering schrodinger's question so many years ago
the other maxwell at all who raised that question and sparked
really a phase transition in the discourse and that was also like one of those
it was one of the papers that really drew me in and got me excited and so it's amazing to see
what other questions and answers have been risen 6.3 and then g so 6.3 is a slightly
longer section and it's on maps and territories so yeah
what is that i'm really glad i'm really glad that we were able to write this so
um i i never found this particularly confusing but i i i i it has led to a
lot of confusion um so in particular there's this entire
paper by thomas van ness that just is just confused about uh this issue uh i forget what it's called
as the living life modeled or
what anyway um so folks have said well so is is the free
energy principle um just just a description
that we are uh you know a model that we are using to describe
interesting features of the world or is it saying that um
you know self-organizing systems actually are models of the world
um and so you know we i never particularly
found this problematic um because i so
the this phrase uh in in the paper i think sums it up correctly uh
the free energy principle is in some sense a map of that part of the territory that looks as if
it is a map um and so uh thomas metzinger actually retweeted our
paper and pointed uh called this nested representationalism which i found
interesting so yeah there are these kind of two distinct levels at play
but there's no foul play here because the fep model is very explicit about
which parts of the formalism pertain to our map of the territory and which parts
of the formalism pertain to the map that self-organizing systems are
constructing according to our map um yeah so i i i think it's important to
point out that you know there isn't a contradiction here um that there are just these two probability densities
that are at play in the construction the q density and the p density and you can understand the
the generative model or the p density as basically uh our model of uh
the self-organizing system in terms of uh yeah joint probability density uh
over uh it's it's state space or potentially it's a space of paths
um so in that sense you know um the
the self-organizing system being its own best model uh really means we have a
model uh we can explain the system's dynamics and the the system's uh
potential uh is is formalized uh you know as a as a generative model as a
joint probability density it just so happens that part of the
variables that are described by that joint probability density uh play the
role of parametrizing additional probability densities over another
subset of variables described by the generative model so there are really these two i
think unambiguously different senses of being a model that are at play
um and yeah i don't think this is a sleight of hand
and hopefully we have clarified yeah what
what exactly is at stake here um i think there are some nice connections to the
maximum entropy uh formulation so as dalton articulated
in the paper at least uh and no he you said you said as much in discussion today um i think you
by by flipping to the perspective of uh maximization of entropy we we
effectively recover our own position as modelers trying to model the system
um so the the the prism through maximum entropy is uh adds
this additional clarification that uh yeah we can entirely recover the perspective of a model or using maximum
entropy modeling to model a free energy type system by invoking this duality of perspectives
and i think that's really important [Music] then there's this other piece here which
says that the the maps that we construct in fep and in max end uh both adhere to a kind of
epistemic minimalism so maximum entropy inference is basically uh saying i'm going to uh well
given some data set uh the uh probability density that most that is uh
the one that best explains the data set is the one with the highest entropy what this means is that
we are uh building in to that uh probability distribution as little prior
information as possible it's like starting from the point of view of maximal ignorance given a few constraints what is the underlying
probability density the fep has a similar you know starting
point for maximal ignorance which says i can't go beyond the blanket like i i am stuck with the data that i'm generating
and uh with the way that i probe the world this data generating process to
generate my data and th there is no going beyond that you can't go beyond the blanket unless you break the blanket
but then you're just introducing a new blanket so for example um you know i i can't see in your brains um i could put
you in an fmri machine and break the blanket but then i'm i'm really introducing another
another blanket you know which is this new set of data that i have to continue making inferences from um
so i mean the then the the fep and accent kind of emerge as uh these
epistemically um minimalistic or um
you know they kind of emerge as the way that you would construct a map of the part of the
territory that acts as a map from a perspective from from a starting point of maximal ignorance
great and i think that's connected in the active inference textbook to figure 9.1
the meta bayesian perspective and there it's not described in the context of maximum entropy but it's
something very similar with this nested representationalism on any other philosophical notes before we
go to section seven yeah that's exactly right that's exactly right yeah yeah i love
this book um yeah
is that anything to add before we launch into g theory no i think you raised an interesting
point um so we can talk about you know when we use the fep to model a system
what we're doing is forming a model of the system where the system forms a model of its environment
and so there is this nested representationalism what's interesting about the maximum
entropy point of view is you can um kind of uh dualize it you can you can take the
sort of mirror image of this thing and you can ask okay well we're not interested in a model of the
system modeling something all we want is a model of the system so what does the system look like when it's creating that
model not what does the system's model look like so this is this is the dualization
aspect of things and so you can talk about and when you dualize you can talk about things like constraints on agents
states rather than the predictions and actions of the agent so it's a bit of a
different viewpoint it's just emphasizing different uh
levels of the nest so to speak um which is which is kind of interesting
because you do get both of these perspectives for free as soon as you commit to this relational
symmetry of an observer in an environment and an agent in an environment and how those two things do
model each other um and that's what you get when you dualize things
uh but that's yeah that's that's it for me on that section i think maxwell pretty much covered uh a lot of the
important points i i mean i i will say that you know this this probably is not obvious
until you really look at the mathematical formulation uh and notice that there are two you
know as i as i wrote in that paper from a few years ago the fep is a tale of two densities
um and you really need to uh like take take a look at the math to
understand that there isn't a this isn't like a case of reification
this is just formulated so it it it isn't so simple that you could just put
it in a direct and a simple graph and say hey look here are these two uh
but definitely if you take the time to work through the um the formalism
there are clearly these two different senses of uh being a model that are at play um
that are cleanly distinguished and i think are actually not all that problematic
awesome it's almost like thinking through other minds highlighted some of the social consequence and theory of
mind and behavioral aspects of certain types of cognitive entities but systems
thinking of through about other systems or infers thinking through other infers
infra ants that type of dual view from the inside view from the outside is again what
you're suggesting is enabled by that kind of a commitment to these foundations and
of course it could be a whole other guest stream and perhaps should be on g theory
but as we close here what can we say today on
613 2022 about g theory and what is exciting you
all about how you're going to continue forward
do you want to take this one dalton uh yeah sure uh so
i mean like i mentioned earlier on um there's already a lot of really promising stuff in the literature about
patented girls and path entropy and the kind of power it has to deal
with systems that we would uh normally kind of balk at and
and so it's it's already very promising there's reason to be optimistic about how this extension will benefit us in
the future um so g theory itself is is um
maxwell coined this term to describe the uh extension of this duality from
mode matching and accent max cal which will involve um precisely this
we'll try to formulate um the free energy principle in its full generality as dual to uh entropy in its full
generality on paths and so forth um and and so
the reason why this is so exciting is because already there's a very clear path towards talking about um systems
that are non-stationary so systems whose statistics change more complicated forms
of inference uh more complicated forms of constraints and preferences and so it seems like already it's a much
more faithful description of the kinds of systems that we want to talk about and extends to things like um
more complex systems uh things like humans potentially um
so so this is really the uh i guess the the end goal is to do this
dualization to now build an fep dual model of something like a
brain which we know models its environment in this very complicated way and so the kinds of representations it
does are very complicated so how do we model that um
that that should uh arise out of maximum caliber and and therefore out of g
theory and in principle you know eventually we'll have a very faithful uh very
foundational picture of complex systems but this is a very um long-term goal
in the short term we just want to get the maths to work to connect that a bit to lars's uh
question earlier uh what does it mean to have a non-stationary density over paths
well i mean what we're interested in is the way that the density changes as a function of the dynamics so that you
really have like these moving surfaces over a space of paths or space of states
and to really capture all of that kind of time dependency uh
yeah requires moving from uh accent to maxcal uh from states to paths
and um all of these kind of more fine-grained uh
you know wandering blankets and moving attractors and all of that good stuff
should fall fairly naturally out of yeah g theoretic formulation of this
stuff i like how within fep as we know it we
have variational free energy f and then expected free energy takes us into the future and planning and that's g and
then we see a little bit of like free energy principal f and then g is the next letter so that's a funny little
would know duel analogy um well if anybody has any closing thoughts it
would be a great time for that but just wanted to say that there's a lot of appreciation in the chat and a lot of
excitement around this work so we hope that you just continue
acting and inferring and serving that's that's kind of you to say uh
yeah thank you very much for the invitation to discuss our work
this has been great uh and yeah we uh we look forward to uh you know exploring
the future uh with this whole community and um thanks for your time your attention your energy
uh very very positive always a pleasure to be on actin flab and uh yeah thanks for the guest stream
yes i can only echo that uh it's been a pleasure so thank you
thank you thank you maxwell and dalton at all thank you lars for joining and
until the next time bye may the gradient descend ever in your
favor my friend and with yours slash ours