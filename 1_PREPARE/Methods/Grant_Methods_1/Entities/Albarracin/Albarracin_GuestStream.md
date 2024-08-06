ActInf GuestStream #017.1 ~ Mahault Albarracin "Epistemic Communities under Active Inference" https://www.youtube.com/watch?v=aEYQCmFl1Bw

Hello, it is March 9th, 2022. We're here in ActInf Lab guest stream number 17.1 with Mahault Albarracin. Mahault is a product director at Game Addict, a researcher at Versus Computational Phenomenology Lab, and finishing a PhD in cognitive computing at UQ. We'll have a fun discussion today. Feel free to write any questions in the chat during the presentation, and we'll have a great time learning. So thanks a lot for joining this guest stream and really looking forward to what you have to share. Yeah, thanks for having me. I'm really glad to be able to present this paper. We've submitted it and we're in the process of reviewing it, so it's a really exciting paper that I'm hoping we can get out soon. Today I'm going to try to go through a lot of big concepts and how they apply in Active Inference, and then I'm going to try to explain the nitty-gritty of a generative model, how to make a simulation, and then what are the takeaways and limitations. I'm going to try to keep this quick. If you have any questions, feel free to ask them and I'll take anything as it goes.

Confirmation bias and conformity
Let's begin with the main concept here, which is confirmation bias and conformity. This was the starting point of our research. We were thinking with my co-authors, which are Connor Hines and Daphne Demakas and Maxwell Ramstead, we were trying to think through what leads people to see the world in such a way that they have a hard time then reconciling their view of the world with other people. And so it went back to the practice of exchanging ideas, sharing concepts and values between different minds, which is a fundamental process. It really allows humans and other living agents to coordinate and basically operate socially by sharing ideas. Individuals and communities can really pursue their pragmatic goals. So basically, you know, get food is one of the permanent goals you might want to optimize for. They improve their understanding of the world, and then we notice that humans are compulsory co-operators. Human individuals survive based on the predication that they have access and they can leverage the bodies of accumulated cultural knowledge. Over the course of evolutionary history, humans have developed an exquisitely sensitive capacity to discriminate between reliable sources of information from unreliable ones, which seems counterintuitive in the age that we're at, but you have to understand how far we've come before we got to the arms race towards misinformation. So the epistemic process, as I just said, it's really not without flaws. Humans are not computing machines, they're not perfect. They mostly use heuristics. They process information by reasoning to limit the consumption of energy and facilitate rapid decision making. That's the basis of survival.

Confirmation bias
For example, confirmation bias implies that all other things being equal, individuals who prefer sticking to their own beliefs over changing their minds, it's easier for them to potentially change their model less than if they had to really all the time constantly deal with the volatile model of the world. There's a lot of research about confirmation bias and its relation to cognitive dissonance. We really don't like cognitive dissonance. We don't like feeling like the world is not what we understand it to be, and when we're faced with information that conflicts with our core beliefs, we do in fact experience cognitive dissonance. The tolerance for cognitive dissonance tends to vary across individuals, but there's people who can really tolerate a wildly volatile world and they accept that they don't know things and they said that they could be wrong, and then there's personality types who are much less likely to take this dissonance and are more likely to try to avoid this dissonance. And so confirmation bias in this way has a social influence. Individuals will prefer sampling data from their in-group and will seek to confirm their own ideas by foraging for confirmatory information from their in-group. This allows ensures that they have access to like-minded allies and they choose to belong to communities where their deeply held beliefs are promoted and shared. This limits the cognitive effort that is already expended in the forging of information. This in-group delivery also influences how strongly information is integrated. So if a group membership is important for the individual, they'll tend to integrate way more information that comes from someone they believe believes the same things as them. For instance, you can think of news sources and Fox News. So people, it's not like people from different aisles don't know what the others are saying, they just tend to take what their preferred channel says and completely ignore what other channels are saying even if they've heard it.

Conformity
The confirmation bias is echoed by another heuristic, and we're talking about conformity. So that's the need to cohere with the beliefs of one's in-groups. So it's kind of a push and pull, right? I want to be in a group of people who are like-minded and I want to believe the same things that I believe, therefore going in a group of people who are like-minded is the best way to do so. I also don't want to be kicked out from the group because the group has access to a lot of resources that is very good for me, right? It limits how much information any one agent has to gather to be part of a group. It also increases how much each agent is trusted. In-group agents can be way more precisely predicted by their other members of their group. This is in part due by norms and behaviors scripts. We wrote another paper about this, and generally these scripts tend to benefit the members of the group, right? That's why they also want to uphold these scripts. So being able to sample from the group entails a continued relationship to other members. If I lose access to this, I can lose access to information, food, shelter, and you know, it leads to difficulties. If you want to read more, I can eventually give you all the resources. So this is a natural stopping point if you want. If you have any questions, if you have any notes, you can share them now.

Scripts
It was really powerful what you said about the losing access to the group benefits, especially from just the evolutionary and ecological point of view. What are the scripts and how does this current work that you're sharing relate to the work that you had done with narrative and scripts? Yeah, so I mean the definition of scripts is not perfectly shared across the board. There's a lot of fields that use it, but the way that we've reviewed the literature and brought together, we have weak scripts and strong scripts. So weak scripts are like clusters of connected concepts that tend to exist with one another in a sort of, it's like it's like the building of a context with naturally co-occurring concepts. And then the strong scripts is how these concepts tend to sequence over time. So like for instance, there is going to be a natural entailment to certain events that they gather the concepts together, and then you're going to be able to exist in a space like this. And that's that's how you norm not only how people behave in a group, but how they coordinate. That is how you norm how they sample reality. Because let's imagine my script in this place says that I must do this, this, and that. So I'm going to do this, this, and that, which means I'm not going to have access to all the other things I might have done if my script had been a little different. So that's one way that we force people to only look at a subset of the available information in a given space. Cool, and then how did it relate or how does this research build upon what you had done those few months ago? Right, so the previous paper had formalized what a script means in terms of Active Inference, and basically you, with you as an agent with your niche, predict what you're supposed to do next. So it puts a strong emphasis on your available policies and the way that your policies are shaped, and then you're going to tailor your prediction error on the response of the niche. So then you're going to get to this sort of sequenced patterns of synchronization that reinforce each other, right? So the more I get the right pattern, the more I'm likely to get good reinforcement, and therefore I'm going to, you know, think that this is the right pattern for this group, and this is going to shape the niche so much so that if anyone even wants to or tries to enact something different, they may just get so much prediction error that, you know, people just will will push back on it and you're gonna stay within this sort of manifold that has, you know, the center points that gets all the states in. But the way that we're using this research to build on the previous one is that we understand that a script takes many forms, right? The weak version of the script is really something you could call an ideology, right? So if you take all of my weak scripts, really what this is is how do I map my observations to my states? It's really what it is, right? And so this new research is saying, well, agents are going to map things differently, and thus they're going to end up into different groups by simple virtue of mapping so differently that eventually it makes no sense for them to try to interact with one another because they couldn't synchronize anyway. So that's how this builds upon the previous research. Cool, does that make sense? Yeah, please carry on. Okay, so we've discussed confirmation bias and conformity, and we've discussed how they mutually reinforce each other. So to save energy, confirmation bias leads to agents being drawn to groups that validate their opinion and increase the probability of behavioral and epistemic conformity, right? Believe the same things and they form the basis of information spread. So agents spread information through media and through connections to one another given a network structure, right? And the spread of ideas and behaviors serves local and larger scale coordination. This is very much based on the work of Maxwell, who has effectively discussed how Active Inference works across scale in nested Markov blankets that eventually build and become one another.

Synchronization
Similar norms and coordination can be understood as synchronization, which lowers the cost of information flow. This increases the certainty of the message being spread as well as the quality of its reception. So just right there, this increased certainty, the capacity to spread messages, this quality of reception, you can see already how this might lead towards better synchronization, right? Because more certainty means you may have less attention to give to one thing in order for it to happen, and you can start thinking about other things and start specializing in other areas with this certainty staying up, right? The message will be more intelligible to group members who share the common set of codes, and agents who are more likely to integrate new information if it fits better with their understanding of the world. So one example of optimization of message passing includes hashtags. They have been known to be heavy carriers of information in echo chambers. They're used in partisan ways to reach people of similar mindsets who understand what the hashtag means and understand that this is a signal for them to interpret what's being said in the life they want to interpret. So the spread of information is optimized through hashtags as pseudo-meta-linguistic categorization markers. That was those a lot of words, but really what it means is just that we see a hashtag, we know what it means, we know it has a lot of meaning without having to have a whole text for it, which is great for Twitter, right?

Epistemic Communities
We labeled our communities in this study, formed in the process of belief sharing, as epistemic communities. Now this term already exists, it was already used by other fields, but we've tailored it a little bit to mean specifically that our communities that share and spread a worldview or a paradigm or normalized sampling behaviors. Individuals in the community are tied together by these practices, which reinforce the social signals acting as evidence for the shared model of the world. So hashtags, the echo chamber formation is an extreme example of epistemic communities. Echo chambers type people with similar views together, and they tend to actively work against the engagement with external sources. They become very epistemically vulnerable when members can really no longer assess when an information is true or not. Only having access to a few sources limits how much information can be gathered, and relevant sources of evidence really fall through the gaps, and error will be propagated because it goes really well, really fast, and is integrated really strongly. And so if the people can no longer tell whether it's false or not, then the system is much likely to be more vulnerable to misinformation and errors. They'll have a difficult time to check errors against anything, and most mines in the echo chambers will become more and more synchronized and thus poised to make the same mistakes. So that's a pretty chunk right there. If you want, we can like take a beat.

Healthy Hashtags
Yeah, I had a question. What does a healthy usage of hashtags look like, or how do we compress information and context and perspective in a way that might not have some of these like threats or failures that you're talking about? So for the first parts, I have an idea, but I've never read anything that specifically said this is a healthy use. I'll venture a guess, but I'll start with the second part of the question that will give you a good sense. The way to keep communities healthy is to force them to be exposed to viewpoints they may not agree with, sources that they're not necessarily familiar with, and that have more nuanced takes. So the more you expose people to different kinds of people, different kinds of beliefs, the more likely they are to depolarize and be more open to possibilities. That's just a fact. Like we may think through experience, no, you know what, when I see my conservative uncle, my racist homophobic conservative uncle, when he talks, my teeth grit and I stop listening. Yes, that's true, but you still are exposed to him. You still have to engage with his thoughts to some degree, and so your reaction to push him away, that's a natural reaction and you know, you might actually do it. But if you're never ever exposed to his thoughts, you will never be able to actually, first of all, really know whether they're not true because you've never engaged with them, right? So that's one thing. So the guess about the hashtags is maybe try to research hashtags that are not part of your community and try to reach people who may not normally listen to you in a language that is potentially less polarized. So if you really want someone, the best example of this is, oh, so she's a YouTuber, she's amazing. Natalie Wynn, do you know her? Not familiar right now. I just, the thing is, I just don't remember the name of her channel, but she basically specialized in philosophically deconstructing conservative talking points in a way that steel-manned them and didn't just destroy them on a sort of, you know, value-based basis. It was more like, let's take these points, let's remove everything that actually really isn't true and take the kernel of truth in there and understand it through their eyes and reinterpret why this might actually still be wrong, but not in a way that was demeaning. And she reached a lot of people this way. She reached a lot of conservatives who were like, wow, okay, no, you know what, I get it. And it was very effective. So I think that's the answer to your question. Cool, carry on. Maybe I'm sure we'll be able to bring Active Inference in, but it's awesome to be just building the context and seeing how there was motivation and the perspective on the work. Awesome. So yeah, so one of the elements that maybe will in fact give you a good sense of how we're bringing Active Inference is the concept of volatility and habit formation. So stability in the group is not guaranteed. Optimal inference in a changing world requires integrating sensory data, right, with beliefs about the intrinsic volatility of the environment. So environments with higher quality volatility change more often and thus have shorter intrinsic time scales at which the agent has to keep updating their beliefs. And conversely, environments with lower volatility require, you know, longer time scale to start updating your beliefs. On the other hand, so having a better ability to track potentially important fluctuations in information requires to pay attention to smaller changes, but increased attention to environmental fluctuations will potentially lead to increased sensitivity to random non-informative changes in the environment. So that might be called a higher false positive rate, right? So it's important for agents to have the right step, understanding of the volatility in their environment. One way to cope with volatility is to use the coping mechanism to constrain the uncertainty related to their own behaviors via habit formation.

Habit Formation
So here we're going to model habit as a form of behavioral reinforcement where behaviors become more probable as a function of how often they are engaged. So an agent has engaged in a given behavior enough, a habit can then be formed and become hard to unlearn. This is important as we understand both how parameters are set in our generative model, but also how echo chambers can form by habit formation. So in our model, behavior is driven by information seeking, which drives, it's a drive that leads agent to preferentially sample information from other agents with beliefs that they believe are similar to their own. So this, the way that I'm saying this, believe that they believe is important in Active Inference because in Active Inference, we're starting from the assumption that we don't ever really know things are kind of hidden from us and we have to infer what things might be. So I never really have access to what the other person believes. I think they might think this, and I'm going to try to infer their beliefs based on some observations they're putting out into the world. Okay, now we've point that down.

Confirmation bias and conformity
Hello it is March 9th 2022 we're here in ActInf Lab guest stream number 17.1 with Mahault Albarracin. Mahault is a product director at Game Addict, a researcher at Versus Computational Phenomenology Lab, and finishing a PhD in cognitive computing at UQ. We'll have a fun discussion today. Feel free to write any questions in the chat during the presentation and we'll have a great time learning. So thanks a lot for joining this guest stream and really looking forward to what you have to share. Yeah, thanks for having me. I'm really glad to be able to present this paper. We've submitted it and we're in the process of reviewing it so it's a really exciting paper that I'm hoping we can get out soon. Today I'm going to try to go through a lot of big concepts and how they apply in Active Inference and then I'm going to try to explain the nitty gritty of a generative model, how to make a simulation and then what are the takeaways and limitations. I'm going to try to keep this quick. If you have any questions feel free to ask them and I'll take anything as it goes. Let's begin with the main concept here which is confirmation bias and conformity. This was the starting point of our research. We were thinking with my co-authors which are Connor Hines and Daphne Demakas and Maxwell Ramstead, we were trying to think through what leads people to see the world in such a way that they have a hard time then reconciling their view of the world with other people. And so it went back to the practice of exchanging ideas, sharing concepts and values between different minds which is a fundamental process. It really allows humans and other living agents to coordinate and basically operate socially by sharing ideas. Individuals and communities can really pursue their pragmatic goals. So basically, you know, get food is one of the permanent goals you might want to optimize for. They improve their understanding of the world and then we notice that humans are compulsory co-operators. Human individuals survive based on the predication that they have access and they can leverage the bodies of accumulated cultural knowledge. Over the course of evolutionary history, humans have developed an exquisitely sensitive capacity to discriminate between reliable sources of information from unreliable ones, which seems counterintuitive in the age that we're at, but you have to understand how far we've come before we got to the arms race towards misinformation. So the epistemic process, as I just said, it's really not without flaws. Humans are not computing machines, they're not perfect. They mostly use heuristics. They process information by reasoning to limit the consumption of energy and facilitate rapid decision making. That's the basis of survival.

Confirmation bias
For example, confirmation bias implies that all other things being equal, individuals who prefer sticking to their own beliefs over changing their minds, it's easier for them to potentially change their model less than if they had to really all the time constantly deal with the volatile model of the world. There's a lot of research about confirmation bias and its relation to cognitive dissonance. We really don't like cognitive dissonance. We don't like feeling like the world is not what we understand it to be, and when we're faced with information that conflicts with our core beliefs, we do in fact experience cognitive dissonance. The tolerance for cognitive dissonance tends to vary across individuals, but there's people who can really tolerate a wildly volatile world and they accept that they don't know things and they said that they could be wrong, and then there's personality types who are much less likely to take this dissonance and are more likely to try to avoid this dissonance. And so confirmation bias in this way has a social influence. Individuals will prefer sampling data from their in-group and will seek to confirm their own ideas by foraging for confirmatory information from their in-group. This allows ensures that they have access to like-minded allies and they choose to belong to communities where their deeply held beliefs are promoted and shared. This limits the cognitive effort that is already expended in the forging of information. This in-group delivery also influences how strongly information is integrated. So if a group membership is important for the individual, they'll tend to integrate way more information that comes from someone they believe believes the same things as them. For instance, you can think of news sources and Fox News. So people, it's not like people from different aisles don't know what the others are saying, they just tend to take what their preferred channel says and completely ignore what other channels are saying even if they've heard it.

Conformity
The confirmation bias is echoed by another heuristic, and we're talking about conformity. So that's the need to cohere with the beliefs of one's in-groups. So it's kind of a push and pull, right? I want to be in a group of people who are like-minded and I want to believe the same things that I believe, therefore going in a group of people who are like-minded is the best way to do so. I also don't want to be kicked out from the group because the group has access to a lot of resources that is very good for me, right? It limits how much information any one agent has to gather to be part of a group. It also increases how much each agent is trusted. In-group agents can be way more precisely predicted by their other members of their group. This is in part due by norms and behaviors scripts. We wrote another paper about this, and generally these scripts tend to benefit the members of the group, right? That's why they also want to uphold these scripts. So being able to sample from the group entails a continued relationship to other members. If I lose access to this, I can lose access to information, food, shelter, and you know, it leads to difficulties. If you want to read more, I can eventually give you all the resources. So this is a natural stopping point if you want. If you have any questions, if you have any notes, you can share them now.

Scripts
It was really powerful what you said about the losing access to the group benefits, especially from just the evolutionary and ecological point of view. What are the scripts and how does this current work that you're sharing relate to the work that you had done with narrative and scripts? Yeah, so I mean the definition of scripts is not perfectly shared across the board. There's a lot of fields that use it, but the way that we've reviewed the literature and brought together, we have weak scripts and strong scripts. So weak scripts are like clusters of connected concepts that tend to exist with one another in a sort of, it's like it's like the building of a context with naturally co-occurring concepts. And then the strong scripts is how these concepts tend to sequence over time. So like for instance, there is going to be a natural entailment to certain events that they gather the concepts together, and then you're going to be able to exist in a space like this. And that's that's how you norm not only how people behave in a group, but how they coordinate. That is how you norm how they sample reality. Because let's imagine my script in this place says that I must do this, this, and that. So I'm going to do this, this, and that, which means I'm not going to have access to all the other things I might have done if my script had been a little different. So that's one way that we force people to only look at a subset of the available information in a given space. Cool, and then how did it relate or how does this research build upon what you had done those few months ago? Right, so the previous paper had formalized what a script means in terms of Active Inference, and basically you, with you as an agent with your niche, predict what you're supposed to do next. So it puts a strong emphasis on your available policies and the way that your policies are shaped, and then you're going to tailor your prediction error on the response of the niche. So then you're going to get to this sort of sequenced patterns of synchronization that reinforce each other, right? So the more I get the right pattern, the more I'm likely to get good reinforcement, and therefore I'm going to, you know, think that this is the right pattern for this group, and this is going to shape the niche so much so that if anyone even wants to or tries to enact something different, they may just get so much prediction error that, you know, people just will will push back on it and you're gonna stay within this sort of manifold that has, you know, the center points that gets all the states in. But the way that we're using this research to build on the previous one is that we understand that a script takes many forms, right? The weak version of the script is really something you could call an ideology, right? So if you take all of my weak scripts, really what this is is how do I map my observations to my states? It's really what it is, right? And so this new research is saying, well, agents are going to map things differently, and thus they're going to end up into different groups by simple virtue of mapping so differently that eventually it makes no sense for them to try to interact with one another because they couldn't synchronize anyway. So that's how this builds upon the previous research. Cool, does that make sense? Yeah, please carry on. Okay, so we've discussed confirmation bias and conformity, and we've discussed how they mutually reinforce each other. So to save energy, confirmation bias leads to agents being drawn to groups that validate their opinion and increase the probability of behavioral and epistemic conformity, right? Believe the same things and they form the basis of information spread. So agents spread information through media and through connections to one another given a network structure, right? And the spread of ideas and behaviors serves local and larger scale coordination. This is very much based on the work of Maxwell, who has effectively discussed how Active Inference works across scale in nested Markov blankets that eventually build and become one another.

Synchronization
Similar norms and coordination can be understood as synchronization, which lowers the cost of information flow. This increases the certainty of the message being spread as well as the quality of its reception. So just right there, this increased certainty, the capacity to spread messages, this quality of reception, you can see already how this might lead towards better synchronization, right? Because more certainty means you may have less attention to give to one thing in order for it to happen, and you can start thinking about other things and start specializing in other areas with this certainty staying up, right? The message will be more intelligible to group members who share the common set of codes, and agents who are more likely to integrate new information if it fits better with their understanding of the world. So one example of optimization of message passing includes hashtags. They have been known to be heavy carriers of information in echo chambers. They're used in partisan ways to reach people of similar mindsets who understand what the hashtag means and understand that this is a signal for them to interpret what's being said in the life they want to interpret. So the spread of information is optimized through hashtags as pseudo-meta-linguistic categorization markers. That was those a lot of words, but really what it means is just that we see a hashtag, we know what it means, we know it has a lot of meaning without having to have a whole text for it, which is great for Twitter, right?

Epistemic Communities
We labeled our communities in this study, formed in the process of belief sharing, as epistemic communities. Now this term already exists, it was already used by other fields, but we've tailored it a little bit to mean specifically that our communities that share and spread a worldview or a paradigm or normalized sampling behaviors. Individuals in the community are tied together by these practices, which reinforce the social signals acting as evidence for the shared model of the world. So hashtags, the echo chamber formation is an extreme example of epistemic communities. Echo chambers type people with similar views together, and they tend to actively work against the engagement with external sources. They become very epistemically vulnerable when members can really no longer assess when an information is true or not. Only having access to a few sources limits how much information can be gathered, and relevant sources of evidence really fall through the gaps, and error will be propagated because it goes really well, really fast, and is integrated really strongly. And so if the people can no longer tell whether it's false or not, then the system is much likely to be more vulnerable to misinformation and errors. They'll have a difficult time to check errors against anything, and most mines in the echo chambers will become more and more synchronized and thus poised to make the same mistakes. So that's a pretty chunk right there. If you want, we can like take a beat.

Healthy Hashtags
Confirmation bias and conformity
hello it is march 9th 2022 we're here in actin flab guest stream
number 17.1 with mao abrasion and mao is a product director at game addict
a researcher at versus computational phenomenology lab and finishing a phd in
cognitive computing at uq am we'll have a fun discussion today feel
free to write any questions in the chat during the presentation and we'll
have a great time learning so thanks a lot for joining this guest stream and really
looking forward to what you have to share yeah thanks for having me i'm really
glad to be able to present this paper we've uh we've submitted it and we're in the process of reviewing it so it's a
really exciting paper that i'm hoping we can get out soon so
today i'm going to try to go through a lot of big concepts and how they apply an active inference and then i'm going
to try to explain um the nitty gritty of a generative model how to make a simulation and then
what are the takeaways and limitations i'm going to try to keep this quick if you have any questions feel free to ask
them and i'll take anything as it goes so
Confirmation bias and conformity
let's uh begin with the main concept here which is uh confirmation bias and
conformity this uh this was the the starting point of our research
we were we were thinking with my co-authors which are connor hines
and daphne demacus and maxwell ramstead we were trying to think through
what leads people to see the world in such a way that they have a hard time then reconciling their
view of the world with other people and so it went back to the practice of
exchanging ideas sharing concepts and values uh between different minds which is a fundamental process
it really allows humans and other living agents to coordinate and basically operate socially
by sharing ideas uh individuals communities can really pursue their pragmatic goals
so basically um you know get food is one of the permanent goals you might want to
optimize for um they improve their understanding of the world and then
we notice that humans are compulsory co-operators
human individuals and survive based on the predication that
they have access and they can leverage the bodies of accumulated cultural knowledge
over the course of evolutionary history humans have developed an exquisitely sensitive capacity to
discriminate between reliable sources of information from unreliable ones which seems counterintuitive in the age that
we're at but you have to understand how far we've come before we got to the to the arms race
towards misinformation so the epistemic process as i just said
Confirmation bias
it's really not without flaws humans are not computing machines they're not perfect
they mostly use heuristics they process information by reasoning to limit the consumption of energy and
facilitate rapid decision making that's that's the basis of survival
for example confirmation bias uh implies that all other things being
equal individuals who prefer sticking to their own beliefs over changing their minds it's
easier for them to potentially um change their model less than if they had
to really all the time constantly deal with the volatile model of the world
there's a lot of research about confirmation bias and its relation to cognitive dissonance we really don't
like cognitive dissonance we don't like feeling like the world is not what we understand it to be
and when we're faced with information that conflicts with our core beliefs we do in fact
experience cognitive dissonance the tolerance for cognitive dissonance
tends to vary across individuals but there's people who can really tolerate a wildly volatile world and they accept
that they don't know things and they said that they could be wrong and then there's personality types who are
much less likely to take this dissonance and and are more likely to try to avoid this dissonance
and so confirmation bias in this way has a social influence individuals will prefer sampling data
from their in-group and will seek to confirm their own ideas by foraging for confirmatory information from their
in-group this allows ensures that they have access to like-minded allies
and they choose to belong to communities where their deeply held beliefs are promoted and shared this limits the
cognitive effort that is already expended in the forging of information this in-group delivery
um also influences how strongly information is integrated so if a group
membership is important for the individual uh they'll tend to integrate
way more information that comes from someone they believe believes the same things as them
for instance you can think of news sources and fox news so people it's not like people from different aisles don't
know what the others are saying they just tend to take what their preferred channel says
and completely ignore what other channels are saying even if they've heard it so
Conformity
the confirmation bias is echoed by another uh heuristic and we're talking about conformity so that's the need to cohere
with the beliefs of one's in groups so it's kind of a push and pull right i want to be
in a group of people who are like-minded and i want to believe the same things that i believe therefore going in a
group of people who are like-minded is the best way to do so i also don't want to be kicked out from
the group because the group has access to a lot of resources that is very good for me right um
it limits how much information any one agent has to gather to be part of a group
uh it also increases how much each agent is trusted um
in-group agents can be way more precisely predicted by their their the other members of
their group uh this is in part due by norms and behaviors scripts we wrote
another paper about this and generally these scripts tend to benefit the members of the group right
um that's why they also want to uphold these um these scripts
so being able to sample from the group entails a continued relationship to other members
if i lose access to this i can lose access to information food shelter and
you know it leads to difficulties if you want to read more i can
eventually give you all the resources so this is a natural stopping point if you
Scripts
want if you have any questions if you have any notes you can share them now
it was really powerful what you said about the losing access
to the group benefits especially from just the evolutionary and ecological
point of view what are the scripts and how does this current work that
you're sharing relate to the work that you had done with narrative and scripts yeah
so i mean the definition of scripts is not perfectly shared across the board
there's a lot of fields that use it but the way that we've reviewed the literature and brought together we have
weak scripts and strong scripts so we weak scripts are like clusters of connected uh concepts that
tend to exist with one another in a sort of um it's like it's like the building of a
context with naturally co-occurring concepts and then the strong scripts is
how these concepts tend to uh sequence over time so like for instance um there is going to be a
natural entailment to certain events that they gather the concepts together and then you're going to be able to to
exist in a space like this um and that's that's how you
you norm not only how people behave in a group but how they coordinate that is how you norm how they uh sample reality
because let's let's imagine my script in this place says that i must do this this and that so i'm going to do this this
and that which means i'm not going to have access to all the other things i might have done if my script had been a little different so that's one way that
we um we force people to only look at a subset of the of the available information in a given space
cool and then how did it relate or how does this research build upon what you had done
[Music] those few months ago right so the the previous paper had
formalized what a script means in terms of active inference and basically um
you with you as an agent with your niche um
predict what you're um what you're supposed to do next so it it it puts a strong
emphasis on your on on your available policies and the way that your policies are shaped and then
you're going to tailor your prediction error on the response of the nation so then you're
going to get to this sort of um sequenced patterns of synchronization that reinforce each other right so the
more i get the right pattern the more i'm likely to get good reinforcement and
therefore i'm going to you know think that this is the right pattern for this group and this is going to shape
the niche so much so that if anyone even wants to or tries to enact something different they may just get so much
prediction error that you know people just will will push back on it and you're gonna stay within this sort of manifold
that has you know the center points that that gets all the states in but
the way that we're using this research to build on the previous one is that we understand that a script takes many
forms right the weak version of the script is really something you could call an ideology
right so if you take all of my weak scripts really what this is is
how do i map my observations to my states it's really what it is right
and so this new research is saying well agents are going to map things
differently and thus they're going to end up into different groups by simple virtue of
mapping so differently that eventually it makes no sense for them to try to interact
with one another because they couldn't synchronize anyway so that's um that's that's where that's how this
builds upon the previous research cool does that make sense
yeah please carry on okay so we've discussed confirmation
bias and conformity and we've discussed how they mutually reinforce each other
so to save energy confirmation bias leads to agents being drawn to groups that
validate their opinion and increase the probability of behavioral and epistemic conformity right believe the same things
and they form the basis of information spread so agents spread information through media and through connections to
one another given a network structure right um and the spread of ideas and behaviors
serves local and larger scale coordination this is very much based on the work of maxwell
who has effectively um discussed how active inference works across scale in nested
markov blankets that eventually build and become one another so
Synchronization
similar norms and coordination can be understood as synchronization which lowers the cost of information
flow this increases the certainty of the message being spread as well as the
quality of its reception so just right there this increased certainty the capacity to spread messages this uh
quality of reception you can see already how this might lead towards better synchronization right because um more
certainty means you may have less attention to give to one thing in order for it to happen and you can
start thinking about other things and and start specializing in in other areas with this certainty staying up right
uh the message will be more intelligible to group members who share the common set of codes uh and agents who are more
likely to integrate new information if it fits better with their understanding of the world so
one example of optimization of message passing includes hashtags they have been known to be heavy
carriers of information in echo chambers they they're used in partisan ways to reach people of similar mindsets who
understand what the hashtag means and understand that this is a signal for them to interpret what's being said in
the life they want to interpret so the spread of information is optimized through hashtags as
pseudo-meta-linguistic categorization markers that was those a lot of words but really really what it means is just
that uh we see a hashtag we know what it means we know it has a lot of meaning without having to have a
whole text for it which is great for twitter right um so
Epistemic Communities
we labeled our communities in this study um formed in the process of belief sharing
as epistemic communities now this term already exists it was already used by other um other fields but we've tailored
it a little bit to mean specifically that our communities that share and spread a worldview
or a paradigm or normalized sampling behaviors individuals in the community are tied
together by these practices which reinforce the social signals acting as evidence for the shared model of the
world so hashtags the echo chamber formation is an extreme
example of epistemic communities echo chambers type people with similar views together and they tend to actively work
against the engagement with external sources they become very epistemically
vulnerable when members can really no longer assess when an information is true or not
only having access to a few sources limits how much information can be gathered and relevant sources of
evidence really fall through the gaps and error will be propagated because it
goes really well really fast and is integrated really strongly and so if the people can no longer tell whether it's
false or not then the the the system is much likely to to be more
vulnerable to misinformation and errors they'll have a difficult time to check errors against anything and um most
mines in the echo chambers will become more and more synchronized and thus poised to make the same mistakes
um so that's a pretty uh that's pretty chunk right there if you want we can like take a beat
Healthy Hashtags
yeah i had a question what does a healthy usage of hashtags
look like or how do we compress
information and context and perspective in a way that might not have some of
these like threats or failures that you're talking about so for the first parts i
i have an idea but i've never read anything that specifically said this is a healthy you saw i'll venture a guess
but i'll start with the second part of the question that will give you a good sense the way to keep communities
healthy is to force them to be exposed to viewpoints they may not agree with
sources that they're not um necessarily familiar with
and that have more nuanced takes so the more you expose
people to different kinds of people different kinds of beliefs the more likely they
are to depolarize and be more open to possibilities
that's just a fact like we may think through experience no you know what when i see my uh
my conservative uncle my racist homophobic conservative uncle when he talks
my teeth grit and i stop listening yes that's true but you still are exposed to him
you still have to engage with his thoughts to some degree and so your reaction to push him away
that's a natural reaction and you know you might actually do it but
if you're never ever exposed to his thoughts you will never be able to actually first of all really know
whether they're not true because you you've never engaged with them right
so that's one thing so the the guess about the hashtags is
maybe try to research hashtags that are not part of your community
and try to reach people who may not normally listen to you in a
language that is potentially less polarized so if you really want someone the best
example of this is um oh so she's a youtuber she's amazing
natalie wynne do you know her not familiar right now
uh i i just the thing is just i don't remember the name of her channel but uh
she basically specialized in philosophically deconstructing
um conservative talking points in a way that um
steel manned them and didn't just destroy them on a sort of
you know value-based basis it was more like let's take these points let's remove
everything that actually really isn't true and take the kernel of truth in there and understand it through their
eyes and reinterpret why this might actually still be wrong but not in a way that was demeaning and she reached a lot
of people this way she reached a lot of conservatives who were like wow okay no you know what i get it and
and it was very effective so i think that's the answer to your question
cool carry on maybe i'm sure we'll be able to bring active inference in but it's awesome to be just
building the context and seeing how there was motivation um and the
perspective on the work awesome so yeah so one of the elements that
maybe will in fact give you a good sense of how we're bringing active inferences is the concept of volatility and habit
formation so stability in the group is not guaranteed optimal inference in a changing world
requires integrating sensory data right with beliefs about the intrinsic volatility of the environment
so environments with higher quality volatility change more often and thus have shorter intrinsic time scales
at which the agent has to keep updating their beliefs and conversely environments with lower volatility
require you know longer time scale to start updating your beliefs um on the other hand
so um having a better ability to track potentially important fluctuations in
information requires to pay attention to smaller changes but increased attention to environmental fluctuations will
potentially lead to increased sensitivity to random non-informative changes in the environment so that might
be called a higher false positive rate right so it's important for agents to is to have
the right step um understanding of the volatility in their environment one way to cope with volatility is to
Habit Formation
use the copic mechanism to constrain the uncertainty related to their own behaviors via habit formation
so um here we're going to model habit as a form of behavioral reinforcement where
behaviors become more probable as a function of how often they are engaged so an agent has engaged in a given
behavior enough a habit can then be formed and become hard to unlearn and this is important as we understand both
how parameters are set in our generative model but also how echo chambers can form by habit formation
so in our model behavior is driven by information seeking which drives uh it's a drive that leads
agent to preferentially sample information from other agents with beliefs that they believe are similar to
their own so this um the way that i'm saying this believe that they believe is important in active
inference because the inactive inference we're starting from the assumption that we don't ever really know things are
kind of hidden from us and we have to infer what things might be so i never
really have access to what the other person believes i think they might think this and i'm going to
try to infer their beliefs based on some observations they're putting out into the world
okay now we've point that down
let's start with doing friends so we're getting to the meat of it i'm gonna do a very uh short
introductory inference if you already know great if you don't then this is gonna be very informative
it's a biologically motivated framework that rests on first principles of
self-organization in complex adaptive systems so
self-organization part is probably the most important part here because active inference is potentially less
interesting for rocks for instance because they they tend to self-organize a little less um i'm pretty sure we
could effectively use it for larger models of um astrology but in uh sorry
astronomy but effectively what you really care here is for things that tend to fight entropy
so it's focused on the notion that internal states of any biological system are statistically insulated from the
environment that generates sensory observations so basically they have an inside and they have an outside
um and so they engage in inference about the the causes of what gives them
sensory states to really behave optimally to keep fighting entropy so biological systems entertain a
generative model of the latent environmental causes of their sensory input so latent because i don't know
really what causes it i can only infer so it's a little different from reinforcement learning or reflexive
behavioral algorithms um because actions taken under active inference are guided
by these internal beliefs and themselves they are optimized with respect to an internal world model or a
representation of the world's causal and data-generative structure we call the generative model
agents in active inference represent their own actions in their generative model
by performing inference on both hidden environment states of the world
and the consequences of their own actions they can select behavior which first
achieves their goal or fulfills preferences and second reduces uncertainty in the age and world
model so this is where we get to the epistemic part right i don't i want a certain the world to be a
certain way and i also want to be less uncertain about my uncertainty of the world being the
certain way right so an agent's main objective is to increase their model evidence
and to reduce suppress surprised that like a consider an agent which is in the
world um if i want to predict myself surviving i
want to see things which are likely to make me survive if i'm surprised by something it's
probably not likely to make me sir survive and therefore it's probably something i should avoid like for right
now i'm in my room i expect the room to stay where it is as it is this is good if we're there were to appear on my
right would be very surprising and probably very bad for me so
processes like learning perception planning and goal-directed behavior emerge from this single drive to
increase evidence for the agent's generative model of the world so far
still good so the agents never directly act on
Bayesian Inference
sensory data but they change their belief about what causes that data this is a core step in active inference
it consists in optimizing these beliefs using a generative model it's also known as bayesian inference or
bayesian model inversion this inference answers the question what is my best guess about the state of
the world given my sensory data and my prior beliefs i don't come into the world not
knowing anything i have some basic beliefs about how what's what's
going to happen and then i'm getting observations and i make predictions about what might happen and then i act
on those predictions this follows bayes rule where the optimal belief about hidden or
latent variable given some sensory data is called the posterior distribution um if you want
and keep going into that or i can skip that automatically but but basically um
you you you basically calculate uh the probability of something given something else active inference perception
uh the generation of the best guess about the current hidden states of the world is formalized as the computation of a
posterior distribution over some hidden states and action so the active part of active
inference is the computation of a posterior distribution over policies policies are
just a sequence of um of potential states of the world
okay so now we introduce the actual model
is it is it clear so far is the active inference part pretty clear that's awesome you
hit on many great active pieces um
the only piece that really i wanted to mention was the difference
between the observations like what was said and then the hidden hypothesized cognitive states
it opens up a space between what happened and why somebody
said that and so that comes up all the time in epistemic communities what did the
author mean by those words or what did the person mean by saying that and so that's why the context is so important
and active gives a framework that might help us model that kind of a scenario exactly and i mean this is this is
exactly where we're trying to go with this research is that what right now we want to model how
people tend to have different views of the world but the underlying phenomenon here and we're
going to try to dig more into that is that or the hypothesis anyway is that there
is a literal different mapping between an observation and a state which means for the same
thing being seen by two different people we're going to infer two very different
things and the funny thing is
then you come into the world of values where it's it's a whole other
scale and stuff where we may be interpreting the same thing
but we'll have a spin on it and that spin being like no no i know what he meant i just
fundamentally disagree with it and this is how we get into the web these these scripted webs of conceptual spaces where
um you see these these graphs of concepts being connected but at some point there's a rift
and and that rift makes it so that i value this and you do not and we're still and so we can converge towards
understanding without necessarily being able to converge towards um acceptance
so this is still very hypothetical though
one other note on on what you just said there it's like the difference between an orthodoxy and orthopraxis
so what is the similarity between conformity of thought and
latitude on action vice versa and then in what way are the
systems around us like aligned or not with our preference about those features of systems
yeah absolutely absolutely i mean i feel like this could all be encased in c
right like we can interpret the same thing but my fee is way over
there over here so i'll explain see later
this made very little sense a lot of people um so let's introduce the model a little
more um we have individuals agents who share
information with one another and they come to form beliefs about their local environment and about the beliefs of
other agents in their community so to understand this phenomenon we leverage thus the active framework
here the organisms tend to minimize a quantity called variational free energy which quantifies the
divergence between the expected and the sense data as explained before
from this point of view to select an action is to infer what i must be doing given what i believe and what i sense
so there's been a lot of work done in this field on active inference to study social systems i'm not going to go over
all of it but um there's really cool studies i've just highlighted a few here
where basically um systems uh minimize free energy give
rise to large-scale behavioral coordination much of the work though is still theoretical so it'll be interesting to
see how experimental work can delve into this um i know jonas mago uh uh rudy pitia and maxwell ramsey are
doing a lot of work on this i think uh lars senzvet as well as doing some cool work on this
Epistemic Confirmation Bias
i'm just throwing on me so um at first glance it might appear
difficult to model a phenomenon like confirmation bias using active inference formulation why
because remember our agents are supposed to be guided by the principle of maximizing
beijing surprise or earth silence which requires to constantly seek out information that is expected to
challenge one's world right because the more surprised that consumed now the less likely i am to be surprised later
right but information gain is subjective
um epistemic value or the the basin surprise or information
gain is always an expected surprise from the point of view of the agent
it's in relation to the agent's set of beliefs or genetic model and because of this subjectivity
the informativeness of epistemic value or or epistemic value of an action can
be arbitrarily far from the agent's expectation so taking advantage of this
we gave agents what we refer to as epistemic confirmation bias by building
a prior belief into the degenerative model that agents are more likely to sample informative information from agents with
whom they agree a priori and this a priori notion is important so
agents will sample agents with whom they agree under the belief that the agents are more likely to
provide higher quality information there you go
Active Inference vs Traditional Opinion Models
um this has a key difference with some traditional opinion model so there's been a lot of opinion models out there
not a lot with active inference but definitely a lot with traditional approaches and so the implementation of bounded
confidence to motivate polarization is usually hard-coded in the agent's
ability to perceive and thus update their beliefs in our model
polarization is motivated by the positive effect of confirmation bias and
is thus directly in the agent's model of the world this allows agents to get more evidence
about their environment if the information comes from another agent that shares the same worldview
they're implicitly motivated in their generative models to gain more evidence about the world if
it confirms their pre-existing beliefs also agents normally in traditional
models can directly perceive the belief state of other agents right directly perceived that's the key here
um but in our model this is pretty we believe this is unrealistic because we
we only infer the beliefs of others and thus um agents do not have direct access to
each other's belief states they they infer the belief states and change them through observation
Bayesian Brain Hypothesis
um there's been a few recent papers on that begin to build bayesian
models of opinion dynamics which are motivated by the bayesian brain hypothesis
a crucial point that distinguishes approaches like active inference and planning as inference from the genitive
bayesian approach is the notion that actions themselves are inferred behavior is cast as the result of
inference specifically by sampling actions from a posterior distribution over actions
so actions are selected in order to achieve goals that minimize future
uncertainty and to maximize a lower bound on bayesian model evidence so um
we're using this to supplement the goal-directed aspect of policy inference which is driven by the expected free
energy um and this becomes habits when the prior over the actions becomes
inflexible right so if the prior over action becomes so strong it's just always going to be that right
um this prior is learned over time and in the context of opinion dynamics
it can lead to a propensity to continue sampling agents that have been sampled previously so it's this idea of choosing
action through inference in accordance with the minimization of uncertainty it's a powerful modeling technique
because through the choice of policy inference one can encode various social behaviors like conformity
habit formation hostility and indifference here we really only did um
habit formation because we had to focus but eventually this could lead to very
very powerful modeling tools for social uh
so i can stop here before i launch into the hypothesis
awesome with active inference let's keep going
so we have three hypotheses the first one is uh that we cast confirmation bison actor inference as a
form of biased curiosity in which agents selectively gather information from other agents with whom they agree
um epistemic confirmation can mediate the formation of echo chambers uh and polarization in social networks
but we also believe that uh confirmation bias episode confirmation bias and network connectivity will will
mod and modulate the formation of polarized epistemic communities um hypothesis number two is we consider
the effect of agents beliefs about the volatility of their social environments so we try to see how beliefs about
social volatility impact their sampling behaviors and which itself may interact with
epistemic confirmation bias so we hypothesize that beliefs about less quickly changing social environments
will increase the likelihood of polarization and hypothesis tree uh we hypothesize that we can model uh
selective exposure effects and conformity through habit formation which emerges through bayes optimal learning
so we show that agents will begin to sample only those who belong to a particular epistemic community
a greater learning rate for habit formation will lead to clusters within the network amplifying and quickening
the formation of echo chambers so the model
The Model
this is a multi-agent active inference model uh a group of agents
update their beliefs about an abstract binary state that represents two conflicting ideas and the opinion states
about these ideas each agent also generates an action that is observable
to other agents in the context of digital social network we're using the twitter linguistics but this was um we
basically tried to replicate distributions that were fine in previous studies on twitter over time
each agent updates posterior distribution or beliefs about which idea is true
and as well as a belief about what a connected set of other agents in the network believes so basically what do their neighbors believe
and uh both of these inferences are achieved by observing the behavior of other agents
agents can only observe the behavior of one agent at a time so they have to they have to um specific
pick who they want to uh look at all right the generator model
Generator Model
um i can go into detail if you want but um this is pretty
i know it looks like a lot but it's actually pretty simple um these encapsulate observations right so this
is the observation about uh what i'm tweeting who i'm looking at and what they're tweeting right
and then the a matrix is mapping the probability of a state
having caused this observation so we have states about like what is um is the id true or not is it id1 is it
id2 um this is a bit blurry but uh basically like uh which neighbor am i
looking at and this one is who we're looking at what do they believe right so it's it's it's pretty simple mapping
here you have d which is the priors um so what do i believe about the world before having any observation about the
world then b is the transitions right so how are the states likely to succeed one
another here you have the the policies so uh what kinds of actions am i likely to
take to bring about this uh this exception of um of of states
and c are my preferences so then there are other terms but they're a bit more complicated so i'm not going to go into them but basically
these are the main um these are the main things you have to know about a generative model
so i'm going to skip real fast because there were little arrows and i could explain more but man
just yep uh here each agent's
Active Reference Agents
each active reference agent in the multi-agent simulation is equipped with the same generative model
a single agent observes the action of other agents um they form beliefs about an abstract
binary environmental states and then they choose actions which themselves are observing observable to other actions
the focal agent consists of two simultaneous choices an expression and an observation so
basically what am i tweeting and who am i looking at an agent can only observe one neighbor
at a time so at each time step a vocal agent both tweets its own hashtag and chooses to read a hashtag tweeted by
another single agent so here we're saying hashtag again this is just linguistics right we could have said anything basically these are numbers in
a matrix um effectively in a much more complex model we could have had them um
read a hashtag and a sentence and then try to infer what the sentence really says like that we could have done something much more complex but for now
the point was just to make them try to infer a belief based on
Surprise
hmm
i hope mal will rejoin and then we'll continue
hey are you there yep so sorry i don't know what happened
oh we get all kinds of of surprises we we prefer surprises here you can reshare
and just continue it was only a few seconds but it was it was great you know when you say the right keywords
and then the internet short circuits it happens all right well
i don't see you anymore oh yeah i'm here no no i'm here don't worry
i'll share my screen again awesome actually can i no let's just go
with this okay can you see my screen again and i'm back is everything cool
great great wonderful we're back now where did you cut off because i don't know if we kept talking
for a minute um we heard observing one neighbor at a time like and then how you could have
modeled more complex interaction effects with uh like multiple artifacts yeah
right okay awesome okay cool yeah
Hidden States
so um now let's explain the hidden states so what are the states they're trying to infer
s idea so it's basically a binary variable id one id two is id one true is
id two true meta belief which is um the particular neighbors beliefs about
which of the id is true so does my neighbor believe this or not that
the tweet so what am i tweeting and who should i attend to which neighbor am i attending to so um this
was actually very complex uh daphne and connor did an amazing job
here because we wanted to change the number of neighbors and so the the matrices had to
grow in relation to how many neighbors there were and they did it was it was beautiful
the way that they did this so shout out to connor who's obviously a genius and daphne as well
um so i'll discuss control sticks so control states are which of the states can my agents
Control States
actually act upon so here it was um the tweet so i can
decide to tweet you know hashtag one or hashtag two and i can decide to look at neighbor
you know one through k now observation modalities what can they see
they can see their own tweets and this is important because the thing is oftentimes you have to have a sort of
identity mapping between your observations and your states so that the states can be taken into consideration in the actions um so here you have to
know what you're tweeting you have to know what your neighbor is tweeting and you have to know who you're
attending to right pretty simple now for likelihood so
um you know in a palm dp in a generative model we have to describe the
likelihoods that determine how hidden states relate to observations right um
so the entire a array is a set of tensors with one sub-tensor per
observation modality each modality-specific likelihood tensor is a potentially multi-dimensional array that
encodes the conditional dependencies between each combination of hidden states and observations for that modality
so we also have a transition model so the transition likelihood uh the
dynamical likelihood uh in b that i explained earlier the environmental dynamics so um how are things likely to
change a higher value means the same idea remains valid over time a lower value means the same idea is less likely
to be true over time so more environmental volatility and then um the dynamics of
whether my neighbors are likely to change their ideas of the world
Priors
then the next component here is the degenerative models the priors over
the observations so in discrete in discrete active inference we represented these as vector c d and e so
um goal directed action is motivated by appealing to a baseline prior
um over observations so that specifies the agent's preferences so that's the c i was talking about earlier what do i
want to encounter in the world what are the outcomes i'd like to see and those usually act as kinds of rewards
then there's the prime over hidden states at the initial time step which is the d vector it encodes the agent's
beliefs about the initial state of the world before having made any observations and um in the current model
we make the prior over control states an empirical prior parameterized by the link function
denoted by the et vector so i'm not going to go too much into this but basically this implies that the prior
over those control states corresponding to tweet actions depending on the posterior of the idea so basically your
agents are always going to tweet exactly the same as they believed they're not lying but they could but we could change
that so habit learning under active inference uh learning also emerges as a form of
Habit Learning
variational inference so um it's not an inference uh over hidden states but
rather over model parameters so the parameter inference is referred to as learning because it is often
assumed to occur on a fundamentally way slower time scale than hidden state and policy inference
in this model we use habit learning to model the development of epistemic habits so as i said the the the tendency
to resample the same people and so um they simultaneously infer which
neighbor to attend to based on the prerogative to minimize expected free energy and they also continuously learn the
habit based on the frequency with which they tend to ask our neighbor all right the actual simulation so
Simulation
in a given simulation we had several agents but we didn't always use
the same number of agents we were very limited by computational constraints we would have wanted to make something much
larger much bigger to really model an actual social media but this is very computational heavy in the future
studies we may try to increase the number of agents but for now we tried to stay between 12 and 30 agents
again same model for each agent at each time step agents simultaneously update their belief
and take an action each agent's observation or a function of its own actions at the previous time step as
well as the actions of a selected set of neighbors at the previous time set so not everyone is connected to
everyone so i don't need to see everyone all the time each agent has a fixed set of neighbors
where the particular neighbors are determined by a randomly chosen network topology
okay all right so so focal agents with a higher ecb
believes that tweets are more reliable if they come from neighboring agents that believe to share the same opinion
right to like-minded people uh the inverse social volatility is a
parameterized focal agent's beliefs about the stochasticity of the social dynamics the learning rate is associated
with updating the habit vector over neighbor attendance and network connectivity um
is the number the way that individuals um [Music] are connected to one another it's pretty
simple so these are the parameters that we tweaked uh during the during the simulations um you'll see
that um they tend to enter in interact with one another and they're related to the hypotheses we formed initially
Discussion
so this figure um is really cool
it visualizes opinion formation in a single active inference agent and shed light on the relationship between
inverse volatility and epistemic confirmation um we use a simplified three agent setup
here so we just were trying to test something at each time step the focal agent chooses to read a hashtag from one
of its two neighbors and the two neighbors are not actually active inference agents here they're
just uh they're just part of the generative process they're sources of sequence of distinct hashtags and who
tweet hashtag one or hashtag two and as you can see a higher epistemic confirmation bias
induces a positive feedback effect where the focal agent comes to agree with one of its two neighbors with a higher
certainty as you know it it tweets the thing that it believes
um even if it's exposed to a sequence of hashtag over 100 time steps
the agent receives the observation and um here below each subplot the heat map
shows that the temporal evolution of the probability of sampling uh neighbor one versus neighbor two over time shows that
it's clearly it clearly goes towards the one he started at prior with um
the beliefs in more metabolic volatility lead to higher posteriors uncertainty
about the idea but it still eventually leads to um you know
believing in the same idea you initially started so
okay now this is much much more informative as to
the actual uh phenomenon and you can see here that we have two very interesting phenomenon
consensus and polarization um they emerge when simulating uh the
network we can see that every agent is generated by the action uh
the observations of every agent is generated by the actions of other agents um and so collective belief dynamics
here under different generative parameterization really show um
the the evolving beliefs of all agents about idea one or about idea two
in panel a and d we see polarization where two subset of agents end up believing in two different levels of the
idea of the idea hidden states with a high certainty so you can really see like they go very far it goes
one or zero it's not it's not like 0.6 no it's really one or zero they're really certain
and panels b and c on the other hand shows consensus where the whole network converges on the same opinion by the end
of the simulation this really showcases the rich phenomenology uh displayed by
collectives of active inference agents which validates our model really alongside known opinion dynamics model
and that was really able to replicate um distributions that we were trying to uh
to converge doors do you have any questions
yeah um maybe go back to the slides what kind of dynamics might result in
persistent diversity or not just the absolute consensus or
absolute bifurcation but like you did mention you said you didn't see there to be a continuum of like people
who aren't sure so what kind of parameters or what kind of cognitive mechanisms
would facilitate that so um lower epistemic confirmation bias
for sure would would potentially lead to more variety
we would look it to network structure eventually uh lower habit formation would definitely help as well as you can
see here it's uh and and also higher belief in volatility so if you believe that volatility is
high you're going to keep sampling a lot of people because you do believe that uncertainty is going to continue arising
right so these are three parameters that really lead to more diverse and less polarized beliefs and some ideas
because it's so interesting how you you captured like the two things you can do on a classic social media platform which is
decide who to follow and then kind of at a finer scale who to pay attention to
even though it's also partially like put in front of you with a feed in the algorithm but also it's a little bit of agency in like what you pay attention to
and who you follow at a slower time scale and then how you act and how that modifies the epistemic
niche and some people follow a lot and act little and vice versa and different
people's cognitive models get updated in a different way despite having access to similar platform affordances
so these are really great points in future studies one you might want to see how the niche responds so right now that
they're they're crafting their niches simply as a function of who they're talking to right but you could also
model the algorithm screwing with you right so the algorithm
knows you're looking for this so it's going to cut some things from you
and so you you like for instance um one way we could have done this is the niche could have determined well okay well
you're listening less to this so i'm not going to cut that connection i'm just not going to let it be broadcasted
to you right now so that's one way that the algorithm works right it basically selects things
it puts in your feed even though the people aren't gone they're still there you just see them less so that's that's one way we could have done like a
relationship with the niche and as you said yeah we could have modeled different kinds of behaviors for people who are more lurkers right how do their
beliefs change if they're not showing so that's one way that eventually we're going to be able to model like influencers
if they're people who potentially broadcast to a lot of people and a lot of the other people don't broadcast as
much so the beliefs of these people are going to be super influential as opposed to the beliefs of these smaller people
who are much less influenced so that's i mean there's a lot that can be done it's really cool uh but yeah
i'm excited about this the only problem in life is there's not enough time but yeah it's really cool
so anyway i'm gonna i'm gonna keep going because we're going towards the um the cool plot
um so there was an interaction between episode confirmation bias and network
connectivity here you can see a heat map of the mean polarization index across like
100 independent realizations of the multi-agent opinion dynamic simulations
for unique combinations of network connectivity and epistemic confirmation bias so in the bottom
the selected plot lines show extreme settings of p so p02 and p08
and uh y which is uh yeah so shaded areas around each line
represent the standard deviation of the polarization index across independent realizations so
this is hypothesis one we investigated hypothesis one or how
episomic confirmation bias so why and network connectivity p determine collective formation of epistemic
communities we systematically vary both epistemic conformation bias so 15 values
for epistemic confirmation bias tilling the range three and nine and network connectivity so 15 values for p tilling
the range 0.2 to 0.8 in networks of 15 agents and over 100
different realizations of each conditions for a hundred times steps so it's really a lot it's really a lot but
the results are beautiful and so we were trying to see how higher epistemic confirmation bites in sparse
network might drive the emergence of epistemic community uh through the the
formation of belief clusters that are both dense and far apart in belief space right so they really believe different
things um to assess the emergence of epistemic communities or clusters we define the
polarization index which measures the degree of epistemic spread in a system and so a high value of p so close to one
indicates more spread out beliefs and implies clustering in echo chamber formation whereas a low p
implies the network agents have similar beliefs about an idea or you know less um
less diversity or less polarization so it shows the effects of varying epistemic confirmation bias and network
connectivity on polarization it is clear in the first column of the heat map that highly spread out beliefs
can offer it can occur at all values of epistemic confirmation bias in the presence of a sparse connectivity
denser networks in general uh reduce the risk of polarization
as seen by the by the drop-off so how increased episodic confirmation bias
can still counteract this effect to some extent by marginally bumping up the risk of polarization so this is a really
interesting result but it comes back to what we were saying earlier a dense network means there's a lot of people
who you can see the opinion of and who may not agree with you so you have more access to people's beliefs
sparser networks means you're very quickly going to fall into an echo chambers because you're going to cut off
some some people you don't want to listen to and then boom you have no more connection with these people
there we go so in this one um you see another heat
map so these are really noisy we're sorry about that uh we redid them
for the for the reviewers but they're not ready so they're pretty noisy but i'm going to
help you uh make a little sense of them so here you have a heat map of the polarization index for 225 combinations
of inverse believe volatility so that's hypothesis two and epistemic confirmation bias
precision so the above right heat map i don't know if i'm pointing to the right i
yeah the heat map of the re-attendance rate
for 225 combinations of inverse believe volatility and epistemic confirmation
bias and below left it's a line plot of the most extreme rows of the
polarization heat map so below right is the plot line of the most extreme columns of the reattendance heat
map so for hypothesis two we modeled behavior under different values of
inverse social volatility to see how it would interact with epistemic confirmation bias
we swept over epistemic conformation bias and social volatility and we measured the reattendance rate
and polarization index for each configuration it portrays a complex picture of the
relationship between ecb and inverse social volatility in the case of high volatility over meta
beliefs agents are driven to periodically re-attend to neighbors in order to
resolve growing uncertainty about their beliefs you can see a higher average re-attendance rate
interestingly there seems to be an interaction between re-attendance rate and epistemic confirmation bias such that in the
presence of both high volatility and low epistemic confirmation bias the reattendance rate is maximized so
they'll they'll reattend the same people even if they have low epistemic confirmation
bias because you know there is they oh sorry they have high volatility they
constantly think that people are likely to change their mind so they're going to continue to keep attending these people
with um a little bit of a lower of all volatility they're it's not the lowest
though because if if you have the lowest setting of volatility you're just you know not
going to care so much what other people think you're just gonna keep reattending so we speculate that the absence of ecb
makes the epidemic value of attending to every neighbor pretty much equally high
and thus agents are going to continue revisiting neighbors uh sequentially
with the attendance preference for any given neighbor solely dependent on the time lapse between the last reading of
their last hashtag um so this is interesting it will lead to
diverse social attendance patterns such that agents will prefer to constantly sample either new neighbors with no
particular neighbor left or uh uncertainty driven resampling so they can either
sample everyone for example the same people but they but they'll they'll try to attend to their neighbors a lot
okay so here we have uh the last hypothesis hypothesis tree
we got there it's a heat map of the polarization index for all 225 combinations of
learning rate and epistemic confirmation bias precision so above right you have a heat map of
the re-attendance rate for 225 combinations and epistemic confirmation bias so the
parameters represent the centers of the normal distribution sampled from across trials for each configuration
below left the most extreme row of the polarization index heat map and below right the most extreme column of the
reattendency map so here we're trying to see if the polarization of networks via habit
formation follows hypothesis three we swept over ecb so 15 values uh tiling
the range three to nine and learning rates so 15 values tilling from zero to nine
and the networks were pretty small 15 agents with a connection probability of 0.4
and an inverse social volatility of uh you know six and as before the the same idea so nine
so etb was again normally distributed with a fixed mean
uh and a variance of one so we we we um we sampled from a normal distribution
and we eventually we lowered uh the the variance and it it gave us much better
results but um the learning rate was fixed for the condition to really understand what the
effect of it was the learning rate incentivizes agents to to the same neighbor by forming a habit
this competes with the epistemic value of attending to a new neighbor with unknown beliefs this tested the
hypothesis that a higher learning rate stronger habit formation increased polarization and here we can demonstrate
that a higher learning rate and epistemic confirmation bias interact to influence outcomes at the collective
level so a higher learning rate induces more polarization implying the formation of more stubborn epistemic communities
in the network okay so
do you want me to go into the takeaways that'd be awesome
okay so um here we showed a confirmation bias as an
epidemic phenomenon our agents have wise beliefs um we
saw that ecb confers a higher weight to information that comes from peers and that can lead to a bad bootstrap
um we find that opinion dynamics heavily depend on network density this was not
counter-intuitive but the way that it happens was a little bit counter-intuitive uh the clustering phenomenon is
exacerbated by adding the capacity to form habits so this is important
we found that east tb the presence of rabbit formation
exacerbated polarization due to the formation of echo chambers or tight
communities of agents that only read each other's hashtag and the contributing influence of beliefs
about social volatility to exploratory social sampling leads us to consider the role of norms
and social settings if an agent is incentivized via epistemic value or curiosity to pay
attention to neighbors whom they are uncertain about their social group could be a source of constant surprise as long
as their beliefs about the neighbors are constantly fickle so in other words even in the presence of a group of
like-minded peers thank you good burritos i guess um
burritos modification uh the best kind of niche modification i know right
ghost brings me peruse um so we we expect that increased beliefs about social volatility leads to
repeated retentive peers amongst one another um okay we have limitations in this work as
i said a very low number of people uh we only modeled beliefs of two
believe two exclusive ideas it would have been maybe more interesting to have more and we would have wanted to um
to notice the emergence of similar but distant sub communities as well um even
if they're not already uh connected so yeah that was that was all of it that
was all of it cool work really
fun to hear about um nice well if anyone's
watching live they can uh ask any questions otherwise what would you like to start
off by talking like when you present that for what audience what do people often ask about
um they ask the same questions you ask really they ask um what can we do about
social media how do we factor in the algorithm uh what this can
how this ties into misinformation um i guess this question we haven't really talked about the notion of
misinformation so that's something you're interested in let's hear about it yeah
so this is this information is kind of a tricky question right because you'd
think um you'd think that misinformation would be
if it doesn't agree with us if it's about something we don't agree with we cast it instantly as misinformation
and in fact um we tend to fall very heavily for most
sources of misinformation the only thing is uh we fall for misinformation that tends to
reinforce our view of the world so even if it's part of a sort of
conservative if you're if you're um more liberal more um
i forgot the word for not conservative but if you're more left
um if you're seeing some piece that's been crafted by the right but it kind of confirms your view of the world you're
more likely to integrate it and this is this is pretty important especially when we're trying to think
about the q and on people and and [Music]
people whose views aren't necessarily completely polarized but who want to
view the world as something they um they can unfold right something they
have they have control over the epistemic value that they can gather
um and so they're being fed information which feeds into that sort of meta view of the
world that they they can understand the hidden truth about the world and so
this becomes a sort of pool you know where it doesn't really matter when i pitch at you
so long as it gives you this sort of sensation that you have access to something that others really don't and
therefore you now understand the structure of the world a little better even if
when you take the whole thing together when you look at the entire structure of um
you know conspiracy beliefs they're extremely unlikely extremely
complex and one way that we've noticed that we can um
identify these conspiracy theories compared to you know
true facts they tend to have a really interesting structure which is they're very sparsely connected to very
large elements but like normally in a true in a true story and something that's real even if there's a
lot of elements or or fields that are combined there's a lot of connections amongst things right because because
it's real so you can really you can see from a lot of directions these real
connections if you lose one connection everything doesn't fall apart in conspiracy beliefs
those connections are so sparse that if you lose one the entire theory doesn't make sense anymore
so it's it's that's that's the kind of structure that we see so it's kind of sort of
you can see how this would have epistemic value right because everything is so surprising and uncertain that
people would like feel a lot of value from accruing all this information right so
i think that's where we fall into the bad bootstrap but there are other kinds of bad bootstraps like um
let's say um so i don't want to i don't want to make any community feel like they're
being targeted or that or or that i'm being negative towards it but
there are communities like let's talk about a cult right let's think about it called who who starts believing a very
niche set of beliefs and they the way that they do this is by cutting off contact to everybody else
right so it's much easier for me to instill a belief in you there's nobody else to tell you this is this crazy this
like what are you doing so one of the first thing is they tell you to cut off contact with a lot of people
they reinforce the beliefs constantly they punish anyone who who dissents because that's how you reinforce a
belief and then you find them in these sort of communities which are like
very only locally functional and if you take someone out of that community afterwards and you put them
somewhere else they're like kind of lost because well
that's not how the world works so like they they they're they need to re-learn
a lot of things they need to um develop behaviors that are distinct from
their previous belief systems that allow them to exist and and you know be humans in a already pretty complex civilization
system
that was very interesting about the resilience of the meta view so
how do we use active inference to study these different phenomena like how
do you connect the nodes and edges from the graph the generative model the
cognitive model how does that visualization representation connect
with like the phenomena that we want to model
i mean that's the that's the question isn't it that's what we're working on at the computational
phenomenology lab i have a theory um but it's not like it's still being developed but my sense
is um you're gonna start treating
events as observations right and you're gonna start treating
so you're a node you're here in the graph and everything around you is a sort of
observation and you're you're trying to determine
layers in the graph which becomes states right so you're going to move across the graph by trying to predict uh
effectively what is the next state and trying to see if this new thing that you're going to observe matches with the
state you're trying to see so um so that's just how you move in the graph and then
the way that you're going to establish what is true or not so that's one way to do it
there are other ways right there's also swarm um beliefs and stuff but like one way to do it is well
how much can i predict from this node how much is actually connected to this
node and if if we take this structure again of like the the graphs which are sparsely connected
and don't allow for any connection to be lost you're going to start seeing that
there's going to be a lot of dense connections between concepts and it's going to be very easy for you
to sort of find your way through the graph and be like well i can go there and i can go there and i can go there
and and and try to make predictions about the next potential nodes given these two that you or these
three that you already have right i have these three things and i know everything's sparse it's densely
connected i can go there it's easy and and if i go there i don't lose any connection to anything else so that's
one way another way to do this is agents are going to start forming
beliefs by observing real life or reality and agents who
have a lot of observations about the world are likely to you know have a more
accurate model of the world so the more they make predictions about things that eventually happen the more we can give
them a reliability rating right so like this person sees a lot of things one and two when
they say something it tends to happen so we give them a high rating and then you know the agents talk to one
another and sort of like uh coordinate their beliefs and eventually there's gonna be this dude over there that you
know says green and everybody else says right it says red and it's like well you know the probability of this green being true
like there's a high surprisal there the kicker is there's a high surprise though so we're
giving it a lower reliability rating but if it does end up happening well then the value is
you know it is much higher as well right because we reduced a lot of variational free energy here so like
like i think that's that's how we're going to get to these two things combined with the the graph
leading to the nodes that you can connect together and the agents with reliability ratings that
swarm towards a true belief are ways that we can integrate these things i think
cool the first mode you had i kind of wrote down it was like dense connections
ideas that have grounding you know good maps for territories more stable territory
more effective map it's like in a family if you went to someone else's family reunion you
shouldn't be too surprised that any given two people know each other because there's kind of a coherence or
there's a prior about the density of that network whereas if the network's very sparse
then um the coherence of it is susceptible to single facts being wrong so you kind of
point it to like where a thread will be tied well this person knew that person
that this money was sent here and then it's like if even one of those things weren't true then the whole contraption
is fallacious um and then and then like the dense connections
have an element of conformity to them because you have an intrinsically validating world model like the
epistemic network of epicycles and that way of predicting how the planets moved and then you have
insight from outside that goes against the conformity bias the prior
but that can be how the community can move into a new space
so we can't have like just novelty driven like simply different is better but we can't have simply the same is
better puts us in this active inference situation which is why it's so cool to
see epistemic modeling like you have all done
there's something really interesting here about the optimal space um
around which you start you know computing the right amount of
information so mark miller is working on this alex kiefer is working on this as well um i
know that we're working on it with also alejandra syria bruno lara so there's
this whole group we're working on like what is the optimal computation space right um
and so this is this is truly the question you just posed should i stay exactly where i
am or should i try consuming error and i think that's the beauty of groups and
this is where we sort of fall into what what a group is in terms of a market blanket right
so in the inner spaces of a group you'll have people who are less likely to start
consuming error they're just like you know they're just staying within what's being done and and
and that's stability right and then towards the external parts of the group there are people who are more
connected to other groups right and then who can start consuming error and this
because the internal parts of the group are very densely connected to one another because you know they're an
in-group this error can be passed in like um it
can be consumed in a way that is efficient for the group to deal with
through this like sort of um blanket
so the the real question becomes like what's an active state what's a sensory like
yeah a state at the level of a blanket for a group but you can start you can start to conceptualize it as like
you know your influencers and your lurkers right like the lurker is consuming information and the
influencers promote information and then this whole thing becomes sort of like
there are people who just consume what this one do says and there are people who just like
um push out information and then maybe they take a little bit of information but they have like you know this
this sparse network of people who are like like you know people who are like 90 000 followers but they themselves
follow three so so so then there's this like sort of layering of people who listen to others
and so the the smaller people who have less followers they're still connected to one another and there's degrees of
through which um i think information is passed and consumed and so what mark miller is trying to say is
that the computational optimal is where you compute enough error
that you continue to uh to grow in your sort of fitness
landscape so you're still learning about things you're still discovering
but you're still stable enough that no error is going to topple you right
so because you have all these other people here who keep your group relatively stable
you know that consuming a little bit isn't gonna like destroy your group right it's like
it's like think of um of a polycule like we're we know we're in love this new
metamorph is not gonna like break our up so it's good right um
so that's that's i think what allows like this sort of large-scale coordination
among groups is that there are people who are like specialized in consuming the error and who can only do this because there are other people who
ensure there's resources being produced for them yeah well um two thoughts so
one the core to periphery or fringe continuum it also happens like in ant
colonies where there might be a brood chamber that is the most homeostatically
controlled and then there's like a periphery out to like kind of a lobby or an anti-chamber where there is a lot
more like in and out and then of course that's the interface like with the external world
and so then there's um analyses with tracking of like where the ants go
and so there'll be some who's continue whose distribution spatially is more like the top parts of the nest or just
the entry room and a little bit in and there might be another one that spends more of its time
towards the core and spends then it goes a little bit out um but that last piece you said like
what roles contribute to colony or epistemic
community stability or collective open-mindedness or resilience like those are such
critical questions that people frame qualitatively every day
and so it's just really cool to have the conversation
and open it up to many different perspectives about what roles do play in communities and then
try to use the model to follow up and
describe complex situations rather than like constraining to what
communities can be or how they can regulate yeah and there's something beautiful about
active inference here right because we could like we can literally potentially measure or predict
what might be an optimal state for a group given the free energy that the
group can consume right so if we can understand how this consumption of error can be distributed over the group or at
least can be absorbed um we can say well listen we don't need to destroy your your q
anon group all we need to do is give you a little bit you know like enough in the right
distributed areas so that you guys integrated on your own and potentially shift without us having to
uh further push and and potentially even polarized like one of the worst things you can do with one of your q and on
family members is antagonize them because then they isolate and they're gone you're never finding them again
like they will they will be lost to that thing which will consume them and this is and it's it's not just true
for for for fringe groups it's it's true for a lot of groups where we're like we rely on that community for survival
as we said like there's a lot of communities out there who need to stay tight-knit because well it's beneficial
for them to be tight-knit so um let's say we're like a city right and
and there's nothing wrong inherently about being a city and what you want to do is to try to prevent a catastrophe
right but we can't we can't all be researching
the types of catastrophes that might happen and like someone's gotta you know make bread right so so you start having these
people who you can predict over time that i don't have to think about this i don't have to
pay attention to this scale because i'm paying attention to this and i know that
they can rely on that so my model of the scales makes it so that my role is super
clear and allows for others to make these predictions right so
i think i mean it's not fully um it's not fully realized yet and there's a lot of work
to be done still but i feel like we you know we have it's right there it's right there
here's something that kind of makes me think about like the city is enabled by specialization and all
these other features um what are epistemic infrastructure projects
like what are the thankless or thankful jobs
that people do like moderation governance care for themselves and for other
participants like what are those infrastructure tier
roles where it's like this is building the road so we we have to contextualize how well
this shop does in light of the effort to build the road and the community that contributed there and so
it kind of like opens up the idea of attribution and community and it's like very
generative space yes i feel like they um
it would be would be difficult to say that there is a very clear distinction in any given
infrastructure right so like every field
has people who innovate every field has people who just stay on tradition every
field has people who just provide like it's not it's not just like bakers just provide right there are people who
innovate in bread there are people who think of new recipes or think of new ways or try to bring the same recipes to
different parts of the world so like it's it's more distributed than that but
um i i really i really do think that these structures kind of self-emerge
right so like we all kind of have not i'm not gonna
make that but i do believe that there's um a natural instinct to
um to try something new once you have
the certainty that isn't gonna fall under you right
and because we have this sort of distribution of like uh people who have more or less money and people who have
had past experiences of having more or less money they kind of tend to focus and so it
naturally sort of synchronizes into well you know what i was poor my whole life
i'm gonna be careful i'm not gonna go crazy and that's why you know that the fallacy of the entrepreneur who had like
nothing and he became something like that that is bull like it is so easy to
be an entrepreneur when you have barely anything to lose you know the notion of risk
and capitalism isn't true you they can do it because to them the risk
is minimal if i lose everything tomorrow i can do it again so there isn't really a risk whereas if
if little lady over there who has like 20 000 in her bank account decides to
put everything in a business is a real risk it's a real risk and
like obviously she's less likely to do it because like
what happens to her children if she loses everything you know i mean like so there's going to naturally be these
tears of people who because of the the their states faced right so the
probability of them continuing accessing resources over time is is less
spread out they they have to stay con concentrate on this and by virtue of doing this they
also you know keep producing um value and resources for people who
tend to accrue this and thus have more way to you know trash
it out and innovate i mean there's a reason that it's so easy to go
to university when your parents are rich like obviously if you if you parents
have the means to support you you're going to try and continue studying longer and longer and it's much harder
if you have to support yourself it's not impossible but it's so much harder so anyway
yeah capitalism well to connect it to active inference you
kind of brought up the situational risk sensitivity and how that relates to
someone's experience and their situation and then in active inference the policy selection
for whether the binary decision go to this university or go to
some other path or a continuous policy it's broken down into that pragmatic or
kind of outcome or goal reward orientation as well as the epistemic
and so what happens when people don't have to
have anxiety or find out epistemically about how they're going to get pragmatic reward for their action
and how does that move us beyond the sort of like web 2 engagement maximization
[Music] relationship with platforms where
there's a very specific generative model generative process relationship and it's based around like behavioral
summaries of the person's time spent on the site or like their spending or something like that versus like taking
the cognitive rains and saying we want to have lower anxiety and we want people to be
exposed to different perspectives or some other preference for platforms that's
specified using an active inference framework there's a lot in there
ah so i'm going to try to so think of a think of
the generative model always like generative models aren't
one scale right there's scales on scales on scales and scales on scales and what happens when you when you go across
scales is that your your state's at one level becomes the observation at the next level and then it embeds and embeds
it in beds okay and then the embeddings can sort of like again
track into one another so i'm here and um there's the bear so i'm gonna stop
focusing on you which is a higher level i'm gonna focus on directly this right now and there's the bear and i'm gonna focus on the bear but eventually the
bear goes away because then you know i was having a hallucination and suddenly i can go back to a higher level
and start monitoring other things and notice okay well you know what this lasted a long time and maybe i should be
cooking because i'm gonna get hungry so i'm gonna you know slowly navigate the scales of where where i'm supposed to
put attention based on how the free energy is is rising at a given point in
this form all this is to say um for the web or for monitoring
or for resource attribution what am i really trying to do what i'm
trying to do is to make sure that a person never has to feel like they're
constantly putting out fires so anxiety is that right anxiety is the
constant belief that you're like peaking everywhere and you have to pay attention to everything you're hyper sensitive so
let's let's lower that let's feel like you can start like giving a little bit
more attention to a longer time frame or even a shorter one but just on the moment
because like all of the parts of your model are pretty certain like there's not going to be a fire
so like i have certainty across all my scales and i'm going to start paying attention
to just this now and then like i don't need to like you know give too much to my model
how do you do this with monitoring well with monitoring you're like well look given this trajectory right now and
given this personality type and given like what we know already about her she's gonna freak out in about five minutes about x and i'm monitoring this
so before she freaks out let's give a little reminder about this or
like um actually through iot or whatever let's start something like my dream is like
in the morning i wake up my breakfast is like started like nobody's starting it for me it's just starting so
you know i do my my house predicts the kinds of things i'm likely
to need so that eventually i i never like ever have to feel like i need to pay
attention to anything with too much like which too much uncertainty is going to rise anymore i'm not sure i answered
your question exactly but i feel like i'm going in that direction there's the um
preparing your breakfast when you wake up and there's sort of the cybernetics 1.0 version which is we have
a prediction about what time you're going to wake up and then we're just going to do it like setting the thermostat we're going to just prepare
it for it to be ready at this time then this is kind of taking that
physical biofeedback layer to another level but also
what should we epistemically forage for in the morning how do we experience
that sleep-wake transition in a way where like we wake up and sort of like
sharpen or become more vigilant and focus on the things that matter and
that have impact and at the end of the day sort of have some unwind or some sort of
relaxing process so that we can move into a healthy sleep
there was um ah there was this i'm watching a lot of youtube lately
it's like um there's this one dude who tried to replicate
a billionaire morning right it was it was striking what the billionaire does in the morning and
which is basically like i'm doing all this to make my body feel better and all that great and then
he did this stuff to think about who he wanted to be today and what kind of
qualities he wanted to embody and it's like yo i gotta think about not missing my bus
or whether i'm gonna freeze my house outside or whether you know i might get fired if i get laid like you see what i
mean like my concerns my direct epistemic concerns in the morning are fastly different from what that dude has
to care about because everything that i'm talking about he's certain about like he has no qualm about it he does
not care like so how might one sort of shift this well i
feel like there could be structures that we could put in place in order for someone to not feel like they have to you know feel that but also
maybe a focus i know it seems hard to say but maybe a focus on the things that he has to focus
on would potentially limit the sort of
you know constant need to feel like you need to
put out fires so let's say that i'm a smart interface and i'm like well
this person needs to be certain about these things because their life has x constraints well maybe we're going to do
is give you x report and look you don't need to worry about it it's there you have that information now what about you
tried to think about things that are longer scale what about you tried to think about things that if you had nothing else to
care about you'd start thinking about so you know maybe these are the sort of epistemic foraging that
would lead people to a slightly more peaceful life but maybe i'm coming from a very privileged place and maybe this
is completely unrealistic so you'd have to ask people who are much less privileged might have a
different view on this on this question awesome
points um just in our last few minutes like
what are you going to continue to work on or what are you excited about or what do you want to talk about or ask
anything you want to talk about well i mean you did you mentioned your paper but we never got to it
we have time or sure so with um a handful of co-authors
we wrote a paper about um using active imprints to study
specifically the epistemic community of science and so we as a group read and
shared your paper on epistemic communities and then took the idea of like this
epistemic entity and now we've seen active inference entities be at different scales
that's several years and many like um different things we've talked about there
including the narrative scale and so we thought well how could we model the scientific
epistemic ecosystem how can we do a systems description
of the scientific ecosystem so like the entities like the person but also the lab the
university the dao in the case of decentralized science or like web 3 or open science
how do we model the active entities and for the active entities
eventually flesh out a cognitive model like you've presented today
but also include the informational entities which map not on to the adaptive active inference
agents but the mere active inference agents so we can still model
the paper as like an entity but it doesn't have any policy selection that
it can engage in where or like a code can engage in limited policy selection um when it's
used by computer system and so the goal was to develop
an ontology the eos the active entity ontology for science that would be able to
link up natural language descriptions like i sent a message to my friend
person friend sent a message so have the natural language representation with the
graphical flowchart representation kind of like a social network
of different kinds of entities including the informational ones and then be able to connect that to a simulation
architecture
so sorry you cut off what i think oh so okay so you were going to try and simulate
agents using your ontology so basically like so the first eos paper from last week
we focused a little bit more on the conceptual and the history of
decentralized sense making and history of science and an introduction to web 3 and dsi
decentralized science and then some of our ongoing work and collaborations are to
go from the flow charts that we kind of sketched out in some of the figures like a funding
motif or an information sharing motif or communications motif
into a simulation that uses the active inference entity
model okay wow you really need to talk to maxwell about this like he's been trying
to think about how communities react to active inference specifically
and this this makes me feel this makes me think of lactose right like how there's this like core and then people
test out the the external hypotheses until they reach the core or if they don't reach the core then expands and so
there's something really cool there i can't wait to see more of this work
awesome um yeah i hope that we can continue strangely attracting and intertwining
and including just collaborators from different backgrounds in the discussion as
some people who are listening might be hearing about active inference for the first time and
might be connecting with like a community in us that likes to do this kind of modeling
and framing and also there's people who might be more familiar with the active inference modeling and hopefully this
like brought their attention to a really important and contemporary case and of course excellent recent
research yes let's do a interdisciplinary research for the win
cool anything else you want to add oh no we've covered a lot of graphs i
know i know seriously the time goes fast so thanks a ton for joining see you
around bye