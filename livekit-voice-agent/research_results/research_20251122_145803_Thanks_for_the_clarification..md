# Research Results
**Query:** Thanks for the clarification.
**Timestamp:** 2025-11-22T14:58:03.585018
**Summary:** The automatic evaluation protocol for CLAM assesses the effectiveness of the Selective Clarification framework designed to handle ambiguous questions using generative language models. CLAM, or CLarify-if-AMbiguous, aims to improve clarity by selectively prompting for additional information when questions lack specificity.

## Detailed Results

### Result 1
**Title:** CLAM: Selective Clarification for Ambiguous Questions with Generative Language Models
**URL:** https://arxiv.org/abs/2212.07769?utm_source=valyu.ai&utm_medium=referral
**Source:** valyu/valyu-arxiv

**Content:**
# 4. Automatic Evaluation Protocol

In this section, we introduce an automatic evaluation protocol that allows us to evaluate multi-turn dialogues without requiring human input. In the selective clarification QA setting (Figure 2), the user provides clarification when the model asks a clarifying question about an ambiguous user input. We show that we can automate this step of providing clarification using a language model that is given privileged information about the ambiguous question. On a high-level, we thus suggest that model evaluation should move towards *evaluation data-generating processes* rather than evaluation data sets.

The automated evaluation of dialogue systems is attractive given that human evaluations have numerous problems. They are too expensive for most researchers to access. They cannot be easily reproduced and are idiosyncratic in ways that are hard for external researchers to observe and critique (unlike automatic evaluations, whose flaws are relatively easy to examine). Lastly, in many cases experiments involve humans can create additional ethics risks that in even the best cases incur additional administrative and ethical approvals costs, which can reduce research iteration speed, and in the worst cases create hazards for research participants.

Instead, we therefore use a language model to provide clarifying information when asked. This then allows us to automatically evaluate performance on the selective clarification task. Using machine learning models to simulate users to evaluate dialogue systems has been suggested before (see e.g. Su et al. (2016)). To the best of our knowledge, our work is the first to suggest that a parallel corpus of unambiguous and ambiguous questions can be used to prompt large language models to provide clarifying information about ambiguous questions.

For selective clarification QA, the language model may ask the user for clarifying information about the user's initial question (see Figure 3). Instead of a human, in our protocol, an 'oracle' language model which has access to privileged information about the unambiguous question provides the clarifying information when asked (see Figure 4). Since our data set contains both ambiguous and corresponding unambiguous questions, we provide the oracle model with privileged information by including the unambiguous question

[_page_4_Figure_1.jpeg]: Using a language model to provide clarification. We prompt a language model to provide clarifying information given a clarifying question about an ambiguous user input. Our parallel corpus of ambiguous and corresponding unambiguous questions allows us to provide the unambiguous question to the oracle LM, based on which it can then provide appropriate clarifying information about the ambiguous question. See Figure 3 for a description of the other conversational turns.

in its prompt. When appropriately asked for clarification, the oracle can then reliably provide clarifying information based on the unambiguous question in its prompt.
['<FG id="_page_4_Figure_1.jpeg">\n**Figure 4**: Figure 4\n<F href="_page_4_Figure_1.jpeg">\nFigure 4. Using a language model to provide clarification. We prompt a language model to provide clarifying information given a clarifying question about an ambiguous user input. Our parallel corpus of ambiguous and corresponding unambiguous questions allows us to provide the unambiguous question to the oracle LM, based on which it can then provide appropriate clarifying information about the ambiguous question. See Figure 3 for a description of the other conversational turns.\n</F>\n</FG>']
**Published:** 2022-01-01

### Result 2
**Title:** CLAM: Selective Clarification for Ambiguous Questions with Generative Language Models
**URL:** https://arxiv.org/abs/2212.07769?utm_source=valyu.ai&utm_medium=referral
**Source:** valyu/valyu-arxiv

**Content:**
# 3. CLAM: Selective clarification Framework

In this section, we introduce CLarify-if-AMbiguous (CLAM)—a framework for language models to ask for selective clarification about possibly vague user questions.

The framework involves four stages, illustrated in Figure 2. In the first stage, the user asks a language model a question. The question is then classified as ambiguous or not ambiguous. For questions that are not ambiguous, we return the answer immediately. However, when questions are ambiguous, we generate a disambiguating follow-up question, as illustrated in Figure 3. The model then uses the entire dialogue, including clarifying information, to answer the original question as it was intended. Although we complete only a single iteration, it is also possible to

recur the clarification process until the entire dialogue is considered to unambiguously ask a precise question which is an interesting direction for future research. We describe this formally in Algorithm 1.

Implementing the CLAM framework requires choosing a specific technique for:

- classifying questions as ambiguous or not ambiguous;
- producing a clarifying question to follow up with.

In this paper, we implement both of these steps using prompting. To classify a question's ambiguity, we prompt the model using few-shot prompts consisting of examples of ambiguous and unambiguous questions from the given data set. For Ambiguous TriviaQA, for instance, we use the following prompt:

> Q: Who was the first woman to make a solo flight across this ocean? This question is ambiguous: True.

> Q: Who was the first woman to make a solo flight across the Atlantic?

This question is ambiguous: False.

Q: In which city were Rotary Clubs set up in 1905?

This question is ambiguous: False.

Q: Who along with Philips developed the CD in the late 70s? This question is ambiguous: False.

Q: Where is the multinational corporation based? This question is ambiguous: True.

Q: [question to be classified] This question is ambiguous:

We then take the model's log probability of the next token being True as a continuous predictor of whether the given question is ambiguous or not.

Interestingly, the fact that this works means that SotA models are able to detect ambiguous questions but do normally not ask the user for clarification. We conjecture that this is the case because there are few dialogues including clarifying questions in the pre-training or finetuning data sets of these models. We leave a thorough investigation of why current models do not ask for clarification for future work.

We then produce a clarifying question using another prompt. We simply append the string:

> "In order to answer this question, I have to ask the following clarifying question:"

to the original ambiguous question.

We use a zero-shot prompt on the Ambiguous TriviaQA data set, and a few-shot prompt on the more challenging CLAQUA data sets. We describe the data set specific prompts in Appendix B.

We then present the user with the clarifying question that is generated by the model based on this newly constructed prompt. Lastly, we present the combination of ambiguous question, clarifying question and the user's clarification to the language model to generate a final answer to the original question.

### 3.1. Meta-cognition

In humans, meta-cognition is the process of thinking about your own thought process. Working with foundation models, meta-cognition can involve using information that we have about the default sequence completion task to choose a new sequence completion task to perform instead.

In this paper, we use the example of prompting the model to detect whether a given question is ambiguous to then ask the user a clarifying question, rather than directly trying to answer the ambiguous question. But in broader contexts, one can imagine many useful pipelines in which a secondary classifier is used to 'redirect' the 'thought process' of a foundation model. For example, a classifier detecting some form of toxicity might be able to redirect the question to a more

constructive frame by selecting an alternative prompt, allowing it to answer the question in a less toxic way. Using this sort of pipeline, predictable failure modes can be gracefully and easily recovered from without resulting in any errors that are visible to the user. Chain-of-thought prompting (Wei et al., 2022) can be thought of as an implicit form of meta-cognition, while a more sophisticated pipeline might use additional information about the problem to shape the prompt construction.
[]
**Published:** 2022-01-01

### Result 3
**Title:** Clarification and transparency on ILR migration review
**URL:** https://pubmed.ncbi.nlm.nih.gov/PMC11999572?utm_source=valyu.ai&utm_medium=referral
**Source:** valyu/valyu-pubmed

**Content:**
Thank you for sharing your concerns [1]. I appreciate the opportunity to address these points and provide further clarification.

My review [2] began after reading a specific case report on ILR migration, which sparked my interest in exploring its occurrence and contributing factors. This led me to conduct an extensive literature search to identify relevant cases.

To ensure a comprehensive review, I used multiple databases, including PubMed, Cochrane, and CINAHL, as well as reference lists of related articles. I also reviewed preprints to capture the most current data, though I did not find any recent preprints directly related to this topic. It was only recently (30-03-2025) that I became aware of your group's work on this subject.

I have great respect for your research and the valuable contributions your team has made in this field. My methodology was independently developed, and I took great care to ensure originality. This review employed a systematic approach to meta-summarise case reports, focusing on a thorough review of these cases.

As researchers, we share a common goal of advancing scientific knowledge, and I fully uphold the principles of ethical research. If further discussion is needed to clarify any remaining concerns, I am more than happy to engage in dialogue. Additionally, I will inform the editorial boards of *American Heart Journal Plus: Cardiology Research and Practice* to ensure all relevant parties are aware of the situation and proper acknowledgment is made.

Thank you again for bringing this to my attention. Please do not hesitate to reach out if there is any additional information I can provide.

Kind regards

Dr A. Harfoush

30/03/2025

## CRediT authorship contribution statement
**Allam Harfoush:** Writing - original draft.

## Declaration of competing interest
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

**Published:** 2025-04-01

### Result 4
**Title:** Problem-Based Learning to Encourage Active Learning and Teamwork Among First Year Medical Students - Student Reports in 2020 - What is the Best Response When Listeners Fail to Hear English Correctly? (Course name: Listening Skills: Development and Assessment)
**URL:** https://pubmed.ncbi.nlm.nih.gov/PMC11284285?utm_source=valyu.ai&utm_medium=referral
**Source:** valyu/valyu-pubmed

**Content:**
## Introduction
Seeking clarification is one of the vital skills that language learners need to acquire. Compared with native speakers, language learners encounter many occasions where they cannot understand what the other people are saying. The lack of understanding comes from various reasons, such as insufficient vocabulary knowledge, limited cultural knowledge, or simply the fast speech rate. A member of our team is an international student who understands the difficulty of learning a foreign language. Adapting to life in a foreign country necessitates the ability to seek clarification when failing to understand the meanings of utterances. Even when there are no language barriers, we need to seek clarification in many occasions. For example, during lectures, an unavoidable problem for the students is that students sometimes fail to hear an utterance correctly owing to a loss of concentration[1]. If we cannot understand what the others are saying, various problems arise. For language learners, they cannot communicate with others. For students, they cannot learn what they are supposed to.
For the reasons stated above, we think this issue is an interesting topic for exploration. Correspondingly, this research investigated the best way to seek clarification by administering questionnaires to Japanese students and four teachers (three from the US and one from Canada) who are native English speakers.

## Literature review
The purpose of the current research is to inquire into the most effective strategies for seeking clarification in situations where utterances are misheard or misunderstood and to examine how native and non-native speakers of English use different strategies for seeking clarification.
Mizuta[2] examined language learners' use of strategies in listening to a lecture. The participants were Chinese students who studied Japanese. They listened to a lecture in Japanese and reported their listening comprehension process. Based on the results, Mizuta classified the reasons for mishearing into external distractions, a lack of recognition, a lack of vocabulary, and a lack of understanding of connections. External distraction is related to listeners losing focus, and a lack of recognition refers to the failure to understand speech sounds. A lack of vocabulary means listeners may encounter problems understanding certain words, and a lack of understanding of connections pertains to listeners' comprehension of the meanings of words or phrases but not the link between these within a sentence.
Tsubaki[3] conducted a study about teaching communication strategies. The participants were international students who studied Japanese at a university in Japan. The participants received instruction about how to use communication strategies in conversations. The results showed that half of the participants acquired the skills of asking back after the training. In her study, Tsubaki advocated a theory that posited five patterns of seeking clarification. These patterns are requesting to repeat an utterance, requesting for explanation, repeating unknown words, checking for understanding, and attempting to understand utterances indirectly. A request to repeat an utterance means asking someone to restate a sentence, while a request for an explanation means asking for elaboration. Repeating unknown words involves restating a word that is unfamiliar to a listener, and checking for understanding means verifying if meaning is comprehended by asking a question. Finally, attempting to understand utterances indirectly entails grasping a word or phrase through some other known information. Clarification questions play a significant role to attain mutual understanding in spoken dialogue systems. Gabsdil[4] defines the term clarification question or clarification request as the questions that speakers ask when they do not fully understand or is uncertain about what the previous speaker said or meant with an utterance. According to Schlangen[5], clarification requests vary in their form and their function. Clarification requests take various forms, such as conventional forms, full sentences and sentential fragments. Regarding functions of clarification request, they include acoustic understanding and possibility. Linguistic differences between English and Japanese should also be mentioned. Modern English is an analytic language that primarily conveys relationships between words in sentences through particles, prepositions, and similar components[6]. For example, “laugh on” and “laugh at” carry varying meanings, given the change in prepositions. By contrast, Japanese is an agglutinative language, in which differences in morphemes comprising words determine their meanings[7].
Based on the past studies stated above, seeking clarification is a vital skill that language learners need to acquire. Also, comparing native speakers' ways to seek clarification with those of language learners give important suggestions to language learners who need to improve their communication skills in target language.
The following are the research questions (RQs) for the current study.
RQ1: What are the main reasons for language learners' failure to hear utterances?
RQ2: How are language learners seek clarification when facing different situations of mishearing?
RQ3: Are the ways language learners seek clarification different from those used by native speakers?
Regarding the way language learners seek clarification, we hypothesized that attempts at indirect understanding would be the favored strategy. Tsubaki[3] argued that endeavors to understand utterances indirectly do not change the flow of Japanese conversations. Therefore, we hypothesized that this idea also applies to English conversations.

**Published:** 2022-11-18

### Result 5
**Title:** CLAM: Selective Clarification for Ambiguous Questions with Generative Language Models
**URL:** https://arxiv.org/abs/2212.07769?utm_source=valyu.ai&utm_medium=referral
**Source:** valyu/valyu-arxiv

**Content:**
# 2. Selective Clarification QA Data Set

User: Provide clarification LM: Give final answer In this section, we introduce a data set that allows us to evaluate the performance on *selective clarification QA* (Figure 2). Selective clarification QA models the real-world observation that some user questions will be well-defined and thus will not need clarification, while other user questions will be ambiguous, and require clarification. The desired behaviour of a language model is to directly provide answers to unambiguous questions without asking for unnecessary clarification and on the other hand, ask the user for clarification if the user's question is ambiguous.

Existing data sets such as ClariQ (Aliannejadi et al., 2020) and CLAQUA (Xu et al., 2019) do not allow us to evaluate models on all the steps of the selective clarification QA setting, see Table 1. We describe existing data sets and their limitations in Section 5.

To study this setting, we therefore introduce a data set of pairs of questions that we call Ambiguous TriviaQA. For each pair, there is one ambiguous question and one precisely disambiguated question. We construct the data set so that just one piece of clarifying information is needed to make an ambiguous question precise. In Section 4, we explain how these sets of ambiguous and unambiguous questions let us automatically provide clarify ambiguous questions.

Our data set consists of 200 pairs of ambiguous and unambiguous questions that we derive from TriviaQA (Joshi et al., 2017). Given a randomly sampled TriviaQA question, we derive an ambiguous question by either:

**clarification** Figure 3. Overview of the prompts used to clarify ambiguous user inputs. In step 1a, the user asks an ambiguous question. In step 1b (omitted for clarity) the question is classified as ambiguous using a few-shot prompt. In step 2, the model is few-shot prompted to generate a clarifying question about the ambiguous user input. In step 3, the user (or an oracle model, see Section 4) provides clarifying information given the clarifying question. In step 4, the model is prompted to answer the initial question given the clarification from the user.

- Replacing a noun phrase with a class the noun belongs to, e.g. "Which country is Europe's largest silk producer?" becomes "Which country is Europe's largest producer?"
We use closed-book TriviaQA questions, that is, questions that stand alone and for which no accompanying context is provided. An additional advantage of deriving a data set from TriviaQA is that the reference answers are typically short, and only contain few non-essential words both of which increase the reliability of automatic accuracy metrics to evaluate models.
[]
**Published:** 2022-01-01

### Result 6
**Title:** Taking Action Towards Graceful Interaction: The Effects of Performing
  Actions on Modelling Policies for Instruction Clarification Requests
**URL:** https://arxiv.org/abs/2401.17039?utm_source=valyu.ai&utm_medium=referral
**Source:** valyu/valyu-arxiv

**Content:**
Actions on Modelling Policies for Instruction Clarification Requests

Authors: Brielen Madureira, David Schlangen

Title: Taking Action Towards Graceful Interaction: The Effects of Performing
  Actions on Modelling Policies for Instruction Clarification Requests

 Authors: Brielen Madureira, David Schlangen

 Content: # 1 Introduction

The concept of *graceful interaction* (Hayes and Reddy, 1979, 1983) was proposed as a set of skills that machines should exhibit to properly engage in cooperative dialogue with humans, among which are being able to ask for, understand and offer clarification. More than forty years later, the ineptitude of large language models and voice assistants to handle underspecifications and to properly process or produce clarification requests (CR) is still being documented (Larsson, 2017; Kuhn et al., 2022; Li et al., 2023; Deng et al., 2023; Shaikh et al., 2023). It is also one of the acknowledged limitations of the currently prevailing commercial chat-optimised LLM.1

[_page_0_Figure_9.jpeg]: Clarification requests posed by an instruction follower, demonstrating uncertainty on deciding what actions to take due to ambiguity or underspecification. From: CoDraw dialogue game 8198, CC BY-NC 4.0, cliparts from Zitnick and Parikh (2013).

Given that they are modulated for instructions, this seems to be a peculiar fault: CRs are a crucial mechanism used to repair misunderstandings in instruction following interactions (Benotti, 2009), as we see in Figure 1. On second thought, it comes as no surprise. Clarification exchanges are metacommunication acts that do not normally appear in non-interactive data (Kuhn et al., 2022) and are also relatively rare in dialogue data. As a specific dialogue phenomenon, CRs have an empirical frequency of 4% of turns in spontaneous conversations to 11% of turns in strictly instructionfollowing interactions (Purver et al., 2001; Benotti and Blackburn, 2021; Madureira and Schlangen, 2023b). Therefore, it is still unclear to what extent CR strategies can be learnt with data-driven approaches (Benotti and Blackburn, 2021).

Many existing CR datasets, despite their utility for applications like conversational search (Keyvan and Huang, 2022; Rahmani et al., 2023), either have not been collected via real interactions or are synthetic, so that learnt CR policies may not correspond to genuine human behaviour. Moreover, current best-performing data-driven models are still

<sup>1</sup> In the blogpost releasing chatGPT, the limitations section says: "*Ideally, the model would ask clarifying questions when the user provided an ambiguous query. Instead, our current models usually guess what the user intended.*". Source: https: //openai.com/blog/chatgpt.

not doing very well in deciding when to request clarification (see §2), and we must understand why.

CRs can occur in all four levels of communication (Clark, 1996): Attention (due to problems in the channel), identification (due to acoustic impediments), recognition (when the signal is understood but a lexical, parsing or reference problem manifests) and consideration (when the intention is unclear) (Rodríguez and Schlangen, 2004). Instruction CRs (iCR) emerge mostly at Clark's 4th level of communication (Clark, 1996), *i.e.* at the level of uptake (Schlöder and Fernández, 2014), to solve ambiguities and underspecifications.

Recently, Madureira and Schlangen (2023b,a) have argued that the multimodal CoDraw game (Kim et al., 2019) is a rich resource for iCRs, naturally produced as a by-product of game playing via actions, as in the example in Figure 1. This dataset offers a balance between size (in comparison to well-curated but small corpora) and retaining ecological validity (as opposed to massive datasets collected or crafted artificially). Supposing underlying iCR strategies can emerge from data, we can reasonably assume that action-taking is a key component in modelling policies for deciding when and what to repair in this type of game.

However, one major drawback of the proposed baseline models is the *overhearer* paradigm: Models are not trained to act as authentic dialogue participants. Instead, they process other people's interactions, and at some points have to predict when to ask iCRs, a decision detached from the actual actions required by the game. Understanding is different for overhearers and addressees, and the latter have advantages in building common ground (Schober and Clark, 1989). Clark (1992) argues that subjects in psycholinguistics are actually usually treated as overhearers; we add to that that many NLP approaches are also modelling overhearers.

Contributions Given that background, this work aims to expand the boundaries of the open question of learning meta-communication acts from human data. We do that by (i) implementing a more wellmotivated model for learning *when to ask* iCRs in CoDraw; (ii) taking another step towards a more realistic agent by defining and modelling the task of *what to ask* about; and, most importantly, (iii) testing three hypotheses to study the effect of actiontaking in learning iCR policies, verifying whether a measure of certainty can be used to probe for iCR abilities and inform predictions.

## 2 Related Work

Learning *when to ask* questions The problem of knowing when to ask questions in an interaction appears in various contexts. Relevant work has been done in language-aided visual navigation (Nguyen and Daumé III, 2019; Thomason et al., 2020; Chi et al., 2020; Nguyen et al., 2022), in which the agent must take actions in an environment and decide when to ask for help, where RL is a suitable method. Similar policies are necessary in interactive settings like visual dialogue games that require deciding when to stop asking (Shekhar et al., 2018) or incremental predictions on when to answer a question (Boyd-Graber et al., 2012).
['<FG id="_page_0_Figure_9.jpeg">\n**Figure 1**: Figure 1\n<F href="_page_1_Figure_1.jpeg">\nFigure 1: Clarification requests posed by an instruction follower, demonstrating uncertainty on deciding what actions to take due to ambiguity or underspecification. From: CoDraw dialogue game 8198, CC BY-NC 4.0, cliparts from Zitnick and Parikh (2013).\n</F>\n</FG>']
**Published:** 2024-01-30

### Result 7
**Title:** Problem-Based Learning to Encourage Active Learning and Teamwork Among First Year Medical Students - Student Reports in 2020 - What is the Best Response When Listeners Fail to Hear English Correctly? (Course name: Listening Skills: Development and Assessment)
**URL:** https://pubmed.ncbi.nlm.nih.gov/PMC11284285?utm_source=valyu.ai&utm_medium=referral
**Source:** valyu/valyu-pubmed

**Content:**
## Discussion

### RQ1: What are the main reasons for language learners' failure to hear utterances?
The findings related to Question 1 showed that failure among the respondents to hear and understand content was most frequently caused by limitations in vocabulary. These results support what Mizuta[2] argued. According to Mizuta, a lack of vocabulary is one of the reasons why language learners mishear in their listening comprehension process. Speed was the most common cause of the participants' failure to hear understandable sentences. These results point to the importance of being careful with these two aspects so that people can correctly hear utterances.

### RQ2: How are language learners seek clarification when facing different situations of mishearing?
The most popular answers to Question 2 were “request to repeat” and “request to explain” in various situations of mishearing. Both can be classified as instances of direct asking, which contrasts with indirect asking, such as attempts to understand utterances indirectly and checking for understanding.” We initially hypothesized that attempts at indirect understanding would be the favored strategy. This assumption was promoted by Tsubaki[3], who asserted that endeavors to understand utterances indirectly do not change the flow of Japanese conversations. We speculated that this idea is also applicable to English conversations. The results negated our hypothesis.
Some of the Japanese participants could not ask for clarification in an indirect manner because English and Japanese are different languages. As the structure of English is different from that of Japanese, some Japanese learners' insufficient language skills prevent them from asking for clarification in an indirect manner.
The choices made by the Japanese non-native students and native English teachers were compared. In all the cases (Questions 2a-2d), the most frequent choices made by the students were identical to those made by the teachers. That is, both groups tended to choose “asking directly” as a response. This finding suggests that whether listeners are native or non-native English speakers does not matter considerably.
The comparison of the results on two types of failure to hear (able to hear but could not understand meaning and able to understand but could not recognize an utterance) uncovered certain trends. For the most frequently occurring failure-the ability to understand accompanied with the inability to recognize an utterance-the most popular solution was to request repetition. For the other type of failure, the most favored strategy was to request an explanation. These findings are logical because the chosen strategies are the shortest way to solve the corresponding problems. People change their approaches depending on what a problem is.
For the other type of failure-the ability to understand accompanied with the inability to recognize an utterance-the second common strategy was attempting to understand utterances indirectly. These results accord with the argument suggested by Schlangen[5]. Schlangen stated that clarification request vary in their form and their function.

### RQ3: Are the ways language learners seek clarification different from those used by native speakers?
In order to compare the way language learners and native speakers seek clarification, we asked four faculty members whose native language was English. We observed some similarities and differences between the students and native speakers. About Question 2a, talking to a best friend, all of the native speakers chose the direct way of asking, “What's ‘ennui'?” In case of the students, even though half of them chose the same option, repeating, “Did you say ‘ennui'?” was the second most popular response. About Question 2c, talking to an older person, most of the students chose “Sorry, could you please say that again?” However, the responses from native speakers varied. Two of them chose a direct way, “What does ‘Alu sequence' mean?” Only one native instructor chose “Sorry, could you please say that again?”
We also observed some differences in the students' responses depending on their language proficiency levels. Among those who chose the strategy of attempting to understand utterances indirectly as answers to Questions 2b and 2d, approximately 60% to 70% were from English classes A and B-classes attended by high-level English users. It can be hypothesized that individuals who can handle English better tend to choose indirect understanding, as this strategy requires high English proficiency. The differences between native speakers and language learners, as well as those between high-proficient and low-proficient learners could be due to linguistic differences. As stated in the past studies, English is an analytic language conveying relationships between words in sentences through particles, prepositions, and similar components[6]. Compared to English, the meanings in Japanese are determined by morphemes. As English speakers try to find relationships between words, they might opt for indirect understanding.

## Conclusion
The study's findings are summarized as follows: First, the most common causes of hearing failure were a lack of vocabulary and speech speed. Second, “asking directly” was the most popular strategy for seeking clarification. Note, however, that the native speakers and highly proficient students tended to favor indirect understanding. No clear patterns were found when the fellow interactant of a speaker was different, familiar versus unfamiliar. In the future, more accurate conclusions would be obtained using more randomized and larger samples.

## Funding
No funding was received.

## Author contributions
MK, MS, and HM planned the work and wrote the manuscript. RF supervised the work and revised the manuscript. All authors read and approved the final manuscript.

## Conflicts of interest statement
The authors have declared that no conflicts of interest exist.

**Published:** 2022-11-18

### Result 8
**Title:** CLAM: Selective Clarification for Ambiguous Questions with Generative Language Models
**URL:** https://arxiv.org/abs/2212.07769?utm_source=valyu.ai&utm_medium=referral
**Source:** valyu/valyu-arxiv

**Content:**
We first establish the overall accuracy improvement of our implementation of the CLAM framework on selective clarification QA (steps 1 through 4 in Figure 2). Then, we study the performance on each of the necessary steps in Figure 2: detecting ambiguous questions (step 1b), generating useful clarifying questions (step 2), and giving final answers after

[_page_5_Figure_10.jpeg]: CLAM improves question-answering accuracy on a set of ambiguous and unambiguous Trivia questions. (a) CLAM clarifies ambiguous questions without asking for unnecessary clarification on unambiguous questions (which is reflected in the adjusted accuracy metric). Always prompting the language model to ask the user for clarification increases the accuracy on ambiguous questions but incurs a penalty on unambiguous questions. The prompting baseline rarely asks the user for clarification and thus only improves the accuracy slightly. (b) Accuracy on full data set: Without penalizing unnecessary clarifying questions, always prompting for clarification and CLAM perform comparably well, and much better than default GPT and the prompting baseline. CLAQUA and ClariQ only cover parts of the selective clarification pipeline which is why only TriviaQA results are reported here.

receiving clarification (step 4). Lastly, we show that our automatic evaluation scheme for selective clarification QA works reliably, by showing that the oracle language model correctly provides clarification when asked (step 3).

We report the results of the text-davinci-002 model in the main part of the model and provide the results for davinci in the Appendix. davinci performs less well across all tasks but the differences between the different methods are qualitatively similar to those of the text-davinci-002 model.

ClariQ and CLAQUA each only contain components to evaluate some of the parts of the pipeline (see Table 1), and some figures thus report results on a subset of the data sets.

[_page_6_Figure_1.jpeg]: CLAM reliably distinguishes ambiguous from unambiguous questions. The AUROC measures how accurately the different methods predict whether a given question is ambiguous or not. *Default GPT* almost never asks for clarification whereas *Force clarification* always asks for clarification. Both methods thus do not distinguish ambiguous from unambiguous questions.
['<FG id="_page_5_Figure_10.jpeg">\n**Figure 5**: Figure 5\n<F href="_page_5_Figure_10.jpeg">\nFigure 5. CLAM improves question-answering accuracy on a set of ambiguous and unambiguous Trivia questions. (a) CLAM clarifies ambiguous questions without asking for unnecessary clarification on unambiguous questions (which is reflected in the adjusted accuracy metric). Always prompting the language model to ask the user for clarification increases the accuracy on ambiguous questions but incurs a penalty on unambiguous questions. The prompting baseline rarely asks the user for clarification and thus only improves the accuracy slightly. (b) Accuracy on full data set: Without penalizing unnecessary clarifying questions, always prompting for clarification and CLAM perform comparably well, and much better than default GPT and the prompting baseline. CLAQUA and ClariQ only cover parts of the selective clarification pipeline which is why only TriviaQA results are reported here.\n</F>\n</FG>', '<FG id="_page_6_Figure_1.jpeg">\n**Figure 6**: Figure 6\n<F href="_page_6_Figure_1.jpeg">\nFigure 6. CLAM reliably distinguishes ambiguous from unambiguous questions. The AUROC measures how accurately the different methods predict whether a given question is ambiguous or not. *Default GPT* almost never asks for clarification whereas *Force clarification* always asks for clarification. Both methods thus do not distinguish ambiguous from unambiguous questions.\n</F>\n</FG>']
**Published:** 2022-01-01

### Result 9
**Title:** CLAM: Selective Clarification for Ambiguous Questions with Generative Language Models
**URL:** https://arxiv.org/abs/2212.07769?utm_source=valyu.ai&utm_medium=referral
**Source:** valyu/valyu-arxiv

**Content:**
### 5.1.1. OVERALL PERFORMANCE

Overall, we find that CLAM boosts the language model's adjusted accuracy on ambiguous TriviaQA (containing both ambiguous and unambiguous questions) by roughly 20 percentage points (Figure 5a). Recall that the adjusted accuracy multiplies the accuracy on a given question with a penalty term λ = 0.8 each time the model unnecessarily asks for clarification on unambiguous questions as described in Section 5. *Force clarification* improves the accuracy on ambiguous questions but incurs a large penalty on unambiguous questions for unnecessarily asking for clarification. Using the *Prompting baseline* only leads to a moderate accuracy improvement. Without the penalty term for asking unnecessary clarifying questions, the performance of always prompting for clarification and *CLAM* on the data set of both ambiguous and unambiguous questions is comparable, and they both clearly outperform default GPT and the prompting baseline (Figure 5b).

On the ambiguous questions only, we find that, as expected, both *Force clarification* and *CLAM* greatly improve the question-answering accuracy as compared to the default GPT performance, see appendix Figure 10a. Importantly, always clarifying and CLAM almost entirely close the gap on performance on ambiguous questions as compared to the performance on unambiguous questions, see appendix Figure 10b. On the unambiguous questions, the different methods generally do not affect the model performance as compared to the default GPT behaviour. However, always prompting for clarification always leads to unnecessary turns of conversation on unambiguous questions which is bad for the user experience, and sometimes actually hurts the accuracy by leading the conversation off-topic.

[Table 2]: LMs can accurately generate clarifying questions and provide clarification during evaluation. Human evaluation of each of the conversational turns. *ClariQ* does not contain answers for the ambiguous questions and is thus not displayed in this table.

### 5.1.2. INDIVIDUAL PIPELINE COMPONENTS

### Step 1b: Detect Ambiguity

*CLAM* reliably distinguishes ambiguous from unambiguous questions, see Figure 6. The few-shot prompting-based log probability of a given question being ambiguous or unambiguous achieves high AUROCs on all data sets. *Default GPT* almost never asks for clarification and thus achieves an AUROC of roughly 0.5 on all data sets. *Force clarification* on the other hand treats all questions as ambiguous questions, and thus always has an AUROC of 0.5. The *Prompting baseline* does sometimes asks for clarification on ambiguous questions and almost never asks for clarification on unambiguous questions, and is thus slightly better than random at detecting ambiguity.

### Step 2: Ask clarifying questions

We manually label 100 randomly selected pairs of ambiguous questions and model-generated corresponding clarifying questions for each data set to test how reliably the language model generates the correct clarifying question (Table 2). According to our judgment, the model generates the correct clarifying question for 84%, 99% and 95% of the questions in Ambiguous TriviaQA, CLAQUA I and CLAQUA II respectively. We find that on TriviaQA the model sometimes asks incorrect clarifying questions either by just repeating the given ambiguous question or by asking an unrelated additional question about the subject of the ambiguous question.

### Steps 2 through 4: Final answer after clarification

Ignoring the task of detecting ambiguity and focusing only on questions which are known to be ambiguous, asking the user for clarification lets the model answer ambiguous questions much more accurately for all data sets (Figure 7).

### Step 3: Oracle automatic evaluation

Our oracle language model (Section 4) provides accurate clarifying information given a clarifying question by the language model under evaluation. We manually label 100 randomly sampled conversations based on ambiguous ques-

[_page_7_Figure_1.jpeg]: Prompting the model to ask the user for clarification improves QA accuracy on ambiguous questions. ClariQ does not contain answers for the ambiguous questions and is thus not displayed in this figure.

tions from Ambiguous TriviaQA, CLAQUA I and CLAQUA II. We report for what fraction of correct clarifications the oracle language model provides.

The oracle model reliablly provides the correct clarifying information on TriviaQA and CLAQUA II, see Table 2. On CLAQUA I the clarifying information has to disambiguate two possible meanings of a proper noun. We find that, while the model is generally able to do so, it will sometimes provide information that applies to both possible entities, and thus does not correctly disambiguate the two options.
['<FG id="Table 2">\n**Table 2**: Table 2\n<T href="Table 2">\n| METHOD | AMBIGUOUS TRIVIAQA | CLAQUA I | CLAQUA II |\n| --- | --- | --- | --- |\n| STEP 2:CORRECT CLARIFYING QUESTION | 84.0% | 99.0% | 95.0% |\n| STEP 3: CORRECT ORACLE ANSWER | 98.8% | 67.7% | 98.7% |\nTable 2. LMs can accurately generate clarifying questions and provide clarification during evaluation. Human evaluation of each of the conversational turns. *ClariQ* does not contain answers for the ambiguous questions and is thus not displayed in this table.\n</T>\n</FG>', '<FG id="_page_7_Figure_1.jpeg">\n**Figure 7**: Figure 7\n<F href="_page_7_Figure_1.jpeg">\nFigure 7. Prompting the model to ask the user for clarification improves QA accuracy on ambiguous questions. ClariQ does not contain answers for the ambiguous questions and is thus not displayed in this figure.\n</F>\n</FG>']
**Published:** 2022-01-01

### Result 10
**Title:** CLAM: Selective Clarification for Ambiguous Questions with Generative Language Models
**URL:** https://arxiv.org/abs/2212.07769?utm_source=valyu.ai&utm_medium=referral
**Source:** valyu/valyu-arxiv

**Content:**
# 5. Experiments

In this section, we experimentally validate the ability of CLAM to successfully detect and seek clarification to ambiguous questions.

We first demonstrate its overall improved accuracy on the end-to-end task of question answering on a data set that contains both ambiguous and unambiguous questions.

We then evaluate the performance on CLAM on each step of the pipeline (Figure 2) that involves the language model individually: step 1b, distinguishing ambiguous from unambiguous questions; step 2, generating appropriate clarifying questions; and step 4, giving correct final answers given clarifying information.

Lastly, we evaluate whether our automatic evaluation setup works reliably. That is, we test whether the oracle language model reliably provides the correct clarification when presented with a clarifying question.

Models: In principle, our framework should apply to any large language model architecture. In our experiments, we use the text-davinci-002 and davinci models via the OpenAI API. davinci is a pre-trained language model similar to the original GPT-3 model (Brown et al., 2020) Table 1. Overview of which data sets can be used to evaluate which of the steps of selective clarification QA.

and text-davinci-002 1 is a GPT-3 model with an additional supervised fine-tuning stage on human-written demonstrations. These models are publicly available to researchers from any institution, which improves the reproducibility of our results and evaluation protocol. It can, however, be difficult to confirm whether the currently actively served version of the model is the same as the one used in these experiments, which is a challenge for reproducibility.

Data sets: There are many different types of ambiguity in text (see (Keyvan & Huang, 2022) for a taxonomy). To account for this, we evaluate CLAM on a range of data sets that cover different types of ambiguity. Our own data set *Ambiguous TriviaQA* (described in Section 2) primarily covers under-specified user questions. *ClariQ* (Aliannejadi et al., 2020) is an information retrieval data set consisting of real search engine queries from the TREC Web Track (Clarke et al., 2012). For each query human labellers also indicate on a scale of 1 to 4 to what extent clarification is needed. We convert ClariQ into a binary classification problem by labelling queries with *clarification needs* of 1 and 2 as unambiguous and queries with *clarification needs* of 3 and 4 as ambiguous. Furthermore, we evaluate CLAM on *CLAQUA* (Xu et al., 2019), a data set consisting of two sub-datasets that cover different types of ambiguity: a task that we call *CLAQUA I*, in which a proper noun in the question can refer to different entities, and a task that we call *CLAQUA II* which consists of multi-turn conversation where the last turn is a question that could refer to multiple different previous conversational turns. To reduce the costs of our experiments from calling the OpenAI API, we use random sub-samples of 400 of each data set when evaluating ambiguity detection, and 100 random samples from each data set to evaluate the generation of clarifying questions and question answering accuracy.

However, only our data set can be used to evaluate all of the steps of our pipeline end-to-end. Because of limitations in the design of the other data sets, which were designed for different purposes, they can only be used for a subset of the steps in our pipeline. Table 1 provides an overview of which data set can be used to test which of the steps.

Metrics: We measure the accuracy of a model answer by

<sup>1</sup> https://beta.openai.com/docs/model-index-for-researchers

evaluating whether the model answer contains the reference answer. This accounts for the fact that the language model often answers in full sentences while the reference answer consists only of the target terms themselves.

One challenge in the automatic evaluation of free-form generations is that one answer can be expressed in many different ways, see e.g. Kuhn et al. (2022). To account for this, we manually evaluate the accuracy metric on all of our data sets. Similarly, we manually evaluate whether the language models ask appropriate clarifying questions.

In addition to the raw accuracy, we introduce an *adjusted accuracy* which is suitable for selective clarification QA specifically. This measure penalizes the language model system for asking unnecessary clarifying questions about unambiguous questions. To adjust the accuracies we begin with a score of 1 for a correct answer and 0 for an incorrect answer (as normal) but then multiply it with 0.8 if the question is unambiguous and the model nonetheless asks for clarification. The specific value of 0.8 is arbitrary and our results hold for a range of penalty terms, see Table 4.

To evaluate how well the different methods can distinguish ambiguous from unambiguous questions, we measure the commonly used Area Under the Receiver Operator Characteristic Curve (AUROC). The AUROC metric is equivalent to the probability that a randomly chosen correct answer has a predictor score than a randomly chosen incorrect answer. Higher scores are better, with perfect uncertainty scoring 1 while a random uncertainty measure would score 0.5.

Baselines: We compare CLAM to three baselines. *Default GPT* prepends the question with a question-answering prompt: This is a conversation between a user and a question-answering bot.

*Prompting baseline* uses a prompt that explicitly instructs the model to selectively ask the user for clarifying questions: This is a conversation between a user and a question-answering bot. The bot asks the user for clarification if the user's question is ambiguous or imprecise.

*Force clarification* does not distinguish between ambiguous and unambiguous questions, and always prompts the language model to ask for clarification about the user's input.

### 5.1. Results
[]
**Published:** 2022-01-01
