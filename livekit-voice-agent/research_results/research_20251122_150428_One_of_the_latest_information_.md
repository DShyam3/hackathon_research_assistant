# Research Results
**Query:** One of the latest information on large language models.
**Timestamp:** 2025-11-22T15:04:28.200299
**Summary:** Large language models (LLMs) are advanced AI systems designed to understand and generate human-like text based on vast amounts of data. Recent developments, such as OpenAI's new LLM, have revealed deeper insights into their mechanisms, enhancing our understanding of AI functionality.

## Detailed Results

### Result 1
**Title:** Large language model - Wikipedia
**URL:** https://en.wikipedia.org/wiki/Large_language_model?utm_source=valyu.ai&utm_medium=referral
**Source:** web

**Content:**
Large language model

- [Article](https://en.wikipedia.org/wiki/Large_language_model) - [Talk](https://en.wikipedia.org/wiki/Talk:Large_language_model)

Not to be confused with [Logic learning machine](https://en.wikipedia.org/wiki/Logic_learning_machine).

"LLM" redirects here. For other uses, see [LLM (disambiguation)](https://en.wikipedia.org/wiki/LLM_(disambiguation)).

A **large language model** (**LLM**) is a [language model](https://en.wikipedia.org/wiki/Language_model) trained with [self-supervised](https://en.wikipedia.org/wiki/Self-supervised_learning) [machine learning](https://en.wikipedia.org/wiki/Machine_learning) on a vast amount of text, designed for [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing) tasks, especially [language generation](https://en.wikipedia.org/wiki/Natural_language_generation).[1][2] The largest and most capable LLMs are [generative](https://en.wikipedia.org/wiki/Generative_artificial_intelligence) pre-trained [transformers](https://en.wikipedia.org/wiki/Transformer_architecture) ([GPTs](https://en.wikipedia.org/wiki/Generative_pre-trained_transformer)) and provide the core capabilities of [chatbots](https://en.wikipedia.org/wiki/Chatbot) such as [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT), [Gemini](https://en.wikipedia.org/wiki/Gemini_(chatbot)) and [Claude](https://en.wikipedia.org/wiki/Claude_(language_model)). LLMs can be [fine-tuned](https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)) for specific tasks or guided by [prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering).[3] These models acquire [predictive power](https://en.wikipedia.org/wiki/Predictive_learning) regarding [syntax](https://en.wikipedia.org/wiki/Syntax), [semantics](https://en.wikipedia.org/wiki/Semantics), and [ontologies](https://en.wikipedia.org/wiki/Ontology_(information_science))[4] inherent in human [language corpora](https://en.wikipedia.org/wiki/Text_corpus), but they also inherit inaccuracies and [biases](https://en.wikipedia.org/wiki/Algorithmic_bias) present in the [data](https://en.wikipedia.org/wiki/Training,_validation,_and_test_data_sets) they are trained on.[5]

They consist of billions to trillions of [parameters](https://en.wikipedia.org/wiki/Parameter#Artificial_intelligence) and operate as general-purpose sequence models, generating, summarizing, translating, and reasoning over text. LLMs represent a significant new technology in their ability to generalize across tasks with minimal task-specific supervision, enabling capabilities like [conversational agents](https://en.wikipedia.org/wiki/Conversational_agent), [code generation](https://en.wikipedia.org/wiki/Automatic_programming), [knowledge retrieval](https://en.wikipedia.org/wiki/Information_retrieval), and [automated reasoning](https://en.wikipedia.org/wiki/Automated_reasoning) that previously required bespoke systems.[6]

LLMs evolved from earlier [statistical](https://en.wikipedia.org/wiki/Statistical_model) and [recurrent neural network](https://en.wikipedia.org/wiki/Recurrent_neural_network) approaches to language modeling. The [transformer architecture](https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)), introduced in 2017, replaced recurrence with [self-attention](https://en.wikipedia.org/wiki/Attention_(machine_learning)), allowing efficient [parallelization](https://en.wikipedia.org/wiki/Parallel_computing), longer context handling, and scalable training on unprecedented data volumes.[7] This innovation enabled models like [GPT](https://en.wikipedia.org/wiki/GPT_(language_model)), [BERT](https://en.wikipedia.org/wiki/BERT_(language_model)), and their successors, which demonstrated [emergent behaviors](https://en.wikipedia.org/wiki/Emergence) at scale such as [few-shot learning](https://en.wikipedia.org/wiki/Prompt_engineering) and compositional reasoning.[8]

[Reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning), particularly [policy gradient algorithms](https://en.wikipedia.org/wiki/Policy_gradient_method), has been adapted to [fine-tune](https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)) LLMs for desired behaviors beyond raw next-token prediction.[9] [Reinforcement learning from human feedback](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback) (RLHF) applies these methods to optimize a policy, the LLM's output distribution, against reward signals derived from human or automated preference judgments.[10] This has been critical for aligning model outputs with user expectations, improving factuality, reducing harmful responses, and enhancing task performance.

[Benchmark](https://en.wikipedia.org/wiki/Language_model_benchmark) evaluations for LLMs have evolved from narrow linguistic assessments toward comprehensive, [multi-task](https://en.wikipedia.org/wiki/Multi-task_learning) evaluations measuring [reasoning](https://en.wikipedia.org/wiki/Reasoning_model), [factual accuracy](https://en.wikipedia.org/wiki/Accuracy_and_precision), [alignment](https://en.wikipedia.org/wiki/AI_alignment), and [safety](https://en.wikipedia.org/wiki/AI_safety).[11][12] [Hill climbing](https://en.wikipedia.org/wiki/Hill_climbing), iteratively optimizing models against benchmarks, has emerged as a dominant strategy, producing rapid incremental performance gains but raising concerns of [overfitting](https://en.wikipedia.org/wiki/Overfitting) to benchmarks rather than achieving genuine [generalization](https://en.wikipedia.org/wiki/Generalization_(machine_learning)) or robust capability improvements.[13]

## Contents

- [1 History](#History) - [2 Dataset preprocessing](#Dataset_preprocessing) 2.1 Tokenization 2.1.1 Byte-pair encoding 2.1.2 Problems 2.2 Dataset cleaning 2.3 Synthetic data - [3 Training](#Training) 3.1 Cost 3.2 Fine-tuning - [4 Architecture](#Architecture) 4.1 Attention mechanism and context window 4.2 Mixture of experts 4.3 Parameter size 4.3.1 Quantization - [5 Extensibility](#Extensibility) 5.1 Prompt engineering 5.2 Dialogue processing (chatbot) 5.3 Retrieval-augmented generation 5.4 Tool use 5.5 Agency 5.6 Reasoning 5.6.1 Chaining 5.6.2 Model-native reasoning 5.7 Inference optimization - [6 Forms of input and output](#Forms_of_input_and_output) 6.1 Multimodality 6.2 Non-natural languages - [7 Properties](#Properties) 7.1 Scaling laws 7.2 Emergent abilities - [8 Interpretation](#Interpretation) 8.1 Mechanistic interpretability 8.2 Understanding and intelligence - [9 Evaluation](#Evaluation) 9.1 Perplexity 9.1.1 Measures 9.2 Benchmarks 9.2.1 Datasets 9.2.2 Adversarial evaluations - [10 Limitations and challenges](#Limitations_and_challenges) 10.1 Hallucinations 10.2 Algorithmic bias 10.2.1 Stereotyping 10.2.2 Selection bias 10.2.3 Political bias - [11 Safety](#Safety) 11.1 CBRN and content misuse 11.1.1 Content filtering 11.2 Sycophancy and glazing 11.3 Security 11.3.1 Prompt injection 11.3.2 Sleeper agents - [12 Societal concerns](#Societal_concerns) 12.1 Copyright and content memorization 12.2 Human provenance 12.3 Energy demands 12.4 Mental health 12.5 Sentience - [13 See also](#See_also) - [14 References](#References) - [15 Further reading](#Further_reading)

## History

[edit](https://en.wikipedia.org/w/index.php?title=Large_language_model&action=edit&section=1)

The number of publications about large language models by year grouped by publication types.

The training compute of notable large models in FLOPs vs publication date over the period 2010–2024. For overall notable models (top left), frontier models (top right), top language models (bottom left) and top models within leading companies (bottom right). The majority of these models are language models.

The training compute of notable large AI models in FLOPs vs publication date over the period 2017–2024. The majority of large models are language models or multimodal models with language capacity.

Before the emergence of transformer-based models in 2017, some [language models](https://en.wikipedia.org/wiki/Language_model) were considered large relative to the computational and data constraints of their time. In the early 1990s, [IBM](https://en.wikipedia.org/wiki/IBM)'s statistical models pioneered [word alignment](https://en.wikipedia.org/wiki/Bitext_word_alignment) techniques for machine translation, laying the groundwork for [corpus-based language modeling](https://en.wikipedia.org/wiki/Construction_grammar). In 2001, a smoothed [n-gram model](https://en.wikipedia.org/wiki/Word_n-gram_language_model), such as those employing [Kneser–Ney smoothing](https://en.wikipedia.org/wiki/Kneser%E2%80%93Ney_smoothing), trained on 300 million words, achieved state-of-the-art [perplexity](https://en.wikipedia.org/wiki/Perplexity) on benchmark tests.[14] During the 2000s, with the rise of widespread internet access, researchers began compiling massive text datasets from the web ("web as corpus"[15]) to train statistical language models.[16][17]

Moving beyond *n*-gram models, researchers started in 2000 to use neural networks to learn language models.[18] Following the breakthrough of [deep neural networks](https://en.wikipedia.org/wiki/Deep_learning) in image classification around 2012,[19] similar architectures were adapted for language tasks. This shift was marked by the development of [word embeddings](https://en.wikipedia.org/wiki/Word_embedding) (eg, [Word2Vec](https://en.wikipedia.org/wiki/Word2vec) by Mikolov in 2013) and sequence-to-sequence ([seq2seq](https://en.wikipedia.org/wiki/Seq2seq)) models using [LSTM](https://en.wikipedia.org/wiki/Long_short-term_memory). In 2016, Google transitioned its translation service to [neural machine translation](https://en.wikipedia.org/wiki/Neural_machine_translation) (NMT), replacing statistical phrase-based models with deep [recurrent neural networks](https://en.wikipedia.org/wiki/Recurrent_neural_network). These early NMT systems used LSTM-based [encoder-decoder architectures](https://en.wikipedia.org/wiki/Encoder-decoder_model), as they preceded the invention of [transformers](https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)).

An illustration of main components of the transformer model from the original paper, where layers were normalized after (instead of before) multiheaded attention

At the 2017 [NeurIPS](https://en.wikipedia.org/wiki/NeurIPS) conference, [Google](https://en.wikipedia.org/wiki/Google) researchers introduced the transformer architecture in their landmark paper "[Attention Is All You Need](https://en.wikipedia.org/wiki/Attention_Is_All_You_Need)". This paper's goal was to improve upon 2014 seq2seq technology,[20] and was based mainly on the [attention](https://en.wikipedia.org/wiki/Attention_(machine_learning)) mechanism developed by Bahdanau et al. in 2014.[21] The following year in 2018, [BERT](https://en.wikipedia.org/wiki/BERT_(language_model)) was introduced and quickly became "ubiquitous".[22] Though the original transformer has both encoder and decoder blocks, BERT is an encoder-only model. Academic and research usage of BERT began to decline in 2023, following rapid improvements in the abilities of decoder-only models (such as GPT) to solve tasks via [prompting](https://en.wikipedia.org/wiki/Prompt_engineering).[23]

Although decoder-only [GPT-1](https://en.wikipedia.org/wiki/GPT-1) was introduced in 2018, it was [GPT-2](https://en.wikipedia.org/wiki/GPT-2) in 2019 that caught widespread attention because [OpenAI](https://en.wikipedia.org/wiki/OpenAI) claimed to have initially deemed it too powerful to release publicly, out of fear of malicious use.[24] [GPT-3](https://en.wikipedia.org/wiki/GPT-3) in 2020 went a step further and as of 2025[update] is available only via [API](https://en.wikipedia.org/wiki/Web_API) with no offering of downloading the model to execute locally. But it was the 2022 consumer-facing chatbot [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT) that received extensive media coverage and public attention.[25] The 2023 [GPT-4](https://en.wikipedia.org/wiki/GPT-4) was praised for its increased accuracy and as a "holy grail" for its [multimodal](https://en.wikipedia.org/wiki/Multimodal_learning) capabilities.[26] OpenAI did not reveal the high-level architecture and the number of [parameters](https://en.wikipedia.org/wiki/Parameter#Artificial_intelligence) of GPT-4. The release of ChatGPT led to an uptick in LLM usage across several research subfields of computer science, including robotics, software engineering, and societal impact work.[23] In 2024 OpenAI released the [reasoning model](https://en.wikipedia.org/wiki/Reasoning_language_model) [OpenAI o1](https://en.wikipedia.org/wiki/OpenAI_o1), which generates long chains of thought before returning a final answer.[27] Many LLMs with parameter counts comparable to those of OpenAI's GPT series have been developed.[28]

Since 2022, open-weight models have been gaining popularity, especially at first with [BLOOM](https://en.wikipedia.org/wiki/BLOOM_(language_model)) and [LLaMA](https://en.wikipedia.org/wiki/LLaMA), though both have restrictions on usage and deployment. [Mistral AI](https://en.wikipedia.org/wiki/Mistral_AI)'s models Mistral 7B and Mixtral 8x7b have a more permissive [Apache License](https://en.wikipedia.org/wiki/Apache_License). In January 2025, [DeepSeek](https://en.wikipedia.org/wiki/DeepSeek) released DeepSeek R1, a 671-billion-parameter open-weight model that performs comparably to OpenAI o1 but at a much lower price per token for users.[29]

Since 2023, many LLMs have been trained to be [multimodal](https://en.wikipedia.org/wiki/Multimodal_learning), having the ability to also process or generate other types of data, such as images, audio, or 3D mesh.[30] These LLMs are also called large multimodal models (LMMs),[31] or multimodal large language models (MLLMs).[32][33]

As of 2024, the largest and most capable models are all based on the transformer architecture. Some recent implementations are based on other architectures, such as [recurrent neural network](https://en.wikipedia.org/wiki/Recurrent_neural_network) variants and [Mamba](https://en.wikipedia.org/wiki/Mamba_(deep_learning_architecture)) (a [state space](https://en.wikipedia.org/wiki/State-space_representation) model).[34][35][36]

Open-weight LLMs have increasingly shaped the field since 2023, contributing to broader participation in AI development and greater transparency in model evaluation. Vake et al. (2025) demonstrated that community-driven contributions to open-weight models measurably improve their efficiency and performance, with user participation growing rapidly on collaborative platforms such as Hugging Face.[37] Paris et al. (2025) further argued that openness in AI should extend beyond releasing model code or weights to encompass inclusiveness, accountability, and ethical responsibility in AI research and deployment.[38] Collectively, these studies highlight that open-weight LLMs can accelerate innovation and enhance scientific reproducibility, while fostering a more transparent and participatory AI ecosystem.

## Dataset preprocessing

[edit](https://en.wikipedia.org/w/index.php?title=Large_language_model&action=edit&section=2)

See also: [List of datasets for machine-learning research § Internet](https://en.wikipedia.org/wiki/List_of_datasets_for_machine-learning_research#Internet)

### Tokenization

[edit](https://en.wikipedia.org/w/index.php?title=Large_language_model&action=edit&section=3)

As [machine learning](https://en.wikipedia.org/wiki/Machine_learning) algorithms process numbers rather than text, the text must be converted to numbers. In the first step, a vocabulary is decided upon, then integer indices are arbitrarily but uniquely assigned to each vocabulary entry, and finally, an [embedding](https://en.wikipedia.org/wiki/Word_embedding) is associated to the integer index. Algorithms include [byte-pair encoding](https://en.wikipedia.org/wiki/Byte-pair_encoding) (BPE) and WordPiece. There are also special tokens serving as [control characters](https://en.wikipedia.org/wiki/Control_character), such as `[MASK]` for masked-out token (as used in [BERT](https://en.wikipedia.org/wiki/BERT_(language_model))), and `[UNK]` ("unknown") for characters not appearing in the vocabulary. Also, some special symbols are used to denote special text formatting. For example, "Ġ" denotes a preceding whitespace in [RoBERTa](https://en.wikipedia.org/wiki/RoBERTa) and GPT and "##" denotes continuation of a preceding word in BERT.[39]

For example, the BPE tokenizer used by the legacy version of [GPT-3](https://en.wikipedia.org/wiki/GPT-3) would split tokenizer: texts -> series of numerical "tokens" as

| token | izer | : | texts | -> | series | of | numerical | " | t | ok | ens | " |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Tokenization also [compresses](https://en.wikipedia.org/wiki/Data_compression) the datasets. Because LLMs generally require input to be an [array](https://en.wikipedia.org/wiki/Array_(data_structure)) that is not [jagged](https://en.wikipedia.org/wiki/Jagged_array), the shorter texts must be "padded" until they match the length of the longest one. The average number of words per token depends on the language.[40][41] In English, the ratio is typically around 0.75 words per token, with 4 characters per token on average.[42]

#### Byte-pair encoding

[edit](https://en.wikipedia.org/w/index.php?title=Large_language_model&action=edit&section=4)

Main article: [Byte-pair encoding](https://en.wikipedia.org/wiki/Byte-pair_encoding)

As an example, consider a tokenizer based on byte-pair encoding. In the first step, all unique characters (including blanks and [punctuation marks](https://en.wikipedia.org/wiki/Punctuation_mark)) are treated as an initial set of [n-grams](https://en.wikipedia.org/wiki/N-gram) (i.e. initial set of uni-grams). Successively the most frequent pair of adjacent characters is merged into a bi-gram and all instances of the pair are replaced by it. All occurrences of adjacent pairs of (previously merged) *n*-grams that most frequently occur together are then again merged into even lengthier *n*-gram, until a vocabulary of prescribed size is obtained. After a tokenizer is trained, any text can be tokenized by it, as long as it does not contain characters not appearing in the initial-set of uni-grams.[43]

#### Problems

[edit](https://en.wikipedia.org/w/index.php?title=Large_language_model&action=edit&section=5)

A token vocabulary based on the frequencies extracted from mainly English corpora uses as few tokens as possible for an average English word. However, an average word in another language encoded by such an English-optimized tokenizer is split into a suboptimal amount of tokens. GPT-2 tokenizer can use up to 15 times more tokens per word for some languages, for example for the [Shan language](https://en.wikipedia.org/wiki/Shan_language) from [Myanmar](https://en.wikipedia.org/wiki/Myanmar). Even more widespread languages such as [Portuguese](https://en.wikipedia.org/wiki/Portuguese_language) and [German](https://en.wikipedia.org/wiki/German_language) have "a premium of 50%" compared to English.[41]

### Dataset cleaning

[edit](https://en.wikipedia.org/w/index.php?title=Large_language_model&action=edit&section=6)

Main article: [Data cleansing](https://en.wikipedia.org/wiki/Data_cleansing)

In the context of training LLMs, datasets are typically cleaned by removing low-quality, duplicated, or toxic data.[44] Cleaned datasets can increase training efficiency and lead to improved downstream performance.[45][46] A trained LLM can be used to clean datasets for training a further LLM.[47]

With the increasing proportion of LLM-generated content on the web, data cleaning in the future may include filtering out such content. LLM-generated content can pose a problem if the content is similar to human text (making filtering difficult) but of lower quality (degrading performance of models trained on it).[3]

### Synthetic data

[edit](https://en.wikipedia.org/w/index.php?title=Large_language_model&action=edit&section=7)

Main article: [Synthetic data](https://en.wikipedia.org/wiki/Synthetic_data)

Training of largest language models might need more linguistic data than naturally available, or that the naturally occurring data is of insufficient quality. In these cases, synthetic data might be used. Microsoft's [Phi](https://en.wikipedia.org/w/index.php?title=Phi_(LLM)&action=edit&redlink=1) series of LLMs is trained on textbook-like data generated by another LLM.[48]

## Training

[edit](https://en.wikipedia.org/w/index.php?title=Large_language_model&action=edit&section=8)

See also: [Fine-tuning (machine learning)](https://en.wikipedia.org/wiki/Fine-tuning_(machine_learning))

An LLM is a type of [foundation model](https://en.wikipedia.org/wiki/Foundation_model) (large X model) trained on language. LLMs can be trained in different ways. In particular, GPT models are first pretrained to predict the next word on a large amount of data, before being fine-tuned.[49]

### Cost

[edit](https://en.wikipedia.org/w/index.php?title=Large_language_model&action=edit&section=9)

Substantial infrastructure is necessary for training the largest models. The tendency towards larger models is visible in the [list of large language models](https://en.wikipedia.org/wiki/List_of_large_language_models). For example, the training of GPT-2 (i.e. a 1.5-billion-parameters model) in 2019 cost $50,000, while training of the [PaLM](https://en.wikipedia.org/wiki/PaLM) (i.e. a 540-billion-parameters model) in 2022 cost $8 million, and Megatron-Turing NLG 530B (in 2021) cost around $11 million. The qualifier "large" in "large language model" is inherently vague, as there is no definitive threshold for the number of parameters required to qualify as "large". [GPT-1](https://en.wikipedia.org/wiki/GPT-1) of 2018 has 117 million parameters.[citation needed]

### Fine-tuning

[edit](https://en.wikipedia.org/w/index.php?title=Large_language_model&action=edit&section=10)

Before being [fine-tuned](https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)), most LLMs are next-token predictors. The fine-tuning shapes the LLM's behavior via techniques like [reinforcement learning from human feedback](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback) (RLHF) or [constitutional AI](https://en.wikipedia.org/wiki/Constitutional_AI).[50]

Instruction fine-tuning is a form of [supervised learning](https://en.wikipedia.org/wiki/Supervised_learning) used to teach LLMs to follow user instructions. In 2022, OpenAI demonstrated [InstructGPT](https://en.wikipedia.org/wiki/InstructGPT), a version of GPT-3 similarly fine-tuned to follow instructions.[51]

Reinforcement learning from human feedback (RLHF) involves training a reward model to predict which text humans prefer. Then, the LLM can be fine-tuned through [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning) to better satisfy this reward model. Since humans typically prefer truthful, helpful and harmless answers, RLHF favors such answers.[52]

## Architecture

[edit](https://en.wikipedia.org/w/index.php?title=Large_language_model&action=edit&section=11)

LLMs are generally based on the [transformer](https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)) architecture, which leverages an [attention](https://en.wikipedia.org/wiki/Attention_(machine_learning)) mechanism that enables the model to process relationships between all elements in a sequence simultaneously, regardless of their distance from each other.[citation needed]

### Attention mechanism and context window

[edit](https://en.wikipedia.org/w/index.php?title=Large_language_model&action=edit&section=12)

See also: [Attention (machine learning)](https://en.wikipedia.org/wiki/Attention_(machine_learning))

When each head calculates, according to its own criteria, how much other tokens are relevant for the "it_" token, note that the second attention head, represented by the second column, is focusing most on the first two rows, i.e. the tokens "The" and "animal", while the third column is focusing most on the bottom two rows, i.e. on "tired", which has been tokenized into two tokens.[53]

In order to find out which tokens are relevant to each other within the scope of the context window, the attention mechanism calculates "soft" weights for each token, more precisely for its embedding, by using multiple attention heads, each with its own "relevance" for calculating its own soft weights. For example, the small (i.e. 117M parameter sized) [GPT-2](https://en.wikipedia.org/wiki/GPT-2) model has had twelve attention heads and a context window of only 1k tokens.[54] In its medium version it has 345M parameters and contains 24 layers, each with 12 attention heads.
**Published:** 2025-11-18

### Result 2
**Title:** OpenAI’s new LLM exposes the secrets of how AI really works | MIT Technology Review
**URL:** https://www.technologyreview.com/2025/11/13/1127914/openais-new-llm-exposes-the-secrets-of-how-ai-really-works/?utm_source=valyu.ai&utm_medium=referral
**Source:** web

**Content:**
OpenAI’s new LLM exposes the secrets of how AI really works | MIT Technology Review

EXECUTIVE SUMMARY

ChatGPT maker OpenAI has built an experimental large language model that is far easier to understand than typical models. That’s a big deal, because today’s LLMs are black boxes: Nobody fully understands how they do what they do. Building a model that is more transparent sheds light on how LLMs work in general, helping researchers figure out why models hallucinate, why they go off the rails, and just how far we should trust them with critical tasks.

“As these AI systems get more powerful, they’re going to get integrated more and more into very important domains,” Leo Gao, a research scientist at OpenAI, told *MIT Technology Review* in an exclusive preview of the new work. “It’s very important to make sure they’re safe.”

This is still early research. The new model, called a weight-sparse transformer, is far smaller and far less capable than top-tier mass-market models like the firm’s GPT-5, Anthropic’s Claude, and Google DeepMind’s Gemini. At most it’s as capable as GPT-1, a model that OpenAI developed back in 2018, says Gao (though he and his colleagues haven’t done a direct comparison).

But the aim isn’t to compete with the best in class (at least, not yet). Instead, by looking at how this experimental model works, OpenAI hopes to learn about the hidden mechanisms inside those bigger and better versions of the technology.

It’s interesting research, says Elisenda Grigsby, a mathematician at Boston College who studies how LLMs work and who was not involved in the project: “I’m sure the methods it introduces will have a significant impact.”

Lee Sharkey, a research scientist at AI startup Goodfire, agrees. “This work aims at the right target and seems well executed,” he says.

### Why models are so hard to understand

OpenAI’s work is part of a hot new field of research known as mechanistic interpretability, which is trying to map the internal mechanisms that models use when they carry out different tasks.

That’s harder than it sounds. LLMs are built from neural networks, which consist of nodes, called neurons, arranged in layers. In most networks, each neuron is connected to every other neuron in its adjacent layers. Such a network is known as a dense network.

Dense networks are relatively efficient to train and run, but they spread what they learn across a vast knot of connections. The result is that simple concepts or functions can be split up between neurons in different parts of a model. At the same time, specific neurons can also end up representing multiple different features, a phenomenon known as superposition (a term borrowed from quantum physics). The upshot is that you can’t relate specific parts of a model to specific concepts.

“Neural networks are big and complicated and tangled up and very difficult to understand,” says Dan Mossing, who leads the mechanistic interpretability team at OpenAI. “We’ve sort of said: ‘Okay, what if we tried to make that not the case?’” Instead of building a model using a dense network, OpenAI started with a type of neural network known as a weight-sparse transformer, in which each neuron is connected to only a few other neurons. This forced the model to represent features in localized clusters rather than spread them out. Their model is far slower than any LLM on the market. But it is easier to relate its neurons or groups of neurons to specific concepts and functions. “There’s a really drastic difference in how interpretable the model is,” says Gao. Gao and his colleagues have tested the new model with very simple tasks. For example, they asked it to complete a block of text that opens with quotation marks by adding matching marks at the end. It’s a trivial request for an LLM. The point is that figuring out how a model does even a straightforward task like that involves unpicking a complicated tangle of neurons and connections, says Gao. But with the new model, they were able to follow the exact steps the model took. “We actually found a circuit that’s exactly the algorithm you would think to implement by hand, but it’s fully learned by the model,” he says. “I think this is really cool and exciting.” Where will the research go next? Grigsby is not convinced the technique would scale up to larger models that have to handle a variety of more difficult tasks. Gao and Mossing acknowledge that this is a big limitation of the model they have built so far and agree that the approach will never lead to models that match the performance of cutting-edge products like GPT-5. And yet OpenAI thinks it might be able to improve the technique enough to build a transparent model on a par with GPT-3, the firm’s breakthrough 2021 LLM. “Maybe within a few years, we could have a fully interpretable GPT-3, so that you could go inside every single part of it and you could understand how it does every single thing,” says Gao. “If we had such a system, we would learn so much.”
**Published:** 2025-11-20

### Result 3
**Title:** A new type of large language model is set to turbocharge vibe coding in 2026, says JetBrains - Neowin
**URL:** https://www.neowin.net/news/a-new-type-of-large-language-model-is-set-to-turbocharge-vibe-coding-in-2026-says-jetbrains/?utm_source=valyu.ai&utm_medium=referral
**Source:** web

**Content:**
JetBrains, the company behind the IntelliJ IDE, has said that developer workflows could be disrupted next year by Diffusion Large Language Models (d-LLMs) replacing the dominant autoregressive (AR) models. These models will offer several benefits including out-of-order generation, bi-directional context, flexibility in editing, coordinated multi-region updates, and potential speed improvements. The core difference between d-LLMs and AR-LLMs is that the prior are capable of non-sequential generation. Developers work non-sequentially, they focus on editing and refactoring their code in an iterative manner rather than typing complete functions in one sequence. AR-LLMs generate code token-by-token in a strict left-to-right sequence whereas d-LLMs look at past and future context and make edits directly and plan token generation more globally. This aligns better with the non-linear nature of writing code we see from human developers. While d-LLMs hold promise, there are significant drawbacks standing in their way right now. Right now, the best quality output from these models is when they unmask only one token per step, but this slows them down to AR model speeds. Furthermore, when you push a d-LLM, it may output incoherent text like repetition, early termination, and malformed syntax. Right now, state-of-the-art d-LLMs show mixed performance against strong AR baselines. Despite the issues with d-LLMs, there are some currently useful niches for them. These include code completion with context editing where missing parts are filled, not just extending text; refactoring less rigid code blocks; and structured text tasks and reversal problems that rely heavily on bi-directional context. According to JetBrains, we could see d-LLMs become more prominent as researchers resolve the quality-efficiency trade-offs. The potential faster code generation could make them the core of future coding assistants that feel like “principled, code structure-aware, programming collaborators.” We could see this new generation of LLMs show up in AI coding editors such as Visual Studio Code, Cursor, and Windsurf sometime next year. The rise of these AI editors has led to a phenomenon called Vibe Coding where AI handles most of the code generation. The introduction of d-LLMs could further help people rely on AI to write correct code.

#### Tags

- [Jetbrains](https://www.neowin.net/news/tags/jetbrains/) - [Vibe coding](https://www.neowin.net/news/tags/vibe_coding/) - [D-llms](https://www.neowin.net/news/tags/d-llms/) - [Ar-llms](https://www.neowin.net/news/tags/ar-llms/) - [Llms](https://www.neowin.net/news/tags/llms/) - [Ai](https://www.neowin.net/news/tags/ai/) - [Coding](https://www.neowin.net/news/tags/coding/)

Like Post Share [Report a problem with article](https://www.neowin.net/news/report/a-new-type-of-large-language-model-is-set-to-turbocharge-vibe-coding-in-2026-says-jetbrains/) [Follow @NeowinFeed](https://twitter.com/neowinfeed)
**Published:** 2025-11-22

### Result 4
**Title:** In a First, AI Models Analyze Language As Well As a Human Expert | Quanta Magazine
**URL:** https://www.quantamagazine.org/in-a-first-ai-models-analyze-language-as-well-as-a-human-expert-20251031/?utm_source=valyu.ai&utm_medium=referral
**Source:** web

**Content:**
In a First, AI Models Analyze Language As Well As a Human Expert

If language is what makes us human, what does it mean now that large language models have gained “metalinguistic” abilities?

Among the myriad abilities that humans possess, which ones are uniquely human? Language has been a top candidate at least since Aristotle, who wrote that humanity was “the animal that has language.” Even as large language models such as ChatGPT superficially replicate ordinary speech, researchers want to know if there are specific aspects of human language that simply have no parallels in the communication systems of other animals or artificially intelligent devices.

In particular, researchers have been exploring the extent to which language models can reason about language itself. For some in the linguistic community, language models not only *don’t* have reasoning abilities, they *can’t*. This view was summed up by Noam Chomsky, a prominent linguist, and two co-authors in 2023, when they [wrote in The New York Times](https://www.nytimes.com/2023/03/08/opinion/noam-chomsky-chatgpt-ai.html) that “the correct explanations of language are complicated and cannot be learned just by marinating in big data.” AI models may be adept at using language, these researchers argued, but they’re not capable of analyzing language in a sophisticated way.

That view was challenged in a recent [paper](https://ieeexplore.ieee.org/document/11022724) by [Gašper Beguš](https://vcresearch.berkeley.edu/faculty/gasper-begus), a linguist at the University of California, Berkeley; [Maksymilian Dąbkowski](https://maksymilian-dabkowski.github.io/), who recently received his doctorate in linguistics at Berkeley; and [Ryan Rhodes](https://wavyphd.com/about) of Rutgers University. The researchers put a number of large language models, or LLMs, through a gamut of linguistic tests — including, in one case, having the LLM generalize the rules of a made-up language. While most of the LLMs failed to parse linguistic rules in the way that humans are able to, one had impressive abilities that greatly exceeded expectations. It was able to analyze language in much the same way a graduate student in linguistics would — diagramming sentences, resolving multiple ambiguous meanings, and making use of complicated linguistic features such as recursion. This finding, Beguš said, “challenges our understanding of what AI can do.”

This new work is both timely and “very important,” said [Tom McCoy](https://ling.yale.edu/profile/tom-mccoy), a computational linguist at Yale University who was not involved with the research. “As society becomes more dependent on this technology, it’s increasingly important to understand where it can succeed and where it can fail.” Linguistic analysis, he added, is the ideal test bed for evaluating the degree to which these language models can reason like humans.

## Infinite Complexity

One challenge of giving language models a rigorous linguistic test is making sure they don’t already know the answers. These systems are typically trained on huge amounts of written information — not just the bulk of the internet, in dozens if not hundreds of languages, but also things like linguistics textbooks. The models could, in theory, simply memorize and regurgitate the information that they’ve been fed during training.

To avoid this, Beguš and his colleagues created a linguistic test in four parts. Three of the four parts involved asking the model to analyze specially crafted sentences using tree diagrams, which were first introduced in Chomsky’s landmark 1957 book, *Syntactic Structures*. These diagrams break sentences down into noun phrases and verb phrases and then further subdivide them into nouns, verbs, adjectives, adverbs, prepositions, conjunctions and so forth.

One part of the test focused on recursion — the ability to embed phrases within phrases. “The sky is blue” is a simple English sentence. “Jane said that the sky is blue” embeds the original sentence in a slightly more complex one. Importantly, this process of recursion can go on forever: “Maria wondered if Sam knew that Omar heard that Jane said that the sky is blue” is also a grammatically correct, if awkward, recursive sentence.

Recursion has been called one of the defining characteristics of human language by Chomsky and others — and indeed, perhaps a defining characteristic of the human mind. Linguists have argued that its limitless potential is what gives human languages their ability to generate an infinite number of possible sentences out of a finite vocabulary and a finite set of rules. So far, there’s no convincing evidence that other animals can use recursion in a sophisticated way.

Recursion can occur at the beginning or end of a sentence, but the form that is most challenging to master, called center embedding, takes place in the middle — for instance, going from “the cat died” to “the cat *the dog bit* died.”

Beguš’ test fed the language models 30 original sentences that featured tricky examples of recursion. For example: “The astronomy the ancients we revere studied was not separate from astrology.” Using a syntactic tree, one of the language models — OpenAI’s o1 — was able to determine that the sentence was structured like so:

> The astronomy [the ancients [we revere] studied] was not separate from astrology.

The model then went further and added another layer of recursion to the sentence:

> The astronomy [the ancients [we revere [who lived in lands we cherish]] studied] was not separate from astrology.

Beguš, among others, didn’t anticipate that this study would come across an AI model with a higher-level “metalinguistic” capacity – “the ability not just to use a language but to think about language,” as he put it.

That is one of the “attention-getting” aspects of their paper, said [David Mortensen](https://www.cs.cmu.edu/~dmortens/), a computational linguist at Carnegie Mellon University who was not involved with the work. There has been debate about whether language models are just predicting the next word (or linguistic token) in a sentence, which is qualitatively different from the deep understanding of language that humans have. “Some people in linguistics have said that LLMs are not really doing language,” he said. “This looks like an invalidation of those claims.”

## What Do You Mean?

McCoy was surprised by o1’s performance in general, particularly by its ability to recognize ambiguity, which is “famously a difficult thing for computational models of language to capture,” he said. Humans “have a lot of commonsense knowledge that enables us to rule out the ambiguity. But it’s difficult for computers to have that level of commonsense knowledge.”

A sentence such as “Rowan fed his pet chicken” could be describing the chicken that Rowan keeps as a pet, or it could be describing the meal of chicken meat that he gave to his (presumably more traditional) animal companion. The o1 model correctly produced two different syntactic trees, one that corresponds to the first interpretation of the sentence and one that corresponds to the latter.

The researchers also carried out experiments related to phonology — the study of the pattern of sounds and of the way the smallest units of sound, called phonemes, are organized. To speak fluently, like a native speaker, people follow phonological rules that they might have picked up through practice without ever having been explicitly taught. In English, for example, adding an “s” to a word that ends in a “g” creates a “z” sound, as in “dogs.” But an “s” added to a word ending in “t” sounds more like a standard “s,” as in “cats.”

In the phonology task, the group made up 30 new mini-languages, as Beguš called them, to find out whether the LLMs could correctly infer the phonological rules without any prior knowledge. Each language consisted of 40 made-up words. Here are some example words from one of the languages:

> θalp > ʃebre > ði̤zṳ > ga̤rbo̤nda̤ > ʒi̤zṳðe̤jo

They then asked the language models to analyze the phonological processes of each language. For this language, o1 correctly wrote that “a vowel becomes a breathy vowel when it is immediately preceded by a consonant that is both voiced and an obstruent” — a sound formed by restricting airflow, like the “t” in “top.”

The languages were newly invented, so there’s no way that o1 could have been exposed to them during its training. “I was not expecting the results to be as strong or as impressive as they were,” Mortensen said.

## Uniquely Human or Not?

How far can these language models go? Will they get better, without limit, simply by getting bigger — layering on more computing power, more complexity and more training data? Or are some of the characteristics of human language the result of an evolutionary process that is limited to our species?

The recent results show that these models can, in principle, do sophisticated linguistic analysis. But no model has yet come up with anything original, nor has it taught us something about language we didn’t know before.

If improvement is just a matter of increasing both computational power and the training data, then Beguš thinks that language models will eventually surpass us in language skills. Mortensen said that current models are somewhat limited. “They’re trained to do something very specific: given a history of tokens [or words], to predict the next token,” he said. “They have some trouble generalizing by virtue of the way they’re trained.”

But in view of recent progress, Mortensen said he doesn’t see why language models won’t eventually demonstrate an understanding of our language that’s better than our own. “It’s only a matter of time before we are able to build models that generalize better from less data in a way that is more creative.”

The new results show a steady “chipping away” at properties that had been regarded as the exclusive domain of human language, Beguš said. “It appears that we’re less unique than we previously thought we were.”

[To Have Machines Make Math Proofs, Turn Them Into a Puzzle](https://www.quantamagazine.org/to-have-machines-make-math-proofs-turn-them-into-a-puzzle-20251110/)

[Q&A](https://www.quantamagazine.org/tag/qa/)

### To Have Machines Make Math Proofs, Turn Them Into a Puzzle

By John Pavlus November 10, 2025 Save Article Read Later

[The Game Theory of How Algorithms Can Drive Up Prices](https://www.quantamagazine.org/the-game-theory-of-how-algorithms-can-drive-up-prices-20251022/)

[game theory](https://www.quantamagazine.org/tag/game-theory/)

### The Game Theory of How Algorithms Can Drive Up Prices

By Ben Brubaker October 22, 2025 Save Article Read Later

[Researchers Discover the Optimal Way To Optimize](https://www.quantamagazine.org/researchers-discover-the-optimal-way-to-optimize-20251013/)

[algorithms](https://www.quantamagazine.org/tag/algorithms/)

### Researchers Discover the Optimal Way To Optimize

By Steve Nadis October 13, 2025 Save Article Read Later
**Published:** 2025-11-03

### Result 5
**Title:** What Are Large Language Models (LLMs)? | IBM
**URL:** https://www.ibm.com/think/topics/large-language-models?utm_source=valyu.ai&utm_medium=referral
**Source:** web

**Content:**
# What are large language models (LLMs)?

## Author

Staff Editor, AI Models

IBM Think

## What are LLMs?

Large language models (LLMs) are a category of deep learning models trained on immense amounts of data, making them capable of understanding and generating natural language and other types of content to perform a wide range of tasks. LLMs are built on a type of neural network architecture called a transformer which excels at handling sequences of words and capturing patterns in text.

LLMs work as giant statistical prediction machines that repeatedly predict the next word in a sequence. They learn patterns in their text and generate language that follows those patterns.

LLMs represent a major leap in how humans interact with technology because they are the first AI system that can handle unstructured human language at scale, allowing for natural communication with machines. Where traditional search engines and and other programmed systems used algorithms to match keywords, LLMs capture deeper context, nuance and reasoning. LLMs, once trained, can adapt to many applications that involve interpreting text, like summarizing an article, debugging code or drafting a legal clause. When given agentic capabilities, LLMs can perform, with varying degrees of autonomy, various tasks that would otherwise be performed by humans.

LLMs are the culmination of decades of progress in natural language processing (NLP) and machine learning research, and their development is largely responsible for the explosion of artificial intelligence advancements across the late 2010s and 2020s. Popular LLMs have become household names, bringing generative AI to the forefront of the public interest. LLMs are also used widely in enterprises, with organizations investing heavily across numerous business functions and use cases.

LLMs are easily accessible to the public through interfaces like Anthropic’s Claude, Open AI’s ChatGPT, Microsoft’s Copilot, Meta’s Llama models, and Google’s Gemini assistant, along with its BERT and PaLM models. IBM maintains a Granite model series on watsonx.ai, which has become the generative AI backbone for other IBM products like watsonx Assistant and watsonx Orchestrate.

Think Newsletter

Stay up to date on the most important—and intriguing—industry trends on AI, automation, data and beyond with the Think newsletter. See the IBM Privacy Statement.

## Pretraining large language models

Training starts with a massive amount of data—billions or trillions of words from books, articles, websites, code and other text sources. Data scientists oversee cleaning and pre-processing to remove errors, duplication and undesirable content.

This text is broken down into smaller, machine-readable units called “tokens,” during a process of “tokenization.” Tokens are smaller units such as words, subwords or characters. This standardizes the language so rare and novel words can be handled consistently.

LLMs are initially trained with self-supervised learning, a machine learning technique that uses unlabeled data for supervised learning. Self-supervised learning doesn’t require labeled datasets, but it’s closely related to supervised learning in that it optimizes performance against a "ground truth." In self-supervised learning, tasks are designed such that ground truth can be inferred from unlabeled data. Instead of being told what the “correct output” is for each input, as in supervised learning, the model tries to find patterns, structures or relationships in the data on its own.

### Self-attention

The model passes the tokens through a transformer network. Transformer models, introduced in 2017, are useful due to their self-attention mechanism, which allows them to “pay attention to” different tokens at different moments. This technique is the centerpiece of the transformer and its prime innovation. Self-attention is useful in part because it allows the AI model to calculate the relationships and dependencies between tokens, especially ones that are distant from one another in the text. Transformer architectures also allow for parallelization, making the process much more efficient than previous methods. These qualities allowed LLMs to handle unprecedentedly large datasets.

Once text is split into tokens, each token is mapped to a vector of numbers called an embedding. Neural networks consists of layers of artificial neurons, where each neuron performs a mathematical operation. Transformers consist of many of these layers, and at each, the embeddings are slightly adjusted, becoming richer contextual representations from layer to layer.

The goal in this process is for the model to learn semantic associations between words, so that words like “bark” and “dog” appear closer together in vector space in an essay about dogs than “bark” and “tree” would, based on the surrounding dog-related words in the essay. Transformers also add positional encodings, which give each token information about its place in the sequence.

To compute attention, each embedding is projected into three distinct vectors using learned weight matrices: a query, a key, and a value. The query represents what a given token is “seeking,” the key represents the information that each token contains, and the value “returns” the information from each key vector, scaled by its respective attention weight.

Alignment scores are then computed as the similarity between queries and keys. These scores, once normalized into attention weights, determine how much of each value vector flows into the representation of the current token. This process allows the model to flexibly focus on relevant context while ignoring less important tokens (like “tree”).

Self-attention thus creates “weighted” connections between all tokens more efficiently than earlier architectures could. The model assigns weights to each relationship between the tokens. LLMs can have billions or trillions of these weights, which are one type of LLM parameter, the internal configuration variables of a machine learning model that control how it processes data and makes predictions. The number of parameters refers to how many of these variables exist in a model, with some LLMs containing billions of parameters. So-called small language models are smaller in scale and scope with comparatively few parameters, making them suitable for deployment on smaller devices or in resource-constrained environments.

During training, the model makes predictions across millions of examples drawn from its training data, and a loss function quantifies the error of each prediction. Through an iterative cycle of making predictions and then updating model weights through backpropagation and gradient descent, the model “learns” the the weights in the layers that produce the query, key and value vectors.

Once those weights are sufficiently optimized, they’re able to take in any token’s original vector embedding and produce query, key and value vectors for it that, when interacting with the vectors generated for all the other tokens, will yield “better” alignment scores that in turn result in attention weights which help the model produce better outputs. The end result is a model that has learned patterns in grammar, facts, reasoning structures, writing styles and more.

## Fine-tuning large language models

After training (or in the context of additional training, “pretraining”), LLMs can be fine-tuned to make them more useful in certain contexts. For example, a foundational model trained on a large dataset of general knowledge can be fine-tuned on a corpus of legal Q&As in order to create a chatbot for the legal field.

Here are some of the most common forms of fine-tuning. Practitioners may use one method or a combination of several.

### Supervised fine-tuning

Fine-tuning most often happens in a supervised context with a much smaller, labelled dataset. The model updates its weights to better match the new ground truth (in this case, labeled data).

While pretraining is intended to give the model broad general knowledge, fine-tuning adapts a general-purpose model to specific tasks like summarization, classification or customer support. These functional adaptations represent new types of tasks. Supervised fine-tuning produces outputs closer to the human-provided examples, requiring far fewer resources than training from scratch.

Supervised fine-tuning is also useful for domain-specific customization, such as training a model on medical documents so it has the ability to answer healthcare-related questions.

### Reinforcement learning from human feedback

To further refine models, data scientists often use reinforcement learning from human feedback (RLHF), a form of fine-tuning where humans rank model outputs and the model is trained to prefer outputs that humans rank higher. RLHF is often used in alignment, a process which consists of making LLM outputs useful, safe and consistent with human values.

RLHF is also particularly useful for stylistic alignment, where an LLM can be adjusted to respond in a way that's more casual, humorous or brand-consistent. Stylistic alignment involves training for the same types of tasks, but producing outputs in a specific style.

### Reasoning models

Purely supervised fine-tuning teaches a model to imitate examples, but it doesn’t necessarily encourage better reasoning, which involves abstract, multi-step processes. Such tasks don’t always have abundant labeled data, so reinforcement learning is often used in the creation of reasoning models, LLMs that have been fine-tuned to break complex problems into smaller steps, often called “reasoning traces,” prior to generating a final output. Increasingly sophisticated means of training models gives them chain-of-thought reasoning and other multi-step decision-making strategies.

### Instruction tuning

Another form of LLM customization is instruction tuning, a process specifically designed to improve a model’s ability to follow human instructions. The input samples in an instruction dataset consist entirely of tasks that resemble requests users might make in their prompts; the outputs demonstrate desirable responses to those requests. Since pretrained LLMs are not inherently optimized for following instructions or conversational goals, instruction tuning is used to better align the model with user intent.

## Using large language models

Once trained, large language models work by responding to prompts by tokenizing the prompt, converting it into embeddings, and using its transformer to generate text one token at a time, calculating the probabilities for all potential next tokens, and outputting the most likely one. This process, called inference, is repeated until the output is complete. The model does not “know” the final answer in advance; it uses all the statistical relationships it learned in training to predict one token at a time, making its best guess at every step.

The easiest and fastest way to get domain-specific knowledge from a general-purpose LLM is through prompt engineering, which does not require additional training. Users can modify prompts in all sorts of ways. For example, a prompt like “answer in the voice of a trained healthcare professional” could yield more relevant results (Note that LLMs are not recommended to be used for medical advice!).

LLMs have other strategies to control their outputs, such as LLM temperature, which controls the randomness of text that is generated by LLMs during inference, or top-k/top-p sampling, which limits the set of tokens considered to the most likely ones, balancing creativity and coherence.

The context window is the maximum number of tokens that a model can “see” and use at once when generating text. Early LLMs had short windows, but newer LLMs have hundreds of thousands of tokens in their context windows, enabling use cases like summarizing entire research papers, performing code assistance on large codebases and holding long continuous conversations with users.

Retrieval augmented generation (RAG) is a method for connecting a pretrained model with external knowledge bases, enabling them to deliver more relevant responses at a higher level of accuracy. The retrieved information is passed into the model’s context window, so the model can use it when generating responses, without needing retraining. For example, by connecting an LLM to a dynamic weather service database, an LLM can retrieve information for a user about that day’s weather report.

## Deploying LLMs

Building an LLM from scratch is a complex and resource-intensive process. The most popular LLMs are the result of immense amounts of data, GPUs, energy and human expertise, which is why most are built and maintained by large tech companies with expansive resources.

However, many of these models are accessible to all developers through APIs. Developers can use pretrained models to build chatbots, knowledge retrieval systems, automation tools and more. For more control over data and customization, many open-source models can be deployed locally or in the cloud. Github, Hugging Face, Kaggle and other platforms make AI development accessible to all.

Developers can use LLMs as the basis for all kinds of AI applications. One of the most exciting developments in AI is the agentic system. AI agents don’t just think; they do. By themselves, LLMs simply generate text based on context, but they can be integrated with memory, APIs, decision logic and other external systems to perform specific tasks, like booking a flight or piloting a self-driving vehicle.

## Large language model use cases

LLMs are redefining business processes and have proven their versatility across a myriad of use cases in many industries.

- Text generation: LLMs can do all sorts of content creation tasks like drafting emails, blog posts or legal memos in response to prompts.

Text generation: LLMs can do all sorts of content creation tasks like drafting emails, blog posts or legal memos in response to prompts.

- Text summarization: LLMs can summarize long articles, news stories, research reports, corporate documentation and customer history into thorough texts tailored in length to a desired output format and style.

Text summarization: LLMs can summarize long articles, news stories, research reports, corporate documentation and customer history into thorough texts tailored in length to a desired output format and style.

- AI assistants: Chatbots powered by conversational AI can perform question answering and provide detailed information as a part of an integrated, real-time customer care solution.

AI assistants: Chatbots powered by conversational AI can perform question answering and provide detailed information as a part of an integrated, real-time customer care solution.

- Code generation: Code assist platforms aid developers in building applications, finding errors in code and uncovering security issues in multiple programming languages, even translating between them.

Code generation: Code assist platforms aid developers in building applications, finding errors in code and uncovering security issues in multiple programming languages, even translating between them.

- Sentiment analysis: Customer tone is analyzed in order to better understand customer feedback at scale.

Sentiment analysis: Customer tone is analyzed in order to better understand customer feedback at scale.

- Language translation: Automated translation provides wider coverage to organizations across languages and geographies with fluent translations and multilingual capabilities.

Language translation: Automated translation provides wider coverage to organizations across languages and geographies with fluent translations and multilingual capabilities.

- Reasoning: LLMs can solve math problems, plan multi-step processes and explain complex concepts in simpler terms.

Reasoning: LLMs can solve math problems, plan multi-step processes and explain complex concepts in simpler terms.

## Evaluating LLMs

LLMs are powerful tools, but they come with several limitations. One major concern is accuracy. During hallucinations, the model generates information that is false or misleading while sounding plausible. LLMs can also reflect and amplify biases present in their training data, producing outputs that are unfair or offensive. Additionally, their resource demands are significant: training and running LLMs requires large amounts of computational power and energy, raising both cost and environmental concerns.

Practitioners can mitigate these negative aspects of LLMs through comprehensive AI governance, the processes, standards and guardrails that help ensure AI systems and tools are safe and ethical. A key part of governance involves evaluating models against benchmarks. LLM benchmarks provide quantitative scores, making it easier to compare models. Because LLMs are general-purpose systems capable of a wide variety of tasks, their evaluation requires multiple dimensions rather than a single benchmark. Researchers and practitioners look at qualities like accuracy, efficiency, safety, fairness and robustness to determine how well a model performs.

LLMs are also evaluated on the basis of alignment and safety, with techniques like red-teaming, where evaluators intentionally try to get the model to produce unsafe or biased responses to expose weaknesses. Fairness and bias evaluations can help practitioners prevent LLMs from reproducing harmful stereotypes or misinformation.

LLMs are also commonly evaluated on the basis of efficiency. Speed, energy consumption, token throughput, memory footprint and ability to handle long context windows are some of the common metrics used to evaluate how efficiently LLMs are able to arrive at outputs.

## A short history of LLMs

The history of LLMs goes back to the early days of computing and natural language processing, when researchers used rule-based systems and statistical methods to model text. These early approaches could capture local word patterns but failed to understand long-range dependencies or deeper semantics.

A major shift came in the 2010s with the rise of neural networks, with word embeddings like Word2Vec and GloVe, which represented words as vectors in continuous space, enabling models to learn semantic relationships. Sequence models such as recurrent neural networks (RNNs) and long short-term memory (LSTM) networks emerged to better handle sequential data.

In 2017, Vaswani et al. introduced the encoder–decoder transformer architecture in the landmark paper “Attention Is All You Need.”[1] Transformers made it possible to train models on large datasets, marking the beginning of the modern LLM era. Google’s BERT (2018), an encoder-only transformer, demonstrated the power of transformers for understanding language, while OpenAI’s generative pretrained transformer (GPT) series, based on a decoder-only variant, showed how generative pretraining on internet-scale text could yield remarkably fluent language generation. Around the same time, encoder–decoder models like Google’s T5 and Facebook’s BART showcased the strengths of the full sequence-to-sequence design for tasks such as translation and summarization. GPT-2 (2019) attracted attention for its ability to generate coherent paragraphs, while GPT-3 (2020), with 175 billion parameters, cemented LLMs as a transformative force in AI.

In addition, new architectures are challenging transformers’ popularity in LLMs. Mamba models work by using a state-space model with selective updates that efficiently filter and combine past information, allowing it to capture long-range dependencies. Diffusion LLMs start with random noise and gradually denoise it step by step, guided by a learned model, until coherent text emerges. Both architectures can be much more efficient than transformers.

Learn how to choose the right approach in preparing datasets and employing foundation models.

## Resources

Discover IBM® Granite™, our family of open, performant and trusted AI models, tailored for business and optimized to scale your AI applications. Explore language, code, time series and guardrail options.

Learn how to select the most suitable AI foundation model for your use case.

Dive into IBM Developer articles, blogs and tutorials to deepen your knowledge of LLMs.

Learn why IBM has been recognized as a Leader in the 2025 Gartner® Magic Quadrant™ for Data Science and Machine Learning Platforms.

Learn how to continually push teams to improve model performance and outpace the competition by using the latest AI techniques and infrastructure.

Explore the value of enterprise-grade foundation models that provide trust, performance and cost-effective benefits to all industries.

Learn how to incorporate generative AI, machine learning and foundation models into your business operations for improved performance.

Read about 2,000 organizations we surveyed about their AI initiatives to discover what's working, what's not and how you can get ahead.

See how InstructLab enables developers to optimize model performance through customization and alignment, tuning toward a specific use case by taking advantage of existing enterprise and synthetic data.

Move your applications from prototype to production with the help of our AI development solutions.

Reinvent critical workflows and operations by adding AI to maximize experiences, real-time decision-making and business value.

Enhance AI model performance with end-to-end model customization with enterprise data in a matter of hours, not months. See how InstructLab enables developers to optimize model performance through customization and alignment, tuning toward a specific use case by taking advantage of existing enterprise and synthetic data.

##### Footnotes

1. “Attention is all you need”, Vaswani et al, arXiv, 12 June 2017
**Published:** 2021-10-06

### Result 6
**Title:** A List of Large Language Models | IBM
**URL:** https://www.ibm.com/think/topics/large-language-models-list?utm_source=valyu.ai&utm_medium=referral
**Source:** web

**Content:**
# A list of large language models

## Authors

Staff Writer

IBM Think

Staff Editor, AI Models

## A list of large language models

The generative AI (gen AI) boom has put a spotlight on the driving force behind it: large language models (LLMs). Dozens of LLMs already exist, but with the technology advancing rapidly, more of these artificial intelligence (AI) models continue to crop up.

Think of it through the lens of the auto industry. Hundreds of car manufacturers across the world have their own models catering to varied consumer needs. Cars have transformed over time too, from gas-powered automobiles to electric vehicles with many smart features.

The same is true for LLMs. These AI systems began as foundation models made up of multiple neural network layers trained on vast dataset volumes. They employ deep learning techniques to accomplish natural language processing (NLP) and natural language understanding (NLU) tasks. However, their capabilities have improved to include agentic AI functions and reasoning.

This fast-paced evolution means that the LLM landscape is constantly changing. AI developers must continuously update their models or even build new ones to keep up with the swift progress.

While NLP and NLU tasks such as content summarization, machine translation, sentiment analysis and text generation continue to be mainstays, AI developers are tailoring their models to certain use cases. For instance, some LLMs are crafted specifically for code generation, while others are made to handle vision language tasks.

While it’s impossible to mention every LLM out there, here’s a list of some of the most current and popular large language models to help organizations narrow their options and consider which model meets their needs:

## Claude

Developer: Anthropic

Release date: February 2025 for Claude 3.7 Sonnet

Number of parameters: Not publicly disclosed

Context window: 200,000 tokens

License: Proprietary

Access: Anthropic API, Amazon Bedrock, Google Cloud Vertex AI

Input: Multimodal (image, text)

Output: Text

Claude is a family of LLMs based on a transformer architecture. It’s the large model behind the conversational AI assistant of the same name. Claude’s design is guided by constitutional AI principles, which focus on AI safety to reduce harmful behaviors such as AI bias.

The Claude family consists of 3 AI models:

● Claude Haiku

● Claude Sonnet

● Claude Opus

### Claude Haiku

Claude 3.5 Haiku is the fastest model. It’s ideal for low-latency use cases, such as customer service chatbots and code completion to speed up software development workflows.

### Claude Sonnet

Claude 3.7 Sonnet is what Anthropic calls its “most intelligent model to date.” This reasoning model has an “extended thinking” mode, allowing it to self-reflect before responding. Those using the Anthropic API can also specify how long the model can think for.

Claude 3.7 Sonnet can be implemented for more specific tasks such as code generation, computer use (allowing the LLM to use a computer the way a human does), extracting information from visual data and question answering.

### Claude Opus

Claude 3 Opus is the most powerful model among the three. It can handle in-depth analysis and longer, more complex tasks with multiple steps.

## Command

Developer: Cohere

Release date: April 2024 for Command R+ and December 2024 for Command R7B

Number of parameters: Up to 104 billion

Context window: 128,000 tokens

Access: Cohere API, Amazon Bedrock, Microsoft Azure AI Studio, Oracle Cloud Infrastructure Generative AI

Input: Text

Command is Cohere’s flagship language model. This family of enterprise-focused LLMs includes these models:

● Command R

● Command R+

● Command R7B

### Command R

Command R is a multilingual text-generation model with 32 billion parameters.1 It has been trained to ground its retrieval augmented generation (RAG) ability by supplying citations in its responses. Command R also offers conversational tool use capabilities.

### Command R+

Command R+ is a more powerful version with 104 billion parameters.2 It can handle complex RAG functions and multistep tool use, allowing AI agents to gather the latest information and update their knowledge base by calling on external tools.

### Command R7B

Command R7B is the smallest and fastest model at 7 billion parameters. It’s ideal for CPU-based deployments, low-end GPUs and other edge devices and can be implemented for on-device inference.

## DeepSeek-R1

Developer: DeepSeek

Release date: January 2025

Number of parameters: 671 billion

License: Open source (MIT License)

Access: DeepSeek API, Hugging Face

DeepSeek-R1 is an open source reasoning model from Chinese AI startup DeepSeek. It uses a Mixture of Experts (MoE) machine learning architecture and was trained using large-scale reinforcement learning to refine its reasoning abilities.

DeepSeek-R1’s performance is similar to or even better than OpenAI’s o1 series of reasoning models on certain LLM benchmarks. DeepSeek-R1 also used knowledge distillation to fine-tune several smaller Llama and Qwen models using the reasoning data generated by the much bigger DeepSeek-R1 LLM. The resulting distilled models enhanced the reasoning capabilities of their original counterparts and even had improved performance over other larger models.3

## Falcon

Developer: Technology Innovation Institute

Release date: December 2024 for Falcon 3

Number of parameters: Up to 180 billion

Context window: Up to 32,000 tokens

License: Open source

Access: Hugging Face

Falcon is a group of open source models developed by researchers at the UAE’s Technology Innovation Institute (TII). These models were trained on TII’s own RefinedWeb, a huge dataset containing filtered English web data.

Falcon consists of these LLMs:

● Falcon 2

● Falcon 3

● Falcon Mamba 7B

Other earlier and larger Falcon versions include Falcon 40B with 40 billion parameters and Falcon 180B with 180 billion parameters.

### Falcon 2

Falcon 2 11B is a causal decoder-only model with 11 billion parameters. It offers multilingual support and will soon feature vision-to-language capabilities.

### Falcon 3

Falcon 3 takes on a decoder-only design and comes in lightweight parameter sizes of 1, 3, 7 and 10 billion. It improves upon its predecessor, advancing its reasoning capabilities.

### Falcon Mamba 7B

Falcon Mamba 7B is a state space language model (SSLM), deviating from the typical LLM transformer architecture. Transformer models use an attention mechanism to “focus their attention” on the most important tokens in the input sequence. However, as the context window grows, transformers require more memory and computing power.

SSLMs continuously update a “state” during processing and employ a selection algorithm to adjust parameters dynamically according to the input. This allows Falcon Mamba 7B to process long sequences of text without needing additional memory and to generate new tokens in the same amount of time regardless of context length.

## Gemini

Developer: Google DeepMind

Release date: December 2024

Context window: 1 million tokens

Access: Gemini API, Google AI Studio, Google Cloud Vertex AI

Input: Multimodal (audio, image, text, video)

Gemini is Google’s suite of multimodal models. It also powers the generative AI chatbot (formerly known as Bard) of the same name. Gemini employs a transformer model, a neural network architecture that originated from Google itself, and builds upon the company’s previous foundational language models, including BERT (Bidirectional Encoder Representations from Transformers) and PaLM 2 (Pathways Language Model).

The latest version, Gemini 2.0, is “built for the agentic era,” according to Google. Gemini 2.0 comes in various variants:

● Gemini 2.0 Flash

● Gemini 2.0 Flash-Lite

● Gemini 2.0 Pro

### Gemini 2.0 Flash

Gemini 2.0 Flash is a lightweight model that supports tool use. Features coming soon include image generation and text-to-speech.

### Gemini 2.0 Flash-Lite

Gemini 2.0 Flash-Lite is an improved version of the previous lightweight and cost-efficient 1.5 Flash. It retains the same speed and cost while enhancing quality.

### Gemini 2.0 Pro

Gemini 2.0 Pro is what Google calls its strongest model for coding and tackling complex prompts due to its tool use capabilities and longer context window at 2 million tokens. It’s still in the experimental phase.

## GPT

Developer: OpenAI

Release date: May 2024 for GPT-4o and July 2024 for GPT-4o mini

Access: OpenAI API using .NET, JavaScript, Python, TypeScript

Output: Multimodal (audio, image, text)

Generative pretrained transformers (GPTs) are a line of large language models developed by OpenAI. GPT includes these LLMs:

● GPT-4o

● GPT-4o mini

### GPT-4o

GPT-4o is a multilingual and multimodal model. As one of the most advanced LLMs, GPT-4o is capable of processing audio, text and visual inputs and producing any blend of audio, image and text outputs. It has improved performance over its GPT-4 Turbo and GPT-4 predecessors. GPT-4o is the current LLM powering OpenAI’s ChatGPT generative AI chatbot.

### GPT-4o mini

GPT-4o mini is a smaller, more affordable model that accepts image and text inputs and generates text outputs. It has surpassed GPT-3.5 Turbo in terms of performance.

## Granite

Developer: IBM®

Release date: February 2025

Number of parameters: Up to 34 billion

License: Open source (Apache 2.0)

Access: IBM® watsonx.ai™, Hugging Face, LM Studio, Ollama, Replicate

IBM® Granite™ is a series of enterprise-ready, open source LLMs. It includes these models:

● Granite 3.2

● Granite Vision

### Granite 3.2

Granite 3.2 incorporates enhanced reasoning capabilities and advanced features for RAG tasks. It comes in 2 and 8 billion parameter sizes.

Granite 3.2’s training data is a mix of open source datasets with permissive license and internally collected high-quality synthetic datasets tailored for solving long-context problems.

### Granite Vision

Granite Vision is a 2-billion-parameter vision language model tailored for visual document understanding. It’s designed for efficient content extraction from charts, diagrams and tables, making it suitable for structured data analysis.

Other LLMs in the Granite series consist of these specialized models:

● Granite Code

● Granite Guardian

● Granite Embedding

### Granite Code

These decoder-only models are designed for code generative tasks, including code editing, code explanation and code generation. Granite Code models were trained with code written in 116 programming languages and are available in sizes of 3, 8, 20 and 34 billion parameters.

### Granite Guardian

Granite Guardian models are LLM-based guardrails designed to detect risks in prompts and responses. Granite Guardian is available in 2, 3, 5 and 8 billion parameter sizes.

### Granite Embedding

Granite Embedding models are sentence-transformer models purpose-built for retrieval-based applications such as semantic search and RAG.

## Grok

Developer: xAI

Release date: February 2025 for Grok 3

Number of parameters: 314 billion

Access: xAI API

Grok is a language model from xAI. The first-generation LLM, Grok-1, is an MoE model with 314 billion parameters. Due to its huge size, only 25% of Grok-1’s model weights are active on a given input token.

In March 2024, xAI released Grok-1.5 with a context window of 128,000 tokens and enhanced problem-solving capabilities. Five months later, xAI launched the beta versions of Grok-2 and its smaller version, Grok-2 mini. Grok-2 has even more improved chat, coding and reasoning abilities and adds support for vision-based tasks.

The latest releases, Grok 3 and Grok 3 mini, are equipped with advanced reasoning and AI agent functions.

## Llama

Developer: Meta

Release date: December 2024 for Llama 3.3

Number of parameters: Up to 405 billion

Access: Meta, Hugging Face, Kaggle

Llama is Meta AI’s collection of LLMs. These autoregressive models implement an optimized transformer architecture, with tuned versions that apply supervised fine-tuning and reinforcement learning with human feedback (RLHF).5

The Llama 3 collection succeeds the Llama 2 LLMs and offers these models:

● Llama 3.1

● Llama 3.2

● Llama 3.3

### Llama 3.1

Llama 3.1 has an 8-billion-parameter model and a 405-billion-parameter flagship foundation model. Both are multilingual text-only models.

### Llama 3.2

Llama 3.2 comes in 1 and 3 billion parameter sizes that are compact enough for mobile and edge devices. The 11 and 90 billion parameter sizes are multimodal LLMs optimized for answering general questions about an image, captioning, image reasoning and visual recognition.6

### Llama 3.3

Llama 3.3 is a 70-billion-parameter multilingual text-only model. It has comparable or even improved performance than Llama 3.1 405B but is more cost-efficient.

## Mistral

Developer: Mistral AI

Release date: July 2024 for Mistral Large 2

Number of parameters: Up to 124 billion

Context window: Up to 256,000 tokens

License: Mistral Research License, Mistral Commercial License, Apache 2.0

Access: La Plateforme, Amazon Bedrock, Microsoft Azure AI Studio, Google Cloud Vertex AI, IBM watsonx.ai

France-based company Mistral AI has a suite of LLMs encompassing these models:

● Mistral Large

● Mistral Small

● Codestral

● Pixtral Large

### Mistral Large

Mistral Large 2 is Mistral AI’s flagship model. It has 123 billion parameters and a context window of 128,000 tokens. It performs well in code generation, math and reasoning. Mistral Large 2 offers multilingual support and function calling capabilities.

### Mistral Small

Mistral Small 3 is a more compact version at 24 billion parameters. This model is suitable for rapid-response conversational AI, low-latency function calling and handling inference locally on resource-constrained machines. Mistral Small 3 is open source and released under the Apache 2.0 license.

### Codestral

Codestral 25.01 is the latest generation of Mistral AI’s coding model. It features a context length of 256,000 tokens and supports tasks such as code completion, code correction, code generation and test generation.

### Pixtral Large

Pixtral Large is a 124-billion-parameter multimodal model. It’s built on top of Mistral Large 2 and extends its capabilities to include image understanding.

## o1

Release date: September 2024 for o1, January 2025 for o3-mini

Context window: Up to 200,000 tokens

Access: OpenAI API

The o1 series of AI models includes o1 and o1-mini. Compared to OpenAI’s GPT models, o1 LLMs are equipped with more advanced reasoning capabilities. Both o1 and o1-mini were trained with large-scale reinforcement learning, allowing them to “think” before responding. They can generate a long chain of thought before answering.

The o1 LLM accepts both image and text inputs, while o1-mini can only handle text inputs.7 Compared to o1, o1-mini is smaller, faster and more cost-effective. It also excels at STEM reasoning and coding.

Meanwhile, o3-mini is the latest reasoning model. Like o1-mini, its strength lies in coding, math and science. It supports function calling and offers 3 reasoning effort options (low, medium and high) to optimize for different scenarios, such as complex problems that need more reasoning effort or simpler problems that require rapid responses and can use less reasoning.

## Qwen

Developer: Alibaba Cloud

Release date: September 2024 for Qwen 2.5 and January 2025 for Qwen2.5-Max

Number of parameters: Up to 72 billion

Context window: Up to 1 million tokens

License: Open source (Apache 2.0), Proprietary for larger models

Access: Alibaba Cloud, Hugging Face

Qwen is a series of LLMs from Chinese cloud computing company Alibaba Cloud. Qwen includes language models and variants optimized for audio, coding, math and vision tasks.

Qwen offers these models:

● Qwen 2.5

● Qwen Audio

● Qwen Coder

● Qwen Math

● Qwen VL

### Qwen 2.5

Qwen2.5 models are decoder-only models for multilingual language processing tasks. They come in 0.5, 3, 7, 14, 32 and 72 billion parameter sizes. Larger models, such as the 72-billion variant, are available only through API access on Alibaba’s proprietary cloud platform.

Qwen2.5-Turbo features a longer context length of 1 million tokens and a quicker inference speed. Meanwhile, Qwen2.5-Max is the latest large-scale MoE model.

### Qwen Audio

Qwen 2 Audio is purpose-built for audio-based tasks. This 7-billion-parameter model can be used to transcribe, detect and classify sounds, handle voice commands and identify musical elements.

### Qwen Coder

Qwen2.5 Coder is a code-specific LLM. It’s available in 1.5, 7, 14, and 32 billion parameter sizes.

### Qwen Math

Qwen 2 Math is a collection of math-optimized LLMs. These models are suitable for advanced mathematical reasoning and solving complex math problems. Qwen 2 Math comes in 1.5, 7 and 72 billion parameter sizes.

### Qwen VL

Qwen 2 VL is a vision-language model that combines visual processing with natural language understanding. Sample use cases entail extracting information from visual data and generating captions and summaries for images and videos. Qwen 2 VL is available in 2, 7 and 72 billion parameter sizes.

## Stable LM

Developer: Stability AI

Release date: April 2024 for Stable LM 2 12B

Number of parameters: Up to 12 billion

Context window: 4,096 tokens

License: Stability AI Community License or Enterprise License

Access: Stability AI, Hugging Face

Stable LM is a group of open-access language models from Stability AI, the makers of text-to-image model Stable Diffusion. Stable LM 2 12B has 12 billion parameters, while Stable LM 2 1.6B has 1.6 billion parameters. These are decoder-only LLMs trained on multilingual data and code datasets. Both models incorporate function calling and tool use.

Stable Code 3B is another LLM fine-tuned on code-related datasets. As a lightweight model with 3 billion parameters, Stable Code 3B can be run in real time on devices, even those without a GPU.

##### Footnotes

All links reside outside ibm.com

1 Model Card for C4AI Command R 08-2024, Hugging Face, Accessed 14 February 2025.

2 Model Card for C4AI Command R+ 08-2024, Hugging Face, Accessed 14 February 2025.

3 DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning, GitHub, 23 January 2025.

4 Access the latest 2.0 experimental models in the Gemini app, Google, 5 February 2025.

5 Model Information, GitHub, 30 September 2024.

6 Model Information, GitHub, 30 September 2024.

7 o1 and o1-mini, OpenAI, Accessed 14 February 2025.

#### Share

Learn how to choose the right approach in preparing datasets and employing foundation models.

## Resources

Discover IBM® Granite™, our family of open, performant and trusted AI models, tailored for business and optimized to scale your AI applications. Explore language, code, time series and guardrail options.

Learn how to select the most suitable AI foundation model for your use case.

Dive into IBM Developer articles, blogs and tutorials to deepen your knowledge of LLMs.

Learn why IBM has been recognized as a Leader in the 2025 Gartner® Magic Quadrant™ for Data Science and Machine Learning Platforms.

Learn how to continually push teams to improve model performance and outpace the competition by using the latest AI techniques and infrastructure.

Explore the value of enterprise-grade foundation models that provide trust, performance and cost-effective benefits to all industries.

Learn how to incorporate generative AI, machine learning and foundation models into your business operations for improved performance.

Read about 2,000 organizations we surveyed about their AI initiatives to discover what's working, what's not and how you can get ahead.

Easily design scalable AI assistants and agents, automate repetitive tasks and simplify complex processes with IBM® watsonx Orchestrate™.

Put AI to work in your business with IBM’s industry-leading AI expertise and portfolio of solutions at your side.

Reinvent critical workflows and operations by adding AI to maximize experiences, real-time decision-making and business value.

Whether you choose to customize pre-built apps and skills or build and deploy custom agentic services using an AI studio, the IBM watsonx platform has you covered.
**Published:** 2025-03-10

### Result 7
**Title:** Top 10 open source LLMs for 2025
**URL:** https://www.instaclustr.com/education/open-source-ai/top-10-open-source-llms-for-2025/?utm_source=valyu.ai&utm_medium=referral
**Source:** web

**Content:**
# Top 10 open source LLMs for 2025

Large Language Models (LLMs) are machine learning models that can understand and generate human language based on large-scale datasets.

## What are open source LLMs?

Large Language Models (LLMs) are machine learning models that can understand and generate human language based on large-scale datasets. Unlike proprietary models developed by companies like OpenAI and Google, open source LLMs are licensed to be freely used, modified, and distributed by anyone. They offer transparency and flexibility, which can be particularly useful for research, development, and customization in various applications.

Researchers and developers can access the underlying code, training mechanisms, and datasets, enabling them to deeply understand and improve these models. This openness fosters a community-driven approach to innovation, which can lead to rapid advancements not possible with closed source models.

This is part of a series of articles about open source AI.

### ROI Calculator How much could you save hosting your LLM?

### How much could you save hosting your LLM?

Use our calculator to get a good estimate of your savings and download a full report.

Calculate savings

## Open source vs closed source LLMs

Open source LLMs are fully accessible for anyone to use, modify, and distribute (although some models require prior approval to use, and some might restrict commercial use of the model). This transparency allows for extensive customization and examination, enabling users to adapt the models to their needs. Open source models offer more freedom, often requiring less financial investment and enabling users to mitigate vendor lock-in risks.

Closed source LLMs are proprietary, with restricted access to the code, training methods, and datasets, limiting user control and customization. Closed source LLMs often provide improved performance and capabilities due to significant resources invested by their creators. However, this comes at a cost—both literally and figuratively. Commercial models are typically priced per token, which can be significant for large-scale usage, and users are dependent on the vendor for updates and support.

Related content: Read our guide to open source databases

## Benefits of using open source LLMs

Open source large language models offer several advantages:

- Enhanced data security and privacy: Users have full control over the data processed by these models, eliminating concerns of third-party access or data mishandling. Organizations can deploy open source LLMs on their private infrastructure, ensuring sensitive information remains in-house and complies with data protection requirements.

- Cost savings and reduced vendor dependency: Since the code and models are freely available, organizations save on pay-per-use and licensing fees and can allocate resources toward customizing and optimizing the models to meet their needs. They can also avoid vendor lock-in scenarios where they are tied to a specific provider for updates, support, and future developments.

- Code transparency: Users have full visibility into the model’s architecture, training data, and algorithms. This transparency fosters trust and enables detailed audits to ensure the model’s integrity and performance. Developers can modify the code to fix bugs or improve features.

- Language model customization: Organizations can tweak the models to better suit their requirements, from adjusting the training processes to incorporating domain-specific knowledge. With closed source models, customization is often limited and might require special permissions and additional costs.

See how to create your first cluster in just 2 minutes.

## Tips from the expert

Chris Carter

Principal Product Manager

With extensive expertise in open source technologies, Chris drives innovation and excellence in the NetApp Instaclustr Managed Platform with a focus on Apache Kafka and Cassandra. With his passion for classical statistics and process improvement, Chris leverages his skills to ensure the integration of business strategy and direction into NetApp solutions.

In my experience, here are tips that can help you better leverage open source large language models (LLMs):

- Optimize for hardware compatibility: While deploying LLMs, ensure you tailor model configurations to leverage the specific capabilities of your hardware, such as GPUs or TPUs, to achieve maximum efficiency.

- Utilize model quantization: Implement quantization techniques to reduce model size and computational requirements without significantly compromising performance, making deployment on edge devices feasible.

- Fine-tune with domain-specific data: Enhance the relevance and accuracy of LLMs by fine-tuning them with data specific to your industry or application domain, improving their contextual understanding and performance.

- Integrate with complementary tools: Combine LLMs with other AI tools such as vector databases for improved search capabilities or knowledge graphs for enhanced reasoning and contextualization.

- Implement differential privacy: Apply differential privacy techniques to ensure that the model does not inadvertently expose sensitive information from the training data, enhancing data security.

## Top open source LLMs in 2024

### 1. LLaMA 3

Meta developed the LLaMA 3 family of large language models, which includes a collection of pretrained and instruction-tuned generative text models available in 8 billion (8B) and 70 billion (70B) parameter sizes. These models are optimized for dialogue use cases, such as in conversational AI applications.

Project information:

- License: Meta Llama 3 community license

- GitHub stars: 23.3K

- Contributors: Joseph Spisak et. al.

- Main corporate sponsor: META

- Official repo link: https://github.com/meta-llama/llama3

Features:

- Model sizes: Available in two sizes: 8 billion (8B) and 70 billion (70B) parameters.

- Context window: Earlier version of Meta LLaMA had a context window of 8K tokens. Version 3.2 upgraded this to 128K tokens.

- Input and output: These models accept text input and are capable of generating both text and code, making them versatile for various applications such as content creation, code generation, and interactive dialogue.

- Architecture: Uses an optimized transformer architecture, which enhances the model’s ability to understand and generate human-like text.

- Tokenizer: Uses a tokenizer with a vocabulary of 128,000 tokens, which helps in efficiently processing and understanding diverse text inputs.

- Training procedure: Trained on sequences of 8,192 tokens, utilizing Grouped-Query Attention (GQA) for improved inference efficiency, allowing the models to handle longer contexts.

### 2. Google Gemma 2

Google DeepMind released Gemma 2, the latest addition to their family of open models designed for researchers and developers. Available in 9 billion (9B) and 27 billion (27B) parameter sizes, Gemma 2 models run at high speeds across different hardware platforms and integrate with popular AI tools.

- License: Apache 2.0

- GitHub stars: 5.2K (PyTorch implementation)

- Main corporate sponsor: Google

- Official repo link: https://huggingface.co/google/gemma-2b

- Model sizes: Available in 9B and 27B parameters, providing options for various computational needs and performance requirements.

- Context window: Gemma 2 has a context window of 8K tokens.

- Performance: According to benchmarks, the 27B model delivers performance similar to models more than twice its size.

- Efficiency: Designed for efficient inference, the 27B model runs on single TPU hosts, NVIDIA A100 80GB Tensor Core GPUs, or NVIDIA H100 Tensor Core GPUs, reducing costs while maintaining high performance.

- Hardware compatibility: Optimized for fast inference across a range of hardware, from gaming laptops to cloud-based setups. Users can access the models in Google AI Studio or use the quantized version with Gemma.cpp on CPUs.

- Integration: Compatible with major AI frameworks like Hugging Face Transformers, JAX, PyTorch, and TensorFlow via Keras 3.0, vLLM, Gemma.cpp, Llama.cpp, and Ollama. It also integrates with NVIDIA TensorRT-LLM and is optimized for NVIDIA NeMo.

Source: Google

### 3. Command R+

Cohere’s Command R+ is built for enterprise use cases and optimized for conversational interactions and long-context tasks. It is recommended for workflows that rely on sophisticated Retrieval Augmented Generation (RAG) functionality and multi-step tool use (agents).

Project information: Command R+ is part of the proprietary Cohere platform. However, Cohere has released an open research version of the model on Hugging Face, which is available for non-commercial use. You can get the open version here.

- Model capabilities: Follows instructions and performs language tasks with high quality and reliability.

- Context window: Supports a context length of 128k tokens and can generate up to 4k output tokens, making it suitable for complex RAG workflows and multi-step tool use.

- Multilingual support: The model is optimized for English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, Simplified Chinese, and Arabic. It also includes pre-training data for 13 additional languages.

- Retrieval augmented generation: Can ground its English-language generations by generating responses based on supplied document snippets and including citations to indicate the source of the information.

- Multi-step tool use: Can connect to external tools like search engines, APIs, functions, and databases. The model can call more than one tool in a sequence of steps, reason dynamically, and adapt based on external information.

### 4. Mistral-8x22b

Mixtral-8x22B is a sparse Mixture-of-Experts (SMoE) model that leverages 39 billion active parameters out of a total 141 billion. It can handle NLP tasks in multiple languages and has strong capabilities in mathematics and coding.

- License: Apache 2.0

- GitHub stars: 9.2K (Mistral AI)

- Main corporate sponsor: Mistral AI

- Official repo link: https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1

- Language proficiency: Fluent in English, French, Italian, German, and Spanish, enabling effective communication and understanding across these major languages.

- Context window: 64K tokens.

- Mathematics and coding: Supports complex problem-solving and software development tasks.

- Function calling: Natively capable of function calling, enhanced by a constrained output mode implemented on la Plateforme, enabling large-scale application development and tech stack modernization.

Source: Mistral

### 5. Falcon 2

Falcon 2 is an AI model providing multilingual and multimodal capabilities, including unique vision-to-language functionality. Available in two versions, Falcon 2 11B and Falcon 2 11B VLM, it is independently verified by the Hugging Face Leaderboard.

- License: Apache 2.0

- Main corporate sponsor: Technology Innovation Institute

- Official repo link: https://github.com/falconpl/Falcon2

- Model versions: Falcon 2 11B is a language model trained on 5.5 trillion tokens with 11 billion parameters. Falcon 2 11B VLM is a vision-to-language model, enabling the conversion of visual inputs into textual outputs.

- Context window: 8K tokens.

- Multilingual: Supports multiple languages, including English, French, Spanish, German, and Portuguese.

- Multimodal capabilities: The VLM version can interpret images and convert them to text, supporting applications across healthcare, finance, eCommerce, education, and legal sectors. It is suitable for document management, digital archiving, and context indexing.

- Efficiency: Operates on a single GPU, supporting scalability and deployment on lighter infrastructure like laptops and other devices.

Source: Falcon

### 6. Grok 1.5

Grok-1.5, developed by Elon Musk’s xAI, builds on the foundation of Grok-1. Grok-1.5V expands traditional text-based LLM capabilities to include visual understanding. This multimodal model can interpret various image types and perform complex reasoning tasks by combining linguistic skills with visual analysis.

- Context window: 128K tokens.

- Multimodal capabilities: Processes and understands a range of visual information, including documents, diagrams, and photographs. It can analyze documents, interpret user interface elements, understand photographs, and handle dynamic visual content such as videos and animations.

- Multi-disciplinary reasoning: Can combine visual and textual information to perform complex reasoning tasks. It can answer questions about scientific diagrams, follow instructions involving text and images, and provide diagnostic insights in medical imaging by analyzing scans and patient records.

- Real-world spatial understanding: Performs strongly on the RealWorldQA benchmark, which measures an AI model’s ability to understand and interact with real-world environments.

Source: X.ai

### 7. Qwen1.5

Qwen1.5, developed by Chinese cloud service provider Alibaba Cloud, is the latest update in the Qwen series, offering base and chat models in a range of sizes: 0.5B, 1.8B, 4B, 7B, 14B, 32B, 72B, and 110B. It also includes a Mixture of Experts (MoE) model. All versions are open-sourced and available in various quantized formats to improve usability.

- License: Tongyi Qianwen research license

- GitHub stars: 6.3K

- Contributors: Qwen team

- Main corporate sponsor: Alibaba China

- Official repo link: https://github.com/QwenLM/Qwen2

- Model versions: Available in sizes from 0.5B to 110B parameters, including a Mixture of Experts (MoE) model. Quantized versions include Int4, Int8, GPTQ, AWQ, and GGUF models.

- Context window: Supports contexts up to 32K tokens, performing well on the L-Eval benchmark, which measures long-context generation capabilities.

- Integration: Qwen1.5’s code is integrated with Hugging Face Transformers (version 4.37.0 and above). The models are also supported by frameworks like vLLM, SGLang, AutoAWQ, AutoGPTQ, Axolotl, and LLaMA-Factory for fine-tuning, and llama.cpp for local inference.

- Platform support: Available on platforms such as Ollama, LMStudio, and API services via DashScope and together.ai.

- Multilingual capabilities: Evaluated across 12 languages, demonstrating strong performance in exams, understanding, translation, and math tasks.

### 8. BLOOM

BLOOM, developed through a large collaboration of AI researchers, aims to democratize access to LLMs, making it possible for academia, nonprofits, and smaller research labs to create, study, and use these models. It is the first model of its size for many languages, including Spanish, French, and Arabic.

- License: BigScience RAIL license

- GitHub stars: 129K

- Contributors: Margaret Mitchell et. al.

- Main corporate sponsor: HuggingFace, BigScience

- Official repo link: Click here

- Multilingual capabilities: Supports 46 natural languages and 13 programming languages.

- Parameter size: Includes 176 billion parameters.

- Accessibility: Available under the Responsible AI License, allowing individuals and institutions to use and build upon the model. It can be easily integrated into applications via the Hugging Face ecosystem using transformers and accelerators.

- Inference API: An inference API is being finalized to enable large-scale use without dedicated hardware.

### 9. GPT-NeoX

GPT-NeoX is a 20 billion parameter autoregressive language model developed by EleutherAI. Trained on the Pile dataset, GPT-NeoX-20B is a dense autoregressive model with publicly available weights. This model, made freely accessible under a permissive license, offers advanced capabilities in language understanding, mathematics, and knowledge-based tasks.

- License: Apache 2.0

- GitHub stars: 6.8K

- Main corporate sponsor: EleutherAI

- Official repo link: https://github.com/EleutherAI/gpt-neox

- Model size: GPT-NeoX-20B has 20 billion parameters, making it one of the largest open-source models available.

- Training setup: It uses Megatron and DeepSpeed libraries for training across multiple GPUs, optimized for distributed computing. It supports parallelism techniques like tensor and pipeline parallelism to enhance efficiency.

- Performance: The model performs particularly well on natural language understanding and few-shot tasks, surpassing similarly sized models like GPT-3 Curie in some benchmarks.

- Dataset: The model was trained exclusively on English data from the Pile, and is not intended for multilingual tasks.

- Usage: While versatile, GPT-NeoX-20B is not fine-tuned for consumer-facing tasks like chatbots and may require supervision when used in such settings.

### 10. Vicuna-13B

Vicuna-13B is an open source chatbot model developed by fine-tuning the LLaMA model with user-shared conversations from ShareGPT. It has achieved over 90% of the quality of OpenAI’s ChatGPT, based on preliminary evaluations using GPT-4 as a judge. The development cost of Vicuna-13B was approximately $300, and both the code and weights are publicly available for non-commercial use.

- License: Non-commercial license

- GitHub stars: 35.8K

- Contributors: Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric P. Xing, Hao Zhang, Joseph E. Gonzalez, Ion Stoica

- Main corporate sponsor: LMSYS

- Official repo link: https://github.com/lm-sys/FastChat

- Performance: Preliminary evaluations using GPT-4 indicate that Vicuna-13B achieves over 90% of the quality of ChatGPT and early versions of Google Gemini. It also outperforms other models like LLaMA and Stanford Alpaca.

- Training: The model was trained using PyTorch FSDP on 8 A100 GPUs in one day, with a focus on multi-turn conversations and long sequence handling. It was trained on approximately 70,000 user-shared conversations from ShareGPT.

- Serving: A lightweight distributed serving system was implemented to serve multiple models with flexible GPU worker integration, using SkyPilot managed spot instances to reduce serving costs.

Related content: Read our guide to managed open source

## NetApp Instaclustr: Empowering open source large language models

Open source large language models have revolutionized natural language processing (NLP) and artificial intelligence (AI) applications by enabling advanced text generation, sentiment analysis, language translation, and more. However, training and deploying these models can be resource-intensive and complex. NetApp Instaclustr steps in to support open source large language models, providing a robust infrastructure and managed services that simplify the process. In this article, we will explore how NetApp Instaclustr empowers organizations to leverage the full potential of open source large language models.

Training large language models requires substantial computational resources and storage capacity. NetApp Instaclustr offers a scalable and high-performance infrastructure that can handle the demanding requirements of model training. By leveraging the distributed computing capabilities and storage capacity provided by NetApp Instaclustr, organizations can efficiently train large language models, reducing the time and resources required for the training process.

Once trained, deploying large language models can present challenges due to their size and resource requirements. NetApp Instaclustr simplifies the deployment process by offering managed services that handle the infrastructure and operational aspects. It takes care of provisioning the necessary compute resources, managing storage, and ensuring high availability and fault tolerance. This allows organizations to focus on utilizing the models for their specific NLP and AI applications without the burden of managing the underlying infrastructure.

NetApp Instaclustr leverages its scalable infrastructure to support the deployment of open source large language models. As the demand for processing power and storage increases, organizations can easily scale their infrastructure up or down to accommodate the workload. This scalability ensures optimal performance, enabling efficient and fast processing of text data using large language models.

Open source large language models often deal with sensitive data, and ensuring data security is crucial. NetApp Instaclustr prioritizes data security by providing robust security measures, including encryption at rest and in transit, role-based access control, and integration with identity providers. These security features help organizations protect their data and comply with industry regulations and privacy standards.

NetApp Instaclustr offers comprehensive monitoring and support services for open source large language models. It provides real-time monitoring capabilities, allowing organizations to track the performance and health of their models. In case of any issues or concerns, NetApp Instaclustr’s support team is readily available to provide assistance and ensure minimal downtime, enabling organizations to maintain the reliability and availability of their language models.

Managing the infrastructure for open source large language models can be costly. NetApp Instaclustr helps organizations optimize costs by offering flexible pricing models. With pay-as-you-go options, organizations can scale their resources based on demand and pay only for what they use. This eliminates the need for upfront investments and provides cost predictability, making it more accessible for organizations of all sizes to leverage open source large language models.

- Use Your Data in LLMs With the Vector Database You Already Have: The New Stack

- How To Improve Your LLM Accuracy and Performance With PGVector and PostgreSQL®: Introduction to Embeddings and the Role of PGVector

- Powering AI Workloads with Intelligent Data Infrastructure and Open Source

- Vector Search in Apache Cassandra® 5.0

## 10 rules for managing Apache Kafka

While Kafka itself is not overly difficult to use, optimizing it for your specific use case comes loaded with challenges. In our updated white paper for 2024, discover the 10 rules you’ll want to know for managing Kafka.
**Published:** 2025-10-29

### Result 8
**Title:** AI am a rheumatologist: a practical primer to large language models for rheumatologists
**URL:** https://pubmed.ncbi.nlm.nih.gov/PMC10547503?utm_source=valyu.ai&utm_medium=referral
**Source:** valyu/valyu-pubmed

**Content:**
## What are Generative Pre-trained Transformers, its chatbot and LLaMA
Large language models (LLMs) are deep learning models trained on huge amounts of text data to generate human-like text based on context and input. Technically, LLMs use advanced NLP techniques, such as tokenization, parsing and named entity recognition (NER) [5]. Tokenization breaks the text into individual words or tokens while parsing analyses the grammatical structure to identify relationships between the tokens. NER locates and classifies named entities, which might also refer to medical conditions and medications. The extracted data can then be structured, aggregated and analysed for actionable insights. GPT are large language models constructed via deep learning methods (namely transformers) first introduced in 2018 by the OpenAI company. The latest version (GPT-4) was recently released in the middle of March 2023. The model has been pre-trained in an enormous amount of unlabelled text data via unsupervised deep-learning techniques and then fine-tuned with reinforced supervised learning from human feedback. Training data consisted of online books, published articles, medical case reports and case series, web pages, social media and online forums up to the end of 2021. GPTs are considered a part of generalized AI, meaning they are not trained for specific tasks. The output is generated in a probabilistic manner in that the model selects the most likely one based on the internal dynamics of the model and input. Interestingly, the models are constantly learning from the inputs and outputs.
ChatGPT is the interactive, conversational interface of the GPT and was released in November 2022 by OpenAI for public use [5]. For now, it is based on GPT-3.5 in the free version and GPT-4 in the paid version. It mainly works with the same principles as GPT: processes inputs, generates multiple possible responses, selects the most likely one, and presents it. Also, ChatGPT remembers what was said earlier in the conversation and replies according to the context of the conversation in a continuous manner. By ChatGPT, we can communicate with machines in a human-like manner and use the power of AI more efficiently.
LLMs of medical interest are not limited to GPT-4. Meta recently released Large Language Model Meta AI (LLaMA), aiming to be more efficient and less resource-intensive compared with other models, increasing its use for a broader base [6]. LLaMA is particularly notable for its availability under a non-commercial licence for researchers and organizations, facilitating its use in various projects. Like GPT, LLaMA is based on a transformer architecture to analyse massive data volumes and generate new content or make predictions based on the data. Another noteworthy difference is their training data. LLaMA is trained on a diverse text corpus, including scientific articles and news articles, while GPT-3.5 is primarily trained on internet text, such as web pages and social media content. As a result, LLaMA may be better suited for generating technical or specialized language, whereas GPT-3.5 may excel in producing informal or conversational language. LLaMA is available in a variety of sizes, ranging from 7 billion to 65 billion parameters (B). The larger models are more powerful, but they also require more computational resources to train and use. LLaMA can run in a local machine and be fine-tuned to improve its performance on specific tasks; this can be done by providing the model with additional data and feedback ([kead291-T1]).

## GPT and ChatGPT in academic life in rheumatology: challenges and possibilities
How can AI aid rheumatologists in their activity? Applications of generative AI will certainly affect almost all sectors. We can just see the tip of the iceberg for now, but we will soon understand its application in the near future. Before diving into the possible applications of GPT and ChatGPT in academic life, we would like to underline the precautions to be always kept in mind.
1.
   All components of the academic community (e.g. authors, editors, publishers, researchers, trainees) should be aware of the basics and the developments in AI.
2.
   Whatever was generated using generative AI, humans should always proofread and supervise the content generated.
3.
   Users of these systems should always keep in mind the limitations and challenges of these systems and use the systems responsibly.
<FG id='kead291-T1'>
**Table 1.**
<T>
| Feature | LlaMA [6] | **GPT-4 [**5**]** |
| --- | --- | --- |
| **Origin** | Developed by Meta | Developed by OpenAI |
| **Model size** | Four versions available according to billion parameters (B): 7B, 13B, 33B, 65B. | >1 trillion parameters (expected) |
| **Computational demands** | Models can be run and fine-tuned on local machines | Dedicated systems based on several high-performance Nvidia A100 Graphics Processing Units |
| **Training data** | Diverse range (e.g. scientific articles, news); it can be easily fine-tuned for accomplishing specific task. | Primarily internet-based text (e.g. web pages) |
| **Language specialization** | More technical or specialized language | More informal or conversational language |
| **Accessibility** | Non-commercial license | Licensing terms and conditions from OpenAI |
Comparison of general features of GPT-4 and LLaMA

</T>
</FG>
**Published:** 2023-06-12

### Result 9
**Title:** ‘Tiny’ AI model beats massive LLMs at logic test
**URL:** https://www.nature.com/articles/d41586-025-03379-9?utm_source=valyu.ai&utm_medium=referral
**Source:** web

**Content:**
Thank you for visiting nature.com. You are using a browser version with limited support for CSS. To obtain the best experience, we recommend you use a more up to date browser (or turn off compatibility mode in Internet Explorer). In the meantime, to ensure continued support, we are displaying the site without styles and JavaScript.

- Twitter

- Facebook

- Email

A tiny recursive model beat large language models in solving logic puzzles, despite being trained on a much smaller data set. Credit: Getty

A small-scale artificial-intelligence model that learns from only a limited pool of data is exciting researchers for its potential to boost reasoning abilities. The model, known as Tiny Recursive Model (TRM), outperformed some of the world’s best large language models (LLMs) at the Abstract and Reasoning Corpus for Artificial General Intelligence (ARC-AGI), a test involving visual logic puzzles that is designed to flummox most machines.

The model — detailed in a preprint on the arXiv server last month1 — is not readily comparable to an LLM. It is highly specialized, excelling only in the type of logic puzzles on which it is trained, such as sudokus and mazes, and it doesn’t ‘understand’ or generate language. But its ability to perform so well on so few resources — it is 10,000 times smaller than frontier LLMs — suggests a possible route for boosting this capability more widely in AI, say researchers.

“It’s fascinating research into other forms of reasoning that one day might get used in LLMs,” says Cong Lu, a machine-learning researcher formerly at the University of British Columbia in Vancouver, Canada. However, he cautions that the techniques might no longer be as effective if applied on a much larger scale. “Often techniques work very well at small model sizes and then just stop working” at a bigger scale, he says.

A test of artificial intelligence

“The results are very significant in my opinion,” says François Chollet, co-founder of AI firm Ndea, who created the ARC-AGI test. Because such models need to be trained from scratch on each new problem, they are “relatively impractical”, but “I expect a lot more research to come out that will build on top of these results”, he adds.

The sole author of the paper — Alexia Jolicoeur-Martineau, an AI researcher at Samsung AI Lab in Montreal, Canada — says that her model shows that the idea that only massive models that cost millions of dollars to train can succeed at hard tasks “is a trap”. She has made the model’s code openly available on GitHub for anyone to download and modify. “Currently, there is too much focus on exploiting LLMs rather than devising and expanding new lines of direction,” she wrote on her blog.

## Tiny model, big results

Most reasoning models are built on top of LLMs, which predict the next word in a sequence by tapping into billions of learnt internal connections, known as parameters. They excel by memorizing patterns from billions of documents, which can trip them up when they come to unpredictable logic puzzles.

The TRM takes a different approach. Jolicoeur-Martineau was inspired by a technique known as the hierarchical reasoning model, developed by the AI firm Sapient Intelligence in Singapore. The hierarchical reasoning model improves its answer through multiple iterations and was published in a preprint in June2.

The TRM uses a similar approach, but with just 7 million parameters, compared with 27 million for the hierarchical model and billions or trillions for LLMs. For each puzzle type the algorithm learns, such as a sudoku, Jolicoeur-Martineau trained a brain-inspired architecture known as a neural network on around 1,000 examples, formatted as a string of numbers.

How AI agents will change research: a scientist’s guide

During training, the model guesses the solution and then compares it with the correct answer, before refining its guess and repeating the process. In this way, it learns strategies to improve its guesses. The model then takes a similar approach to solve unseen puzzles of the same type, successively refining its answer up to 16 times before generating a response.

## Enjoying our latest content? Log in or create an account to continue

- Access the most recent journalism from Nature's award-winning team

- Explore the latest features & opinion covering groundbreaking research

or

doi: https://doi.org/10.1038/d41586-025-03379-9

## References

- Jolicoeur-Martineau, A. Preprint at arXiv https://doi.org/10.48550/arXiv.2510.04871 (2025).

Jolicoeur-Martineau, A. Preprint at arXiv https://doi.org/10.48550/arXiv.2510.04871 (2025).

- Wang, G. et al. Preprint at arXiv https://doi.org/10.48550/arXiv.2506.21734 (2025).

Wang, G. et al. Preprint at arXiv https://doi.org/10.48550/arXiv.2506.21734 (2025).

Download references

Reprints and permissions

- Scientific discovery in the age of artificial intelligence

Scientific discovery in the age of artificial intelligence

- “It keeps me awake at night”: machine-learning pioneer on AI’s threat to humanity

“It keeps me awake at night”: machine-learning pioneer on AI’s threat to humanity

- Could machine learning help to build a unified theory of cognition?

Could machine learning help to build a unified theory of cognition?

- How machine learning could help to improve climate forecasts

How machine learning could help to improve climate forecasts

## Subjects

- Computer science

- Machine learning

## Latest on:

- Computer science

- Machine learning

- If the AI bubble bursts, what will it mean for research? News 19 NOV 25

If the AI bubble bursts, what will it mean for research?

News 19 NOV 25

- Panels of peers are needed to gauge AI’s trustworthiness — experts are not enough Correspondence 18 NOV 25

Panels of peers are needed to gauge AI’s trustworthiness — experts are not enough

Correspondence 18 NOV 25

- ‘It keeps me awake at night’: machine-learning pioneer on AI’s threat to humanity News Q&A 12 NOV 25

‘It keeps me awake at night’: machine-learning pioneer on AI’s threat to humanity

News Q&A 12 NOV 25

- Mind-reading devices can now predict preconscious thoughts: is it time to worry? News Feature 19 NOV 25

Mind-reading devices can now predict preconscious thoughts: is it time to worry?

News Feature 19 NOV 25

- If the AI bubble bursts, what will it mean for research? News 19 NOV 25

- Semantic design of functional de novo genes from a genomic language model Article 19 NOV 25

Semantic design of functional de novo genes from a genomic language model

Article 19 NOV 25

### Jobs

- Senior Principal Investigator, Junior Principal Investigator, and Postdoctoral Positions Cluster hire of PIs and postdocs in Life Sciences and Computational Sciences. Kunming, Yunnan (CN) Kunming Institute of Zoology, Chinese Academy of Sciences‌

#### Senior Principal Investigator, Junior Principal Investigator, and Postdoctoral Positions

Cluster hire of PIs and postdocs in Life Sciences and Computational Sciences.

Kunming, Yunnan (CN)

Kunming Institute of Zoology, Chinese Academy of Sciences‌

- NHP Co-Principal Investigator/Research Professor We are seeking highly motivated Co-Principal Investigators/Research Professors to join i-BRAIN and contribute to cutting-edge neuroscience research. Shenzhen, Guangdong (CN) i-BRAIN, Shenzhen Medical Academy of Research and Translation

#### NHP Co-Principal Investigator/Research Professor

We are seeking highly motivated Co-Principal Investigators/Research Professors to join i-BRAIN and contribute to cutting-edge neuroscience research.

Shenzhen, Guangdong (CN)

i-BRAIN, Shenzhen Medical Academy of Research and Translation

- Faculty Positions in School of Engineering, Westlake University The School of Engineering at Westlake University is seeking to fill multiple tenured or tenure-track faculty positions in all ranks. Hangzhou, Zhejiang (CN) Westlake University

#### Faculty Positions in School of Engineering, Westlake University

The School of Engineering at Westlake University is seeking to fill multiple tenured or tenure-track faculty positions in all ranks.

Hangzhou, Zhejiang (CN)

Westlake University

- Postdoctoral Researcher (m/f/d) The Research Group Infection Resistance (Dr. Katrin Kierdorf) is looking for a Postdoctoral Researcher (m/f/d) Freiburg im Breisgau, Baden-Württemberg (DE) University Hospital Freiburg

#### Postdoctoral Researcher (m/f/d)

The Research Group Infection Resistance (Dr. Katrin Kierdorf) is looking for a Postdoctoral Researcher (m/f/d)

Freiburg im Breisgau, Baden-Württemberg (DE)

University Hospital Freiburg

- Assistant Professor, Associate Professor & Full Professor The Cancer Science Institute of Singapore is seeking outstanding and visionary researchers, ranging from Assistant to Full Professor. Singapore (SG) Cancer Science Institute of Singapore

#### Assistant Professor, Associate Professor & Full Professor

The Cancer Science Institute of Singapore is seeking outstanding and visionary researchers, ranging from Assistant to Full Professor.

Singapore (SG)

Cancer Science Institute of Singapore

## Search

### Quick links

- Explore articles by subject

- Find a job

- Guide to authors

- Editorial policies
**Published:** 2025-11-13

### Result 10
**Title:** Exploring and Comparing the Use of Large Language Models in Supporting | CIA
**URL:** https://www.dovepress.com/exploring-and-comparing-the-use-of-large-language-models-in-supporting-peer-reviewed-fulltext-article-CIA?utm_source=valyu.ai&utm_medium=referral
**Source:** web

**Content:**
- Journals

- Why Publish With Us?

- Editorial Policies

- Author Guidelines

- Peer Review Guidelines

- Open Outlook

- Hot topics

- Podcasts

- Reprints

- Submit New Manuscript

- About

- Contact

- Sustainability

- Press Center

- Testimonials

- Favored Author Program

- Permissions

- Pre-Submission

- Reprints

Back to Journals » Clinical Interventions in Aging » Volume 20

# Exploring and Comparing the Use of Large Language Models in Supporting Osteoporosis Health Consultations

- Fulltext

- Metrics

- Get Permission

- Cite this article

Authors Li X , Li G, Zhao Y, Liang Y, Dong Y, Zhang J

Received 30 July 2025

Accepted for publication 13 November 2025

Published 21 November 2025 Volume 2025:20 Pages 2133—2143

DOI https://doi.org/10.2147/CIA.S551572

Checked for plagiarism Yes

Review by Single anonymous peer review

Peer reviewer comments 3

Editor who approved publication: Prof. Dr. Nandu Goswami

Xin Li,1,* Gen Li,2,* Yue Zhao,3 Yixin Liang,4 Yuefu Dong,1 Jian Zhang1 1Department of Orthopedics, The First People’s Hospital of Lianyungang, Lianyungang, Jiangsu, People’s Republic of China; 2Department of Orthopedics, The Second Affiliated Hospital of Xuzhou Medical University, Xuzhou, Jiangsu, People’s Republic of China; 3Department of Nursing, Lianyungang Maternity and Child Health Hospital, Lianyungang, Jiangsu, People’s Republic of China; 4Department of Osteoporosis, The First People’s Hospital of Lianyungang, Lianyungang, Jiangsu, People’s Republic of China*These authors contributed equally to this workCorrespondence: Yuefu Dong, Department of Orthopedics, The First People’s Hospital of Lianyungang, Lianyungang, Jiangsu, People’s Republic of China, Email [email protected] Jian Zhang, Department of Orthopedics, The First People’s Hospital of Lianyungang, Lianyungang, Jiangsu, People’s Republic of China, Email [email protected]Purpose: To compare the medical accuracy and content comprehensiveness of three large language models (LLMs) in generating responses to frequently asked osteoporosis-related questions and to determine their potential role in clinical support.Methods: Twenty-five questions covering six clinical domains were submitted to each model in isolated sessions. Five senior orthopedic physicians, each with over 25 years of clinical experience, independently rated the medical accuracy of each response using a 5-point Likert scale. Responses rated as “acceptable” or above were further evaluated for content comprehensiveness. Statistical analysis included the Kruskal–Wallis test and Dunn’s post hoc test with Bonferroni correction.Results: A total of 75 unique responses (25 questions × 3 models) were evaluated by five orthopedic experts, yielding 375 ratings. ChatGPT-4o achieved the highest accuracy score (median: 4.6; IQR: 4.4– 4.8), significantly outperforming Gemini-2.5 Pro (p=0.039) and DeepSeek-R1 (p< 0.001). For content comprehensiveness, both ChatGPT-4o and Gemini-2.5 Pro had a median score of 4.4, higher than DeepSeek-R1 (median: 4.2), though differences did not reach statistical significance (p=0.0536). Gemini-2.5 Pro was noted for its fluent and user-friendly language but lacked clinical depth in some responses. DeepSeek-R1, despite offering source citations, demonstrated greater inconsistency.Conclusion: LLMs have clear potential as tools for patient education in osteoporosis. ChatGPT-4o demonstrated the most balanced and clinically reliable performance. Nonetheless, expert medical oversight remains essential to ensure safe and context-appropriate use in healthcare settings.Keywords: large language models, osteoporosis, patient education, AI in healthcare, clinical consultation support

## Introduction

Osteoporosis is a systemic metabolic bone disease characterized by reduced bone mass and deterioration of bone microarchitecture.1 The condition significantly increases the risk of fractures, impairs quality of life, and is associated with higher rates of disability and mortality.2–4 With the global trend of population aging, the prevalence of osteoporosis continues to rise, presenting substantial challenges for its prevention and management.5,6 The global prevalence among adults aged ≥50 years is approximately 19.7%, with higher rates in women (24.3%) than in men (11.9%).7

In clinical practice, patients with osteoporosis exhibit broad and sustained informational needs concerning the disease’s pathophysiology, risk factors, diagnostic procedures, treatment options, medication side effects, and prognosis management.8 However, due to constraints such as limited consultation time, heavy clinician workload, and patients’ varying levels of health literacy, traditional face-to-face communication often falls short in meeting expectations for continuous and personalized health education.9 Therefore, exploring efficient and reliable supplementary tools to enhance the quality and accessibility of patient education has become increasingly important.

In recent years, the rapid advancement of artificial intelligence (AI)—particularly the emergence of large language models (LLMs) such as OpenAI’s ChatGPT series, Google’s Gemini, and domestic models like DeepSeek-R1—has sparked growing interest in their potential applications in medical health education.10–13 These models generate semantically coherent answers to natural language inputs, enabling applications in patient Q&A and health education. However, the accuracy, completeness, and clinical practicality of LLM-generated content remain largely unverified.14

To date, there has been a lack of direct comparative studies evaluating the performance of mainstream LLMs in addressing common questions from osteoporosis patients, particularly in terms of clinical applicability. Given the significant differences in their data sources, training sets, and technical parameters, these models may perform variably in real-world clinical contexts.15,16 Therefore, rigorous clinical simulation studies are necessary to quantitatively assess and compare the medical accuracy and content completeness of their responses, in order determine their potential as valuable tools in patient education.

This study aims to compare the performance of three mainstream LLMs—ChatGPT-4o, Gemini-2.5 Pro, and DeepSeek-R1—in responding to common questions posed by osteoporosis patients. The primary objective is to evaluate their strengths and limitations in terms of medical correctness and content comprehensiveness, and to explore their feasibility and applicability in clinical consultation support and health education.

## Methods

### Study Design

The overall workflow of this study is illustrated in Figure 1. The research was conducted in the Department of Orthopedics at Lianyungang First People’s Hospital, China, from May 3 to May 25, 2025. A group of orthopedic experts and clinical researchers collaboratively designed a set of 25 common questions related to osteoporosis. These questions were initially sourced from multiple authoritative online health information platforms and were subsequently screened and revised by the expert panel to reflect the most frequently asked questions by patients and their primary care providers in clinical practice (see Supplementary Figure 1). Although designed to ensure clinical relevance and content validity, the set of 25 questions was not derived from a previously validated or standardized questionnaire.

|   | Figure 1 Study design and evaluation workflow. Overview of the study procedures, including question selection, model response generation, expert scoring, and statistical analysis steps. |
| --- | --- |

Figure 1 Study design and evaluation workflow. Overview of the study procedures, including question selection, model response generation, expert scoring, and statistical analysis steps.

To further analyze the performance of each LLM across different topical domains, the questions were categorized into six thematic areas based on prior literature: pathogenesis, risk factors, clinical manifestations, diagnosis, treatment and prevention, and prognosis. A designated researcher (XL) generated all model responses between May 20 and May 24, 2025, using three large language models—ChatGPT-4o (OpenAI, https://chat.openai.com), Gemini-2.5 Pro (Google DeepMind, https://gemini.google.com), and DeepSeek-R1 (DeepSeek AI, https://chat.deepseek.com). ChatGPT-4o and Gemini-2.5 Pro were accessed through paid professional subscriptions, whereas DeepSeek-R1 was accessed via its free public interface with real-time web retrieval enabled. Each question was submitted in an independent chat window without prior context, and no post-processing or manual editing of model outputs was performed.

DeepSeek-R1, a free model with real-time web access and source citation capabilities, is characterized by its timeliness and contextual relevance. In contrast, GPT-4o and Gemini-2.5 Pro are subscription-based models with higher parameter counts and computational power, theoretically enabling more complex and in-depth responses. To eliminate contextual interference, each question was submitted in a new chat window, ensuring that the models answered independently without prior conversational context.

This report follows the STROBE (Strengthening the Reporting of Observational Studies in Epidemiology) guidelines, which provide a standardized framework for reporting key elements of observational studies, such as objectives, methods, results, and limitations.

### Accuracy Assessment

The scoring panel consisted of five senior orthopedic physicians, each with over 25 years of clinical experience in diagnosing and treating musculoskeletal disorders, including osteoporosis. To ensure objectivity, model identities were fully concealed during the evaluation, and all metadata or clues that might indicate the source model were removed. Each rater independently assessed the medical accuracy of the LLM-generated answers using a 5-point scale. All model responses were anonymized and randomized prior to expert evaluation to prevent order or source-related bias (Table 1). Each question–answer pair was independently scored by five raters. In cases of disagreement, scores were reviewed collectively, and the final rating was determined by consensus among the experts. The 5-point Likert scale and the cutoff for “acceptable” performance (≥3) were adapted from previous studies evaluating the medical accuracy of large language model outputs in healthcare, where a score of 3 (“acceptable”) or higher indicated clinically adequate content quality.17,18

|   | Table 1 Rating Criteria for Medical Response Evaluation |
| --- | --- |

Table 1 Rating Criteria for Medical Response Evaluation

### Comprehensiveness Evaluation

For responses rated “acceptable” (Likert score≥3), raters also evaluated content comprehensiveness using the following 5-point scale (Table 2). The final comprehensiveness score for each answer was calculated as the mean of the five raters’ individual scores.

|   | Table 2 Scoring Criteria for Comprehensiveness Evaluation |
| --- | --- |

Table 2 Scoring Criteria for Comprehensiveness Evaluation

### Statistical Analysis

All statistical analyses were performed using R software. For each question–model pair, the mean of the five ratings was calculated, and the aggregated accuracy and comprehensiveness metrics (median and interquartile range) were computed across the 75 averaged responses. Shapiro–Wilk tests were applied to assess the normality of continuous variables. As word count data were normally distributed, differences among models were analyzed using one-way ANOVA, followed by Tukey’s post hoc test. Accuracy and comprehensiveness scores did not meet normality assumptions; therefore, the Kruskal–Wallis test was used for overall comparisons, with Dunn’s test and Bonferroni correction applied for post hoc pairwise analyses. To assess inter-rater reliability, intraclass correlation coefficients (ICCs) were computed using a two-way random-effects model. We reported both single-rater and average-rater ICCs, with particular focus on the ICC3k, which showed the degree of consistency across expert ratings. To compare the distribution of categorical ratings across models, Pearson’s chi-square was used as appropriate. A two-tailed p-value of < 0.05 was considered statistically significant. All figures were generated using the ggplot2 and pheatmap packages.

## Results

### Response Length

The average response lengths varied substantially across the LLMs (see Supplementary Tables 1–3). Gemini-2.5 Pro generated the longest responses, with an average word count of 568.9, followed by DeepSeek-R1 (275.5) and GPT-4o (218.7) (Table 3). While longer responses might suggest greater elaboration, length did not consistently correlate with higher scores in either accuracy or comprehensiveness, indicating that verbosity alone is not a reliable proxy for quality.

|   | Table 3 Summary of Performance Metrics Across Three Language Models |
| --- | --- |

Table 3 Summary of Performance Metrics Across Three Language Models

### Inter-Rater Reliability

To assess the consistency of expert ratings across models, we computed intraclass correlation coefficients (ICCs) based on a two-way random-effects model. The ICC for single raters (ICC3) was 0.25 (95% CI: 0.156–0.37), indicating fair agreement. In contrast, the ICC for average ratings across five raters (ICC3k) was 0.63 (95% CI: 0.480–0.75), reflecting good inter-rater reliability. The relatively low single-rater ICC reflects expected variability in subjective expert judgment, whereas the average-rater ICC indicates acceptable overall consistency when aggregated across multiple raters.

### Accuracy of Medical Information

Statistically significant differences in medical accuracy scores were observed among the three language models, as determined by the Kruskal–Wallis test (χ2 = 34.90, df = 2, p < 0.001). GPT-4o achieved the highest accuracy, with a median score of 4.6 and an interquartile range (IQR) of 4.4–4.8, followed by Gemini-2.5 Pro [median: 4.4; IQR: 4.2–4.6] and DeepSeek-R1 [median: 4.2; IQR: 4.0–4.2] (Table 3).

Post hoc pairwise comparisons using Dunn’s test with Bonferroni correction revealed that GPT-4o performed significantly better than both Gemini-2.5 Pro (p = 0.039) and DeepSeek-R1 (p < 0.001). Additionally, Gemini-2.5 Pro showed significantly higher accuracy scores than DeepSeek-R1 (p = 0.002).

These statistical results were corroborated by visual assessment of the boxplot distributions (Figure 2). GPT-4o not only exhibited the highest median and upper quartile values but also demonstrated the narrowest IQR, indicating greater consistency and reduced variability across rated responses. In contrast, DeepSeek-R1 displayed a lower median score with a broader distribution, reflecting greater performance inconsistency and the presence of lower-rated outliers.

|   | Figure 2 Boxplots of accuracy and comprehensiveness scores across large language models. Distribution of expert ratings (median ± IQR) for ChatGPT-4o, Gemini-2.5 Pro, and DeepSeek-R1; overall group differences tested with the Kruskal–Wallis test followed by Dunn’s post hoc comparison. |
| --- | --- |

Figure 2 Boxplots of accuracy and comprehensiveness scores across large language models. Distribution of expert ratings (median ± IQR) for ChatGPT-4o, Gemini-2.5 Pro, and DeepSeek-R1; overall group differences tested with the Kruskal–Wallis test followed by Dunn’s post hoc comparison.

### Comprehensiveness of Content

Differences in content comprehensiveness among the models were modest, with numerical trends favoring GPT-4o but without reaching statistical significance. Both GPT-4o and Gemini-2.5 Pro achieved identical median scores of 4.4, with interquartile ranges (IQR) of 4.2–4.4 and 4.2–4.6, respectively. DeepSeek-R1 had a slightly lower median score of 4.2, with an IQR of 4.0–4.4 (Table 3). Although the Kruskal–Wallis test did not reach conventional significance (χ2 = 5.85, p = 0.0536), the observed numerical trends and visual distributions in Figures 3 and 4 suggest a relative advantage for GPT-4o in comprehensiveness.

|   | Figure 3 Proportion of “Excellent” and “Good” accuracy ratings by model. Stacked bar chart showing the percentage of high-quality responses (Likert ≥ 4) for each model. |
| --- | --- |

Figure 3 Proportion of “Excellent” and “Good” accuracy ratings by model. Stacked bar chart showing the percentage of high-quality responses (Likert ≥ 4) for each model.

|   | Figure 4 Proportion of accuracy and comprehensiveness ratings by model. Comparison of categorical distributions across models; percentages calculated based on five-rater consensus ratings. |
| --- | --- |

Figure 4 Proportion of accuracy and comprehensiveness ratings by model. Comparison of categorical distributions across models; percentages calculated based on five-rater consensus ratings.

Post hoc pairwise comparisons using Dunn’s test with Bonferroni adjustment revealed no statistically significant differences between any model pairs (p > 0.09 for all), indicating that despite small observed differences, overall content comprehensiveness was comparable across models. This may reflect a potential ceiling effect or generally high baseline performance among current-generation LLMs in generating medically complete responses for osteoporosis-related questions.

### Response Consistency Across Questions

Heatmap visualization of Accuracy and Comprehensiveness scores across 25 unique osteoporosis-related questions (Figure 5) showed that GPT-4o maintained consistently high performance, particularly in topics involving clinical diagnosis, fracture risk assessment, and treatment guidelines. Gemini-2.5 Pro demonstrated moderate variability, with lower performance on pharmacologic management questions. DeepSeek-R1 exhibited the greatest inconsistency across questions, with marked fluctuations in both accuracy and completeness, suggesting limited generalizability of its outputs across the medical domain.

|   | Figure 5 Heatmaps of accuracy and comprehensiveness scores across 25 questions. Color intensity represents mean scores for each question–model pair, with darker shades indicating higher accuracy and content depth. |
| --- | --- |

Figure 5 Heatmaps of accuracy and comprehensiveness scores across 25 questions. Color intensity represents mean scores for each question–model pair, with darker shades indicating higher accuracy and content depth.

## Discussion

This study provides a comprehensive comparative analysis of three prominent LLMs—ChatGPT-4o, Gemini-2.5 Pro, and DeepSeek-R1—in addressing common questions frequently asked by patients with osteoporosis. Our findings revealed that all three LLMs exhibited high fluency and coherence in natural language generation. Among them, ChatGPT-4o demonstrated significantly superior performance in both medical accuracy and content comprehensiveness, suggesting it is currently the most promising model for real-world application in patient health education within the context of osteoporosis.

ChatGPT-4o’s answers were consistently rated as “Good” or “Excellent”, with high lexical precision and adequate clinical depth. It covered key domains such as pathophysiology, diagnostic pathways, treatment modalities, and lifestyle interventions. Gemini-2.5 Pro was strong in linguistic fluency and user-oriented expression but occasionally lacked specificity in technical domains. DeepSeek-R1, while offering real-time web-based citations, was prone to factual inconsistencies and terminological inaccuracies, which compromised its reliability in medical communication. Because DeepSeek-R1 retrieves information directly from the internet, its performance may also be affected by real-time data variability, representing a potential confounder when comparing it with models operating on static knowledge bases.

### Interpretation in Light of Other Evidence

The findings of this study align with and expand upon an emerging body of research evaluating the role of LLMs in healthcare communication.19 Previous investigations have consistently shown that advanced models like GPT-4 perform well in general medical question answering and medical licensing exams.20,21 The results of our study reinforce these observations by demonstrating that ChatGPT-4o, an advanced successor to GPT-4, exhibits superior performance in a real-world, domain-specific scenario. Unlike test-based studies, our design simulates patient inquiries that often require both factual precision and an empathetic communication style. The fact that ChatGPT-4o maintained high performance across both clinical depth and patient-oriented readability illustrates its adaptability beyond exam-style content.

Our evaluation of Gemini-2.5 Pro aligns with previous observations regarding Google’s large language models, particularly their emphasis on producing fluent and natural-sounding text.17,22 In our study, Gemini-2.5 Pro consistently generated responses with high linguistic quality, making it well-suited for general health education and user-facing applications. However, we also observed that its performance in tasks requiring precise clinical reasoning and factual consistency was somewhat less robust than that of ChatGPT-4o. This suggests that although Gemini-2.5 Pro delivers user-friendly responses, it may require further optimization to match the clinical precision achieved by GPT-4o.

Interestingly, DeepSeek-R1’s performance diverges from the theoretical advantage expected of models with real-time internet access. Prior research has hypothesized that access to up-to-date information may improve relevance, especially in rapidly evolving fields.23,24 However, our findings suggest that information retrieval does not inherently equate to medical accuracy, particularly when models lack robust content validation pipelines. This aligns with concerns raised in AI safety literature regarding the “hallucination” phenomenon in LLMs, where confidently stated but incorrect information may be generated.18,25,26 In medical contexts, such hallucinations can be especially hazardous, reinforcing the need for controlled content sources and domain-specific fine-tuning.27–29

Recent investigations in musculoskeletal disorders have highlighted the potential of large language models to enhance orthopedic patient communication and clinical decision-making. Studies evaluating these systems in total hip and shoulder arthroplasty demonstrated that they could provide generally accurate and comprehensible responses to common patient inquiries, though challenges remain regarding readability, source verification, and contextual precision.30,31 Similar evaluations in fracture management further indicated that advanced language models can achieve high diagnostic accuracy and recall when analyzing structured clinical information yet still require professional oversight to ensure safety and reliability.32,33 Collectively, these findings illustrate the growing integration of generative AI tools into musculoskeletal health care while underscoring the continued necessity of human supervision and rigorous validation before clinical adoption.34,35

Building upon these prior applications in musculoskeletal contexts, our study addresses a relative gap in the literature: the evaluation of LLMs in chronic disease-specific communication. While prior work has often focused on general medicine or acute care scenarios, few studies have examined performance in conditions like osteoporosis, which require long-term education, risk mitigation, and patient adherence support. The ability of ChatGPT-4o to maintain high ratings across multifaceted domains—pathogenesis, prevention, diagnosis, and prognosis—underscores its potential to serve not only as a question-answering system, but also as a sustainable companion for long-term health management.

### Clinical Implications

The results of this study underscore the considerable promise of LLMs in augmenting both clinical communication and patient education, particularly in the context of chronic, high-prevalence conditions such as osteoporosis. The superior performance of ChatGPT-4o in delivering medically accurate, well-structured, and patient-friendly responses suggests that LLMs can function as effective supplementary tools in routine clinical workflows. In outpatient settings, where consultation time is often limited and patients may struggle to retain verbal explanations, AI-generated summaries and clarifications can serve as valuable reinforcements of key health messages.

A key strength of LLMs is their ability to provide access to easy-to-understand health information, which can help bridge the gap between communication-impaired healthcare providers and patients with varying levels of health literacy.
**Published:** 2025-11-21
