# Research Results
**Query:** Give me the latest information on large language models that are open source and can run locally on mac with sixteen gigabytes of ram
**Timestamp:** 2025-11-22T14:57:13.323614
**Summary:** LLaMA is an open-source series of large language models developed by Meta AI, aimed at advancing language processing capabilities. The study evaluates the effectiveness of vocabulary tests as a benchmark for assessing large language models.

## Detailed Results

### Result 1
**Title:** A Review of Multi-Modal Large Language and Vision Models
**URL:** https://arxiv.org/abs/2404.01322?utm_source=valyu.ai&utm_medium=referral
**Source:** valyu/valyu-arxiv

**Content:**
### 4.4 LLaMA

LLaMA is a series of open source LLMs developed by Meta AI. The goal for Meta was to provide an accessible and open sourced LLM to help make advancements in research and application development in the sub field of NLP, thus enabling others in the research community to access the vast infrastructure resources to study and explore the area of LLMs' rapidly evolving fields of use. LLaMA comprises a collection of foundation language models with parameter sizes ranging from 7B to 65B. Unlike other models that prioritise training speed, LLaMA was designed to run on a single GPU, with the objective being to focus on the inference speed rather than the speed of the fastest model to train [11, 44].

LLMs were based on the common belief that more parameters will lead to better performance and so the bigger the model, the better the performance. A recent study by Hoffman et al. [45] suggested that smaller models trained on more data can yield better performance and results for a given computational budget. Meta AI trained the LLaMA language models using publicly available datasets exclusively, avoiding the use of proprietary or inaccessible data. The main objective of LLaMA was to achieve the best possible performance at different computational budgets for inference. Despite its smaller size, LLaMA-13B outperforms GPT-3 on most benchmarks, while LLaMA-65B is competitive with other LLMs like Chinchilla or PaLM-540B [11, 46, 47].

LLaMA model architecture is based on the original Transformer architecture as described in [25]. Additional improvements were made to the model by incorporating methods proposed by other LLMs. To make the training stable, LLaMA uses a technique called pre-normalisation, as demonstrated in the GPT-3 model. This method normalises the input of the transformer, rather than normalising the output, using the RMSNorm function. This helps to reduce computational time and complexity. LLaMA improves performance through utilising an activation function called SwiGLU. LLaMA uses Rotary positional embedding (RoPE) a technique that rotates the token embedding in a highdimensional space. RoPE preserves the original information, while adding positional understanding. This can save memory and computational resources, making it a more efficient choice for large-scale models [11, 48, 46].

LLaMA was compared with non open source models such as PaLM, GPT-3 and Chinchilla using a total of 20 benchmarks to evaluate Zero-shot and Few-shot learning. Despite LLaMA being a smaller model, it outperformed or stayed competitive with PaLM, GPT-3 and Chinchilla in areas such as Common Sense Reasoning, Closed-book Question Answering, Reading Comprehension, and Code Generation. LLaMA did not perform as well as PaLM and Chinchilla in Massive Multi-task Language Understanding (MMLU). However, it was found that small amounts of instruction fine-tuning applied to the model improved the performance for MMLU. LLaMA-65B efficiency was measured against areas such as truthfulness, bias, and toxic language. The following benchmarks were used: RealToxicityPrompts, CrowS-Pairs, WinoGender, and TruthfulQA. These are covered in more detail in Section 7 and in [11, 48, 46].

### 4.5 LLaMA-2 and LLaMA-2 Chat

In July 2023, Meta AI released LLaMA-2 and LLaMA-2 Chat, an updated version of LLaMA. LLaMA-2 and LLaMA-2 Chat are a collection of models ranging from 7B to 70B parameters in size. They key enhancements in LLaMA-2 included a 40% increase in the size of the pre-training corpus and doubling the context length from 2048 to 4096 tokens. One notable difference in LLaMA-2 and LLaMA-2 Chat from their predecessor LLaMA, is the adoption of the fine-tuning method Reinforcement Learning from Human Feedback (RLHF) in both LLaMA-2 and LLaMA-2 Chat. This fine-tuning technique is discussed in more detail in Section 6.1. Although Meta AI have continued to use publicly available data for training, LLaMA-2 incorporates a new mix of data and have implemented increased safety measures to ensure the model utilised safety-specific data. While LLaMA was released as an open-sourced model with non-commercial license, LLaMA-2 introduces a commercial license to encourage collaborations and facilitate the exploration of new applications. Additionally, Meta AI provided the weights and initial code used to help simplify the process for developers and researchers to build upon existing work. LLaMA-2 adopts a similar architecture to LLaMA, with an important enhancement, the integration GQA mechanism within its transformer-based framework [49, 50, 51].

In terms of performance tasks and benchmarks utilised for LLaMA-2 and LLaMA-2 Chat, similar ones were used as in the case of LLaMA. LLaMA-2 generally out-performed most other open sourced LLMs across various performance tasks, with the exception of coding-based tasks. However, when compared to proprietary LLMs such as GPT-4 and PaLM-2, LLaMA-2 presented lower performance. It closely aligned with results of GPT-3.5 and PaLM in terms of performance outcomes [49, 52, 29].
[]
**Published:** 2024-03-28

### Result 2
**Title:** Establishing vocabulary tests as a benchmark for evaluating large language models Establishing vocabulary tests as a benchmark for evaluating large language models
**URL:** https://pubmed.ncbi.nlm.nih.gov/PMC11637312?utm_source=valyu.ai&utm_medium=referral
**Source:** valyu/valyu-pubmed

**Content:**
## Materials and methods
To assess the usefulness of vocabulary tests in LLM evaluation, we conducted several vocabulary tests on different LLMs. To have a representative sample of current LLMs, we selected two company-owned, commercial LLM tools: ChatGPT (based on GPT3.5 and GPT4 see [https://openai.com/blog/chatgpt]()) and Bard (based on PaLM 2, see [https://ai.google/static/documents/google-about-bard.pdf](), now replaced by Gemini), together with two open source LLMs: Llama 2 [37] and Mistral [38].
ChatGPT, developed by OpenAI, is the most popular LLM-based chatbot today and probably the one that has shown the best performance across a variety of tasks. Two versions of ChatGPT (with different numbers of parameters) were tested. Bard was developed by Google and is intended to compete with ChatGPT, so both are good examples of commercial chatbots. Parameters and source code for these LLMs are not available, which makes them less interesting for research purposes because they can be modified overnight without researchers being able to verify what was done. Still, because of their massive use by the public, it is worthwhile to determine their performance at some point. Llama 2, developed by Meta, is probably the best known open-source LLM right now. Another open-source LLM with good performance is Mistral, developed by a startup of the same name. We tested three versions of Llama 2, of different sizes, to see to what extent performance improves as network complexity increases. The seven models considered in our evaluation are summarized in [pone.0308259.t001]. They range from relatively small models to the largest models that were publicly accessible at the time of conducting the experiments.
1.
   Mistral-7B. LLM developed by Mistral AI and released in September 2023. It has 7.3 billion parameters and is based on a transformer architecture. It stands out for its efficiency, outperforming larger models like Llama2 at the time of its release. It is an open-weight model, but the dataset used for its training is not public [38].
2.
   Llama 2 (7/13/70B). Developed by Meta AI and released in July 2023. It is available in versions of 7B, 13B, and 70B parameters, utilizing a transformer architecture with techniques such as RMSNorm pre-normalization, SwiGLU activation function, and rotary positional embeddings [37]. Unlike other big tech companies, Meta has chosen to offer Llama 2 as open source. It has been trained in over 20 languages, although most of the data is in English (89.7%), while other languages, such as Spanish, represent only 0.13% of the training data.
3.
   PaLM 2. Developed by Google AI and presented in May 2023, it is a lighter version compared to its predecessor (PaLM) while offering better capabilities. The training dataset includes more data in other languages to enhance multilingual capabilities compared with PaLM. Neither the training dataset nor the model weights have been released [39].
4.
   GPT3.5. Commercial model developed by OpenAI and a version of GPT-3. It is estimated to have a size equal to GPT-3 (175 billion parameters), which was primarily trained in English (93%). GPT-3.5 is the model on which the first version of ChatGPT was based (November 2022) [40].
5.
   GPT4: Latest version of the GPT family released in March 2023 [41]. The model adds image processing capabilities and improves its performance compared to its predecessor. Various sources indicate that it contains more than 1 trillion of parameters within a Mixture of Experts (MoE) architecture [42], which allows it to dynamically activate different subsets of its neural network depending on the input.
The tests were run automatically using the Application Programming Interfaces (APIs) of the LLM-based chatbots to create the questions in each test and then produce an excel file with all the answers, as described in [36]. The only exception was Bard (now Gemini), whose API was not accessible in Spain at the time of the evaluation, for Bard the user interface was used for testing. Automation is interesting for running tests at scale, since we evaluated seven LLMs on tests with dozens of questions each. In addition, the use of the API allowed control over LLM parameters, such as temperature, which adjust the variability of answers. For certain models, such as Llama 2, the responses included extra text along with the selected answer (A/B/C/D). When feasible, this text was automatically processed to isolate the answer and compare it with the correct one to generate the evaluation metrics. In cases where this was not possible, a manual analysis was performed to classify the response as correct or incorrect. During evaluation, LLMs were not given context information and default parameters were used except temperature, which was set to zero if it was controllable to produce deterministic responses. The prompts used to interrogate the chatbots were simple and similar to those used in the human tests (see below). The performance of LLMs can be improved by providing context or more sophisticated prompts that force the LLMs to solve the questions step by step using a chain of thought [16]. However, our goal was to understand how LLMs perform in vocabulary tests when presented with the same questions as humans and not to modify the questions or provide additional information to improve the LLMs’ answers.
We use several representative vocabulary tests, both with multiple choice and yes/no questions, in our evaluation. In every case, our use of these tests adheres to the terms and conditions set forth by the sources. For example, for some of the tests, the questions cannot be made publicly available and thus are not included in the dataset that contains the results of the different LLMs for the different tests.
The details of the multiple-choice and yes/no questions tests are summarized in [pone.0308259.t002]. The first test was the TOEFL introduced by Landauer and Dumais [1]. It contains 80 target words with four alternatives to choose from (these are also single words). The difficulty of the items varies, but the level is adapted to non-English-speaking students who want to study at English-speaking universities. The test cannot be freely shared due to copyright restrictions, but researchers can request access to the stimulus material, if use is strictly limited to research purposes. We were kindly granted access to the stimuli by the LSA research group at the University of Colorado.
<FG id='pone.0308259.t001'>
**Table 1**
</FG> <FG id='pone.0308259.t002'>
**Table 2**
</FG>
**Published:** 2024-12-12

### Result 3
**Title:** MacBehaviour: An R package for behavioural experimentation on large language models
**URL:** https://pubmed.ncbi.nlm.nih.gov/PMC11655609?utm_source=valyu.ai&utm_medium=referral
**Source:** valyu/valyu-pubmed

**Content:**
MacBehaviour differs from existing toolkits for probing LLM behaviours in several important ways. First, in contrast to existing packages like “transformer” (Wolf et al., [41]) and “minicons” (Misra, [28]), which focus on analysing locally deployed LLMs, MacBehaviour stands out by enabling interactions with a wide range of non-local language models via API. Second, MacBehaviour distinguishes itself from other packages by offering a streamlined and standardised approach to conducting psychological studies with LLMs. With MacBehaviour, researchers can focus on defining the stimuli and adjusting the relevant parameters, rather than grappling with the intricacies of the underlying code. The package abstracts away the complexities of interacting with language models, handling data collection, and managing the experimental flow. Finally, the standardised approach promoted by MacBehaviour enhances the reproducibility and comparability of experiments across different studies and research groups. By providing a common framework, MacBehaviour facilitates the sharing and replication of experimental designs, fostering collaboration and enabling more robust and reliable findings in the field of psychological research involving language models.
For all supported self-hosted LLMs by FastChat, please see [https://github.com/lm-sys/FastChat/blob/main/docs/model_support.md]().
In the following sections, we provide an overview of MacBehaviour's key features and walk through example use cases. We then carried out a psycholinguistic experiment on some LLMs using different designs and collected different data from the LLMs to demonstrate the validity of the package.

## Methods
The “MacBehaviour” R package works with OpenAI's GPT models, Claude family, Llama family and other models that use the OpenAI-compatible API. This facilitates the conduct of behavioural experiments on LLMs (see Table [Tab2] for a complete list of functions in the package). The package is not limited to psycholinguistic experimentation on LLMs but can be used for behavioural investigation of LLMs in general (e.g., decision-making, Binz & Schulz, [4]; stimulus norming, Alzahrani, [2]).

## Installation and setup
To facilitate ease of use, users can install this package either via the “install.packages” function from CRAN or directly from the GitHub repository, where we have also provided the latest updates, a quick start tutorial, and demo code for immediate application ([https://github.com/xufengduan/MacBehaviour]()), ensuring access to the most current information beyond what is detailed in the paper:
``` r.

# from CRAN.
install.packages(“MacBehaviour”).
```
``` r.
<FG id='Tab2'>
**Table 2**
<T>
| Function | Description |
| --- | --- |
| setKey | Set the API key and URL for an LLM |
| loadData | Load experimental stimuli |
| experimentDesign | Define experiment setup |
| preCheck | Configure model parameters and check the token number of stimuli before execution |
| runExperiment | Execute an experiment and log model responses |
| magicTokenizer | This function provides the number of tokens for a given text list, acting as a wrapper for an internal tokeniser function |
| addMessage | This internal function is used to append a new message (composed of role and content) to an existing list of messages. This is used internally to manage conversations during data collection |
“MacBehaviour” R package main functions

</T>
</FG>
**Published:** 2024-12-18

### Result 4
**Title:** A tutorial on open-source large language models for behavioral science
**URL:** https://pubmed.ncbi.nlm.nih.gov/PMC11525391?utm_source=valyu.ai&utm_medium=referral
**Source:** valyu/valyu-pubmed

**Content:**
### An overview of model types
Since the inception of the transformer architecture (Vaswani et al., [80]), many model variants have emerged that differ in important ways, including the architecture family (i.e., *encoder*, *decoder*, or *encoder-decoder*), model size, stage of training reached by the model, and openness.
Concerning the architecture family, it is helpful to distinguish the *encoder*, *decoder*, and *encoder-decoder* architectures (see Fig. [Fig3]). The encoder architecture is characterized by bidirectional attention, pre-training through masked language modeling (and, sometimes, next-sentence prediction), and the use of special tokens such as "[CLS]", "[SEP]", and "[MASK]". The goal of the encoder architecture is to produce accurate contextualized embeddings, including for the special tokens. Prominent examples following the encoder architecture are the models of the BERT family (e.g., DistilBERT (Sanh et al., [64]) or RoBERTa (Liu et al., [47])), and the instructor models (Su et al., [70]). The decoder architecture, on the other hand, is characterized by causal attention and pre-training through causal language modeling. The goal of the decoder architecture is to generate text via next-token prediction. Prominent examples of the decoder architecture are the GPT (OpenAI, [54]) and LLaMA model families (Touvron et al., [75]). Finally, the encoder-decoder architecture is characterized by a combination of the two, and is the original transformer architecture as proposed in Vaswani et al. ([80]). It is trained with next-token prediction, where the input text is first fed to the encoder, the encoder’s last hidden state is then passed as input to the decoder, which then predicts the next token. Prominent examples of the encoder-decoder architecture are the BART (Lewis et al., [45]) and T5 (Raffel et al., [58]) models.
A second key differentiating factor between LLMs is size. Size is often measured in terms of the number of weights in a model, which can vary between a few hundred million (e.g., most BERT models) and several hundred billion (Smith et al., [67], e.g., Megatron Turing NLG) - or even the trillion weights supposedly reached by OpenAI’s GPT-4 model. Although the number of weights plays a large role in determining a model’s capacity to learn from the training data, how the weights are distributed throughout the various model components also matters (Kaplan et al., [40]). The size of LLMs can also differ in a more functional way, by allowing for different context sizes. The context size is the maximum number of tokens in a sequence that the attention mechanism can evaluate at any given time, and it determines the complexity of connections between tokens that the model can consider. This is important for applications such as few-shot learning (see Section “[Sec8]”). From a practical perspective, context size also determines the amount of random-access memory (RAM) needed to run a model. For large decoder models such as LLaMA-2 (70 billion weights), RAM requirements can be as high as 300 gigabytes, resulting in a need for expensive, high-performance graphical processing units (GPUs).
A third differentiating factor is the stage of training reached by the model. First, there are *pre-trained models*, which have been trained on a large corpus of text using masked or causal language modeling. The text corpus typically includes websites, which in turn include blogs, news articles, Wikipedia, social media platforms (e.g., Reddit), and other sources of text (e.g., books, academic articles). Larger pre-trained models are sometimes also called foundation models (Bommasani et al., [14]), emphasizing their purpose as a basis for task-specific training. Second, there are *fine-tuned models*, which are pre-trained models that have been further trained on task-specific data to selectively increase their performance on certain tasks. These can be basic tasks, such as token classification or prediction of numerical variables, or more complex tasks, such as named-entity recognition or question answering.
A fourth differentiating factor that concerns the set of fine-tuned models and has played an especially important role in the growth in popularity of LLMs in recent times is whether the model is a "chat" model. Specific fine-tuning regimes exist to make pre-trained models better suited to high-quality, assistant-style interactions through a chat interface. These include training steps with explicit human input such as *supervised fine-tuning*, *reinforcement learning from human feedback* (Christiano et al., [18]; Touvron et al., [75]), and *direct preference optimization* (Rafailov et al., [57]). For instance, in supervised fine-tuning, human "annotators" generate prompts and appropriate assistant-style responses to those prompts, such that the model may learn via "imitation" to become a good assistant. Reinforcement learning from human feedback is a more complex, multistage procedure in which human annotators indicate their preferences between model outputs according to specific criteria (e.g., safety or helpfulness) to build a "preference dataset" (stage 1) (Touvron et al., [75]). This dataset is then used to train a reward model that learns the annotators’ preferences (stage 2), which in turn provides feedback on the outputs of the LLM in much vaster quantities than would be possible with human annotations alone. This enables the LLM to learn via reinforcement to become a better assistant. Such fine-tuning can be seen as an example of how LLMs can be tailored to specific behavioral applications. A prominent example of a chat model is ChatGPT, but other open-source models exist, including LLaMA-2 Chat (Touvron et al., [75]) or Falcon Chat (TII, [73]).
A fifth and final differentiating factor is openness. LLMs differ in terms of how much information is available about the training data, training method, or architecture (see Bommasani et al., [14]) and how openly available the models themselves are. Some models, such as GPT-4, are only available through remote user interfaces, whereas others are mostly (e.g., LLaMA) or fully (e.g., BERT) open-source. Most open-source models can be accessed and employed via the Hugging Face ecosystem introduced in this tutorial, which has significant advantages over closed-source models in terms of transparency and reproducibility.
<FG id='Fig3'>
**Figure 3**: Fig. 3
<F href='13428_2024_2455_Fig3_HTML.jpg'>
Overview of pre-training mode and transformer family. The figure illustrates two pre-training modes (masked language modeling, causal language modeling) and associated architecture family (encoder, decoder)
</F>
</FG>
**Published:** 2024-08-15

### Result 5
**Title:** A tutorial on open-source large language models for behavioral science
**URL:** https://pubmed.ncbi.nlm.nih.gov/PMC11525391?utm_source=valyu.ai&utm_medium=referral
**Source:** valyu/valyu-pubmed

**Content:**
### Open-source LLMs and open behavioral science
Behavioral science is going through an open science revolution guided by principles such as transparency, accessibility, and sharing (Vicente-Saez & Martinez-Fuentes, [81]). Open-source and open-access language modeling frameworks such as Hugging Face are closely aligned with these principles. For instance, with Hugging Face, all analysis steps - from data preprocessing to model validation - are in principle accessible to fellow scientists wishing to better understand and perhaps reproduce what others have done. Likewise, models fine-tuned using the |transformers| library can easily be shared on the Hugging Face Hub, making it easier for researchers to build on and benefit from the work of their peers. With over 300,000 models and 60,000 datasets, Hugging Face stands as an exemplary case of the power of sharing in research and beyond.
Hugging Face also supports reproducibility. Features such as the ability to set seeds help improve the reproducibility of nondeterministic processes such as gradient descent. Likewise, because models are saved to the hard drive (instructions for locating models saved to hard drive are regularly updated at [stackoverflow.com/questions/61798573/where-does-hug]()[ging-faces-transformers-save-models]()), the precise version of the model used for the analysis can be permanently saved for future reproductions. This stands in contrast to less open alternatives such as the OpenAI API, which, at the time of writing, does not provide the ability to access the same version of the model indefinitely into the future after model updates.
Open-source and open-access language modeling frameworks also have considerable advantages when it comes to data privacy: Because models can be saved and run locally, sensitive data can remain on the appropriate hardware, and researchers can be sure that the creators of the model will not have access to it. This is crucial in behavioral science, where ensuring the privacy of participant data is paramount from an ethical and legal perspective.
Open-source language modeling frameworks also help mitigate an important disadvantage of LLMs: their poor interpretability. Interpretability is a general problem for neural network models, whose complexity and abstract representational nature have earned them the label "black-box" models (Alishahi et al., [5]). In behavioral science, the limited interpretability of LLMs can hinder a researcher’s ability to draw strong theoretical conclusions. For instance, being able to interpret the internal states of the model presented in the section on Text Generation would help clarify whether it had simply "memorized" answers to the CRT or actually "reasoned" them through. However, a commitment to openness - in this case, transparency about the data used to train the model - could also help resolve this uncertainty by revealing whether the CRT even featured in the training data at all. In general, interpretability is worsened when researchers are not given information about important details concerning the model’s pre-training data, tokenizer, architecture, weights, and fine-tuning regimes. Of course, even when these details are known, it can remain a mystery why a model performs well on some tasks but not on others. This point is exemplified by the existence of *emergent abilities* in LLMs: abilities that arise from model upscaling, but whose arrival is incredibly difficult to predict, even for the developers who trained the model (Wei et al., [87]).

### (Open-source) LLMs and society
Although we believe that open-source and open-access language modeling has its advantages for research, making LLMs publicly accessible also comes with considerable risks. LLMs are, after all, powerful tools, and in the hands of bad actors, they could be used to do serious harm (e.g., spreading mis- and disinformation; Weidinger et al., [88]). Increasing access to LLMs will also have environmental impacts (Strubell et al., [69]), especially when more researchers have the ability not only to use these models for inference but also to train them via ecosystems such as Hugging Face.
Furthermore, it is important to be aware of the broader risks that present and future LLMs may pose to society, especially if they are poorly aligned with people’s preferences and values (Bockting et al., [13]; Russell, [62]). Concerns such as these have motivated research programs into AI alignment from leading AI companies (Leike & Sutskever, [44]; Leike et al., [43]). They have also led to the use of more explicit human behavioral data for fine-tuning LLMs (e.g., via explicit human feedback on model outputs) to achieve closer alignment with human preferences. As has been pointed out (Irving & Askell, [37]; Russell, [62]), this endeavor presents a unique opportunity for behavioral scientists, who of course have expertise in collecting high-quality human data.

**Published:** 2024-08-15

### Result 6
**Title:** A Review of Multi-Modal Large Language and Vision Models
**URL:** https://arxiv.org/abs/2404.01322?utm_source=valyu.ai&utm_medium=referral
**Source:** valyu/valyu-arxiv

**Content:**
# 1 Introduction

Large Language Models (LLMs) are one of the hottest topics in artificial intelligence (AI) research and interest in them and how they can be used in generative AI applications has spilled into the mainstream media. Their popularity in the public sphere has been triggered by the arrival of ChatGPT, first released to the public in 2022 [1]. By LLMs we refer to language models based on the Transformer architecture, with the notable example of 'Generative Pre-trained Transformers (GPT)' from OpenAI first introduced as GPT-1 in 2018 [2]. The sudden popularity of LLMs arises because of their demonstrated usefulness in supporting a wide range of applications and tasks including text summarisation [3], text-to-image [4] and text-to-video [5] generation, conversational search [6], machine translation [7] as well as their role in many Generative AI (GenAI) applications. That role in GenAI is included in a comprehensive review of the literature consisting of over 1,300 articles in [8].

Apart from the GPT-n family of LLMs from OpenAI, other notable examples of proprietary LLM's which are in the public eye include Google's Gemini/BARD [9] and Anthropic's CLAUDE [10] while the most well-known open source LLMs are Meta's LLaMA [11], Google's PaLM and Falcon from the UAE's Technology Innovation Institute. The release of a new LLM or the announcement about an update to an existing one can not only pique the interests of the research community but often also attracts media attention. This makes keeping abreast of all the LLMs that are available, how they compare against each other and what they are being used for, a challenging task.

In this review, we assess the current state of LLM's but with a specific focus on visual/multi-modal LLM's and on their technical aspects, how they can be optimised for a specific task. In [12] the authors presented a short, thorough review of LLMs covering their history, architectures, training methods, applications, impacts, challenges and significance but their scope did not cover models that have been trained on, and can generate output which crosses the boundaries of different modalities namely text, images, videos, and audio. Our review is complementary to that in [12] and guided by the evaluation of LLMs and MM-LLMs, considers factors such as open-source versus proprietary owned models, the benefits of choosing open-source and the computational costs and resources required to pursue open-source. We also address issues such as whether the fine-tuning methods or architectural components in each model that should be considered in order to minimise cost and what evaluation methods are used to assess the quality of these models.

Many ethical concerns have been raised in the literature concerning the use of LLMs, the data used to train them [13, 14], the energy costs associated with their creation [15, 16] and the fact that the largest and most useful of these models are owned by a small number of big tech companies. This review looks to address if and how a Multi-Modal LLM, in particular an open source MM-LLM can be used in practical multimedia applications. We examine how they are trained to become MM-LLMs and how the visual components which defines them as Multi-Modal were incorporated to their base LLM. Additionally, we highlight the comparison between closed source vs. open source from an ethical standpoint, data control issue and application use case.

Other aspects of such models, of which there are several, fall outside the scope of this review.

The rest of this paper is organised as follows. In the next section we briefly re-cap on large language models to explain what they are, the history of their development and the importance of the attention mechanism. We then examine look at the pros and cons for using proprietary vs. open source LLMs. This is followed by a review of the largest and most popular of the mostly textbased LLMs, covering the LLaMA family, Mistral-7B, Falcon and its variants Following that we review the major vision models and the Multi-Modal Large Language Models (MM-LLMs) BLIP-2, CLIP, LLaVA, Kosmos-1, MiniGPT4, and MPLUG-Owl. This is followed by a review of ways to modify a foundational model for specific applications including model fine-tuning, both full tine-tuning and parameter efficient fine-tuning covering Low Rank Adaption (LoRA), Quantised Low-Rank Adaption (QLoRA) and Supervised Fine-Tuning (SFT), prompt engineering and Reinforced Learning Human Feedback (RLHF). Hallucinations, which refer to outputs from a LLM or a MM-LLM which are obviously wrong, factually incorrect, or unrelated to the input prompt, are then presented along with approaches to mitigate their impact, especially for MM-LLMs. Finally, model evaluation and benchmarking to assess the performance of both pre-trained and fine-tuned LLMs and MM-LLMs is an important consideration in any use of such models and a number of commonly used benchmarks for assessing the performance of an LLM in common-sense reasoning tasks, are presented.
[]
**Published:** 2024-03-28

### Result 7
**Title:** A Review of Multi-Modal Large Language and Vision Models
**URL:** https://arxiv.org/abs/2404.01322?utm_source=valyu.ai&utm_medium=referral
**Source:** valyu/valyu-arxiv

**Content:**
### 2.2 Attention Mechanisms

The Transformer architecture has been a paradigm shift in the field of NLP. First introduced in [25], it is an architecture that uses only attention mechanisms, specifically Self-Attention and Multi-Headed attention. Recently, methods utilising the attention mechanism have dominated this area.

Attention mechanisms allow a model to focus on important parts of an input

sequence without being affected or reliant on dependencies of distance in the sequence. The self-attention mechanism relates to different positions of a single sequence in order to compute a representation of the sequence. Each input sequence is broken down into smaller, unique, linear query, key and value vectors for better context understanding.

The Multi-Head attention (MHA) mechanisms repeats the self-attention computation multiple times in parallel. MHA uses multiple heads to attend to all the different aspects of an input sequence simultaneously. This allows it to provide high-quality results. However, this can be computationally expensive due to the parallel processing and can potentially lead to performance deterioration.

Multi Query Attention (MQA) shares one key head and a single value head across all unique query heads. As the number of heads for key and value are reduced, the GPU memory required for storage is also reduced and allows for faster processing. GPU memory saving can then be utilised to increase batch size, and therefore increase overall efficiency. The disadvantage to using MQA over MHA is that the former only uses one head for a key-value pair therefore it is prone to missing potentially important aspects of the input sequence compared to the more in-depth analysis of MHA.

The compromise between MHA and MQA is called Grouped-Query attention (GQA) and 3 variations are shown in Figure 2.2. GQA allows for faster processing than MHA while retaining more detail than MQA through attention within groups. This allows the model to effectively comprehend longer input sequences. GQA addresses this issue found in MHA by assigning each key-value head a corresponding query group, rather than a unique linear query. This optimises performance while mitigating risk of performance degradation [29, 30, 31].

[_page_4_Figure_4.jpeg]: A summary of how an input sequence is decomposed into query, key, and value vectors across the various attention mechanisms, taken from [31].

# 3 Proprietary vs. Open Source LLMs

Throughout 2023, the ongoing surge in research and development of LLMs continued at pace. Prominent companies such as OpenAI and Google competed to develop an LLM that would dominate the market. It was previously considered that the larger the LLM, the greater the competitive advantage that would be obtained. The cost for researchers to build an open sourced LLM had required substantially large funding, as the creation of LLMs demanded extensive data and GPU resources, which could cost anywhere from €1 to €100 million. This was until Meta released their open sourced LLM called LLaMA, their belief being that to foster innovation, enhance security, and improve safety in LLMs, it was important to release an open sourced LLM [32]. Some open source models like Meta's LLaMA-2 and Google's PaLM 2, are now available to use free of charge as opposed to proprietary LLMs such as OpenAI's GPT or Google's BARD which charge enterprises based on their usage of the model [33, 34].

It should be noted that Google has acknowledge the limitations of proprietary LLMs and that there would only be limited time before their own model would be replicated or surpassed by open source LLMs. This is because the innovations that were driving the successes in the open source community had addressed challenges that Google had already been grappling with [35, 36].

Open source LLMs offer several advantages for researchers and for entrepreneurs, primarily due to their long-term cost-effectiveness but also because they provide transparency and flexibility in terms of their methodologies, architecture, and training data. The visibility in open source models aids with audits while facilitating adherence to both ethical and legal standards. This will be especially important when the European Union AI act comes into force in 2025 where such openness and transparency about training data will be a requirement if companies are to deploy use of their LLMs within the European Union [37]. Another benefit is that open source grants researchers and developers' complete control over their own data which they may wish to combine with, or to fine-tune, an LLM. Any sensitive data that might be used will remain within their system which aids in reducing the risk of data leaks or unauthorised access. Furthermore, efficient optimisation of open source LLMs can result in reduced latency and improved performance.

Open source LLMs have been utilised across a diverse range of industries, including healthcare, law, and finance among others. However, there are noteworthy concerns associated with the use of open source LLMs that should be considered. Firstly, there is a lack of formal service agreements between the provider of an open source LLM and the entities utilising it for development. Additionally, there is no guarantee that a company or developer will continue to offer support or continued development for an open source LLM in the future. Furthermore, as open source communities drive technological advancements, proprietary-owned LLMs may progress to become a more practical and reliable option in the future. Lastly, it is important to consider that not all open source LLM adhere strictly to the open source philosophy. For instance, Meta's LLaMA-2 has imposed certain usage conditions through its acceptable use policy [33, 34, 38].
['<FG id="_page_4_Figure_4.jpeg">\n**Figure 1**: Figure 1\n<F href="_page_5_Figure_1.jpeg">\nFigure 1: A summary of how an input sequence is decomposed into query, key, and value vectors across the various attention mechanisms, taken from [31].\n</F>\n</FG>']
**Published:** 2024-03-28

### Result 8
**Title:** Debugging with Open-Source Large Language Models: An Evaluation
**URL:** https://arxiv.org/abs/2409.03031?utm_source=valyu.ai&utm_medium=referral
**Source:** valyu/valyu-arxiv

**Content:**
## 1 INTRODUCTION

"I'd spend an hour figuring out what exactly goes wrong, then five minutes writing the code to fix it, and then half an hour testing the whole thing. That's just over 5% coding vs. almost 95% non-coding."1

Debugging is known to be time consuming and frustrating. Therefore it is not surprising to find out that developers are turning to large language models to help them solve their problems. In a study with practitioners, Khojah et al. [1] found that software engineers were found to turn often to chatGPT for assistance in various software engineering tasks.

ESEM '24, October 24–25, 2024, Barcelona, Spain

© 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM. ACM ISBN XXXXXXXXXXXXXXXX

https://doi.org/XXXXXX/XXXXXXXXXXXXX

Recent research showed promising results in using LLMs for software Engineering tasks in general and for debugging in particular. For example, LLMs were able to perform well in bug reproduction [2], fault localisation [3] and program repair [4]. Despite these advantages, using current state of the art LLMs such as ChatGPT can be inappropriate for practitioners due to code sharing policies. In fact, most companies consider their code to be private and don't want it to be sent to LLMs run by third parties. A solution to this problem would be to run an open source LLM locally. So far, there has been very limited assessments of the debugging capabilities of open-source large language models. In fact, earlier works mostly focus on evaluating code generation capabilities, for which many benchmarks exist such as the famous OpenAI's HumanEval [5] and its descendants (e.g. HumanEval+ [6] and Multilingual HumanEval [7]) or the Google's MBPP [8].

The goal of this work is to evaluate and compare the capabilities of open-source large language models in performing debugging tasks. We would like to answer the following two research questions:

- RQ1: How do open source LLMs perform in debugging? To answer this question, we use benchmarking to evaluate five open-source LLMs. The benchmark we used includes more than 4000 buggy code instances in Python, C++ and Java.
- RQ2: How does the performance of open-source LLMs in code generation impact their performance in debugging? We compare the scores that the LLMs obtained for debugging with the scores that they achieved for coding as evaluated by the HumanEval Benchmark.

Our evaluation suggests that although less capable than the most advanced closed source models (e.g. GPT-4), some open source models were able to achieve decent results compared to their relatively small size. For instance, DeepSeek-coder-instruct, which has only 34B parameters, achieved a score above 63% in all three programming languages. We also found that except for DeepSeek-coder, all models that achieved a higher scores in HumanEval also got better scores in debugging.

The contributions of this work are:

- We conduct an empirical study that evaluates the debugging capabilities of open source Large Language Models using a large benchmark that includes a few thousands of buggy code instances
- We compare the debugging capabilities of the open source LLMs to their coding capabilities as evaluated by the HumanEval benchmark
- We provide an extensive discussion of the strengths and limitations of current debugging and coding benchmarks

<sup>1</sup> text taken from an answer on stackoverflow regarding the time spent debugging https://softwareengineering.stackexchange.com/a/93323

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.

## 2 OPEN SOURCE LARGE LANGUAGE MODELS

There are many open-source LLMs available in the market. Although nearly2 all models use the transformer architecture, they differ in their capabilities due to various factors such as model size, quality and volume of training data, and fine-tuning methods.

For this evaluation, we selected five reputed models. Four of them are code models, while the last one is a general-purpose model.
[]
**Published:** 2024-10-15

### Result 9
**Title:** Natural language processing in the era of large language models
**URL:** https://pubmed.ncbi.nlm.nih.gov/PMC10820986?utm_source=valyu.ai&utm_medium=referral
**Source:** valyu/valyu-pubmed

**Content:**
## 2 Limitations and open challenges
The success of LLMs is not without controversy, which is in turn shaping up ongoing research in NLP and opening up avenues for more research in improving these LLMs. The following are some of the key limitations of LLMs which need further exploration.

### 2.1 Black box models
After the release of the first major LLM-based chatbot system that garnered mainstream popularity, OpenAI's ChatGPT, concerns emerged around the black box nature of the system. Indeed, there is no publicly available information on how ChatGPT was implemented as well as what data they used for training their model. From the perspective of NLP researchers, this raises serious concerns about the transparency and reproducibility of such model, not only because one does not know what is going on in the model, but also because it hinders reproducibility (Belz et al., [3]). If one runs some experiments using ChatGPT on a particular date, there is no guarantee that somebody else can reproduce those results at a later date (or, arguably, even on the same date), which reduces the validity and potential for impact and generalisability of ChatGPT-based research.
To mitigate the impact, and increase our understanding, of black box models like ChatGPT, researchers have started investigating methods for reverse engineering those models, for example by trying to find out what data a model may have used for training (Shi et al., [41]).
Luckily, however, there is a recent surge of open source models in the NLP scientific community, which have led to the release of models like Facebook's LLaMa 2 (Touvron et al., [45]) and Stanford's Alpaca (Taori et al., [44]), as well as multilingual models like BLOOM (Scao et al., [39]). Recent studies have also shown that the performance of these open source alternatives is often on par with closed models like ChatGPT (Chen et al., [4]).

### 2.2 Risk of data contamination
Data contamination occurs when “downstream test sets find their way into the pretrain corpus” (Magar and Schwartz, [24]). Where an LLM trained on large collections of text has already seen the data it is then given at test time for evaluation, the model will then exhibit an impressive yet unrealistic performance score. Research has in fact shown that data contamination can be frequent and have a significant impact (Deng et al., [9]; Golchin and Surdeanu, [15]). It is therefore crucial that researchers ensure that the test data has not been seen by an LLM before, for a fair and realistic evaluation. This is however challenging, if not nearly impossible, to figure out with black box models, which again encourages the use of open source, transparent LLMs.

### 2.3 Bias in LLM models
The use of large-scale datasets for training LLMs also means that those datasets are very likely to contain biased or stereotyped information, which has been shown that LLMs amplify (Gallegos et al., [13]; Li et al., [20]). Research has shown that text generated by LLMs includes stereotypes against women when writing reference letters (Wan et al., [47]), suggesting that LLMs in fact amplify gender biases inherent in the training data leading to an increased probability of stereotypical linking between gender groups and professions (Kotek et al., [18]). Another recent study (Navigli et al., [30]) has also shown that LLMs exhibit biases against numerous demographic characteristics, including gender, age, sexual orientation, physical appearance, disability or race, among others.

### 2.4 Generation of offensive content
Biases inherent in LLMs are at times exacerbated to even generate content that can be deemed offensive (Weidinger et al., [49]). Research in this direction is looking at how to best curate the training data fed to LLMs to avoid learning offensive samples, as well as in eliciting generation of those harmful texts to understand their origin (Srivastava et al., [43]). This research is highly linked with the point above on bias and fairness in LLMs, and therefore both could be studied jointly by looking at the reduction of biases and harm.
Some systems, such as OpenAI's ChatGPT, acknowledge the risk of producing offensive content in their terms of service[fn0001]:
“Our Services may provide incomplete, incorrect, or offensive Output that does not represent OpenAIs views. If Output references any third party products or services, it doesnt mean the third party endorses or is affiliated with OpenAI.”

### 2.5 Privacy
LLMs can also capture sensitive information retrieved from its training data. While this information is encoded in embeddings which are not human readable, it has been found (Pan et al., [32]) that an adversarial user can reverse engineer those embeddings to recover the sensitive information, which can have damaging consequences for the relevant individuals. While research investigating these vulnerabilities of LLMs is still in its infancy, there is awareness of the urgency of such research to make LLMs robust to privacy attacks (Guo et al., [16]; Rigaki and Garcia, [36]; Shayegani et al., [42]).

**Published:** 2024-01-12

### Result 10
**Title:** Natural Language Processing for Digital Health in the Era of Large Language Models
**URL:** https://pubmed.ncbi.nlm.nih.gov/PMC12020548?utm_source=valyu.ai&utm_medium=referral
**Source:** valyu/valyu-pubmed

**Content:**
## 2. Adapting LLMs for the Medical Domain

### 2.1. Training Medical LLMs

Although generic LLMs like ChatGPT
[FNsarker-1]
and GPT-4 [
12
] have demonstrated their robustness in diverse contexts, their performance on medical texts is often suboptimal [
13
,
14
], perhaps due to insufficient medical domain-specific training data [
15
,
16
]. This gap has catalyzed the emergence of medical-specific LLMs that leverage medical big data to optimize domain-specific performance. Three strategies are typically employed for creating medical domain-specific LLMs [
17
,
18
]:

1.
   
Pretraining from scratch [
19
]: This approach requires pretraining a new medical LLM from the ground up using a vast corpus of medical data, employing the transformer architecture [
20
]. Tailor-made for medical applications, these models can develop a deep and nuanced understanding of medical language and contexts. However, this strategy requires extensive resources in terms of data and computational power;

2.
   
Continued pretraining [
21
]: This strategy involves taking a pre-existing, robust general LLM and further training it on medical-specific data. The key is to infuse the general model with enough medical data so that it can effectively represent/encode and generate medical information. Continued pretraining tasks employ the same strategies as the base models, which can be computationally intensive. Due to the importance and popularity of continued pretraining, particularly for domain adaptation, computationally efficient strategies such as low-rank adaptation (e.g., LoRA) have been proposed [
22
];

3.
   
Instruction tuning [
23
]: This method fine-tunes general LLMs for the medical domain using instruction tuning data, improving model performance for medical tasks by providing specific instructions. The training data might include task-based instructions, scenario-based queries, or decision-making processes in a medical context. The effectiveness of instruction tuning heavily depends on the quality and variety of the instructional data.

### 2.2. Emergence of Medical LLMs

Encoder-only transformer models like BERT [
2
] led the way to the current generative models we refer to as LLMs. Early adaptation of transformer models to the medical domain came through the release of models like BioBERT [
7
], PubMedBERT [
38
], and ClinicalBERT [
39
]. BioBERT was pretrained on the original BERT model using 18 billion words from PMC and PubMed, PubMedBERT was pretrained from a randomly initialized BERT model and using the entirety of PubMed data, and ClinicalBERT [
39
] was pretrained on a multi-center EHR dataset of diabetes patients. Explorations of the scaling effects for BERT and GPT-2-style models with increasingly large numbers of model weights, up to 8.3 billion, demonstrated that performance increased for both model types at extremely large sizes [
40
]. This work was followed by pretraining using PubMed data from newly initialized models and models pretrained on general corpora [
41
]. The resulting BioMegatron 345M parameter model showed stronger performance than PubMedBERT on multiple standardized NLP tasks. These works paved the way for new-age generative LLMs with billions of parameters.

We summarize representative LLMs in
[TBsarker-1]
. Among them, MedPaLM [
24
], MedPaLM2 [
42
], ChatDoctor [
25
], MedAlpaca [
26
], Clinical Camel [
28
], AlpaCare [
34
], LLaVA-Med [
31
], MMedLM 2 [
37
] and Med-Flamingo [
33
] adopted the instruction tuning strategy. MedPaLM and MedPaLM2, which utilize the PaLM architecture with 540 billion parameters, and PaLM2 as the backbone, have been shown to be particularly effective in medical question-answering (QA) tasks. AMIE [
34
] also uses PaLM2 as the backbone model, and is specifically fine-tuned for clinical applications, based on medical QA and clinical texts. However, its large parameter size and closed-source nature make it challenging for widespread deployment, particularly in resource-constrained settings. Models such as ChatDoctor and MedAlpaca, based on the open-sourced LLM LLaMA [
11
,
43
], offer a more practical balance. With a focus on QA and conversations, they provide versatility while being less computationally intensive, making them more accessible for diverse medical applications.

GatorTron [
44
] and GatorTronGPT [
29
] represent the few medical LLMs that have been trained from scratch. GatorTronGPT is based on the GPT-3 [
45
] framework, and it was trained using 200 million clinical notes, and 124 NVIDIA DGX nodes.

PMC-LLaMA [
15
], Clinical-LLaMA [
28
], Meditron [
16
] and Me LLaMA [
36
] represent models using the continued pretraining, or domain-adaptive pretraining approach. These models utilize foundation LLMs that are further enhanced with specific medical knowledge. All these models use LLaMA2 as their backbone, given its strong performance in general domain tasks and open-source nature. PMC-LLaMA and Me LLaMA further combine this approach with instruction tuning, demonstrating an effective, hybrid strategy to adapt the LLaMA2 model to the medical domain.
<FG id='TBsarker-1'>
**Table 1.**
<T>
| Model | Backbone | Size | Strategy | Data | Data Size | Modality | License Access | Language | Release date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 
MedPaLM [
24
]
 | PaLM | 540B | IFT | QA | - | Text | X | English | 12/26/22 |
| 
ChatDoctor [
25
]
 | LLaMA | 7B | IFT | Conversation | 100K | Text | Apache 2.0 | English | 03/24/23 |
| 
MedAlpaca [
26
]
 | LLaMA | 7B, 13B | IFT | QA | 160K | Text | GNU GPL v3.0 | English | 04/14/23 |
| 
PMC-LLaMA [
15
]
 | LLaMA, LLaMA2 | 7B, 13B | CPT+IFT | Literature, book, conversation, QA, knowledge graph | 79B, 514K | Text | Apache 2.0 | English | 04/25/23 |
| 
MedPaLM2 [
27
]
 | PaLM2 | - | IFT | QA | - | Text | X | English | 05/16/23 |
| 
Clinical Camel [
28
]
 | LLaMA2 | 13B, 70B | IFT | Conversation, QA | 104K | Text | GNU Affero GPL v3.0 | English | 05/19/23 |
| 
GatorTronGPT [
29
]
 | GPT-3 architecture | 5B, 20B | SPT | General and clinical text | 82B | Text | Apache 2.0 | English | 05/24/23 |
| 
HuatuoGPT [
30
]
 | Baichuan, Ziya | 7B, 13B | IFT+RLMF | Conversation, QA | - | Text | Apache 2.0 | Chinese | 05/25/23 |
| 
LLaVA-Med [
31
]
 | LLaVA | 13B | IFT | biomedical image-text | 630K | Text, image | Microsoft ResearchLicense | English | 06/01/23 |
| 
Clinical-LLaMA [
32
]
 | LLaMA2 | 7B | CPT | MIMIC-IV | - | Text | X | English | 07/12/23 |
| 
Med-Flamingo [
33
]
 | Flamingo | 9B | IFT | General and biomedical image-text | >0.01B | Text, image | √ | English | 07/27/23 |
| 
AlpaCare [
34
]
 | LLaMA2 | 7B, 13B | IFT | Biomedical conversation | 52K | Text | Apache 2.0 | English | 10/23/23 |
| 
Meditron [
16
]
 | LLaMA2 | 7B, 70B | CPT | General and biomedical text | 48B | Text | Apache 2.0 | English | 11/27/23 |
| 
AMIE [
35
]
 | PaLM2 | - | IFT | QA, clinical text | 110K | Text | X | English | 01/11/24 |
| 
Me LLaMA [
36
]
 | LLaMA2 | 13B, 70B | CPT+IFT | QA, clinical text | 129B, 214K | Text | PhysioNet Credentialed HealthData License 1.5.0 | English | 02/20/24 |
| 
MMedLM2 [
37
]
 | InternLM, BLOOM | 7B | IFT | QA, clinical text | 25.5B | Text | cc-by-4.0 | Multilingual | 02/26/24 |
# A detailed comparison of medical LLMs available at the time of writing. This comparative analysis spans multiple dimensions, providing a holistic view of each model's characteristics and capabilities. Key aspects of comparison include: backbone model, model size, training strategy, domain-specific data used and data size, accessibility, language, and release date. IFT: instruction fine-tuning; CPT: continued pretraining; SPT: pretraining from scratch; RLMF: reinforcement learning with mixed feedback; QA: question answering. For MedPaLM2, there is no information about the data size and model size of its backbone model PaLM2 (the same backbone model for AMIE). Models without explicit license terms that can be accessed are denoted by a checkmark while models without access are denoted by ‘X’. Consumer-Mediated Health Information Exchange: Authorize Direct Transmission.

</T>
</FG>
**Published:** 2025-04-08
