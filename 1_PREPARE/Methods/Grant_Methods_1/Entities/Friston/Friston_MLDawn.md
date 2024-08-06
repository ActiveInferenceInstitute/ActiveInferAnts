https://www.youtube.com/watch?v=XohuuIi7Jt8
Active inference explained with Prof. Karl Friston
00:00 A brief introduction of Prof. Friston
00:51 What is the Free-Energy Principle?
09:13 Model evidence optimization (can brain OVERFIT?!) and how BRAIN selects the actions with minimum expected surprise!
28:23 The double-descent phenomenon in over-parametrized models (Including our brain) and WHY these models DO NOT overfit?
40:37 Active Inference vs. Perceptual Inference and how to they work together for US to LEARN!
52:10 The difference between Active Inference and Reinforcement Learning
01:08:32 How 'Abstract Knowledge' generation (Creativity) in brain can be explained?
01:19:45 The ARCHITECTURE of your Nervous System describes the ENVIRONMENT you are living in!
01:31:48 Will we ever FULLY understand how the brain works and how far have we come?
01:35:00 The Goodbye
Hello everyone and welcome to ML Dawn. So today we are having an interview with Professor Karl Friston. Professor Friston is a theoretical neuroscientist and a world-renowned authority on brain imaging. He has invented statistical parametric mapping or SPM, which is a software package designed for the analysis of brain imaging data sequences and also I think his main contribution to theoretical neurobiology is the free energy principle for action and perception that hopefully we'll get the time to also explore. Professor Friston, thank you so much for being with us today.
My pleasure.
Okay, so let's just get started. The free energy principle, right? What is the Free-Energy Principle? Could you just tell us about what the free energy principle is and how has it enriched our understanding of the brain as a unifying brain theory if you will?
Right, so I normally respond to that question by asking whether you want the sort of the high road or the low road approach to understanding what the free energy principle is about. I'll very briefly try to surmise both. So the low road, which is like a sort of bottom-up way of understanding it, which is a kind of way that I think a lot of neuroscientists and psychologists would understand things or more broadly people in neurobiology would be the denouement at the present time of very old and compelling ideas about the brain as literally a fantastic organ, an organ that constructs hypotheses explanations fantasies that afford the best explanation for all the sensory impressions all the sensory data that we have to assimilate and literally make sense of. So the principles that underwrite that perspective were articulated in various disciplines by people like Kant and Helmholtz, Richard Gregory, Nancy Spy synthesis, perception as hypothesis making, leveraged to greater effect in machine learning with people like Jeffrey Hinton and Peter Dayan, and the notion of the Helmholtz machine in turn borrowing technical ideas from the physics and engineering literature such as Feynman's free energy principle as a way of writing down a prescription or a normative account of this kind of sense making. And you end up with a formal first principle account of sense making which you can write down as a computer program or you can write down mathematically but essentially casts the brain as in the service of trying to minimize its variational free energy and you can read variation free energy here essentially as a kind of prediction error. Technically the free energy gradients are prediction errors, so what's the prediction? Well, it's just the difference between what given your beliefs about the current state of affairs out there beyond the skull-bound brain what would I expect to see, what would I predict and then I compare my predictions with what I'm actually sensing and that constitutes a prediction error and then I use the prediction error to drive my beliefs in a way that eliminates that prediction as I got a sufficient account of what's going on and that's often referred to as predictive processing in its inactive form or active inference and when we're drilling down just on the perceptual synthesis that is afforded by this account. The most popular scheme that I would be predictive coding sort of the reciprocal exchange of top-down predictions from the inside out to the parts of the brain dealing with sensory processing that is complemented by an ascending outside in flow of prediction errors where you need the predictions to form the prediction errors and then the predictions or the expectations they that are generating those predictions are informed and updated by the prediction errors technically that's a process called Bayesian belief updating hence the Bayesian brain and the Helmholtz machine formulations of it. So that would be an account of the free energy principle really as a prescription, an algorithm, a technological account of a normative theory for the brain as an active organ making sense of data with the key twist that of course the brain or you and I are in charge of the data that we're trying to make sense of. There's an added inactivist twist here it's not just that we're good Bayesian filters or data assimilators we actively have to decide what kind of data we want to base our inferences upon, literally in terms of where I was where I'm going to look next how I visually palpate the world or you know which news channels to listen to or which Wikipedia page I'm going to forage next. That you know so that that's possibly more of a difficult problem the brain has to solve than just simply making sense of the data but both are bound up in this sort of generic account in terms of free energy minimization or the explaining away and accounting for providing the best explanation that eliminates united's prediction errors. Very briefly the high road is the kind of approach that a physicist would take and you can derive exactly the same mechanics of belief updating the same sort of explanation for sentient behavior where behavior is important because that's the active part just from an analysis of things that exist in in the sense of physics and the particular physics here is the physics of non-equilibrium steady state systems that have the remarkable property of returning to states that they were once in. You know mathematically have attracting sets or characteristic states of being that you know I am found at this temperature in this kind of location and this sort of environment so all the things that would characterize me represent states that I keep on revisiting and that can be written down mathematically in terms of the dynamical systems theory of attracting sets and you can work out the probability distributions or you can appeal to Feynman's work on path integral formulations to work out well if things exist then what properties what dynamics must they have been must they possess in order to exist and to maintain themselves in within these viable states of being. So in the life sciences this would be known as autophagy or self-creation in the computational chemistry of the self-assembly how do molecules assemble themselves and retain their sort of morphology and structural or configurational organization and it turns out that you end up with exactly the same equations that you're trying to you know everything that we do either on the inside or in terms of acting upon the world is in the service of minimizing this variational proxy for prediction error but also mathematically happens to be the quantity that as statisticians would try to optimize namely the marginal likelihood or the evidence for models of the world. So you get this sort of technological account that systems that self-organize look as if they're trying to maximize the evidence for their models of the world sometimes people reflect that as self-evidencing. So that would be a philosophical account of the top-down physicists explanation for the way that you and I actively organize our exchanges with the lived world in order to in order to exist to maintain our existence, some generalized homeostasis that can be described mathematically as a minimization of variation free energy.
Okay, very very interesting. So as far as I understand, so we are it's about as you said we're trying to sort of do actions that would maximize the probability of our existence of our model that we have from the environment that we're living in, which is I think the same thing that you refer to as marginal likelihood, yes the probability of observation given the model that I currently have of the world. What I'm trying to understand is trying to marry that idea with the other idea that the brain selects which kind of which one of these inputs to consider like how to affect the environment because when we say the probability of my input from my receptors given the model I have from the environment it is as if I have a control of what I will necessarily do because I mean there are so many receptions coming I might choose to ignore some of them but then it might not be the right choice also when you talk about optimization I realize that now from if I look at this from a machine learning perspective since we're optimizing could we overfit and fail to generalize?
Okay, well that's a great question. They're about um so first of all just yeah I am sorry I will use technical terms with very little theory of mind because I'm so used to doing so. So you're absolutely right the marginal likelihood is nothing magical it's just the probability that these sensory data would be solicited experienced under my model of how those data were generated. You're absolutely right the marginal bit comes from marginalizing out over or averaging over the unknown parameters of a generative model but we don't need to worry about that. You know the model evidence is the marginal likelihood and the logarithm of that is is a negative free energy. But your more interesting question I mean if you now review well you know this podcast and just listen to the words you use they're very telling. So you talk about selection that's a great word to use you also said I you know so immediately there's a there's an inactive a generational aspect to your question. So a predictive coding scheme that's just assimilating data and making sense of data has no notion of of me has no selfhood and certainly doesn't have any it is not equipped with the ability to choose and to select which data it wants to actually assimilate or to classify or to categorize. So we're going beyond machine learning now we are going beyond simply passively in a sort of outside in way making sense of data we are now asking about this really deep question how on earth do we select the data to assimilate. So the answer is very simple in the same spirit that everything on the inside that's doing this assimilation has to minimize the prediction error sometimes cast in terms of surprise in a technical sense. So this is if you're an information theoretician this will be the self-information. If you're doing that then the natural question then arises well look what happens if I'm in control of the data that I can now select or turn towards well now I have to choose the actions that will produce data that are have the minimum expected surprise or the minimum expected prediction error. So if surprise which is another word for a mathematical expression for this bound on surprise or evidence called variation free energy is the thing in the moment then after I have acted in the future then what I want to do is to minimize my expected surprise my expected prediction error. So what's that? Well expected surprise is technically entropy and more anthropomorphically this would be just uncertainty. So what you're doing is if you're subscribing to the free energy principle and you now have to choose the best kind of act or sampling or selection then you would select those actions that minimize your uncertainty the resolve your uncertainty. Another way of expressing that mathematically is that they have the greatest information gain that those kinds of data resolve my uncertainty more than those kinds of data. So that's a actually a well-known Bayesian principle and it's often cast in terms of optimal Bayesian design and has been known since the 1950s through the work of people like Lindley. There are well-defined objective functions which are simply how much do I shrink my uncertainty and technically measured in terms of a divergence mathematically but you know we just need to know the information gain is just the degree to which I shrink my uncertainty about states of affairs out there. So what that means is that we are if we minimize if we choose those actions or we want to minimize our free energy then we have to choose those actions and minimize the expected free energy which necessarily makes us into curious creatures. Now you were saying to me I don't know how to do that I don't understand how to that you do you're a scientist even if you don't have a PhD every child and every student and every adult is a curious scientist they want to know how their world works either it's your scientific field of study or if you're a little baby it's just how your body works you know what kind of thing is mum is mum your same kind of thing as me all of this information has to be carefully selected in order to resolve uncertainty about this hypothesis on that hypothesis in exactly the same way that you would design a good experiment. So when you design an experiment then you design the experiment to yield data that are going to be maximally informative in relation to your null versus altered hypothesis so it's exactly the same principle governs the selection of natural experiments that we deploy with our eyes looking over there or looking over there it's exactly the same mathematics as the same imperatives and indeed you actually see the same information theoretic constructs emerging in the visual search literature in the neurosciences and you can construe these as salience maps that you know they score the uncertainty reduction the epistemic affordance of making that select selecting those data by by looking over there or by again looking at this Wikipedia page or listening to this news channel and not that fake news channel. So it's a great question because not only does it does it make the I think the really profound point that that curiosity of all kinds is baked in to the first principal account of self-organization that anything that exists must impart be acting or appear to act look as if it is acting to resolve uncertainty about the exchanges with its economic environment its culture or the visual scene the visual scene at hand. Furthermore you're talking about action it's you that's acting so it's it there's an implicit sense of of agency that is owned by the artifact in question so we're now talking about something that would be necessary to equip an agent with some a very elemental selfhood. The third thing it brings to the table is is really common sensical but it's it's a I think a very interesting observation and that in order to select this action over that action then I have to have a model of the consequences of my action but the consequences live in the future which says that your genetic models now must cover the future which means that you've got something that a lot of things in this universe don't have which is a model of the future it has temporal depth. So you know that you could apply the free energy principle to a thermostat you could apply it to a virus and it would work perfectly well you could simulate thermostats and make a thermostat or simulate a virus or possibly even construct one but these kind the genitive models that you would use that has to be in place in order to work out the surprise due to the predictions generated by that model would not have the temporal depth of the models that you and I have. So as soon as you talk about selection you're talking about essentially selecting a plan of action a course of action and that means necessarily rolling out into the future so your genitive models have this temporal depth and furthermore as soon as you entertain the notion that I could do this or that then there is an act of selection in play the thermostat doesn't have that there's only one thing it can do because it acts in the moment but you and I are very have a much more a deeper generative model we bring to the table that allows it now to set amongst a series of counter factual courses of action you can choose what to say next or not to say anything at all and in that choice there is an act of Bayesian technically an act of Bayesian model selection or policy selection. So now you've got thermostats that select provided they have these deep charity models that sort of free you from the moment because they're really about trajectories and paths you know how we navigate the lived world and the about the overfitting thing oh yes could we overfit yes actually why don't we over fit maybe that's the right question.
Hello everyone and welcome to ML Dawn. So today we are having an interview with Professor Karl Friston. Professor Friston is a theoretical neuroscientist and a world-renowned authority on brain imaging. He has invented statistical parametric mapping or SPM, which is a software package designed for the analysis of brain imaging data sequences and also I think his main contribution to theoretical neurobiology is the free energy principle for action and perception that hopefully we'll get the time to also explore. Professor Friston, thank you so much for being with us today.
My pleasure.
Okay, so let's just get started. The free energy principle, right? What is the Free-Energy Principle? Could you just tell us about what the free energy principle is and how has it enriched our understanding of the brain as a unifying brain theory if you will?

hello everyone and welcome to ml dawn so today we are having an interview with
professor carl frisson uh professor furson is a theoretical neuroscientist
and a world-renowned authority on brain imaging he has invented statistical parametric
mapping or spm which is a software package designed for the analysis of brain imaging data sequences and also
i think his main contribution uh to theoretical neurobiology is the free energy principle for action and
perception that hopefully we'll get the time to also explore professor frison thank you so much for
for being with us with us today my pleasure um okay
um so let's just get started the free energy principle right
What is the Free-Energy Principle?
um could you just tell us about what the free energy principle is and
how has it enriched our understanding of the brain as a unifying brain theory if
you will right so i normally respond to that question
by asking whether you want the sort of the high road or the low road approach to um
understanding what the free energy principle is about um i'll very briefly try to surmise both so
the low road uh which is like a sort of bottom-up way of understanding it which is a kind of way that i think
a lot of um neuroscientists and psychologists would understand things or more broadly
people in neurobiology would be the denouement
at the present time of very old and compelling ideas about the brain as
literally a fantastic organ a an organ that constructs hypotheses explanations
fantasies that afford the best explanation for all the sensory impressions all the sensory data that we
have to assimilate and literally make sense of um so the principles that underwrite that
perspective were articulated in various disciplines by people like kant and helmholtz
department richard gregory nancy spy synthesis um perception as hypothesis making
leverage to greater effect in machine learning with people like uh jeffrey hinton and peter diane
and the notion of the helmholtzmann sea machine in turn borrowing technical ideas from the
physics and engineering literature such as feynman's free energy principle as a way of
writing down a prescription or a normative account of this kind of
sense making and you end up with a a formal first principle account of
sense making which you can write down as a computer program or you can write down mathematically but essentially
casts the brain as in the service of trying to minimize its
variational free energy and you can read variation free energy here essentially as a kind of prediction error
technically the free energy gradients are prediction errorism so what's the prediction well it's just the difference
between what given your beliefs about the current state of affairs out there
beyond the skull-bound brain what would i expect to see
what would i predict and then i compare my predictions with what i'm actually sensing and that
constitutes a prediction error and then i use the prediction error to drive my beliefs
in a way that eliminates that prediction as i got a sufficient account of what's going on and that's often referred to as
predictive processing in its inactive form or active inference and when we're drilling down just on the
perceptual synthesis that is of you know afforded by this account um the most
popular scheme that i would be predictive coding sort of the reciprocal exchange of top-down
predictions from the inside out to the parts of the brain dealing with sensory processing
that is complemented by a an ascending outside in flow of prediction errors
where you need the predictions to form the prediction errors and then the predictions or the expectations
they that are generating those predictions um um are informed and updated by the
prediction errors technically that's a process called base in belief updating hence the bayesian brain and the
helmholtz machine formulations of it so that would be an account of the free energy principle
really as a prescription um an algorithm
a technological account of a normative theory for the brain as an active organ
making sense of data with the key twist that of course the brain or you and i
are in charge of the data that we're trying to make sense of there's an added inactivist twist here it's not just that
we're good bayesian filters or data assimilators we actively have to decide what kind of
data we want to base our inferences upon um
literally in terms of where i was where i'm going to look next how i visually palpate the world or you know which news
channels to listen to or which wikipedia page i'm going to forage next that you know so that that's possibly more
um more of a difficult problem the brain has to solve than just simply making sense of the data but both are bound up
in this um in this sort of generic account in terms of free energy minimization or the
explaining away and accounting for providing the best explanation that eliminates uh united's prediction errors
very briefly the high road is the kind of uh approach
um that a physicist would uh take and you can derive exactly the same
mechanics of belief updating the same sort of [Music] explanation for sentient behavior where
behavior is important because that's the active part uh just from an analysis of
things that exist in in the sense of physics and the particular physics here
is the physics of non uh non-equilibrium steady state system systems that have
the the the remarkable property of returning to states that they were
once in you know mathematically have attracting sets or characteristic states of being that you know i
am found at this temperature in this kind of location and this sort of environment
so all the things that would characterize me represent states that i keep on revisiting and that can be written down
mathematically in terms of the dynamical systems theory of attracting sets and you can work out the
probability distributions or you can appeal to fireman's work on path integral formulations um to work out well if
things exist then what properties what dynamics must they have been must they possess in
order to exist and to maintain themselves in within these
viable states of being so in the life sciences this would be known as autophagus or self-creation in the
computational chemistry of the self-assembly how do molecules assemble themselves and retain their sort of
morphology and structural or configurational um organization
and it turns out that you end up with exactly the same equations that you're trying to you know everything that we do
either on the inside or in terms of acting upon the world is in the service of minimizing this
variational proxy for prediction error
but also mathematically happens to be the quantity that
as statisticians would try to optimize namely the marginal likelihood or the
evidence for models of the world so you get this sort of um
technological account um that systems that self-organize
look as if they're trying to maximize the evidence for their models of the
world sometimes people reflect that as self-evidencing so that would be a philosophical account of the top-down
physicists explanation for the way that you and i actively organize our
exchanges with the lived world in order to in order to exist to maintain our existence um some generalized
homeostasis that can be described mathematically as a minimization of um variation free
energy okay uh very very interesting so as far as i understand uh
Model evidence optimization (can brain OVERFIT?!) and how BRAIN selects the actions with minimum expected surprise!
so we are it's about as you said we're trying to
sort of do actions that would maximize the probability of our existence of our model that we have from the the
the environment that we're living in um so which is i think the same thing that uh that you refer to as marginal
likelihood yes the probability of uh observation given the model that i currently have
um of the of the world um what i'm trying to understand is trying to
marry that idea with the with the other idea that the brain selects
which kind of which one of these inputs to consider like how to affect the environment because when we say the
probability of my input from my receptors given the model i have
from from the environment it is as if i have a control of
what i will necessarily do because i mean there are so many receptions coming i might choose to ignore some of
them but then it might not be the right choice also when you talk about optimization i
realize that now from if i look at this from a machine learning perspective
since we're optimizing could we overfit i mean
and fail to generalize okay well that's a great questions they're about they're about
um so first of all just yeah i am sorry i will use technical um
terms with with very little theory of mind because i'm so used to to doing so so
you're absolutely right the marginal likelihood is nothing magical it's just the probability that um these sensory
data would be solicited experienced um under my model of how those data were
generated you're absolutely right the marginal bit comes from um marginalizing out over or averaging
over the unknown parameters of a generative model but we don't need to worry about that you know the model evidence is the marginal likelihood
and the logarithm of that is is a negative free energy um [Music] but your more interesting question i
mean if you now um review well you know this this podcast
um and just listen to the words you use they're very telling so you talk about selection that's a great word to use you
also said i you know so immediately there's a there's a an inactive a generational
aspect to your question so a predictive coding scheme that's just assimilating data and making sense of data has no
notion of of me has no selfhood and certainly doesn't have any it is not
equipped with the ability to choose and to select which data it wants to actually assimilate or to classify or to
categorize so we're going beyond machine learning now we are going beyond um
simply passively um in a sort of um outside in way making
sense of data we are now asking about this really deep question how on earth do we select the data to assimilate
so the answer is very simple um in the same spirit that um
everything on the inside that's doing this assimilation has to minimize the
prediction error sometimes cast in terms of surprise in a technical sense so this
this is if you're an information theoretician this will be the self-information um
the if you're doing that then the natural question then arises well look what
happens if i'm in control of the data that i can i can now select or turn towards
well now i have to choose the actions that will produce
data that are have the minimum expected surprise or the minimum expected prediction error
so if surprise which is another word for a mathematical
uh expression for this um bound on surprise or evidence called variation free energy
um is the thing in the moment then after i
have have acted in the future then what i want to do is to minimize my
expected surprise my expected prediction error so what's that well expected surprise is
technically entropy um and more anthropomorphically uh this
would be just uncertainty so what you're doing is if you're subscribing to the free energy principle
and you now have to choose the best kind of act or sampling or selection um
then you would select those actions that
minimize your uncertainty the resolve your uncertainty another way of expressing that mathematically is that they have the
greatest information gain that those kinds of data resolve my
uncertainty more than those kinds of data so that's a actually
a well-known bayesian principle um and it's um
often cast in terms of optimal bayesian design and has been known um
since the 1950s through the work of people like lindley there are well-defined objective functions
which are simply how much do i shrink my uncertainty and technically measured in terms of a divergence mathematically but
you know we just need to know the information gain is just the degree to which i i shrink my uncertainty about
states of affairs out there so what that means is that we are if we minimize if we choose those
actions or we want to minimize our free energy then we have to choose those actions and minimize the expected free
energy which necessarily makes us into curious creatures now you were saying to me i don't know
how to do that i don't understand how to that you do you're a scientist even if you don't have a phd
every every child and every student and every every adult is a curious scientist they want to know
how their world works either it's your scientific field of study or if you're a little baby it's
just how your body works you know what kind of thing is mum is mum your same kind of thing as me all of
this information um has to be carefully selected in order to resolve uncertainty
about this hypothesis on that hypothesis in exactly the same way that you would design a good experiment so the when you
design an experiment then you design the experiment to yield
data that are going to be maximally informative in relation to your null versus altered
hypothesis so it's exactly the same principle governs the selection of
natural experiments that we deploy with our eyes looking over there or looking over there it's exactly the same
mathematics as the same imperatives and indeed um you actually see the same
information theoretic constructs emerging in the visual search literature in the neurosciences and you can
construe these as salience maps that you know they score the
uncertainty reduction the epistemic affordance of making that select
selecting those data by by looking over there or by again looking at this wikipedia page or listening to this news
channel and not that fake news channel so it's a great question because not only
does it um does it make the i think the really profound point that that curiosity
of all kinds is baked in to the first principal account of self-organization
that anything that exists must impart be acting or appear to act look as if it is
acting to resolve uncertainty about the exchanges with its economic environment
its culture or the visual scene the visual scene at hand furthermore
you're talking about action it's you that's acting so it's it there's an implicit sense of
of agency that is owned by the artifact in question so we're now talking about
something that would be necessary to equip an agent with some a very elemental selfhood
the third thing it brings to the table is is really common sensical but it's it's a i think a very interesting
observation and that in order to select this action over that action
then i have to have a model of the consequences of my action
but the consequences live in the future which says that your genetic models
now must cover the future which means that you've got something that a lot of things in this universe
don't have which is a model of the future it has temporal depth
so you know that you could apply the free energy principle to a thermostat you could apply it to a virus and it
would work perfectly well you could simulate thermostats and make a thermostat or simulate a virus
or possibly even construct one but these kind the genitive models that you would use
that has to be in place in order to work out the surprise due to the predictions
generated by that model um would not have the temporal depth of the
models that you and i have so as soon as you talk about selection you're talking about essentially
selecting a plan of action a course of action and that means necessarily rolling out into
the future so your genitive models have this temporal depth and furthermore
as soon as you entertain the notion that i could do this or that then there is an
act of selection in play the thermostat doesn't have that there's only one thing it can do because it acts in the moment
but you and i are very have a much more uh a deeper generative model we bring to the table that allows it now to set
amongst a series of counter factual courses of action you can choose what to say next
or not to say anything at all and in that choice there is an act of
bayesian technically an act of bayesian model selection or policy selection so now you've got thermostats that
select provided they have these deep charity models that sort of free you from the moment because they're really
about trajectories and paths you know how we navigate the lived world
and the about the overfitting thing oh yes could we overfit yes
actually why don't we over fit maybe that's the right question that's a good question uh yeah that was the fourth
clever part of your question but yeah the reason you don't ever fit in uh and
i'll probably um if you indulge me i'll answer this from the point of view of sort of machine learning um
or statistics so um the answer here um lies in an understanding of the nature
of models and their evidence so the first thing to say is that there
is no true model of the world there is no there is a best model in the world and that's simply the model that has the
greatest evidence but there's no true model in the world there are you know they're all there are many many ways of
explaining um um how some data for us sensory data um was
generated and you know providing an account of that all we can do is find
the one that has the greatest evidence the greatest marginal likelihood the greatest probability of the data under
that model so we can change the model and until the model provides or account
gives you the greatest marginal likelihood so what is evidence this is the key
point evidence is accuracy minus complexity
which means that to find the model with the greatest evidence is to provide an account of these data
in the simplest way possible and that simplicity underwrites the ability to generalize in the absence of
that complexity part of the model evidence you would certainly overfit
so if you did if you were allowed to use as many degrees of freedom um as you
wanted with no constraints on that i know complexity constraints you would certainly overfit these data so that the
next day's data would uh not be extendable because you'd ex you'd fit all the little random
effects and fluctuations in the in the data at hand so that complexity term is
absolutely crucial in ensuring that maximizing model evidence
surprise minimizing free energy all of these are statements essentially the same thing
goes hand in hand with an automatic penalty on the complexity
that precludes overfitting and it's really interesting just to sort of unpack what complexity is here so um on
a um on a technical account the complexity is
basically the degree to which i change my mind having seen some data so
technically it's the difference between some posterior bayesian beliefs some probability just a
probabilistic explanation for some causes of some data in machine
learning this might be called some the latent states generating unobservable latent states hidden states
that are generating observable measurements or observations or sensory sensory input from our perspective
um so i've got two beliefs before we were talking about
this process of dynamically reducing free energy or minimizing prediction error as a process of belief updating
that belief updating is literally updating a prior belief before i see data into a posterior belief after i've
seen a posteriori after i've seen the data and the degree to which you have to move your belief from the prior to the
posterior is a complexity so it's the degrees of freedom that you're using up
in explaining the data now if you've got really good prior beliefs
you don't have to change your mind very much and therefore you can provide an accurate account of this data with a
minimal complexity cost because you've moved your belief updating has been extremely efficient and minimally
complex so it is those kinds of high evidence generative models
that have this complexity penalty in place that are able to generalize to new
data because you've got the right kind of priors so it all goes hand in hand and it's a
really important point you know i don't know i i'm wondering whether you knew this already in virtue of the fact you
asked the question but you know this this this issue is really um
uh you know a difficult issue uh in conventional machine learning
because you know if you just look at the way the field has gone in machine learning they've gone to sort of big data you know sort of you know
committing to the the ideology of you know big data science
with massively over parameterized neural networks so if you read a neural network as a generative model certainly in the
context save an auto encoder then what you're starting with is an overly parameterized overly
complex genitive model which can beautifully explain any given data set
but it's hopeless in generalizing to another context or or some new data simply because the complexity is too
high because there are too many parameters in that model that's only say connection weights in a in a current
neural network or a convolutional neural network variation auto encoder so
what that leads to then is um all sorts of problems with sharp minima
that ensue because you have not put in the the
complexity term um that you can think of in terms of just occam's principle you know so occurs principle has to get into
the objective function so if you've got so the game now it would be to take a
neural network in machine learning say in deep learning and try and find out which collection weights or which you
know what architectural aspects of your your network you didn't need to provide an accurate account which is actually
the opposite direction of travel from most of deep learning at the moment which are aspiring to more parameters
with bigger computers there's an interesting little twist there of course that um there are a
number of um fundamental principles such as landauer's principle the
jarzinski equality which effectively say that information is
energy and energy is information and in this present context the degree of belief updating as scored by the
complexity cost has a thermodynamic cost which means if you're
recognizing things properly and selecting the right things to do properly with the minimum of complexity
you're doing it with the greatest efficiency so you can measure the quality of any artifact
any neural network or neuronal network simply by the amount of energy it has to
expend to exist so again you're the drive towards high performance computing is exactly in the
wrong direction what you're looking for is sort of um sentient edge computing like devices
based upon a an evidence maximization or free energy minimization approach that should do it
um like your brain which would consume the same energy as a light bulb as opposed to a power station so that's
a really good question this you know you know that has some really pragmatic engineering um computer engineering and
uh sort of you know um energetics uh associated with it and
explains to a great extent why you're so much better than any neural network that
lives on a a high performance computer at the moment
The double-descent phenomenon in over-parametrized models (Including our brain) and WHY these models DO NOT overfit?
the idea of overfitting and over parameterized models just reminded me of this paper by
professor mikhail belkin um so
it's it's a it's a paper about this phenomenon that happens in over parameterized
models called the double descend as they've called it now their question was why over
parameterized models don't overfit and does why why why they can do why
they can generalize so well and it's an it's a very interesting paper it was
really shocking to me because we have this famous uh i mean in machine learning we have this famous u-shaped
sort of uh you know plot that shows that okay the more you parameterize your
model the the um well the error in the the error
in your in the predictions of your model keeps going down and down and down and after a certain point it fails to
generalize so it just keeps going high and higher and higher and higher now what they did was they didn't stop there
they kept all adding more parameters they kept adding more and more now what happened then was
after a certain point uh we have a double the a second descend
in the generalization ability or in the error let's say the prediction
error it again keeps going down and down and down in some cases
it goes even below the point where the the minimum of the first
descent it could it could even get to better generalization and in some cases
no it the minimum that it could ever reach would not be as good as the
minimum of the first descent so they've called this double descend and i i'm trying to
and didn't happen oh the devil doesn't always happened based on their experience they used it with decision
trees they used it with neural networks and a couple more models i don't
remember exactly what they were but um the id the notion of accuracy minus
complexity and that being the idea of that being the reason as to why
uh we don't overfit i'm trying to uh sort of mix like to have that next to
the idea of because their their argument was that when you have too much too many number parameters
the model sort of goes towards like you have you have more knobs to control your
search in the hypothesis space you you inevitably go to
you as if you can you can you can search better and then you find
maybe i think they were arguing that you find simpler solutions i think if i'm not mistaken
but how would you marry that idea with the idea with this
accuracy minus complexity being the reason of not overfitting
um right yeah that's a very question that one okay
so um i think if you think of this um the problem in terms of um
finding minima in an objective function landscape
then that that phenomena of double descent makes entire sense in the context of
escaping local minima so let's assume that we've basically got um a difficult
problem say a brittle dynamical system or a highly non-linear problem
where the objective function let's assume it's
either um a free energy objective function or some
approximation to it um then it's likely going to have lots of local minima
around and your one instance and one particularly problematic aspect um you know
probably your your your you have in mind is this notion of sharp minimum other minima that have very steep sides that
are very difficult to escape from with any sort of stochastic annealing or any sort of um device that would sort of
bring you out of that base of attraction of that sharp minimum so
the first point to make before i pursue that analogy and really basically just reiterate the solution that you you've
actually just just described which is absolutely correct i mean i'll i'll do it you know from from
a dynamical perspective um the first point to make is that the failure to
put the complexity term into the objective functions used by typically by
lots of vanilla machine learning not all i mean high-end uh um variation auto
encoders use exactly the variation free energy um or which is um in machine
learning known as an evidence lower bound or an elbow that is exactly the same um objective function we're talking about
um but those um those algorithms that don't do that and just
try to maximize the likelihood as opposed to the marginal likelihood so you know just try
to maximize the accuracy such as scored by the sum of squared residuals for example so they're
forgetting about the complexity and they're just drawing down the accuracy part of it to create these kirin is
sharp minima the reason that these mineral are sharp is that the complexity term
creates it into a u-shaped minimum and this is if you like one expression occurs principle that the good the good
the good explanations have to allow for some latitude um so
the curvature of the minima scores the
the latitude you have in the sense that you're not committing to a very particular explanation that
provides an accurate account of these data there are a number ways of understanding this one of them is in fact from the
point of view of uh james's maximum entry principle that under constraints afforded by say a likelihood and
surprise on a generative model the best explanation is always the
belief that has the maximum entropy which is means it has the minimum
curvature in some free energy landscape so the free energy functional
provides an objective function where all the minima are flat thereby eluding the
sharp minimum problems that plagues most conventional machine learning so i think that's the first
thing to recognize that you will find those free energy minima
um more efficiently provided you can escape the local minima simply because
the free energy minima are always flat and then they're less likely to trap you
um so let's now take what what are what other ways uh could you
escape sharp minima um that are local minima that are high in a free energy landscape
so just so one sort of picture i use for my students is is very much like a mountain
range um that is the genesis of a little stream that turns into a river so the
lower you get in the landscape the wider the rivers the shallower the valleys until ultimately you get to an estuary and so
exactly the same sort of if you like um landscape exists in a free energy
operational free energy concept context so stuff high up uh you know all the sharp minima that have a very
undesirable high free energy um are the rust stuff in the higher mountains and
your job is to get down uh flow down to the nice shallow
um global minima that are much that have this um this sort of maximum entropy
occurs principle um shallowness to them with no curvature so how might you want to get out of
those high hanging valleys those those sharp minima
well you you've said it basically if you imagine from the point of view of
dynamical systems theory flows on a um on a manifold or a um in
this instance a free energy landscape let's imagine we just got one parameter to play with so and we've
found ourselves in a v-shaped minima
and we can't get out of it but if i add another dimension and now make my one-dimensional
um objective function two-dimensional then i can change that fixed-point
attractor that corresponds to the point of the minimum the local minimum in question into a subtle point into an
unstable fixed point and i can escape from it so now i've got a saddle point where there are now roots away from that
local minimum because as you keep on adding dimensions i.e adding parameters
to your model the opportunities for converting a stable fixed point which is a local minima into an unstable fixed
point from which you can escape increases geometrically only supremely
so i think that's the explanation in conversation with people in machine learning uh and i enjoyed one such
conversation with people um at nyu just a couple of weeks ago i
i think that that is is probably the story that you would tell to account for this sort of throwing lots and lots of
parameters um at a model just to destroy stable fixed points that
constitute a local minima so that you can access the global minima and then once you've done that you then prune
away all the parameters that you use as your escape routes to get back to the simple model so what we're talking about
i think this double dissenting is a really lovely notion and it does remind me a little bit of
how the brain works in the sense that you know it starts off with an overly parametrized um genitive model so babies
and children actually have more connections they have more w's um more
um external connections white matter tracts than uh than adolescent something you
and i do so you get this progressive pruning as you grow older so you start
off with this overly parameterized overly complex virgin
tablaraza where you can escape all the local minima and then as time goes on
you then do your pruning and reduce the number of parameters or collection uh connection weights in your
in your model to to simplify to to uh in accord with james's max venture
principle outcomes principle uh from the point of view the free energy minimization it's the complexity part of the minimization so you now get a
smaller parameter model but you've only done the second wave of descent if you like after you've escaped
all the local minima by having an overly parameterized model so i'm sure that that's you know
this must be a universal principle that i suspect is so universal it has been
discovered by evolution uh you know millions of years ago yeah yeah
that was that was amazing wow that was a totally different perspective that the
the i mean the reduction in the number of parameters as you grow old i i i
never thought about that first of all i didn't know that but it was it was really amazing yeah well it has its
penalties because i am much older than you and therefore i am much sparser and wiser than you but i could not adapt to
a new world so i can't go bungee jumping or go to disco oh my god
wow wow wow mind boggling i i don't know what to say
that was that was really enlightening actually um so it seems to me that uh there are
Active Inferencs vs. Perceptual Inference and how to they work together for US to LEARN!
two methods of learning in general when it comes to biological systems so i did a little bit of research on
this i don't know whether i'm right or or not but i could narrow this down to two general
methods one is perceptual inference where and the other one is through
action inference now the perceptual inference i i suppose is when you
generate a model from the world and you keep updating that the parameters
whereas the action one is you actually choose actions um so i know we've discussed this
a little bit at the beginning of the interview but could you explain these two methods in more detail and
uh and compare them as to it in what situation
am i learning through perceptual inference and in what situation do i
choose to learn through action inference
right yeah it does i think speak to this issue of sort of um machines with agency that we were
talking about before artifacts that have sentient behavior so the sentient part would be the sexual inference and the
behavior would be the active inference and i think that they you know once you
think about sort of artifacts that do actively exchange with the world i think they both have to go hand in hand so um
i you know i think it's although another excellent question i will
qualify my answer after i've given you the vanilla answer which is you know these
are this is just a joint optimization process over two kinds of unknowns two
kinds of latent states out there that generate data one kind of latent state is the latent
states over which i have no control so this would be the standard data simulation classification problem
recognition problem i am given some data and i have to classify learn its causal
structure infer the particular state generating latent state generating these data in this particular context so that
would be perceptual synthesis perceptual inference and learning the parameters
of that gender model i would call perceptual learning so in my world i
distinguish between fast processes that infer time dependent states
and slow processes that infer the parameters that underlie the
contingencies and the laws um we would be learning in the machine learning center so that the w is in a neural
network but the states of the network at any one point in time i would interpret as imprints um you know this is the
activity of these nodes and therefore i'm seeing this kind of face so that's one set of unknowns but
there's another hugely important set of unknowns latent states out there those
which i can control those which i have some agency over so
if i make this movement or i secrete this or i switch on this knob then the
states out there will also change if that's the case then you're now conditioning a certain set of hidden
states on latent states which can be thought of as plans or control variables so the you
know sort of uh standard machine learning treatment
so these control variables or uh say in cultural theory
now play a really important role because the transitions the dynamics amongst the latent states um that are controllable
are now conditioned upon this u but this u is another random variable this means i have to infer two sets of
random variables i have to infer the latent states over which i have no
control and i also have to infer the the
control variables if you like the plans um upon which the variables the states
that i do have control over are conditioned so there's two kinds of inference here which you can think of in
terms of the distinction between someone just applying a kalman filter to
estimate the states of some plant versus um estimating the best thing to do if you you were doing applying
control theory and you know when you're controlling a particular plant say in engineering
but because we're now committed to understanding everything in terms of optimizing
a free energy functional of beliefs or probability distributions that now becomes that that planning or control
theoretical part of the problem the active influence part of the problem now becomes planning as inference
so you know in a sense you can read the two perceptual and active sides of
imprints as really the same process working hand in hand in parallel
but acknowledging there are two different kinds of variables that you you you have to infer you have to work
out basically what's the state of affairs out there and what am i doing about it
and then of course you can see now that the active infant side the um the
planning as inference now has to consider a number of plausible plans and then we get back to selecting the um the
most likely plan which minimizes the expected free energy or results which is uncertainty or avoid surprising outcomes
like you know um your your machine crashing if you're in an autonomous driving uh
situation so you can write in uh all your prior preferences into that um
expected free energy in the future conditioned upon the plan
so i would i would say that that term uh that sort of you know there is no choice
to do active inference means that you have to infer both the latent states of the world and the way that you're
intervening and uh on those states through controlling state transitions that just means planning as imprints
that's part and parcel of active influence and just being and
being um existing in a world that you're continually sampling and it's
continually generating data for you to make sense of there's you know there's a circular causality there
the the the the sort of the twist here um the qualification
is that i think you're absolutely right that in fact we do switch between that active and perceptual inference in
reality so if i was building an artifact i probably wouldn't worry about what i'm about to
say but if i want to describe you and me i would describe you and me
as basically machines that are built to um in a saltatory way in an intermittent
way alternatively plan an action and execute it
and then gather some data and then make perceptual inferences or you know
do the perceptual learning side of things so i mean this in the sense that um the way that we the temporal
scheduling and the alternation between the action and the the perception of the active inference
and the perceptual inference the way that it seems to be scheduled and organized in biological artifacts
like like ourselves is that every 250 milliseconds about four times a second
we act and within those
actions we do our perceptual synthesis so this you'll see this yo
for example every 250 milliseconds about four times a second you will move your eyes with
cyclic eye movements so you're you're getting little snapshots every 250 milliseconds at four hertz
um and during the acquisition during the action you actually switch off your
sensory channels it's called sarcanic suppression if you're an engineer you're basically turning the kalman gain down to zero
when you're doing the action bit so you don't see the optical flow
induced by your eye movements you just don't see that what you see is the thing that you've actually fixated on and you
you uh you use that to construct a scene you assimilate you build you build up your
this illusion that the you know there's a visual c down there but in fact in reality that in little snapshots from
here and here at about four hertz the way that you speak if you think about or just listen to me and the way
that you you hear things um well that's not quite the truth certainly the way that you um you
fulfill your proprioceptive predictions during speech all my phonemes are roughly 200 milliseconds long so i'm
just producing a second you know a discrete sequence of little packages of phonemes every 250 milliseconds
if i was a mouse i would sample sample my world by whisking my whiskers
and the frequency of that is 250 milliseconds or four hertz and if you
now look at the belief updating um on the inside which would correspond to
the perceptual inference making sense of the data sampled by my whisking around my burrow
and you see again this profound theta rhythm that dominates the active exploration of the environment
that within it is nested all the fast perceptual belief updating usually at
what's called a gamma frequency about 40 hertz so you've got this lovely separation of time skills where we make
a move on the world at your four times a second we get some data and then we quickly process what
that means when we've reached a conclusion then we go off and get the next bit of data and then we process this
so for artifacts like you and me um there is actually i think a temporal
separation of the active part and the the perceptual part
part of inference so i'm waiting to see until they build that into robots because i think you can very realistic
um behaviors and the way that people respond to things and you know orientate to things or understand things through
this sort of discretization or quantity quantization of discrete packets of
information that live within say you know a few hundred milliseconds and you
know and that dictates the type of scheduling of at least biological uh belief updating
wow unbelievable that was amazing so it it feels like
there is no parallelization there is actually very fast switching between the two um
like a joint optimization yes
just require you know if i was building a computer i wouldn't do that it's just that obviously there's a better way of
doing it an evolution has found that this sort of uh this fast switching is the best way to do it in the to explain
the kinds of worlds in which we live in we are where biological motion has certain time constants were you know
meteorological events or things around us changing a certain time scale it's clearly the most efficient way uh you
know according to evolution anyway oh basically oh yeah absolutely wow that was amazing so uh so
The difference between Active Inference and Reinforcement Learning
we we keep we kept talking about active inference and of all the actions that i
could choose i'm choosing the one that on average would maximize or say minimize surprise in future or minimize
free energy i'm trying to think as to so first of
all it it requires i suppose i don't know whether the word is my wording is right or wrong but
some sort of a knowledge about the future as you said it requires look into the future
um i can't help but notice that there is a similarity between
active inference and reinforcement learning however in reinforcement learning what
we do is we have the ultimate we like we have an end goal and end state and we
just let the machine do whatever it's it wants to do round like exploration exploitation whatever
it wants to do many many many times so eventually it has a way to back
propagate the expected reward to the current state but
a human being that say it's experiencing something for the first time
and wants to choose the action i i don't it doesn't have that that that
option right so first of all how would you differentiate
between active inference and reinforcement learning and second of all
um [Music] let's let's just discuss as i forgot the the second question uh let's just
discuss the first the difference between active inference and uh reinforcement learning yeah i relieve because that's a
very big question but feel free to prepare the next one
while we're well we're dealing with okay perfect so um there are a number of ways of
answering that question and the simplest way of course this is to look at what is on the tin when you pick up
active inference versus reinforcement learning one's about inference and one is about learning
so active inference has an influence and learning which has the
important consequence that you have um beliefs not just about the um states of
the world but also beliefs about the parameters of your genetic model so it comes equipped with beliefs about the
w's in say a neural network reinforcement learning is just about
learning the parameters you could look at reinforcement learning um as a
mechanism to enable machines to learn to infer and in
part i think that's how people often um understand inference in the context of machine learning and strictly speaking
the optimization process is applied to the weights the parameters of a generative model the contingencies so
there's um there's one fundamental difference between reinforcement learning and
active inference in the context of belief updating i don't think that's quite the spirit of
your question though so i think another way of looking at the difference between active inference and reinforcement learning
is just in terms of the tediology and asking what is it that you want to
optimize so reinforcement learning you assume the existence of a reward function or loss function a cost
function a value function and then you optimize your neural network or your
your artifact um to um respond to any given um either explicit state or
inferred state with a particular action the and that action is chosen by the nationality principle to maximize the
expected reward so that presupposes existence of a a
value function um and if that exists then by the optimality principle you can
then events a an optimal state action policy
is that um is it can that be um if you like
framed in terms of active imprints the answer is yes but as a very very special case
so what is that special case well it's a special case where you can reduce
um the um the function that is implicit in active inference
which is a functional of belief so remember your planning as inference
belief updating in terms of perceptual inference and and data assimilation evidence accumulation
and all that good stuff kalman filtering and the action selection via planning as
inference this is inference so the objective function is a functional function of a function or a functional
and that function is a belief so the objective function in active inference is uh belief based
so under what conditions could you actually reduce an active inference
formulation of a problem to a bell to the kind of problem the optimality principle would apply was when you
shrink your belief down to have zero uncertainty so if you take uncertainty off the table
then you can get back to a effectively a um the
the situations in which you can apply the bell but optimality principle interestingly just for your
entertainment the way that you do that technically is just by describing your reward as a log prior
probability of some outcome that you prefer so we often call it a prior preference so we say
that every outcome um is equipped with a reward or a loss function so instead of
having two separate channels sensory information and reinforcement information we simplify the problem and
say no every output every observation or sensory input comes labeled
with a rewarding aspect so your reward function now becomes very high dimensional and
continuous and it's just basically the long probability of a priori
me something that outcome and once you write that down and you take away uncertainty um then you can
apply the beveled optionality principle so you can look at reinforcement learning as a special case of active
inference when there's no uncertainty the problem with doing that though is if there's no uncertainty that means
that the curiosity part of the objective the expected free energy
is zero which means you've lost the opportunity now to simulate artificial curiosity and
exactly the kind of sentient behavior that we were talking about half an hour ago
because there is no information to be gained there is no information seeking at hand because you know everything why
do you know everything well because my in my model of the world in my reinforcement learning model of the world there is no uncertainty i know
everything i can see all the hidden states or at least i can infer them um
so the the the the what you lose by converting a an objective function which
is a function of beliefs which is you know the variational free energy or the marginal
likelihood or the model evidence all of these are usually logarithms of or kl divergences or free energy functionals
of probability distributions beliefs if you now try to you know coerce that
into a function of states as opposed to beliefs about states you take away all
the epistemics you preclude any proper discussion or treatment or account of
artificial curiosity in your robotics this would be intrinsic motivation so um
you know the the the intrinsic value the value of information the epistemic value
of making that move what would happen if i did that has its own if you like epistemic reward
but that part of the reward function also more explicitly not part of the expected free energy uh or the expected
evidence or the expected uh surprise and that part has um
has been removed when you dispense with or you you you try to cast the um
the problem um in terms of the bellman optimality principle just a little technical interesting technical twist
here um when you um when you consider the full
problem where you're dealing with um functionals or probability distributions
for us bayesian beliefs um you are technically dealing with um
usually path integrals because you as we've spoken about before you know our paths go into the future and so the plan
has has a trajectory or a path into the future so now you've got a path integral
of a functional of a log basically a long probability which is an energy so you've got a path interval of
an energy which is called an action and you're trying to minimize expected free energy which is this
this action so all you're saying is that i can explain sentient behavior
with hamilton's principle of least action so now you're replacing the bellman optimality principle
which applies to value functions of states with hamilton's principle of least action
which um deals with if you like value functionals
or belief states or beliefs about about states so that's for me how i would see
that there's a fundamental difference between reinforcement learning and active inference but it's not a
difference that should be overly celebrated in the sense you can get from one to the other you can repair that
dialectic if you like as long as you're prepared to take all the reduceable uncertainty out of the game
or off the off the table does that is that a kind of yeah
yeah yeah um i'm trying to understand one bit of this um so when you say that in reinforcement
learning we actually know there's certainty in reinforcement learning sometimes we're not aware of the world i mean like
many things could happen that could like you know put obstacles on
on the path of our agent that could happen but then the agent somehow learns
to you know get out of them um i i don't get the idea of
not having uncertainty and reinforcement learning i didn't get that part to say that there
is no uncertainty in reinforcement learning would be disingenuous and
and i i think profit possibly for me most easily understood in terms of
reinforcement learning um being one application of
bayes optimality in the context of optimal basic decision making with a loss function so it's really it was
really the nature of the loss function i was talking about what i was trying to get across was that um bayesian decision
theoretic approaches don't have as part of the loss function
any reduction of of uncertainty so you have to build that in by hand so that
novelty bonuses or exploration bonuses and things uh so you have to apply all sorts of widgets or little tricks to to
make your own your your loss function even treated under uncertainty you know in a basic decision
theoretic context or say a partially observed market decision process you have to actually write in what you
get for free if you start with an expected free energy or unexpected um marginal likelihood um
so it's it's a kind of uncertainty that matters in terms of what i believe i was
talking about so you know it's it's a difference between um uh you
know a neural network that's trying to be on target uh for as
much time as it can in a noisy uncertain situation for example
and a neural network that knows it doesn't know certain things that would enable it to find out
what what what particular times it should be from the target or from what particular direction because there are certain
unknowns out there that it can actually resolve with particular epistemic moves
that have this intrinsic value of this intrinsic motivation um that give it this curious aspect so
it contextualizes the optimal bayesian decision theory exactly by adding in the optimal basic
design principle we're talking about before which is this which is this sort of uh information
seeking aspect so the the full picture from my perspective of the perspective of the free energy principle
is that that you would you can decompose the objective function expected free energy
into two parts literally linearly um into into you know an epistemic part
and as a reward or pragmatic part and that's the epistemic part that disappears when you
go straight for optimizing the reward function or the uh or the
your prime beliefs there's an interesting intermediate case um which you can get out just by
rearranging certain terms in the um in the excited free energy functional which
is um kl control so this would be like risk sensitive control
so so i'm not sure whether you put this under reinforcement learning or not um
so i'd have to ask you but so from my point of view this is a an interesting middle ground
where you've now included um uncertainty about the consequences of my
action into the game so instead of now just trying to maximize the expected utility
of the expected loss function on the expected reward under some belief about the consequences of action i'm now um
going to minimize the kl divergence or the difference between what i think will happen the outcomes
that i under my posterior predicted density technically but more intuitively what i
think the outcomes will be if i take this plan or this course of action and then i have this
set of preferences you know that encode my preferred outcomes and then i just choose the action that minimizes the kl
divergence between the two so this has uncertainty um in it um that is not
quite the full info uncertainty reduction but it certainly accommodates a degree of uncertainty um
when it comes to real world applications uh again um i'm thinking about sort of
engineering applications in control theory where this will be known as kl cultural and economics it's called risk
sensitive control so that would be like a finessed reinforcement learning value
maximizing scheme that has gotten uncertainty banked into it and you know
that's an interesting um uh halfway house between the sort of
vanilla expected utility which i'm reading as a reinforcement learning process possibly unfairly um
and the full um the full size of active inference um expected free energy it's a
really great game if you have time in terms of just writing down the you know the probability distributions and then and
just rearranging them to different kinds of divergences and just trying to read them as if you're an economist or you're
a an engineer control theoretician or or you're a behavioral psychologist reinforcement learning or your neuro
roboticist developmental neuro roboticist trying to understand intrinsic motivation but by switching
them around you can get all sorts of interesting different perspectives on this
overall um you know expected surprise minimization uh like objective function
i see oh that was really amazing so we talked about perceptual inference and
How 'Abstract Knowledge' generation (Creativity) in brain can be explained?
active inference now both of those ideas highly rely on the environment one is
modeling the environment and the other one chooses actions that would you know
maximize the the probability of my existence
now both of them rely on the environment but what about when we come up with some abstract knowledge that never existed
before like the first time that someone thought about the wright brothers thought about
an airplane or the first time some someone thought about a mermaid
um so anytime that something if that's even possible i don't know the first time that something jumps into one's
mind that never has existed in the environment and they they try to make it into like
create it into reality can we explain that part the
knowledge generation with with these two ideas uh active inference or perceptual inference
yeah again another very challenging question um i i would contend that you can so i think you're touching now upon
sort of the links between the mechanisms of um um the underwrite
model optimization and to say curiosity but more i think the notions of
creativity and exploring different model spaces so we're now moving
in fact actually completely away from active inference and perceptual inference in terms of um
optimizing both the states and parameters of a generative model as it is exposed to data and now turning
to a third level of optimization which would be the optimization of the model in and of itself
so in various fields this will be known as structural learning for example in medical and uh constructivism the
problem of not they're saying forget about let's assume we've got the perfect scheme if you give me a neural network
or a generative model and a particular environment that can
generate data i can do all the good inference uh or learning to infer um
actively and all the canada's inference and so we've got this little agent now um coupled exchanging with their or her
environment um in in in a base optional way
now we move to a next level hierarchy speaking of an
optimization or free energy minimizing process which is now not applied to the parameters of the model but to the model
itself how many hidden layers how many connections do you use rectified linear
or sigmoid trans you know how do you carve things up in terms of not just hierarchical levels but in terms of
know factorizing or modulating modules or clinician dependencies at any level all sorts of fundamental structural
issues that you would practically have to deal with and contend with when writing down
the architecture of your neural network that you know will read as as the structural form of your
genetic model so this structure learning problem and from the point of view of a statistician
is a bayesian model selection problem and it's basically integrating the marginal likelihood over all the kinds
of data that you could see or all the kinds of data that you have seen and then you choose the model
that best accounts for that has the greatest evidence so now this is a categorical active
selection of selecting the best model and i use those words because this is
mathematically i think an apt description of natural selection so
natural selection and evolution is just nature's way of doing bayesian model selections is selecting
the hypothesis namely the phenotype um where evolution thinks that this
particular hypothesis is a good fit to me the clinician that i am supplying um
and therefore the econis then selects the phenotype through this process of the structural
form of the epigenetically specified for example um structure of the gelatin
model um and as soon as you think of it like that then then um there's a big question
and the big question is well how do you explore the model space because we've just said when you're
doing this bayesian model selection after you've acquired the data so now what kinds of model spaces would
you would you explore and is it necessary to explore there is an
argument which we actually touched upon earlier on that we can actually start off with a completely over parameterized model and prune it so this is a kind of
basic model selection technically called basic model reduction where you just literally if i remove
this parameter of this connection from this model or this hidden layer from this model
would i have um would i increase its the pathogram of its uh of its evidence
um in other words um would i be would i be minimizing complexity without
sacrificing too much accuracy with the kinds of data that this model is
is fitted to explain so you know you could argue that
both the model expansion typically dealt with in amazing context through
non-parametric bays so by having expandable models and priors of the way
that you would add in different parts or chunks so for example in a hierarchical dirichlet process you
might have some sort of stick breaking process on top of that which says you know can i
am i is it justified to bringing the new hidden later variable or you know sort
of uh in my uh dirichlet distribution uh and you'd ask that
question by basically um evaluating the evidence for that model or the
variational free energy um with or without that extra bit and if it improves by adding complexity which more
than pays its way in terms of the accuracy then you keep it if not you wouldn't but you you know what the what
the stick breaking process brings to the table is is a principled way of expanding or growing the model
i repeat in the context of non-parametric basing approaches but i think you can also you can also sorry i
think that both model expansion um and i'm reading that at the moment in
terms of um non-parametric base um or from the point of view of natural
selection um having recombinations of certain sort of codes um or
parameterizations of of um you know of of genitive models that you can think
of in terms of split emerge like operations that you get in genetic recombination ways of exploring a model space in a
principled structured way or and the basal model reduction i think both can be seen um
as the processes that give rise to creativity and insight and aha moments
um so um i'm i'm saying that are using some of the notion of aha moments and
creativity um in um deliberately just to make the point that some
creative acts are actually acts of reduction it's not so much the fact that no one's ever seen this before um sorry
no one has ever represented or um had this um
you know this um object in mind before it's just that no
one's seen that connection before and that it's actually a simpler way of viewing things so if you just think about the
most creative ideas and signs they are not actually
more complicated de novo constructs they are simplifications that make sense of
lots of other things in fact they are instances of the free energy principle itself providing a simple account
of uh but accurate accounting of everything so it's really the the simplification
and the reduction the increase in the evidence when you suddenly see the two things that you separately represented
in say two parts on your network can actually be represented by the same thing and you do that by removing it to the
model so actually many apps of creation uh certainly in sort of minimalist art forms um are actually getting to the
bare essentials of what's going on again in um you know in compliance with occam's principle and you know um
you know um advertising the complexity cost of explanations from for the lived world
that that seems to me you know an important bucket of creative acts is
actually just seeing the structure underneath it's simply the simplicity explaining everything with just one
canonical platonic like um dynamic or construct or narrative or or
sort of factorization however you want you want to um however you want to um
articulate it and in that sense the first person to have that simple insight
that oh it's just one of those this is just one of those the first person is really the genius and the creative
person but they haven't created anything new they've just seen something simpler uh i see um
and in a sense you know that's i think that's the scientific process that's exactly why we're having this conversation that's what you do with
your world so what i do with my life and i guarantee what you do with your life it's this journey of finding the
simplest explanation for everything that we that we experience uh and you know
leaving it as a legacy you know speaking to the uncultured aspects of uh or um
that one could uh appeal to to answer your question uh for the next the you know my children or my students or
whatever so you know that's i think the most that's one way of looking at creativity
the an interesting point that ensues from that is that um you know it is perfectly possible
to be the first art sentient artifact to see that simplicity
um that is actually in the real world so it's not the question really of making
new things that aren't out there they've probably already been out there it's just you're the first person to have uh
to be able to infer them in that simple kind kind of way
the other point to make here of course is well is it really out there well probably not this is your simplest
explanation it comes back there is no true model it says this is the best explanation for what's going on so you
may be the first person to find this simple explanation um for what's going on so i would put most of um most of art
and creativity in that in that bracket but then you compress me on music for example and and
you know why is why is music so attractive and well that would be another question maybe okay yeah
questions yeah perfect um so that was amazing actually professor i
The ARCHITECTURE of your Nervous System describes the ENVIRONMENT you are living in!
was watching one of your talks actually it was 3 a.m as i was watching that and you said something that i mean my mom
was sitting next to me and you said something that it was so interesting that i i it was like i got a nervous
tick or something then my mom asked me what happened i said he said something amazing and i just
want to share that with you and just maybe we could dig a little bit deeper in this
um you said something along the line if i'm if i'm putting this correctly that
the way our biological neural network forms itself tells us something about the environment
that we're living in in other words show me your nervous system then i'll tell you about
the environment you're living in and it's fascinating to me because maybe
um a couple months months earlier i was discussing this this gap between artificial neural networks and
biological neural networks and i was asking my friends that these distances like why these axons are long or why not
or these dandruff we never sort of
create those structural uh foundations into our artificial neural network it seems like
very simplified version of those what do the what do those features entail really
and when i heard the piece that you just said in in that in that talk it was just amazing
now impres and you mentioned the idea of action in the distance and how light you know reflects into our eyes
and at that how that's how we have long neural you know connections in our like
reflection of action the distance now in practice
if we actually see like actually in in a literal meaning if we actually see a ner
the nervous system of an of a biological being how much can we really say about the
environment like is it really possible to to say okay probably it has these rules it has gravity it has whatever is
it really possible yes that was a lovely story
more interesting than my answer yes yes i think it is you know you've just convinced your listeners it is possible
um have you given some of my favorite examples but i'll give you a couple more just to reinforce the point you're
making uh i think the first thing there's a couple of things before i um get into this uh
you know you were noting that the architectures that um have emerged in neural network theory and machine
learning and naturally deep learning have a very simple architecture that is
if you like that is inherited from neural networks and that's a good thing so remember
simplicity is good and inheriting from neural networks if you want your machines to deal with the kinds of
things that human beings deal with those are two good things they may be a bit too simple but i think there are certain
architectural features that you can actually spot which actually would allow you to apply your law that you've just
suggested give me a neural network and i'll give you the world that that neural network is fit to explain or act for um
that law is um another law um
from ross ashby we mentioned the law of requisite variety before the context of natural selection um but he um with
colleagues also formulated the good regulated theorem so i'm not sure whether whether you're probably too
young you're far too young to remember this this is this is um was taught as one of the fundaments of
the inception of cybernetics you know in the early 19th 20th century so the
law the good regulator theorem which you can you can wiki there's a wiki little wiki page or basically what it's saying
is that if any artifact and from from ashby's perspective this would be something called a homeostat which has
all this sort of you know regulatory uh aspects to it that we talked about it if it regulates its environment basically
it does the right kind of active inference and controls the latent states out there the
right kind of way to survive then it must be a good model of that
environment so he was uh and he purportedly or thought that he could prove that and i thought you know i i've
read the paper way where he proves it it's not an easy read but if you have a
3am in the morning with nothing else to do you should try and read it it's original fruits let's see see if you're convinced um
but the key point is that this is a very old idea um and probably you know a very
true idea that anything that um exists um
in some kind of generalized synchrony with its economics environment its heat
bath its world it's uh um climate
uh must effectively be a um be a good model of that climate which
simply means that the architecture the structure that we're referring to in terms of structure learning
must in its function in its structural form recapitulate the causal structure of what's out there so the structure of
the generative model um will tell you an enormous amount about the you're the kind of world that is generating the
sensations that are being used to do the planning as inference to control that
particular world so lots of great examples you've given one well i think one of the most interesting
ones which is why is the brain why does it have an architecture that
involves long thin communications at a distance i mean the liver doesn't and the liver does a wonderful job of doing its job
and presumably complies with the free energy principle and doing its own kind of active imprints in a world of
chemicals and metabolites so you you you've given you've given
the viewers the answer it's just that that must imply a certain kind of conditional dependency
that has this long-range action at a distance and of course we unlike um thermostats
and worms and viruses really have to live in a world where there is actually a distance in the sense that i can hear
you from dublin i can see you from across the room now viruses worms and
thermostats can't do that they are they their world is is you know is much more
immediate and just relies upon the conditional dependencies that are related to the juxtaposition in
symmetric space but we live in a much more complicated world that has this action at a distance that that actually
is necessary to explain the kind of sensations that we that we have to explain particularly sort of vision and
and audition conveyed by waves of one sort or or another or another sort
um so i think that's a wonderful example but you can go even further and sort of
course the grain you know you just look at the brain and it's and it has two hemispheres that tells me immediately
that the embodied world of this particular brain has a bipedal symmetry
yeah so you know if the world includes the body then i can tell you almost immediately
that the kind of creature you dissected this brain from um the part of the world which is most
important to that to that particular brain or neural network maybe in the body that embodies it's it can move
around has a bilateral symmetry will probably have two arms and two legs
and all that good stuff if on the other hand he gave me the brain of an octopus i'll be able to tell you immediately because they have a brain for each arm
it has an eightfold symmetry so i can tell you a lot about the the world and in
in you know in this instance the you know the bodily world uh from just the gross
morphometry but you can go much much further uh i could look at your brain and i will find two streams that emanate
from the visual parts of the brain and i will know that they're visual parts because your eyes are my central
nervous system and i know that they're they're photoreceptors so i will know that they're somehow um trying to
explain the causes of sensations um um in a
visual scene and i will find two streams called the dorsal and the ventral stream
that sort of run eventually in this direction and also also in this direction actually uh towards the
hippocampus more eventually here and that tells me immediately that
there's been a factorization there's been some sort of a fundamental carving nature at its joints in terms of the
causal architecture of this creature's world and in particular what i will be
able to discern is you must believe that certainly that there are
the objects have at least two attributes um in order to um
produce their impressions of the nervous system in the words of the helmholtz and of course those will be what and where
and i'll be able to tell you that you the typically the kind of visual objects that you're trying to
explain um will have these two attributes that are conditionally independent because of the
physical separation and the um the sparse connectivity between these two streams um so
what we're saying just in common sense terms basically means for the typical visual objects that we usually look at
knowing what something is doesn't tell you where it is and and me telling you where something is
doesn't tell you what it is so it is the most efficient simplest minimum complexity representation just to
represent the wholeness and awareness and then you put them together to explain this thing in this in this
location another nice example of minimizing the complexity by using the
minimum degrees of freedom when carving up the world uh you know in terms of
being a good model of that world but you see exactly the same kind of um
if you like factorization and effectively weight sharing in convolutional neural networks which
brings me back to you know don't don't be dismissive of your cnn your favorite cnn it's got some
beautiful factorization uh in it so the very fact that you've got this
weight sharing and this sort of way of carving nature at its joints um in the context
of what you see emerging convolution your networks is that you are now saying that there is some causal structure out
there that has local continuity or contiguity aspects that i'm going to
leverage to provide a really simple explanation for these kinds of data so as soon as you tell me i'm using a cnn i
know exactly what kind of data you're using you're using stuff that has certain regularities in the metric space
spatially extensive uh so image-like data if you give me another kind of
neural network that looks like a transformer network i know you're not doing that i know that now you're trying to deal with things mapping one
set of categorical uh objects onto another set of categorical objects so just by looking at the structural form
of even i think um sort of canonical architectures in deep learning um you
can tell a lot about the causal dependencies the independent the conditional independences that generated
the kind of data that you're trying to classify or um auto encode
i see professor this has been amazing so the final question the last question
um that is going to be a very non-technical i i hope like like a simple and nice question for to
end this talk a light question um that i'm sure many people watching uh
would be interested to know your opinion about will we ever
Will we ever FULLY understand how the brain works and how far have we come?
fully understand how the brain works and how far have we come at the moment
right a simple or is it a [Laughter]
long a long difficult one i i appreciate your attempt to ask a light a light fun
[Laughter]
and i think we've come an enormous way and there is there is an enormous way to go
and i think there are some principled issues about the understandability of ourselves that actually get into some
deep questions about consciousness and metacognition and the kind of creatures we are and of course the kind of curious
creatures we are and have to be in order to exist um so i'm thinking here of um
things like david chalmer's meta problem or met a heart problem so now in
philosophy the question has moved from away from what is it like to be or to see red
really why do we spend all our time puzzling about the fact that we can see red or experience things and of
course that speaks to this hierarchical model or genitive model where parts of this
genetic model now have a construct of meanness and meanness in particular experiential
contexts um hence the metacognitive aspects when you think about very deep character models so i'm sorry what does
what do you mean by meanness oh
so you have something which you could argue um many um
lower forms of life possibly not dogs and cats but sort of possibly birds don't have
you have a part of your genitive model is a hypothesis or a fantasy that you are a person and that you are in charge
of orchestrating your perceptual influence in your deep genitive models and moving and secreting
now you don't need to have that hypothesis or explanation in order to
function quite viably it's quite a sophisticated being like a bird for example but you have that which suddenly
creates the opportunity to think about counter factual ways of me being so when
i said mean us i just meant me in inverted commas less
yeah oh beingness sorry okay okay i i okay okay yeah yeah yeah yeah yeah sorry
sorry yeah yeah just your question will we ever be able to understand ourselves i think um
it's a lovely question in the sense that the answer to that may um hold the
secret um uh to um awareness and particular self-awareness mean awareness
selfhood and what particular kinds of generative models you would have to have in order
to even ask the question um am i yourself and then the philosopher's
question can i understand myself these are really really very very literally
deep problems that rest about deep hierarchical gender models i see perfect
The Goodbye
uh thank you so much professor fristen it was indeed an honor to have this uh talk with you i really enjoyed it i hope
that i didn't try uh tire you out too much it i know it it took a long time he did and i'm
exhausted but thrilled to have spoken to you i really enjoyed talking to you thank you so much thank you so much professor and i'm truly truly sorry for
taking too much because taking too much of your time because it's like one interesting argument brought another one
and then it brought another one and i apologize for that but it was a priceless experience for me well thank
you very much you could have gone on all night but now i i'm worried about all your editing
well that's your problem not mine i gotta have it exactly exactly thank you so much have a lovely evening thank you
so much bye