Cognition, Consciousness, & The Future of Ai | Maxwell Ramstead (EP41)

Jack Roycroft-Sherry 
https://www.youtube.com/watch?v=EAH02vr16U8


TIMESTAMPS:
00:00 - Intro 
00:26 - VERSESAI and Utilizing Cognitive Science to Design AI
09:39 - How All Intelligence Is "Collective Intelligence"
22:26 - Innovative Approaches to AI Development
30:46 - Computational Specialization & The Intelligence of Distributed Cognition
38:26 - Explaining Consciousness Using the FEP
53:56 - Debating the Unity of Consciousness 



when it occurs in nature all intelligence is collective intelligence any any real physical
intelligence system that you can think of is composed of you know a bunch of
subordinate intelligences that are in turn you know and I mean you know depending on how far you want to take
the whole it from bit wheeler thing it goes all the way down to like Quantum fields and atoms and all of that stuff a
VERSESAI and Utilizing Cognitive Science to Design AI
nice place to start might just be if you tell me a bit about that your work versus AI um because it's kind of using
to my understanding active inference and theories and cognition to kind of help us think about and create AI so that
might be a cool place to First maybe introduce active inference and and then
think about how that relates to things like Ai and then we'll see where it goes absolutely that's a great place to start
um so yeah I'm Maxwell ramstead I'm the senior director of research at versus AI
uh versus is a cognitive computing company um and uh basically we're in the
business of uh taking the explanatory principles that have been you know
discovered in neuroscience and the sciences that study cognition broadly um
and turning them into design principles uh for artificial artificial intelligence systems um in particular
we're interested in the physics of information U this has also been called basian mechanics so the physics of
probabalistic beliefs um and applying that to build AI systems that are genuinely able to take
a perspective on the world um and you know engage in active inference right so
uh active inference being kind of online real time uh perceptual inference and
action selection um so yeah uh my uh my
background is uh multidisciplinary like you were saying mainly philosophy and
computational Neuroscience uh I work closely with Carl friston um who uh is
the originator of uh active inference and free energy principle and all those nice things um so yeah we we've been
around for um going on half a decade pretty soon at versus um and yeah we have a we have a
very active inferenced focused lab actually we'll be we're coming out of uh
our cocoon this year um and we'll be rolling out some Benchmark work
comparing active inference based AI to more standard uh you know it's sort of it's a
weird historical circumstance that we now think of like deep learning as just kind of state-of-the-art standard
vanilla stuff but yeah we we'll be benchmarking um and hopefully showing you know a
genuine advantages to flipping yeah it would be interesting if you could tell me a bit about the the challenges and
even the thought process of like thinking about why you could apply active inference and these theories of
understanding cognition to AI because yeah as you say we've been creating like things like large language models and
these more like generic and these you know interesting models in their own right um but they're not things that in
in many ways are sort of directly analogous to how our own cognition works
so how's it has it been trying to think about AI in this life
well I mean you can think of active inference as like going full Bay U so it's a fully basian approach
where U we're basically using um one objective function the variational free
energy to optimize um the full kind of stack of intelligence right so um we
variational free energy it sounds sometimes like a little bit esoteric it's a quantity from information Theory
and essentially it quantifies the uh the Divergence or the distance between the
data that you expected under some model of how the data are produced um and the
data that you actually get so the interest one of the interesting things about using variational free energy is
the kind of backbone um for your stack as opposed to say reward is that you can do the whole
inference uh you can do you can do inference on several different time scales which essentially covers all the
different like forms of intelligence that you might uh encounter in uh in
real time so there's perceptual inference or state estimation right which is basically uh I
think I have a hypothesis I think the world is in a certain configuration or State uh if the world was in that
configuration or state then I would expect to get a certain pattern of data um and then I can use the Divergence
between the pattern that I got and the pattern that I expected to refine my hypotheses right and you end up
selecting the hypothesis that has the lowest free energy which means like that the that that generates data that's the
most consistent with the data that I'm actually getting but you can take that up a level right if you have like one
layer of inference running at like kind of state estimation level um then you
can do uh you can do inference about the the parameters of the uh actual model
like the structure of the process that's generating um your your data so you can
uh learn things like the transition probabilities and the likelihood uh that
Maps your uh basically the states causing data to the data um that is
caused by those States and so yeah you you you get this nice kind of parameter learning again
it's the exact same uh it's the exact same objective function you're just
iterating it at a slower time scale uh so in some sense it's kind of making inferences about your own inferences and
then at the top layer you can actually do whole wholesale and model selection
using the same right so uh there it's not the value of parameters but the actual like existence of parameters
within the model the way that they're hooked up to everything um so yeah it gives you a nice principled kind of
bottomup approach to building a whole AI stack based on the same core techniques
everywhere which I think is uh pretty cool um historically
the the reason these methods haven't been deployed at scale is that basian techniques are are sometimes difficult
to scale I mean there are a number of problems with scaling for example where do your priors come from um and um what
one of the things that we've been doing at versus is uh breaking the
basian wall socalled um so figuring out efficient techniques uh that allow you
to yeah deploy approximate basian inference it's scale without running
into you know the usual intractability problems that you run into with base you
know the problem with basian reasoning is that at the end of the day you need to renormalize everything uh it's
probability distributions right so your posterior is proportional to your likelihood times your prior but it you
need to normalize in order to get probability distributions like that that uh
integrate to one and so on back from from that and often the the uh the this
denominator that you need to like normalize with is intractable um so yeah we've developed a
bunch of alternative techniques uh they've existed in the literature variational Bays is a way of getting
around this so you replace uh an intractable exact inference problem with
a tractable optimization problem um and that's gotten us
uh a big a big part of the way to our objective so yeah you you'll be hearing
a lot about these results over the coming year um but it's been a it's been
very exciting um to develop all this stuff yeah it's helpful I mean one one
thing I want to say is that when you talk about having to think about active inferences occurring at many scales
right so kind of a benefit of like applying that to AI is that in a way obviously that that is how the brain and
how how active inference is occurring within us right it's kind of easy to like say if you're reading a paper hearing about active inflence like oh
yeah you know we predict and then we receive you know sensory data back and we update that but that's occurring you
know at the you know say top level of the cortex but then like lower levels of the brain I mean even like individual
cells must be kind of maybe having their own it's it's going you know from from the lowest levels up to the highest
levels in like in these iterative processes um and and I suppose like any
AI kind of might need to have that I guess think about normal like attention models and things that they're also like
let's try and get more Nuance here by like predicting not just one one level
but like you know how how how accurate uh like intermediary stages going to be
so so yeah very you're putting your finger on something very critical here which is the and I think this is from a
from a global or general kind of design perspective this is where we are most
uh uh I wouldn't say like in conflict with but like we're most opposed to the
kind of standard foundation model approach um so it when it occurs in
How All Intelligence Is "Collective Intelligence"
nature all intelligence is collective intelligence any any real physical
intelligence system that you can think of is composed of you know a bunch of
subordinate intelligences that are in turn you know and I mean you know depending on how far far you want to
take the whole it from bit wheeler thing it goes all the way down to like Quantum fields and atoms and all of that stuff
um so yeah uh the way that nature has
solved the problem of you know intelligent behavior is to offload
intelligent Behavior to communities of intelligent that are able to at The Ensemble level solve problem so even you
know you as an individual are you know the you emerge as an entity from the
coordinated interactions of uh you know an unthinkable number of different
agents that are competent in their own domain yeah you know like uh as my my my
liver does its thing right and my you know your pancreas does its thing and your heart and then the all of these
specific kind of intelligences that are uh expert within their domain right my
my heart does the blood pumping and my pancreas does the etc etc uh something
more emerges from that and so that's that's the blueprint that we're using um ADV veres uh and I think more generally
uh within the active inference approach to really understand intelligence so
like we're not trying to build uh the monolith ADV veres right we we kind of
think that there's a problem currently with uh the idea of kind of building a machine God just like is one monolithic
centralized system that just like encodes all of like that that's just not
it's not that's not how nature designs intelligence is and there are reasons to
think that this is not like an efficient way to go um you know the there's a what
we need um for the future AI of AI is to go I think in opposite direction right
like what ideally and you know our our kind of end goal and we outlined this in
our white paper which was recently published uh so the the paper is called
designing ecosystems of intelligence from first principles and that's precisely what we're trying to do right
we're trying to design ecosystems of intelligent agents some of which are quote unquote artificial uh and some of
which are quote unquote natural like us um but yeah the uh
so I think if you think of AGI artificial and general intelligence
is often presented as the north star of AI research and this can mean a bunch of different things usually in the more
plausible sense what people mean by AGI is something like a system that's able to perform at human level uh on a bunch
of tasks um which you know I guess is fine as far as it goes like that's
aable uh and reasonable engineering objective right um but the the concept
of AGI is kind of incoherent when you stop and think about it for a few minutes in particular intelligence is
not General there's no such thing as general intelligence like all
intelligence is tailored to specific kind of situation and reflects you know
contextually appropriate adequate Behavior within that context right um
even things that might seem General like mathematical reasoning and logic are still Fair narrow applied forms of
intelligence like there's no such thing as general intelligence so you know
there's a sense in which uh the I think a lot of the industry is kind of chasing
a myth here um there is there's no such thing as general intelligence so forget
artificial general intelligence that's probably not what we want to be aiming at uh especially if we
want to have realistic and achievable objectives would you say so it's interesting
because obviously us as human agents we do have the ability to have you could
say deploy intelligence across many different domains but would you think you think it's just better to conceptualize that is not a kind of
intelligence or like as something I mean you can think about it as a kind of intelligence but what I mean is like so
you know you're uh your pancreas right is an expert at secreting different
kinds of things that that's a of intelligence right like these are like
living organ systems that are constantly monitoring your internal State your internal
mear um and uh you know secreting appropriate things when appropriate
that's a form of intelligence like I I I I I as an organism like as as an agent
I'm not very good at secreting B right like this is what I mean like uh
you know uh certainly abstract you know reasoning and stuff is applicable in a
bunch of different domains but when you're thinking about like intelligence there there are various
kinds of intelligence that are just not equivalent to I think like abstract logical reasoning if that makes sense uh
even this kind of you know the IQ or whatever gets captured under the G
factor or whatever I mean it's not it's not completely General uh in that sense
right like it uh it's a it's a specific kind of expertise that is Deployable in
specific kinds of domains like any other you know competence um yeah and I think it's a
bit misleading to think of that as like general intelligence when it's just it's just another it's a highly specialized
form of symbol mainly symbolic kind of reasoning right like this isn't it's not
as general as all that really given that you well well that's interesting because
in in in reformulating intelligence in this way this this white paper you guys
wrote on sort of ecologies of different agents and intelligences how does that that fit in so you know when you're
building you know AI that are based more on the kinds of active inference that we
as human agents might do and and perhaps I'm just you you can tell me are they
maybe more interpretable and unless you know we can kind of uh see in what ways they relate to us I'm just I'm just
wondering how should we to check okay um
so okay active inference-based AI architectures um are constructed to be
human interpretable or transparent that's a big difference right uh so in our stack we don't use any black
boxes uh we use uh you know it's a similar kind of model architecture right
but um every parameter every node that we deploy is explicitly labeled and
corresponds to some aspect of the underlying situation trying to model um
so you know our approach to you know deploying AI in a given situation would
not be to like you know create this monolith that in theory has information
about every context whatsoever it's to deploy agents that are expert within a
specific you know situation or domain of expertise right um and uh then you know
to create an ecosystem of such agents uh that are able to you know deploy in in
real time uh you know they're these are lightweight agents so to speak right
like you're not talking about agents with like 10 trillion parameters I mean
just taking one step back I guess the fundamental difference is what you mean by infms right there's a there's a sense in
which um llms and the current deep learning networks are engaging an
inference uh I mean essentially what you're doing when you're querying one of these models is creating a conditional
probability uh distribution right so like you have you have your model and then you're saying well I have I have
this data so conditioned on this data the models output is in some sense like a big conditioning process and there's a
sense in which well because this kind of process conforms to the rules of you
know basian probability or whatever you can think of it as a form of inference all that is good um you know and I
wouldn't want to say that these systems don't engage in inference because they do in that sense like the computations that they perform uh you know respect
the laws of probability Theory B and all that therefore it's um but in the active
inference liter literature when we talk about inference what we have in mind is changing your mind in light of new
information in real time right uh which is marketly different um so on our
definition systems like you know chat GPT were engaged in inference uh during
their training and then their Deb on arrival right because that's that's the that's the point at which they're in
contact with the the world generating data right so you train these things it
takes three months it cost you $100 million 70% of which is like you know electricity bills and then it's Dead on
Arrival like that to us that's not like genuine intelligence uh I mean it's a kind of
glorified database or lookup table which again you know I don't want to knock uh these Technologies you know deep
learning is a huge Advance uh and you know just like 10 15 years ago like this
was like the absolute pioneering bleeding edge of what was going on and
I'm sure these Technologies uh you know have a future to a certain extent um but
you know it's just what you need if your aim is to do
things like you know drone control and realtime robotics like what you need is to be able to have a system that has a
perspective on the world and is able to change that perspective update its beliefs in real time based on the
information that it's generating continuously right that's really the end
goal in some sense um you're not going to get that uh with systems that like I
said take months to train then to train here means to do one passive inference where you're updating your whole model
based on your data set right um yeah so we're trying to in summary uh draw upon
you know the billions of natural R&D the the you know the universe
consists in in some sense right natural experiment um to design more efficient uh AI
systems you know there's a lot of talk about how the uh next AI Revolution
might need something like uh you know new new power sources or something we
need to develop nuclear fusion or whatever to be able to I mean it doesn't seem like many people have considered
that hey maybe these you know the the brain runs on a banana and a glass of water right like I don't need a nuclear
fusion power plant running my brain like it runs on 20 watts right so yeah if if
you need like you know if you literally need to build new power plant you're
probably doing something wrong right like and so uh but there is another approach and it is to learn from nature
and do things uh parsimoniously uh another way to think about what we're doing is that we're
moving from Big Data to I I hesitate to say smart data I guess Frugal data might
be more appropriate um one of the things that we'll be uh demonstrating actually is the vastly
improved sample efficiency of our system uh so we don't need big data um to to
train our systems uh because we deploy systems that are intelligent about how they use
data so you you seek out informative stimuli and you update your beliefs
right and that's really the key like in some sense we uh it's sort of like the scientific method extended to AI itself
Innovative Approaches to AI Development
it's like we're building little systems that have a hypothesis about the way the world is and then just need to like be
perturbed a little bit and test the hypothesis against incoming data and
that's really the loop you know I have I have some idea some belief about how the world is and then uh necessarily because
the map must be simpler than the territory I'm going to encounter some you know there's going to be like some
uh resistance there's going to be some Divergence right and then you update
your your map and when I say like this is a feature like the the map is necessary necess I'm saying this is a
feature the map is necessarily simpler than the territory right so you know you say you're you're based in the UK how
useless would a onetoone scale map of London be like imagine trying to look something
like just imagine the paper that would you would need right like so the map has to be simpler than the territory to be
useful um and so if you have a simplified map of the territory then
what you can do is use the Divergence as the signal to to then you know make
decisions decide what's going on and to yeah plan and Route yourself through
London right I I like the so there's so many interesting things there but like on that point of pointing to the sort of
immense efficiency of of humans uh the fact that they kind of you know quick inference right so it's almost there's
there's information out there already in our natural environment and it's just the ability to extract sort of the right
information at the right time um I was talking to um a researcher uh from
Michael Lev's Laban yeah and he and he we were talking about uh like you know on your point of
um maybe we'll run out of literally the ability to produce electricity and like transistors because you know the models
we need to make it just so enormous um then that is like the the bottleneck and that makes me think that the more the
more AI progresses the more it has to be almost in that podcast that I just
mentioned we we talked about we have to make computation and and AI more like
humans and we need to like try and learn from like how cells actually fire how neurons fire um because again like how
can we unlock that efficiency and like that natural ability to be parimon
and so it's like AI kind of more and more must sort of look a bit like us to
to to have um the kind of capacities that we might want them to have yeah
absolutely there's no sense Reinventing the wheel right like we want to build intelligent machines well you know every
time a baby is born an intelligent machine has been created in fact uh so you know why not
just borrow from nature right like that it seems like a very par
way to approach this um and it's probably the only sustainable way to do it frankly um like you know whenever uh
you know some new technological Revolution the slogan is we're going to need new energy sources to power this
yeah it's probably not like it's probably not a path path sustainable development right like so I couldn't
agree more yeah on this point of um sustainability of producing AI I'm
wondering what you think of so I was thinking about how in like how say um large language language models are
trained like a lot of it is by the internet but I was thinking in a way the internet is kind of just like one
enormous database but we only have one of it the thing is is a thing and so if you train on that you can train on the
whole thing as much as you can that is actually useful but once you've done that it's like what more is there to
kind of do you've kind of like you you know there are ways you can like get humans to interact with it and train it
but that's that's that's that's slow and it's you know it's not again it's as you say you know these large langu models
are doing inference but you know like they're doing again and again but then you once you actually have them um then
they're no longer doing that that inference uh so so the the training kind of is all before but you know we think
about us you know we can learn kind of instantaneously and then try new
Behavior yeah um I mean I I I agree with all that um not sure what to add I think
well I'm glad yeah I'm glad you say that that like CU um you know one thing I was
listening to um you may not know him but but Jonathan P was was talking about uh you know uh once these large language
models start like producing their own new content and things like now the internet will be filled with more of
what they have produced so it's a kind of regurgitation like we got the internet but it's only one data source
now you start producing more but it's like where does you know new real live
information about the world come from with them so exactly so what what what's going to you know the the future of AI
is IA right the future of artificial intelligence is intelligent agents right
and that that's that's ultimately you know where I think the you know the relevant data is going to come from it's
going to come from the real the real world right like ultimately the you know the the internet is sort of like history
right like you know it's it's it's a repository of all of our knowledge and everything but uh you know what what we
would want is to create systems that are able to assess situations in real time and act within them in a way that
conforms to you know our highest ethical standards our you know the general regulation that conforms to like laws
and customs and the you know uh so to create agents that have some sense of
what is contextually appropriate and then who act in contextually apprpriate ways in real time based on the data that
they generate through their actions in effect so I I agree the that sort of
speaks to like the this idea of the spatial web that we're developing so the
versus has a nonprofit sister organization called the spatial web
Foundation um and part of what we have done um as a kind of Tandem is to um is
to create a stand standardized World modeling language we are we are gifting to the
itle e um if everything goes well it should be uh publicly available this
year um so it's called hyperspace modeling language um and it is I mean
you know this is part of the general push towards an ecosystem intelligences right like so um what would you need to
create like a kind of Patchwork of you know specialized agents well one thing
that you would need is a kind of standardized set of tools to design agents in a way that you might you know
have a repository for example of different agent types that are already appropriate to act in a given kind of
setting right so the this kind of um you know the the metaverse you might think
like of as you know the virtual reality and other but there's this notion especially in the east of the physical
metaverse which is more like a blurring of the lines between physical reality
and the digital world uh where in some sense like our kind of representation of
reality in a world model becomes part of the control Loop itself right so u i
mean it's very ambitious sounding and everything but the the the hope is to
kind of move towards like doing for infrastructure um and just technology
generally what nervous systems do for organisms and their bodies right kind of
create this kind of backbone of coordination uh allowing you know uh
specialized systems to be deployed in specialized circumstances in an appropriate way um you know the brain
works like this right like so um I really like Michael Anderson's work he's
Computational Specialization & The Intelligence of Distributed Cognition
got a a great book beyond phenology where he proposes uh that essentially the the way the brain works um is that
that uh the brain brain areas are computationally specialized not functionally specialized I mean there's
very interesting he does some meta analyses it draws on very uh recent uh
you know neuroimaging work and everything to show that well you know um even areas that we think of as
functionally specialized aren't really so so one of the things he points out for example is the brokas area that
famous area that's supposedly responsible for the production of speech it's involved in more non-speech tasks s
than in speech related tasks so what that tells you is each bit of the brain is actually specialized to take like a
configuration in and to spit out a modified configuration so they're computationally specialized modules and
what the brain is doing in real time on Anderson's account which I think is very compelling account is to assemble
transient ensembles transient neural assemblies that basically on the Fly
pick out which contributions need to be brought to bear to solve the problem in in real time right so you know like
you're you're listening to someone you're going to recruit like the parts of the brain that you need to shuffle
that pattern into the the appropriate kind of pattern and then produce the appropriate response so we're basically
trying to do to AI what you know brains do in some sense to in the kind of
compositional modular structure uh and kind of just take this strategy but
right at large right to say well you know there are certain agent types that you might depl like drone agents camera
agents car agents whatever uh and then you know you can like kind of tune them
as specifically as you want to the specific context in which they're going to be uh needed and deployed ultimately
so you can think of this kind of build a brain If you I yeah yeah I really like you bringing that in that that that
brain are is a well that they kind of it's more specialized in in um ways of
of doing computation um because it kind of It kind of again points to we talking at the start about everything being a
kind of collective intelligence and the more like I was listening to Michael Evan recently talking about um like even
if you're using like you know very simple like you know agents of like literally like small code blocks the more and more agents you have up to a
point there's a there's like a critical point where the more and more you have like they almost each of them uh can
give their own like you know ideas their own perspective and so it's like if you just have enough things you know they
can search almost such space almost so you know you know human intelligence is
a lot like this U sperber and Mercier are two cognitive anthropologists that I
like a lot um and they put out a book called the Enigma of Reason which you may have heard of uh and their whole uh
argument I mean they make a bunch of very interesting contributions in that book but one of the interesting things that they point out is that we think of
confirmation bias as a kind of mistake right like it's a kind of mistaken heuristic but um provided that we have
instruments and tools to exchange reasons amongst ourselves right
confirmation bias is is the optimal search strategy it's it's much easier
especially if the brain operates like active inference suggests right where you have a belief and then there's a Divergence and you know what you're
trying to do is to in some sense change your mind as little as possible given the new
information receiving trying to be uh parimon about the way that your
information the information that you're getting is changing your beliefs well it's most efficient if everyone H is
very kind of strong minded about their beliefs and looks for evidence to the
effect they're right so long as others can say hey actually you're wrong about this and consider this evidence so they
they they propose like my side bias as a better way of understanding the phenomenon of confirmation bias which is
see I'm going to be biased towards my own beliefs but provided that we are a community and that we have like you know
the appropriate communication protocols and channels then that actually turns out to be an optimal search strategy and
yeah you can think of like collective intelligence more broadly as that you know uh the immune system is another
great example of that where you have like these cells that uh are essentially
are kind of like a register for you know okay we'll produce this kind of antigen and this kind of context and everything
um and uh yeah it's all about like you know activating the right cells and getting those populations to effectively
clone themselves in order to like generate an appropriate immune response
so you know uh what in some sense what we're trying to do is to build this out like move move from like explanatory
principles to like genuine design principles for artificially intelligent
system interesting I was going to even bring up the Enigma of reason you know that the fact that we actually should be
biased in our reasoning if because if individually we all are then collectively we're more likely to get to
to the right result um and even relatedly I was reading a paper on bacteria and how it seems that like
looking at like the species of bacteria is actually kind of irrelevant so again doesn't matter like what it is just like
in a brain reion region we actually you shouldn't split up as like where you know it's more actually like they almost fill functional roles um the different
it doesn't matter what species they are and actually in some days useful to think about you could say the kind of computations the kind of thing they're
doing in that Collective and as long as like everyone FS certain things then overall like the way I was understanding
is that even bacteria they have kind of niches and so like they almost work like a little ecosystem and they can all help
each other survive and it's just someone someone needs to fill one role and someone needs to fill the other that's
correct yeah I mean on the active inference view what you have at the end of the day is like this nesting of agent
environment relationships um so like at in some sense my body is an environment for the
organ systems that make me up right and in turn each of these organ systems is
an environment for you know the individual organs that compose it and
and so on and so on right or organs are an environment to the relevant cell types and cells are an environment of
the relevant organel and nuclei and all this stuff and so on and so forth all
the way down like you can really think of like the uh you can think of biological self-organization as a kind
of stack of environment organism relationships like you know so echoing
like ecological psychology and this kind of stuff but maybe uh maybe stretching some of the concepts to the breaking
point like I had disagreements with ecosy people uh it seems like they want
you know affordances to pick out one specific layer of the stock which is like the
organismal that of the organism I kind of feel like it might be more fruitful to just blow that up and to think of the
affordances that are available to cells the affordances that are available to organ systems and so on so you really
have like this genuinely multiscale ecological kind of approach that opens
up with active inference that I find quite exciting yeah oh fascinating um so so
we've talked about Collective intelligences um Ai and and the future so maybe another uh you know easy and
Explaining Consciousness Using the FEP
simple topic would be uh Consciousness just you know easy just you know another
another another um classic topic uh no I mean yeah it's and and I guess the reason why I want to bring that up now
especially is because you know we talked a lot about things needing to be agents um or or not that's that's kind of an
open thing you know just the way it seems is that you know maybe like again you you had a paper on active inference
kind of needs to be named inactive inference it's so much of it is about asess you say sampling the world and doing things and and so yeah know maybe
maybe one way to start is yeah how should we think of Consciousness in light of active inference and the free energy principle and and maybe even what
it says about Ai and that's a great set of questions so I think um it was uh
debated amongst us in the FP literature whether the FP really had anything
unique to say about Consciousness um I guess like at one end
of the of the question um we've proposed and when I say we it's
folks like folks like anel Seth and myself uh and our co-authors uh you know
ton luds and a few others we we proposed a few years ago this project of computational
phenomenolog um so this is a kind of um it it's it's deploying the free
energy principle and active inference um as a modeling meth methodology for a new
kind of data which is phenomenological data so like okay just roughly speaking
um the context of Discovery for you know active inference the free energy principle and so on um is a generative
modeling in neurophysiology so a generative model is a model of process
that generates the data that we're interested so originally these techniques were first developed in the
context of neurophysiology ology neuroimaging where the data that we're interested in is uh indirect or direct
measurements of brain activity usually indirect so if you're talking about fmri uh so functional magnetic resonance
imaging Works basically by uh detecting the magnetically active byproducts of
oxygen use by neurons so the neurons use oxygen when they they burn you know ATP
and all that stuff and about five to six seconds after that activity there's a temporal lag but with very high spatial
Precision you're able to say okay oxygen was used here because you got this so the the signal that you pick up is
called the Bold signal blood oxygenation level dependen and then so what you what you
use generative models for in that framework is to say okay well what is the most probable set of underlying
neurophysiological responses that would have elicited that bold signal and in that context well you have a bunch of
different models that that represent what the underlying phys physiological activity might be and you use free
energy minimization right you say well the the model that's the most probable
is the model with the least free energy so I have you know the data that I picked up and then a bunch of models saying well if if this was the activity
then you would get that data and you end up picking up the right picking the right model by picking the one with the lowest free
IMG um active inference is the same idea but now the data that I'm trying to
explain isn't data that I'm generating using a big magnet thing it's the data
that my eyes my ears my skin all of my sensory organs are uh generating and
then the model isn't a model of the underlying neurophysiological activity
that that you know caused the data that I'm picking up it's a model of me acting in the
environment right but it's the same idea right like I think I'm acting in this or that way I think I'm walking in a
straight line U on a street and then there's a Divergence and then I realize
that oh you know like I slipped and I fell or whatever right like so it's but it's the same idea like you have a
generative model a model of the process of generating my data it's just the data type is change so uh generative modeling
is agnostic to the data type that you're interested in computational phenomenology is the idea that we can
basically generate descriptions of first-person experience using phenomenological or other qualitative
first person methods and then write down a generative model of that phenomenology so kind of um you know
then there's a kind of two-step process where once you've written down a model of that phenomenology well that constrains the space of possible models
that might ex you know uh be related to the brain processes underlying
that um so that's one whole project uh it doesn't say anything about whether
Consciousness it's self conforms to the free energy principle it's just saying well um you know and maybe taking one
step back for the purposes of the audience because we've been talking about the free energy principle uh
Without Really defining it so the free energy principle is a principle of information physics and it basically
says if I exist in the physical Universe in the sense that I can be reliably
reidentified as the same thing over time by an external Observer then it'll look
as if that thing is tracking the thing things that it's coupl another way of thinking about it
is that the Fe is a is a principle of information physics applied to coupled
random dynamical systems and it says that random dynamical systems that are coupled will appear to track each other
by virtue of the fact that they're coupled but separable right so sort of like um you
know if you were talking about one thing then it would all kind of blur and diffuse you know like cream in a coffee
right um but since there talking about two separate things the best you can do is that they begin to resemble each
other you don't get like one kind of like you know uh light brown colored coffee you get like two kind of things
that couple to each other um so yeah and so the free energy principle says if you
exist in the physical Universe then you're going to look as if you infer what you're coupled to and clearly uh
you know in some sense um systems that are conscious are things
and therefore they they should be modelable using the free energy principle so then you're not making any
strong kind of commitments about what kind of thing Consciousness is and the free energy principle isn't necessarily
Illuminating like the the Deep nature of Consciousness when you're doing this it's really like okay this is a general
modeling framework and can apply to anything clearly my experience is such a thing and therefore we am I am I right
go on no no go go well just want to say am I right so then in saying that yeah the free eny principle like it's one
framework to apply to something like cognition but like inherently doesn't say anything like something has to be
cognition or whatever it's like it's about like yeah objects in the world and so it's it's about things it's you can
think about it as a a mathematical approach to thingness per se so you know and it's
been mischaracterized by by myself in the past for example as a theory of organisms and living is um it it it can
be used as the basis for such a theory but intrinsically it's even broader than
that um it's it's a theory of thingness if you're a thing in the physical
Universe in the sense that you don't just dissolve into your environment then you necessarily will conform to this
principle like it's going to look as if you're tracking what you're coupl okay um so the key construct
behind the free energy principle is this idea of a marov blanket which you may have heard of um and so yeah the marov
blanket is essentially the interface between something and what it is
not um yeah so I mean in some sense you can think of the marov blanket as all of
the degrees of freedom that couple two systems together and that separate those
systems so the the set of degrees of freedom that separate and couple two systems um so we were talking about
computational phenomenology given the marov blanket I can talk about the opposite extreme view which I think can
coexist but it's it depends on what your interest is like if you want to say something about Consciousness per se or
if you want to just you know model interesting kinds of experience in a kind of like you know neuro
phenomenology style um so the marov blanket in some sense is where all of the information that describes the
coupling between two systems lives right so if two things are coupled
everything that you need to describe that coupling by definition lives on the blanket it's where all of the classical
information that describes the coupling lives so um the uh the hypothesis that
was put forward a few years ago by Chris Fields uh Jim glazbrook and Mike Levan
um in a a grade paper I think it's called minimal physicalism or something like that uh they proposed the inner
screen hypothesis which is to say say that well um if if classical information
must live on the blanket then maybe Consciousness is related to the existence of an inner
blank or uh in other words Consciousness requires internal boundaries right um so we have this
we've elaborated this in a whole paper which is uh you know pre-printed and
currently under revision um yeah the uh the idea there is that Consciousness
corresponds to uh the existence of this kind of irreducible internal screen
where the system that you're considering is kind of partitioned in such a way that like some of the information that's
relevant to its actions lives on a kind of inner screen and um yeah you can kind of see
this as a a naturalization of the pulus maybe provocatively so I we've
been going around calling this like neoc cartisian um yeah uh we we do avoid the kind of
infinite regress because the idea there is that the inner screen does not observe itself the most it can do is
observe subordinate screens uh so you know what when when you think about like the cortical
hierarchy we usually focus on each layer and say well this layer is connected to
this layer is connected to this layer the the perspective from the free energy principle says don't focus on the layers
focus on their interface the the same structure is actually just a series of
screens between the layers and what the screens do in effect is coar grain the subordinate screen right so like you
know you have at the sensory end you have you know screens that kind of encode all of the information coming up
welling up from the sensory ends and then as you ascend the cortical hierarchy what each successive screen is
doing is basically core screening so kind of removing the ex access kind of information and saying well all of these
things are basically this and you know there there is at the top and at the
bottom two screens that are right only in some sense right the sensory end can
only push things in and at the very top it can only write down right um and
that's really the key we think to like the reflexive aspect of self-consciousness like there exists an
irreducible layer that in some sense can only in infer itself into existence it
doesn't have direct access to itself it has to infer that it exists through its effect on the other layers and
ultimately the bottom layer being the sensory motor interface itself uh its
effects on the world so yeah so there is something a bit more robust that you can say about Consciousness based on the
free energy principle it's very speculative right now like you know we're we're in the very very early days
of modeling this but we'll be uh moving moving into a more kind of experimental setting and actually like testing out
these hypotheses uh over the next few years interesting um to see if I understand it
I mean that this inner kind of is it so is it basically people kind of before
they would be like kids obviously there is a boundary by which things interact that's that's the point of the freey
principle but no one sort of thought about wait what it's going sort of on more inside of that thing doing that
that interaction um and uh and yeah it's the way it does sound a little cartisian
but it's like not necessarily or like it has to be something looking at a screen but more is it to be honest like you
know deckart is one of the most like misunderstood philosophers like ever uh
honestly I don't think I don't think you know depending on the time in history that you're considering deckart is
everyone's favorite like person to use as a foil right so uh in the 18th century de art
was uh criticized for inventing physicalism and the soulless Clockwork
Universe right uh more more recently like in the 20th century dickart uh gets
beaten up because he's the inventor of dualism and brings like the mysterious soul back into where you know so
depending on the period you know deart is accused of a bunch of stuff when he's actually like struggling with some
pretty uh core questions and you know you have folks like Merlo ponti who
everyone loves but who took deard very seriously you may know this Merlo ponti died from a stroke reading while he was
reading Leon didn't know yeah it died on his desk like reading deart which
is it's it's it's it's you know I mean but it's interesting I think jnan V has
also talked about like we kind of misunderstand dear and he had like loads of great things and I I think we should think about that a lot well I should
because it's easy to be like you know you hear other people criticizing philosophers and obviously we want make progress and it's necessary to think
about ways in which some might be wrong but like you also have to appreciate like how amazing a thinker they would be
um that's why we're talking about them and maybe think I don't think philosophy makes progress that's not how philosophy
work um so it's like it's it's in this theory of of
Consciousness then um uh I've kind of heard you talk a little bit about it before like ultimately sometimes I
wonder like it and and I'm guilty of this too we kind of maybe sensationalize Consciousness like we don't even want to
think it's something that can be understood because it's it's so interesting how could it just be reduced to to things so there's like a there's
like also a part of you which goes like I will there's no Theory Of Consciousness I'd ever accept you know
and that can be that can be problematic so but but yeah is is it an answerable question to think about like though
though even like you know things have their own inner inner like like you know um Mark of blanket as well and this
could be fundamental to Consciousness but I'm interested in like uh why do we feel
Debating the Unity of Consciousness
like we have a unified Consciousness then Andes that is there way of going about explaining that and I experience I
think that's precisely what the inner screen model large part explains right because the the basically the when if
you're considering each layer of the brain is like course graining the following there you reach a layer where
no more Co graining is possible so there is an a topmost layer
and you know it it this doesn't have to be like a pyramid right it maybe that like 80% of the brain subserves that
kind of top layer um but yeah I mean um I I would
think that this kind of the the the structure of the flow of information throughout the brain kind of imposes
this kind of centrifugal sorry centripetal kind of
but um on the flip side though I think uh one of the great lessons um of you
know say psychoanalysis and the uh the phenomenology that is closer to
psychoanalysis so like I'm thinking of recur and people like that I think it was Merlo ponti who said you can
recapture all of the core Freudian insights by abandoning the intuition Consciousness is at all times
unified and you know when I think about my own Consciousness like I'm a little bit ADHD brain and U like I I don't feel
like my consciousness is Unified into one flow all the time certainly may
that's my own pathology but uh yeah I think it's a kind of it's a very um it's
probably not the most fruitful way to think about Consciousness is like continuously
unified um I mean the the self might be something like that but then I would
recommend looking at the work of St Anil Seth um to kind of get some insight into
why the the self might be a stable thing although I think given the given the
time that we have remaining that's probably too big a yeah I even Point people to John vei and and some of his
colleagues had a series called The elusive eye which is like even if yeah even if you know even like K young
talked about like there's an an ego which is a bit Elusive and only one part of of a bigger self but there is a way
in which like through narratives through over time through our connections with others there is there are these things
which B all the different parts together and um un like a final thing is that um you
talk about sometimes you don't feel like you're necessarily unified and and you know Frey def like you know would say
there are different parts of us and there's some great work by people like Damien kely Stevens talking about like
um the the multifractality of think sometimes things bind together and there are like there are these flow these flow
like nature to to our movements where like we we suddenly have these like uh
critical moments of coordination and everything comes together but but there are also like at all times you could say
like small brain processes small small movements like going in other directions and and that's how and we can sometimes
stop them but then sometimes we let them happen and so there is a a kind of flow in nature where um we are letting as
we've been talking about you could say smaller subsystems smaller computational levels that are allowed to do their own
thing see different possibilities see different and even you know embodied more active possibilities and and and
then there are sometimes with FR Francisco Vela in his work no I don't
think I don't think so verela has this uh this great little collection on
ethics um actually uh where he talks about like micro selves so like the self is basically
like a pasti of micro selves that are like appropriate to certain context um
yeah and again I think we overemphasize the degree to which we're like integrated and uh you know unified that
might be like a kind of Hangover from Enlightenment philosophy um you know like a kind of
it's basically a through Line running from deart to Hegel effectively this kind of unified self idea um I think uh
you know the the Freudian Revolution slash you know the cognitive Revolution
kind of undermine that premise really significantly um you know it's a and
which brings us back I think appropriately to the beginning right like intelligence is collective
intelligence uh and you know I think even even if our our sense of self is is
Unified and one that doesn't mean that that unification and Oneness doesn't emerge from a kind of you know Patchwork
or meshwork of you know different selves interacting um so all of these things
can be true we can have our cake and eat it too with thank you um this has been great so
where can people find your work and do you have anything more you want to say um well uh you can follow our
developments at versus. a um I'm um I'm
quite active on X Twitter um which is where I think we met um so yeah that's I
I basically post everything there um and yeah we will'll be regularly posting our
updates um like I said on versus uh. I there's a whole R&D subsection I'd
recommend following our blog we uh regular well more increasingly regularly
uh we'll be putting out um yeah short pieces uh kind of explaining to an
informed play audience what we're doing um and you'll yeah that that's probably
the easiest way to keep track of what we're doing um let me just Express gratitude uh for the invitation this has
been a really fun conv ation and yeah um hope you have a great one yeah