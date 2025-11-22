# Research Results
**Query:** Tell me the latest information on open source models that are running locally.
**Clarification:** Anything that can run locally with eight gigabytes of vram.
**Timestamp:** 2025-11-22T15:14:27.047779
**Summary:** The article from Niftytechfinds.com explores over fifty open-source large language models (LLMs) along with their PC requirements, including specifications for RAM, SSD, and GPU/VRAM. Additionally, it highlights LocalAI as a comprehensive, free alternative to OpenAI and Anthropic, designed to facilitate powerful AI functionalities.

## Detailed Results

### Result 1
**Title:** Top local Opensource LLMs with PC requirements (RAM, SSD, GPU/VRAM)- Niftytechfinds.com - A tech blog dedicated to latest innovations in ai.
**URL:** https://niftytechfinds.com/local-opensource-llm-hardware-guide/?utm_source=valyu.ai&utm_medium=referral
**Source:** web

**Content:**
In this article you will learn about more than fifty open-source solutions for running large language models (LLMs) locally on your PC or server. You will get a full breakdown of categories (runtimes, web UIs, model families, edge/mobile formats), plus hardware guidance (system RAM, SSD storage, GPU/VRAM). If you are setting up a local AI assistant, chatbot, or experimentation platform, this guide will help you choose the right tool and hardware.

## Why run LLMs locally (and key hardware questions)

Running a large language model locally brings benefits: full data privacy, offline access, cost savings compared to cloud API usage, and control over the model and code. But it also raises questions: how much VRAM do I need? Can I use CPU only? What storage requirements exist?We’ll answer those here and then map each open­source option to its hardware guidance.

Key hardware variables:

- System RAM: your computer’s main memory.

- SSD (storage): where model files reside and possibly offload storage.

- GPU / VRAM: for inference on graphics card, the GPU memory matters when using fp16 or fp32, or with quantized int8/int4.

- CPU-only mode: possible for small quantized models but slow for larger ones.

Before diving into the list, here are rough hardware tiers:

- Small models (1B–6B parameters) → maybe 4–8 GB VRAM, ~16 GB system RAM, ~30 GB SSD.

- Mid models (7B–13B) → ~12–24 GB VRAM, 32–64 GB RAM, ~50–100 GB SSD.

- Large models (30B–70B+) → 48–100+ GB VRAM, 128+ GB RAM, maybe 200+ GB SSD.Quantization and optimized runtimes can reduce these by 2–8× in many cases.

Let’s now explore the categories and list the tools.

## Category A: Lightweight CPU / embedded runtimes and libraries

These are best when you do not have a massive GPU or you want to run on laptop / embedded.Open-source options include:

### 1. llama.cpp (ggml) – C/C++ inference for many LLaMA-style models

A minimalist runtime for running large language models in GGML / GGUF format on CPU or with minimal GPU. It enables models to run on lower VRAM or even purely CPU with quantization.Hardware guidance: For a 7B model quantized to int4/int8 you might run on 8–16 GB system RAM plus ~20–30 GB SSD for model file. GPU is optional; VRAM requirement minimal if using CPU mode.

### 2. GGML / GGUF tooling (model format & quantization)

These formats and conversion tools enable optimized storage and inference of models in low-float or integer formats.Hardware: Same as above; quantized files drastically reduce VRAM and RAM requirements.

### 3. GPT4All (Nomic) – packaged local models and easy interface

Designed for local use out of the box; supports CPU or GPU.Hardware: Minimum ~8 GB system RAM; SSD space depends on model (≈10–30 GB). GPU optional for better speed.

### 4. llama.c (Windows or ports) – ultra light ports

Ports for lower-power machines or laptops.Hardware: Suitable for small quantized models on laptops with 8–16 GB RAM. GPU may be integrated iGPU.

### 5. GGML bindings (Python / JavaScript) – runtime bindings

These libraries help run GGML models in languages like Python or JS.Hardware: Follows ggml requirements; very useful for embedding models in applications without heavy hardware.

## Category B: Local servers / web UIs and orchestration

These provide user-friendly interfaces or local servers to make it easier to run models and interact with them.

### 6. text-generation-webui (oobabooga)

A popular web UI frontend supporting many backends (PyTorch, bitsandbytes, ggml).Hardware: For 7B models you may need ~8–14 GB GPU VRAM; for 13B models you’ll get comfort with ~24 GB VRAM. System RAM around 32 GB recommended.

### 7. LocalAI – fast local server with automatic backend detection

Fits use-cases where you want a REST API locally.Hardware: GPU recommended for interactive speed; 12-24 GB VRAM sweet spot for mid sized models.

### 8. Ollama – model management + runner

Simplifies installation and switching models; supports GPU acceleration.Hardware: Discrete GPU preferred; integrated GPU may limit model size or speed.

### 9. LM Studio – desktop GUI for local LLMs

Supports Vulkan offload for laptops/mini-PCs.Hardware: Works even on machines with integrated GPU; for decent performance a discrete 12GB+ GPU is recommended.

### 10. KoboldAI – storytelling UI + multiple backends

Ideal if you want creative applications.Hardware: Varies by backend; for modern models plan for ~12 GB VRAM or more.

### 11. LocalAGI – agentic stack for local models

Focuses on building agents locally rather than just chat.Hardware: Depending on complexity; GPU recommended for mid/large models.

You might also like our blog post on Ai War Between Google, Deepseek and Chatpgt.

## Category C: Low-level acceleration & quantization tools

These tools help you get more out of your hardware by reducing memory, boosting speed, or enabling larger models on smaller systems.

### 12. bitsandbytes – 8-bit optimizers & loaders

Allows you to load models in 8-bit (int8) to reduce GPU memory usage by about half compared to fp16.Hardware: With int8 you can run 13B models on 12-24 GB VRAM cards depending on other factors.

### 13. AutoGPTQ – automatic quantization for faster inference and lower VRAM

Focuses on converting models to int4/int8 with minimal loss of quality.Hardware: After quantization, models that previously needed 24+ GB VRAM might run on 12-16 GB VRAM at reduced performance cost.

### 14. ExLlama – fast CUDA inference kernels for LLaMA derivatives

Optimized for NVIDIA GPUs; improves throughput and efficiency for large models.Hardware: Best with Nvidia cards; helps when using 24-48 GB VRAM for 30B models.

### 15. GGUF/GGML quantizers (TheBloke tools)

Community tools to convert many popular model checkpoints to optimized GGUF format for minimal hardware.Hardware: Makes many large models viable on 12-24 GB VRAM systems when quantized properly.

## Category D: Hugging Face / PyTorch / Transformers ecosystem

The “standard” deep-learning framework approach to local inference or training.

### 16. Hugging Face Transformers

Large ecosystem supporting many models, fine-tuning, inference.Hardware: Running models in fp16 or fp32 often needs higher VRAM than optimized runtimes. For example a 13B model may need 24–30+ GB VRAM.

### 17. Text Generation Inference (TGI) – Hugging Face

Designed for high-performance inference servers for large models.Hardware: Multi-GPU or high-VRAM setups are typical; good for production rather than hobby.

### 18. Accelerate – Hugging Face

Allows multi-GPU, offload, distributed inference.Hardware: If you have two or more GPUs or GPU+CPU offload, you can run 30B+ models locally.

## Category E: Major open-source model families (to run locally)

These are individual model checkpoint families you can download and run locally. I’ll group by size class to make hardware guidance easier.

### Small / portable (1B–6B)

- GPT-J (6B) – easier to run; ~12 GB VRAM in fp16; smaller with quantization.

- Pythia small sizes – 1–6B models suitable for desktops.

- Alpaca / Alpaca-style fine-tuned models (7B) – hardware similar to 7B class below.

### Mid class (7B–13B)

- Mistral-7B – efficient 7B model; ~12–16 GB VRAM in fp16.

- Llama-2 / Llama-3 (7B) – runs well on 12-16 GB VRAM with quantization.

- Vicuna-7B / Vicuna-13B – instruction-tuned; expect ~16–24 GB VRAM for 13B in fp16.

- MPT-7B / MPT-13B – runs comfortably on 16-24 GB VRAM.

- Baichuan-7B – similar profile.

- Mixtral-7B / 13B – high-performance; 13B version likely ~24+ GB VRAM.

- CodeLlama-7B – code-specialized; VRAM similar to text-models of same size.

### Large class (30B–70B+)

- Falcon-40B – requires ~48–100+ GB VRAM in fp16; but quantization and sharding let you run on smaller setups (with trade-offs).

- Llama-2-70B – very heavy; multi-GPU or offload required.

- GPT-NeoX-20B+ – 20B model requires ~40+ GB VRAM.

- RedPajama-30B – similar scale.

- BLOOM-176B – server-class.

- OPT-175B – very large; not practical for most local setups.

- Gemma family large sizes – scale accordingly.

- TheBloke GGUF quantized versions of large models – make them feasible on smaller hardware via quantization.

- RWKV large versions – memory efficient but still large.

- Dolphin (Databricks Dolly large) / Orca large versions – heavy hardware needed.

- Koala large sizes – similar.

- Qwen / Other Chinese large language model families – hardware scale matches size.

## Category F: Edge / Mobile formats and toolchains

These allow inference on laptops, small PCs, or mobile/embedded devices.

- CoreML / Apple Metal runtimes – for Macs with M1/M2. A 7B model may run with 16–32 GB unified memory.

- ONNX Runtime with quantization – convert models to ONNX and run on CPU or other accelerators.

- Apache TVM – compile models for embedded inference.

- (bonus) WebAssembly / browser-based quant models – some very small models run fully in browser.

## Category G: Full-stack servers, containers, and orchestration

For enterprise or heavy local deployment.

- Docker images for Text Generation Inference – containerised production setups.

- KServe / KFServing – Kubernetes-based serving for LLMs.

- Ray + Serve – distributed inference orchestration.

- NVIDIA Triton Inference Server – multi-GPU high-performance serving.

- Multi-node GPU clusters – running large models across nodes.

## Category H: Research and experimental runtimes / novelty

- RWKV.cpp – CPU-friendly implementation of RWKV architecture; runs smaller versions on modest hardware.

- FlashAttention variants / fused kernels – for high throughput but still hardware demanding.

- Community forks of ggml/llama.cpp targeting extreme quantization and small GPUs.

- Experimental browser-based local LLM runtimes (edge WebGPU) – still early but promising.

# How to choose your hardware for local LLMs

You’ll need to decide: what model size will you use, what budget/PC do you have, how fast must inference be? Use this process:

- Decide model size (7B vs 13B vs 30B).

- Check VRAM budget: Do you have 12 GB card, 24 GB, or more?

- Pick runtime: If you use optimized runtime/quantization you may cut VRAM—so a 12 GB GPU may support a 13B model if quantized.

- Check system RAM and SSD: For a 13B model, plan 32–64 GB RAM and 50–100 GB SSD.

- Consider future growth: If you may want to run 30B later, buy a 24 GB or 40+ GB GPU or a dual-GPU rig.

Here are budget tiers:

- Entry hobbyist build: 32 GB system RAM, 1 TB NVMe SSD, GPU ~12 GB VRAM. Good for 7B models or small 13B quantized.

- Power user build: 64 GB RAM, 2 TB SSD, GPU ~24 GB VRAM (e.g., 3090/4080). Can run many 13B models comfortably and some quantised 30B.

- Server/enthusiast build: 128 GB+ RAM, multi-TB NVMe, GPU(s) 40+ GB VRAM each or dual/tri GPU. For 30B–70B class.

# Hardware requirement details by model-size category

Here is an expanded table with more details and explanation for each model size category. Use it as a planning reference.

| Model size | Typical VRAM (fp16) | System RAM | SSD storage | Real-world comments |
| --- | --- | --- | --- | --- |
| 1–6B | ≈ 4–8 GB | 8–16 GB | 10–30 GB | Many laptop GPUs or CPU only. Good for prototypes. |
| 7B | ≈ 6–16 GB | 16–32 GB | 10–50 GB | The “sweet spot” for consumer hardware. 12 GB GPU often works with quantization. |
| 13B | ≈ 12–30 GB | 32–64 GB | 20–80 GB | Requires a higher-end consumer GPU (24 GB) or offload strategy for smaller VRAM. |
| 30B | ≈ 24–48+ GB | 64–128 GB | 40-160 GB | Multi-GPU or GPU+CPU offload required. Quantization helps. |
| 40B | ≈ 48-100+ GB | 128+ GB | 80–250 GB | High end workstation or server required for non-quantized. |
| 70B+ | ≈ 100-250+ GB | 256+ GB | 200+ GB | This is enterprise/cluster territory unless heavily quantized and sharded. |

Note: Quantization (int8, int4) can reduce the VRAM needs significantly—sometimes by half or more. If you use a runtime that supports quantization and efficient memory offload, you can stretch smaller hardware further.

# Best workflow for getting started with local LLMs

- Begin with a 7B model and a friendly UI (e.g., text-generation-webui or LM Studio).

- Use a GPU of at least 12 GB VRAM, 32 GB system RAM, 1 TB SSD to store several models.

- Choose a runtime that supports quantization (bitsandbytes / AutoGPTQ) to lower VRAM usage.

- When you’re comfortable, move to 13B models and test performance.

- If you have access to 24+ GB VRAM or multi-GPU, experiment with 30B+ models.

- Use model families and format conversion tools to ensure compatibility with your hardware.

- Monitor inference latency, memory usage, and model behaviour. Consider offload or model-sharding for large models.

You might also like our post on Best Open Source Projects 2025 for AI, Python, Java, Web & DevOps

# Frequently Asked Questions (FAQ)

Q: Can I run a 70 B-parameter model on a normal desktop GPU?A: Not realistically in fp16/float32 without heavy hardware. You would need 100+ GB VRAM or use advanced quantization and sharding frameworks. Better to start with 7B or 13B models.

Q: Is GPU absolutely required for local LLM inference?A: No, but GPU greatly speeds up inference. You can run very small models on CPU only (especially with llama.cpp/ggml), but latency will be higher.

Q: What is the best model size for a 12 GB VRAM GPU?A: A 7B model is the most practical. With quantization, some 13B models can run but expect trade-offs in speed or accuracy.

Q: Does storage (SSD) matter a lot?A: Yes. Many model files are tens of gigabytes, and you’ll likely want fast NVMe SSD for quick load and offload support. A 1 TB SSD is a good safe starting point.

Q: How do I future-proof my hardware if I might later want 30B models?A: Invest in at least a 24 GB VRAM GPU, 64 GB_SYSTEM_RAM, and NVMe SSD 2 TB+. That gives you room to grow to 30B class models with quantization or offloading.

# Conclusion

This article covered over fifty open-source tools and model families for running large language models locally. We grouped them by runtime type, UI/serving layer, model family, edge formats, orchestration stacks, and experimental options. We provided hardware guidance (RAM, SSD, GPU/VRAM) and a competitor-style analysis of different approaches.If you are ready to experiment with local LLMs, start with a 7B model on modest hardware, pick a user-friendly UI, and consider quantization to make better use of your GPU. Then scale up to 13B or 30B as your budget and hardware allow.

### Madan Chauhan

View all posts by Madan Chauhan

Madan Chauhan is a Learning and Development Professional with over 12 years of experience in designing and delivering impactful training programs across diverse industries. His expertise spans leadership development, communication skills, process training, and performance enhancement. Beyond corporate learning, Madan is passionate about web development and testing emerging AI tools. He explores how technology and artificial intelligence can improve productivity, creativity, and learning outcomes — and regularly shares his insights through articles, blogs, and digital platforms to help others stay ahead in the tech-driven world. Connect with him on LinkedIn: www.linkedin.com/in/madansa7
**Published:** 2025-11-16

### Result 2
**Title:** LocalAI
**URL:** https://localai.io/?utm_source=valyu.ai&utm_medium=referral
**Source:** web

**Content:**
# LocalAI

The free, OpenAI, Anthropic alternative. Your All-in-One Complete AI Stack - Run powerful language models, autonomous agents, and document intelligence locally on your hardware.

No cloud, no limits, no compromise.

⭐ Star us on GitHub - 33.3k+ stars and growing!

Drop-in replacement for OpenAI API - modular suite of tools that work seamlessly together or independently.

Start with LocalAI’s OpenAI-compatible API, extend with LocalAGI’s autonomous agents, and enhance with LocalRecall’s semantic search - all running locally on your hardware.

Open Source MIT Licensed.

## Why Choose LocalAI?

OpenAI API Compatible - Run AI models locally with our modular ecosystem. From language models to autonomous agents and semantic search, build your complete AI stack without the cloud.

### Key Features

- LLM Inferencing: LocalAI is a free, Open Source OpenAI alternative. Run LLMs, generate images, audio and more locally with consumer grade hardware.

- Agentic-first: Extend LocalAI with LocalAGI, an autonomous AI agent platform that runs locally, no coding required. Build and deploy autonomous agents with ease.

- Memory and Knowledge base: Extend LocalAI with LocalRecall, A local rest api for semantic search and memory management. Perfect for AI applications.

- OpenAI Compatible: Drop-in replacement for OpenAI API. Compatible with existing applications and libraries.

- No GPU Required: Run on consumer grade hardware. No need for expensive GPUs or cloud services.

- Multiple Models: Support for various model families including LLMs, image generation, and audio models. Supports multiple backends for inferencing.

- Privacy Focused: Keep your data local. No data leaves your machine, ensuring complete privacy.

- Easy Setup: Simple installation and configuration. Get started in minutes with Binaries installation, Docker, Podman, Kubernetes or local installation.

- Community Driven: Active community support and regular updates. Contribute and help shape the future of LocalAI.

## Quick Start

Docker is the recommended installation method for most users:

```bash
docker run -p 8080:8080 --name local-ai -ti localai/localai:latest
```

For complete installation instructions, see the Installation guide.

## Get Started

- Install LocalAI - Choose your installation method (Docker recommended)

- Quickstart Guide - Get started quickly after installation

- Install and Run Models - Learn how to work with AI models

- Try It Out - Explore examples and use cases

## Learn More

- Explore available models

- Model compatibility

- Try out examples

- Join the community

- Check the LocalAI Github repository

- Check the LocalAGI Github repository
**Published:** 2025-11-19

### Result 3
**Title:** How To Run an Open-Source LLM on Your Personal Computer – Run Ollama Locally
**URL:** https://www.freecodecamp.org/news/how-to-run-an-open-source-llm-on-your-personal-computer-run-ollama-locally/?utm_source=valyu.ai&utm_medium=referral
**Source:** web

**Content:**
Running a large language model (LLM) on your computer is now easier than ever. You no longer need a cloud subscription or a massive server. With just your PC, you can run models like Llama, Mistral, or Phi, privately and offline.

This guide will show you how to set up an open-source LLM locally, explain the tools involved, and walk you through both the UI and command-line installation methods.

## What We’ll Cover

- Understanding Open Source LLMs

Understanding Open Source LLMs

- Choosing a Platform to Run LLMs Locally

Choosing a Platform to Run LLMs Locally

- How to Install Ollama

How to Install Ollama

- How to Install and Run LLMs via the Command Line

How to Install and Run LLMs via the Command Line

- How to Manage Models and Resources

How to Manage Models and Resources

- How to Use Ollama with Other Applications

How to Use Ollama with Other Applications

- Troubleshooting and Common Issues

Troubleshooting and Common Issues

- Why Running LLMs Locally Matters

Why Running LLMs Locally Matters

- Conclusion

Conclusion

An open-source large language model is a type of AI that can understand and generate text, much like ChatGPT, but it can function without depending on external servers.

You can download the model files, run them on your machine, and even fine-tune them for your use cases.

Projects like Llama 3, Mistral, Gemma, and Phi have made it possible to run models that fit well on consumer hardware. You can choose between smaller models that run on CPUs or larger ones that benefit from GPUs.

Running these models locally gives you privacy, control, and flexibility. It also helps developers integrate AI features into their applications without relying on cloud APIs.

To run an open source model, you need a platform that can load it, manage its parameters, and provide an interface to interact with it.

Three popular choices for local setup are:

- Ollama — a user-friendly system that runs models like OpenAI GPT OSS, Google Gemma with one command. It has both a Windows UI and CLI version.

Ollama — a user-friendly system that runs models like OpenAI GPT OSS, Google Gemma with one command. It has both a Windows UI and CLI version.

- LM Studio — a graphical desktop application for those who prefer a point-and-click interface.

LM Studio — a graphical desktop application for those who prefer a point-and-click interface.

- Gpt4All — another popular GUI desktop application.

Gpt4All — another popular GUI desktop application.

We’ll use Ollama as the example in this guide since it’s widely supported and integrates easily with other tools.

Ollama provides a one-click installer that sets up everything you need to run local models. Visit the official Ollama website and download the Windows installer.

Once downloaded, double-click the file to start installation. The setup wizard will guide you through the process, which only takes a few minutes.

When the installation finishes, Ollama will run in the background as a local service. You can access it either through its graphical desktop interface or using the command line.

After installing Ollama, you can open the application from the Start Menu. The UI makes it easy for beginners to start interacting with local models.

On the Ollama interface, you’ll see a simple text box where you can type prompts and receive responses. There’s also a panel that lists available models.

To download and use a model, just select it from the list. Ollama will automatically fetch the model weights and load them into memory.

The first time you ask a question, it will download the model if it does not exist. You can also choose the model from the models search page.

I’ll use the gemma 270m model which is the smallest model available in Ollama.

You can see the model being downloaded when used for the first time. Depending on the model size and your system’s performance, this might take a few minutes.

Once loaded, you can start chatting or running tasks directly within the UI. It’s designed to look and feel like a normal chat window, but everything runs locally on your PC.

You don’t need an internet connection after the model has been downloaded.

If you prefer more control, you can use the Ollama command-line interface (CLI). This is useful for developers or those who want to integrate local models into scripts and workflows.

To open the command line, search for “Command Prompt” or “PowerShell” in Windows and run it. You can now interact with Ollama using simple commands.

To check if the installation worked, type:

```python
ollama --version
```

If you see a version number, Ollama is ready. Next, to run your first model, use the pull command:

```python
ollama pull gemma3:270m
```

This will download the Gemma model to your machine.

When the process finishes, start it with:

```python
ollama run gemma3:270m
```

Ollama will launch the model and open an interactive prompt where you can type messages.

Everything happens locally, and your data never leaves your computer.

You can stop the model anytime by typing /bye.

Each model you download takes up disk space and memory. Smaller models like Phi-3 Mini or Gemma 2B are lighter and suitable for most consumer laptops. Larger ones such as Mistral 7B or Llama 3 8B require more powerful GPUs or high-end CPUs.

You can list all installed models using:

```python
ollama list
```

And remove one when you no longer need it:

```python
ollama rm model_name
```

If your PC has limited RAM, try running smaller models first. You can experiment with different ones to find the right balance between speed and accuracy.

Once you’ve installed Ollama, you can use it beyond the chat interface. Developers can connect to it using APIs and local ports.

Ollama runs a local server on http://localhost:11434. This means you can send requests from your own scripts or applications.

For example, a simple Python script can call the local model like this:

```python
import requests, json

"http://localhost:11434/api/generate"

"model": "gemma3:270m",
    "prompt": "Write a short story about space exploration."
}

True)

for line in response.iter_lines():
    if line:
        data = json.loads(line.decode("utf-8"))
        if "response" in data:
            print(data["response"], end="", flush=True)This setup turns your computer into a local AI engine. You can integrate it with chatbots, coding assistants, or automation tools without using external APIs.
```

If you face issues running a model, check your system resources first. Models need enough RAM and disk space to load properly. Closing other apps can help free up memory.

Sometimes, antivirus software may block local network ports. If Ollama fails to start, add it to the list of allowed programs.

If you use the CLI and see errors about GPU drivers, ensure that your graphics drivers are up to date. Ollama supports both CPU and GPU execution, but having updated drivers improves performance.

Running LLMs locally changes how you work with AI. You’re no longer tied to API costs or rate limits. It’s ideal for developers who want to prototype fast, researchers exploring fine-tuning, or hobbyists who value privacy.

Local models are also great for offline environments. You can experiment with prompt design, generate content, or test AI-assisted apps without an internet connection.

As hardware improves and open source communities grow, local AI will continue to become more powerful and accessible.

Setting up and running an open-source LLM on Windows is now simple. With tools like Ollama and LM Studio, you can download a model, run it locally, and start generating text in minutes.

The UI makes it friendly for beginners, while the command line offers full control for developers. Whether you’re building an app, testing ideas, or exploring AI for personal use, running models locally puts everything in your hands, making it fast, private, and flexible.

Hope you enjoyed this article. Signup for my free newsletter TuringTalks.ai for more hands-on tutorials on AI. You can also visit my website.

If you read this far, thank the author to show them you care. Say Thanks

Learn to code for free. freeCodeCamp's open source curriculum has helped more than 40,000 people get jobs as developers. Get started
**Published:** 2025-11-10

### Result 4
**Title:** 7 Best LLM Tools To Run Models Locally (November 2025) – Unite.AI
**URL:** https://www.unite.ai/best-llm-tools-to-run-models-locally/?utm_source=valyu.ai&utm_medium=referral
**Source:** web

**Content:**
- Best Of 10 Best AI Tools for Business (November 2025) Artificial intelligence (AI) technologies have opened up countless new opportunities for every size business... Full Answer Alex McFarland

#### 10 Best AI Tools for Business (November 2025)

- Best Of 10 Best Machine Learning Software (November 2025) Machine learning (ML) has become a critical driver of business success in today's world. This technology... Full Answer Alex McFarland

#### 10 Best Machine Learning Software (November 2025)

- Best Of 10 Best AI Assistants (November 2025) Artificial intelligence (AI) assistants are becoming indispensable in today’s society. You see them... Full Answer Alex McFarland

#### 10 Best AI Assistants (November 2025)

- Best Of 5 Best Large Language Models (LLMs) in November 2025 The top 5 large language models (LLMs) have separated themselves from the pack with capabilities that... Full Answer Alex McFarland

#### 5 Best Large Language Models (LLMs) in November 2025

- Best Of 10 Best Machine Learning Algorithms Though we're living through a time of extraordinary innovation in GPU-accelerated machine learning, the... Full Answer Martin Anderson

#### 10 Best Machine Learning Algorithms

- Best Of 5 Best Open Source LLMs (November 2025) Open source AI has caught up to closed-source systems. These five large language models (LLMs) deliver... Full Answer Alex McFarland

#### 5 Best Open Source LLMs (November 2025)

Unite.AI is committed to rigorous editorial standards. We may receive compensation when you click on links to products we review. Please view our affiliate disclosure.

Improved large language models (LLMs) emerge frequently, and while cloud-based solutions offer convenience, running LLMs locally provides several advantages, including enhanced privacy, offline accessibility, and greater control over data and model customization.

Running LLMs locally offers several compelling benefits:

- Privacy: Maintain complete control over your data, ensuring that sensitive information remains within your local environment and does not get transmitted to external servers.

- Offline Accessibility: Use LLMs even without an internet connection, making them ideal for situations where connectivity is limited or unreliable.

- Customization: Fine-tune models to align with specific tasks and preferences, optimizing performance for your unique use cases.

- Cost-Effectiveness: Avoid recurring subscription fees associated with cloud-based solutions, potentially saving costs in the long run.

This breakdown will look into some of the tools that enable running LLMs locally, examining their features, strengths, and weaknesses to help you make informed decisions based on your specific needs.

## 1. AnythingLLM

AnythingLLM is an open-source AI application that puts local LLM power right on your desktop. This free platform gives users a straightforward way to chat with documents, run AI agents, and handle various AI tasks while keeping all data secure on their own machines.

The system’s strength comes from its flexible architecture. Three components work together: a React-based interface for smooth interaction, a NodeJS Express server managing the heavy lifting of vector databases and LLM communication, and a dedicated server for document processing. Users can pick their preferred AI models, whether they are running open-source options locally or connecting to services from OpenAI, Azure, AWS, or other providers. The platform works with numerous document types – from PDFs and Word files to entire codebases – making it adaptable for diverse needs.

What makes AnythingLLM particularly compelling is its focus on user control and privacy. Unlike cloud-based alternatives that send data to external servers, AnythingLLM processes everything locally by default. For teams needing more robust solutions, the Docker version supports multiple users with custom permissions, while still maintaining tight security. Organizations using AnythingLLM can skip the API costs often tied to cloud services by using free, open-source models instead.

#### Key features of Anything LLM:

- Local processing system that keeps all data on your machine

- Multi-model support framework connecting to various AI providers

- Document analysis engine handling PDFs, Word files, and code

- Built-in AI agents for task automation and web interaction

- Developer API enabling custom integrations and extensions

Visit AnythingLLM →

## 2. GPT4All

GPT4All also runs large language models directly on your device. The platform puts AI processing on your own hardware, with no data leaving your system. The free version gives users access to over 1,000 open-source models including LLaMa and Mistral.

The system works on standard consumer hardware – Mac M Series, AMD, and NVIDIA. It needs no internet connection to function, making it ideal for offline use. Through the LocalDocs feature, users can analyze personal files and build knowledge bases entirely on their machine. The platform supports both CPU and GPU processing, adapting to available hardware resources.

The enterprise version costs $25 per device monthly and adds features for business deployment. Organizations get workflow automation through custom agents, IT infrastructure integration, and direct support from Nomic AI, the company behind it. The focus on local processing means company data stays within organizational boundaries, meeting security requirements while maintaining AI capabilities.

#### Key features of GPT4All:

- Runs entirely on local hardware with no cloud connection needed

- Access to 1,000+ open-source language models

- Built-in document analysis through LocalDocs

- Complete offline operation

- Enterprise deployment tools and support

Visit GPT4All →

## 3. Ollama

Ollama downloads, manages, and runs LLMs directly on your computer. This open-source tool creates an isolated environment containing all model components – weights, configurations, and dependencies – letting you run AI without cloud services.

The system works through both command line and graphical interfaces, supporting macOS, Linux, and Windows. Users pull models from Ollama’s library, including Llama 3.2 for text tasks, Mistral for code generation, Code Llama for programming, LLaVA for image processing, and Phi-3 for scientific work. Each model runs in its own environment, making it easy to switch between different AI tools for specific tasks.

Organizations using Ollama have cut cloud costs while improving data control. The tool powers local chatbots, research projects, and AI applications that handle sensitive data. Developers integrate it with existing CMS and CRM systems, adding AI capabilities while keeping data on-site. By removing cloud dependencies, teams work offline and meet privacy requirements like GDPR without compromising AI functionality.

#### Key features of Ollama:

- Complete model management system for downloading and version control

- Command line and visual interfaces for different work styles

- Support for multiple platforms and operating systems

- Isolated environments for each AI model

- Direct integration with business systems

Visit Ollama →

## 4. LM Studio

LM Studio is a desktop application that lets you run AI language models directly on your computer. Through its interface, users find, download, and run models from Hugging Face while keeping all data and processing local.

The system acts as a complete AI workspace. Its built-in server mimics OpenAI’s API, letting you plug local AI into any tool that works with OpenAI. The platform supports major model types like Llama 3.2, Mistral, Phi, Gemma, DeepSeek, and Qwen 2.5. Users drag and drop documents to chat with them through RAG (Retrieval Augmented Generation), with all document processing staying on their machine. The interface lets you fine-tune how models run, including GPU usage and system prompts.

Running AI locally does require solid hardware. Your computer needs enough CPU power, RAM, and storage to handle these models. Users report some performance slowdowns when running multiple models at once. But for teams prioritizing data privacy, LM Studio removes cloud dependencies entirely. The system collects no user data and keeps all interactions offline. While free for personal use, businesses need to contact LM Studio directly for commercial licensing.

#### Key features of LM Studio:

- Built-in model discovery and download from Hugging Face

- OpenAI-compatible API server for local AI integration

- Document chat capability with RAG processing

- Complete offline operation with no data collection

- Fine-grained model configuration options

Visit LM Studio →

## 5. Jan

Jan gives you a free, open-source alternative to ChatGPT that runs completely offline. This desktop platform lets you download popular AI models like Llama 3, Gemma, and Mistral to run on your own computer, or connect to cloud services like OpenAI and Anthropic when needed.

The system centers on putting users in control. Its local Cortex server matches OpenAI’s API, making it work with tools like Continue.dev and Open Interpreter. Users store all their data in a local “Jan Data Folder,” with no information leaving their device unless they choose to use cloud services. The platform works like VSCode or Obsidian – you can extend it with custom additions to match your needs. It runs on Mac, Windows, and Linux, supporting NVIDIA (CUDA), AMD (Vulkan), and Intel Arc GPUs.

Jan builds everything around user ownership. The code stays open-source under AGPLv3, letting anyone inspect or modify it. While the platform can share anonymous usage data, this stays strictly optional. Users pick which models to run and keep full control over their data and interactions. For teams wanting direct support, Jan maintains an active Discord community and GitHub repository where users help shape the platform’s development.

#### Key features of Jan:

- Complete offline operation with local model running

- OpenAI-compatible API through Cortex server

- Support for both local and cloud AI models

- Extension system for custom features

- Multi-GPU support across major manufacturers

Visit Jan →

## 6. Llamafile

Llamafile turns AI models into single executable files. This Mozilla Builders project combines llama.cpp with Cosmopolitan Libc to create standalone programs that run AI without installation or setup.

The system aligns model weights as uncompressed ZIP archives for direct GPU access. It detects your CPU features at runtime for optimal performance, working across Intel and AMD processors. The code compiles GPU-specific parts on demand using your system’s compilers. This design runs on macOS, Windows, Linux, and BSD, supporting AMD64 and ARM64 processors.

For security, Llamafile uses pledge() and SECCOMP to restrict system access. It matches OpenAI’s API format, making it drop-in compatible with existing code. Users can embed weights directly in the executable or load them separately, useful for platforms with file size limits like Windows.

#### Key features of Llamafile:

- Single-file deployment with no external dependencies

- Built-in OpenAI API compatibility layer

- Direct GPU acceleration for Apple, NVIDIA, and AMD

- Cross-platform support for major operating systems

- Runtime optimization for different CPU architectures

Visit Llamafile →

## 7. NextChat

NextChat puts ChatGPT’s features into an open-source package you control. This web and desktop app connects to multiple AI services – OpenAI, Google AI, and Claude – while storing all data locally in your browser.

The system adds key features missing from standard ChatGPT. Users create “Masks” (similar to GPTs) to build custom AI tools with specific contexts and settings. The platform compresses chat history automatically for longer conversations, supports markdown formatting, and streams responses in real-time. It works in multiple languages including English, Chinese, Japanese, French, Spanish, and Italian.

Instead of paying for ChatGPT Pro, users connect their own API keys from OpenAI, Google, or Azure. Deploy it free on a cloud platform like Vercel for a private instance, or run it locally on Linux, Windows, or MacOS. Users can also tap into its preset prompt library and custom model support to build specialized tools.

#### Key features NextChat:

- Local data storage with no external tracking

- Custom AI tool creation through Masks

- Support for multiple AI providers and APIs

- One-click deployment on Vercel

- Built-in prompt library and templates

Visit NextChat →

## The Bottom Line

Each of these tools takes a unique shot at bringing AI to your local machine – and that is what makes this space exciting. AnythingLLM focuses on document handling and team features, GPT4All pushes for wide hardware support, Ollama keeps things dead simple, LM Studio adds serious customization, Jan AI goes all-in on privacy, Llama.cpp optimizes for raw performance, Llamafile solves distribution headaches, and NextChat rebuilds ChatGPT from the ground up. What they all share is a core mission: putting powerful AI tools directly in your hands, no cloud required. As hardware keeps improving and these projects evolve, local AI is quickly becoming not just possible, but practical. Pick the tool that matches your needs – whether that is privacy, performance, or pure simplicity – and start experimenting.

Top 10 AI Practice Management Solutions for Healthcare Providers (November 2025)

10 Best AI Humanizer Tools (November 2025)

Alex McFarland is an AI journalist and writer exploring the latest developments in artificial intelligence. He has collaborated with numerous AI startups and publications worldwide.

#### You may like

- 10 Best AI Tools for Business (November 2025)

10 Best AI Tools for Business (November 2025)

- 10 Best Machine Learning Software (November 2025)

10 Best Machine Learning Software (November 2025)

- 10 Best AI Assistants (November 2025)

10 Best AI Assistants (November 2025)

- 5 Best Large Language Models (LLMs) in November 2025

5 Best Large Language Models (LLMs) in November 2025

- 10 Best Machine Learning Algorithms

10 Best Machine Learning Algorithms

- 5 Best Open Source LLMs (November 2025)

5 Best Open Source LLMs (November 2025)
**Published:** 2025-11-19

### Result 5
**Title:** Best Local LLMs For Coding
**URL:** https://www.mslinn.com/llm/7900-coding-llms.html?utm_source=valyu.ai&utm_medium=referral
**Source:** web

**Content:**
Published 2025-11-03. Last modified 2025-11-12. Time to read: 16 minutes.

Did you know that all the computers on your LAN can pool their VRAM so your LLM models run across your entire LAN? That means a modest laptop, attached via a solid Wi-Fi connection could employ some impressive local horsepower for AI tasks. If this type of topic interests you, please read the entire series.

The following articles were written sequentially.

- Renting vs. Purchasing GPUs for LLMs Throughout Canada

- Best Local LLMs For Coding

- Running an LLM on the Windows Ollama app

- Early Draft: Multi-LLM Agent Pipelines

This article discusses the best open-source LLMs for coding that run with acceptable performance on my workstation. “Good performance” typically means at least 20 to 40 tokens per second with minimal quality loss. If I were renting GPUs, the list of contenders would focus on larger versions of the same models.

Topics discussed in this article include:

- The workstation used for testing

- A summary of results

- Graphs that compare the performance of leading open-source and commercial LLMs

- Details on each model tested, listed in order of preference

- Conclusions and recommendations

I had several long discussions with LLMs, principally Grok. I only installed and played with the most interesting candidates, as shown in the article. Information that seemed reasonable from Grok was provisionally accepted without verification. I have been burrowing my way through it, correcting and expounding as I felt relevant. I have not found any quantitative errors from Grok, just bad URLs, imaginary references, a fixation on deterministic initialization sequences, and a total lack of understanding of human needs. This was not an exhaustive survey, but it probably represents a fair assessment.

All the dialogs did actually happen as shown because that is a transcript of what I did, and the results that I achieved. At least you can trust the code presented and the TUI dialog.

## Bear and Gojira

The workstation I use the most for developing software is called Bear and has the following components that affect the performance of LLMs that run on it:

- Intel Core i7-13700K (16 cores: 8 performance + 8 efficiency, up to 5.4 GHz).

- NVIDIA RTX 3060 with 12 GB GDDR6 VRAM

- 64 GB DDR5

- Z790 chipset motherboard

Gojira, an Ubuntu server in the room next to my desk, is built with similar hardware as Bear, except it has an older GPU. The GPU is an RTX 1660 with 6 GB VRAM. Older GPUs can run most smaller LLMs just fine.

## Context Length

An optimized context refers to using specific techniques and software frameworks to manage a context in an efficient manner, minimizing the computational overhead and memory usage that typically scale poorly with long contexts.

In standard Transformer architectures, the computational cost (both memory and speed) of processing the self-attention mechanism grows quadratically with the context length. A 16K context is substantial, and if handled naively, it would consume a massive amount of VRAM and slow down inference significantly. Optimization Techniques

- PagedAttention is an efficient memory management algorithm used in serving frameworks like vLLM. It pages (sqps) the KV Cache, storing it in "pages" rather than contiguous memory blocks. This prevents memory fragmentation and maximizes the GPU's memory utilization, allowing for much larger effective batch sizes and greater throughput, especially with long contexts.

- Flash Attention is an optimized implementation of the attention mechanism that uses tiling and recomputation memory management techniques on the GPU to avoid reading/writing the large intermediate attention matrices to and from the relatively slow GPU High-Bandwidth Memory (HBM). This dramatically speeds up prompt processing for long contexts.

- Context Compression/Summarization distills the most important information from older parts of the conversation into a shorter summary that is then injected into the prompt. This keeps the effective context length manageable without losing important information.

- Multi-Block Attention (MBA) is used in libraries like TensorRT-LLM. This technique partitions long contexts into smaller blocks that can be processed in parallel across different Streaming Multiprocessors (SMs) on the GPU during the decode phase, merging the results efficiently.

## Results Summary

The following benchmarks were used to evaluate the contending models. Recall that the models must run on my computer. If models were run remotely, they could be much larger, which helps in a detailed computation. However, smaller models read faster, so bigger is not necessarily better. The benchmarks that were referred to provide metrics on coding-related capabilities:

- HumanEval: code generation accuracy

- LiveCodeBench v5: real-world algorithmic coding

- BFCL v3: function calling and tool use

- ToolBench: agentic task completion

I did not run the benchmarks myself. Grok provided the data. Here is a summary of the results. Details follow in separate sections.

| Model and Variant | HumanEval(Accuracy) | LiveCodeBench(Algorithms) | BFCL(Tool Calling) | ToolBench(Agency) | Notes |
| --- | --- | --- | --- | --- | --- |
| CodeLlama 13B/34B | 53–67.8% | ~30–40% | <50% | <50% | Outdated (2023). Minimal agency; fine for basic gen but lags in real-world/agents. |
| Codestral 22B | 71.4–86.6% | 37.9% | 65–70% | 65–70% | Solid coding. Good agency via prompt-based tools, but not as integrated as Qwen3;strong for multi-language but weaker planning. |
| DeepSeek-Coder-V2 (Lite 16B) | 90.2% | 43.4% | 65–70% | 70–75% | Excellent coder but algorithmic capability lags GLM-Z1-9B.Strong agency via MoE efficiency for tool chains; good for multi-step agents. |
| Gemma2:9B | 82–86% | ~60–70% | 75–80% | 72–78% | Fastest, strong function calling, reliable with structured prompts.Good multi-step task completion, minor edge-case failures.Weaker reasoning and planning; less accurate on complex logic. |
| GLM-Z1-9B-0414 | 75–80% | 65–70% | 55–60% | 60–65% | Excellent reasoning/planning but prompt-only agency; no native tools.Strong on math-integrated code. |
| MiniMax-M2 | 85-87% | 70–75% | 80-85% | 80-85% | The latest hotness. 1M context; SOTA open-source for agency and tools;excels in multi-step reasoning and execution. |
| Qwen3-Coder (14B–30B) | 89.3% | 70.7% | 75–80% | 75–80% | Strong coder. Excellent agency with native tool calling and agentic tuning;supports 128K+ contexts for multi-file agents. |

The above table is very wide, in fact you can only see a portion of it at a time. Drag left with your finger over the above table or use the horizontal scrollbar and push right to see the rest of the table.

Of the models discussed in this series, MinMax-M2 is the overall best performer. It excels in coding, tool use, and multi-step agency due to its massive 1M token context and advanced architecture.

Qwen3-Coder is the runner-up, matching or exceeding GLM-Z1-9B’s coding while offering significantly better agency through native tool support and agentic tuning. DeepSeek-Coder-V2 is a strong runner-up for coding but lags in tool calling. Codestral is balanced but not as agentic, and CodeLlama trails because it is an outdated 2023 model with weak tool support.

After the graphs shown in the next section, the rest of this article discusses each model in the above table in more detail. Subsequent articles are linked at the top and bottom of this web page.

## Graphs

artificialanalysis.ai publishes analysis of both commercial and open-source LLMs. Their website shows costs for the open-source models; however, they do not indicate how those costs were computed.

minimax.io, the Chinese company that makes MiniMax-M2, provide the following graph on their website. Note that the X axis is reversed, which is confusing, just so their product can appear in the upper right quadrant. Someone spent too much time reading Gartner magic quadrant summaries.

I think MinMax.ai just copied the data from artificialanalysis.ai without thinking too much about what the graphs actually mean. All they seemed to care about having their product in the upper-right quadrant.

Click on a section header below to see its contents.

## Codestral

### Model Collection Overview

The Codestral family is published by Mistral AI. These open-weight models specialize in code generation, completion, and editing across 80+ programming languages. Released in 2024, they emphasize developer workflows like autocomplete, debugging, and multi-language support, with strong benchmarks on HumanEval and MultiPL-E. Context lengths reach 32K tokens natively.

Two variants:

- Codestral-22B-v0.1: Dense Transformer-based, 22B parameters, instruct-tuned for code tasks. Base and chat versions available.

- Mamba-Codestral-7B-v0.1: 7B parameters, Mamba architecture outperforms similar-sized Transformers in speed and memory while matching code quality.

Quantized GGUF formats (e.g., from TheBloke or bartowski repos) support local runs via llama.cpp or Ollama. No major 2025 updates in current listings—these remain the core models, with community fine-tunes.

On Bear setup (i7-13700K, RTX 3060 12 GB VRAM, 64 GB RAM), both versions would run well with quantization, but the 22B version would require compromises for "good" performance.

### Compatibility and Performance Assessment

Short Answer: Yes for both—the 7B Mamba excels (fast and accurate); the 22B is viable but needs to be quantized/offloaded for acceptable speeds.

#### Mamba-Codestral-7B-v0.1

Mamba2's linear-time scaling makes it more VRAM- and compute-efficient than Transformers, ideal for your hardware.

| Quantization Level | Approx. File Size (VRAM Est. for Weights) | Fits in 12 GB? | Quality Impact | Expected Speed on RTX 3060 (4K Context) |
| --- | --- | --- | --- | --- |
| FP16 (unquantized) | ~14 GB | No (offload) | None | 40–60 t/s |
| Q8_0 | ~7.5 GB | Yes | Negligible | 50–70 t/s |
| Q5_K_M | ~5.5 GB | Yes | Minimal | 60–80 t/s |
| Q4_K_M | ~4.8 GB | Yes | Low | 70–90 t/s |

- Performance Notes: Blisteringly fast due to Mamba's architecture—often 1.5–2x quicker than 7B Transformers on Ampere GPUs. Full GPU load at Q5 delivers interactive coding (e.g., real-time autocompletion). Benchmarks show it rivaling 13B models on code eval while using half the resources.

#### Codestral-22B-v0.1

Dense model; larger for better multi-language reasoning but hungrier on resources.

| Quantization Level | Approx. File Size (VRAM Est. for Weights) | Fits in 12 GB? | Quality Impact | Expected Speed on RTX 3060 (4K Context) |
| --- | --- | --- | --- | --- |
| Q8_0 | ~23 GB | No | Negligible | N/A (heavy offload) |
| Q5_K_M | ~15 GB | No (offload ~15 layers) | Minimal | 12–20 t/s |
| Q4_K_M | ~13 GB | Barely (offload 5–10) | Low | 15–25 t/s |
| Q3_K_M | ~10.5 GB | Yes | Medium | 20–30 t/s |
| Q2_K | ~8 GB | Yes | High | 25–35 t/s (quality drop) |

- Performance Notes: Q4 with partial offload to your 64 GB RAM yields usable speeds for code gen, though not as snappy as smaller models. Mamba's efficiency edge makes the 7B preferable unless you need the 22B's superior benchmark scores (e.g., 75%+ on RepoBench). Avoid long contexts (>8K) to keep KV cache low.

#### CPU and RAM Role

- i7-13700K handles Mamba offloads seamlessly (negligible slowdown); for 22B, it manages 10–20 layers without frustration.

- 64 GB RAM enables full model loading in RAM if VRAM overflows, supporting 32K contexts fluidly.

#### 4. How to Run (Recommended: 7B for Speed, 22B for Power)

- Tools: Ollama (ollama run codestral-mamba) or llama.cpp: Download GGUF from bartowski/mistralai_Mamba-Codestral-7B-v0.1-GGUF, run ./llama-cli --model codestral-7b-q5.gguf --n-gpu-layers -1 -c 4096.

- Tips: Set temperature=0.1 for deterministic code; use --flash-attn for boosts. Test: "Generate a Go function for JWT validation with error handling."

- Quality: Q5 preserves 95%+ of original capabilities; Mamba variant shines in low-resource scenarios.

## CodeLlama

### Model Collection Overview

The search on Hugging Face for "codellama" under Meta Llama yields the Code Llama family: a 2023 release (no major updates through 2025) of code-focused LLMs based on Llama 2, fine-tuned for generation, completion, infilling, and explanation across 20+ languages. They support 16K token contexts (extendable via RoPE), with strengths in benchmarks like HumanEval (~50–70% pass@1 depending on size). All models are gated—require Meta approval for access.

Key variants (all available in HF Transformers format; community GGUF/AWQ quants via TheBloke/bartowski repos for local runs):

- 7B: CodeLlama-7b-hf (base), -Instruct-hf (chat/code tasks), -Python-hf (Python specialist).

- 13B: CodeLlama-13b-hf (base), -Instruct-hf, -Python-hf.

- 34B: CodeLlama-34b-hf (base), -Instruct-hf, -Python-hf.

- 70B: CodeLlama-70b-hf (base), -Instruct-hf (no Python variant).

Instruct/Python tunes excel for interactive coding; base for raw completion. Quantized versions enable Ollama/llama.cpp deployment.

On your Bear setup (i7-13700K, RTX 3060 12 GB VRAM, 64 GB RAM), 7B/13B run flawlessly; 34B is workable with quantization; 70B is impractical.

### Compatibility and Performance Assessment

Short Answer: Yes for 7B–34B (good performance with quants); no for 70B (VRAM overload even quantized).

#### 7B Variants

Lightweight and efficient; full GPU load at high precision.

| Quantization Level | Approx. File Size (VRAM Est. for Weights) | Fits in 12 GB? | Quality Impact | Expected Speed on RTX 3060 (4K Context) |
| --- | --- | --- | --- | --- |
| FP16 (unquantized) | ~14 GB | No (offload) | None | 40–60 t/s |
| Q8_0 | ~7.2 GB | Yes | Negligible | 50–70 t/s |
| Q5_K_M | ~5.3 GB | Yes | Minimal | 60–80 t/s |
| Q4_K_M | ~4.6 GB | Yes | Low | 70–90 t/s |

- Performance Notes: Snappy for code autocompletion (e.g., 70+ t/s on Instruct). Python variant shines for scripting; rivals modern 7B coders.

#### 13B Variants

Balanced sweet spot; quants fit comfortably.

| Quantization Level | Approx. File Size (VRAM Est.) | Fits in 12 GB? | Quality Impact | Expected Speed (4K Context) |
| --- | --- | --- | --- | --- |
| Q8_0 | ~13.5 GB | No (offload) | Negligible | 25–35 t/s |
| Q5_K_M | ~9.5 GB | Yes | Minimal | 35–50 t/s |
| Q4_K_M | ~8 GB | Yes | Low | 40–55 t/s |
| Q3_K_M | ~6.5 GB | Yes | Medium | 45–60 t/s |

- Performance Notes: Interactive for debugging/refactoring (40+ t/s at Q5). Instruct version handles multi-turn code chats well.

#### 34B Variants

Larger for complex reasoning; needs aggressive quants/offload.

| Quantization Level | Approx. File Size (VRAM Est.) | Fits in 12 GB? | Quality Impact | Expected Speed (4K Context) |
| --- | --- | --- | --- | --- |
| Q5_K_M | ~19 GB | No (offload ~20 layers) | Minimal | 10–18 t/s |
| Q4_K_M | ~16 GB | No (offload 10–15) | Low | 12–20 t/s |
| Q3_K_M | ~12.5 GB | Barely | Medium | 15–25 t/s |
| Q2_K | ~9 GB | Yes | High | 20–30 t/s (quality trade-off) |

- Performance Notes: Usable for heavy tasks like full function gen, but Q4 offload to RAM adds ~1s latency per response. Tops older 30B on infill.

#### 70B Variants

Flagship but resource-intensive; MoE-like density.

| Quantization Level | Approx. File Size (VRAM Est.) | Fits in 12 GB? | Quality Impact | Expected Speed |
| --- | --- | --- | --- | --- |
| Q4_K_M | ~38 GB | No | Low | N/A (<3 t/s with heavy offload) |
| Q3_K_M | ~28 GB | No | Medium | N/A |
| Q2_K | ~19 GB | No | Very high | N/A |

- Performance Notes: Overwhelms 12 GB VRAM; even max offload to 64 GB RAM yields <3 t/s. Cloud or 24+ GB GPU needed.

#### CPU and RAM Role

- i7-13700K manages offloads for 13B+ (e.g., 15 layers with <10% slowdown).

- 64 GB RAM absorbs KV cache for 16K contexts and spillover, enabling stable runs.

#### How to Run (Recommended: 13B-Instruct for Versatility)

- Access: Request via HF model page (Meta form; approved in ~1 day).

- Tools: Ollama (ollama run codellama:13b-instruct-q5_K_M) or llama.cpp: Download GGUF from TheBloke/CodeLlama-13B-Instruct-GGUF, run ./llama-cli --model codellama-13b-instruct-q5.gguf --n-gpu-layers -1 -c 4096 --infill.

- Tips: Use temperature=0.2 for code; enable --rope-scaling for longer contexts. Test: "Complete this C++ class for a neural net layer."

- Quality: Q5 retains 95%+ benchmark fidelity; Python tunes boost lang-specific accuracy.

In summary, CodeLlama is a decent option for local coding on Bear. The 7B or 13B versions work, save the 34B version for when you need depth. The 70B is too large to run on Bear.

## DeepSeek-Coder-V2

The Hugging Face collection for DeepSeek-Coder-V2 features two primary variants of the DeepSeek-Coder-V2 models, both Mixture-of-Experts (MoE) architectures optimized for code generation, completion, and instruction-following tasks. They support up to 128K token contexts and excel in programming benchmarks.

- DeepSeek-Coder-V2-Lite-Instruct: 16B total parameters (2.4B active during inference).

- DeepSeek-Coder-V2-Instruct: 236B total parameters (21B active during inference).

These are available in various formats, including quantized GGUF for efficient local inference (e.g., via llama.cpp or Ollama). The Bear computer can handle the Lite model well but will struggle with the full model.

### Compatibility and Performance Assessment

Short Answer: Yes: for the 16B Lite variant (good performance with quantization). No: for the 236B full variant (impractical on single-GPU system like Bear).

### DeepSeek-Coder-V2-Lite-Instruct (16B)

This fits and runs smoothly on your hardware using quantized versions. The MoE design keeps active compute low, aiding efficiency.

- Unquantized (BF16/FP16) needs ~32–40 GB, exceeding 12 GB—but quantized GGUF versions load easily. Quantization Level Approx. File Size (VRAM Est. for Weights) Fits in 12 GB VRAM? Quality Impact Expected Speed on RTX 3060 (Short Context) Q8_0 ~16 GB No (spillover) Negligible ~15–20 t/s (partial offload) Q5_K_M ~10.5 GB Yes Minimal ~25–35 t/s Q4_K_M ~9 GB Yes Low ~30–40 t/s Q3_K_M ~7.5 GB Yes Medium ~35–45 t/s Q2_K ~6 GB Yes High ~40–50 t/s (but avoid for quality)

| Quantization Level | Approx. File Size (VRAM Est. for Weights) | Fits in 12 GB VRAM? | Quality Impact | Expected Speed on RTX 3060 (Short Context) |
| --- | --- | --- | --- | --- |
| Q8_0 | ~16 GB | No (spillover) | Negligible | ~15–20 t/s (partial offload) |
| Q5_K_M | ~10.5 GB | Yes | Minimal | ~25–35 t/s |
| Q4_K_M | ~9 GB | Yes | Low | ~30–40 t/s |
| Q3_K_M | ~7.5 GB | Yes | Medium | ~35–45 t/s |
| Q2_K | ~6 GB | Yes | High | ~40–50 t/s (but avoid for quality) |

With Q5/Q4, expect interactive speeds (20+ tokens/second) for code tasks. The 64 GB RAM allows seamless layer offloading if needed (e.g., via --n-gpu-layers 999 in llama.cpp), but full GPU loading is feasible. Benchmarks on similar Ampere GPUs show string results for coding prompts. Tools like Ollama or LM Studio simplify setup; download from repositories like bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF.

#### DeepSeek-Coder-V2-Instruct (236B)

This is infeasible for good performance on your setup due to sheer size, even with MoE efficiencies.

- Unquantized needs ~472 GB (multi-GPU cluster). Quantized versions are still massive. Quantization Level Approx. File Size (VRAM Est. for Weights) Fits in 12 GB VRAM? Quality Impact Expected Speed on RTX 3060 Q4_K_M ~133–142 GB No Low N/A (won't load) Q3_K_M ~100+ GB No Medium N/A Q2_K ~70–80 GB No (heavy offload) Very high <2 t/s (CPU-dominant)

| Quantization Level | Approx. File Size (VRAM Est. for Weights) | Fits in 12 GB VRAM? | Quality Impact | Expected Speed on RTX 3060 |
| --- | --- | --- | --- | --- |
| Q4_K_M | ~133–142 GB | No | Low | N/A (won't load) |
| Q3_K_M | ~100+ GB | No | Medium | N/A |
| Q2_K | ~70–80 GB | No (heavy offload) | Very high | <2 t/s (CPU-dominant) |

Even aggressive Q2 quantization exceeds 12 GB VRAM, forcing massive offload to 64 GB RAM (which can hold ~half the model). Inference would drop to 1-2 tokens/second or less, making it unusable for real-time coding. Multi-GPU (e.g., 8x 80 GB) or cloud is required for viable runs. Quantized files are available (e.g., bartowski/DeepSeek-Coder-V2-Instruct-GGUF), but are not practical here.

#### CPU and RAM

- A 16 core i7-13700K handles offloads decently for the Lite model but bogs down the 236B (pure CPU: <1 tokens/second).

- 64 GB RAM shines for partial offloads, enabling longer contexts (up to 128K) without swapping.

#### How to Run the Lite Model

Go for the 16B Lite—it's a powerhouse for coding on Bear with quantization. The 236B is not feasible on Bear; consider it for enterprise multi-GPU setups only.

For a quick test, type:

```
PS C:\Users\Mike Slinn> ollama run deepseek-coder-v2:lite
pulling manifest
pulling 5ff0abeeac1d: 100% ▕█████████████████████████████████████▏ 8.9 GB
pulling 22091531faf0: 100% ▕█████████████████████████████████████▏ 705 B
pulling 4bb71764481f: 100% ▕█████████████████████████████████████▏ 13 KB
pulling 1c8f573e830c: 100% ▕█████████████████████████████████████▏ 1.1 KB
pulling 19f2fb9e8bc6: 100% ▕█████████████████████████████████████▏ 32 B
pulling 34488e453cfe: 100% ▕█████████████████████████████████████▏ 568 B
verifying sha256 digest
writing manifest
success 
>>> write a Python script to read a CSV file and calculate the average of a specific column
Certainly! Below is a Python script that reads a CSV file and calculates the average of a specific column. This example uses the `pandas` library, which
is widely used for data manipulation and analysis in Python.

First, make sure you have the `pandas` library installed. You can install it using pip if you haven't already:

```sh
pip install pandas
```

Here's the script:

```python
import pandas as pd

def calculate_average(csv_file, column_name):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Check if the specified column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the CSV file.")

    # Calculate the average of the specified column
    average = df[column_name].mean()

    return average

# Example usage
csv_file = 'your_file.csv'  # Replace with your CSV file path
column_name = 'your_column_name'  # Replace with the name of the column you want to calculate the average for

try:
    avg = calculate_average(csv_file, column_name)
    print(f"The average of {column_name} is: {avg}")
except ValueError as e:
    print(e)
```

### Explanation:
1. **Import pandas**: The script starts by importing the `pandas` library.
2. **Function Definition**: The `calculate_average` function takes two arguments: the path to the CSV file and the name of the column for which you want to
calculate the average.
3. **Read CSV**: It reads the CSV file into a DataFrame using `pd.read_csv(csv_file)`.
4. **Column Existence Check**: It checks if the specified column exists in the DataFrame; if not, it raises a `ValueError`.
5. **Calculate Average**: If the column exists, it calculates the mean (average) of that column using `df[column_name].mean()`.
6. **Return and Print**: The average is returned and printed.
7. **Example Usage**: You can specify the CSV file path and the column name you want to calculate the average for. If an error occurs, it catches the
exception and prints the error message.

Replace `'your_file.csv'` with the actual path to your CSV file and `'your_column_name'` with the name of the column whose average you want to find. 
```

The context length defaults to 4K to 8K. For best performance on Bear, increase it to 128K by setting the num_ctx parameter inside a chat, as follows:

```
PS C:\Users\Mike Slinn> ollama run deepseek-coder-v2:lite

>>> /set parameter num_ctx 131072
Set parameter 'num_ctx' to '131072' 
```

Use a low temperature for code. In a chat, type:

```
>>> /set parameter temperature 0.2
Set parameter 'temperature' to '0.2' 
```

#### Performance

| Context Length | VRAM Used | t/s (Q4_0) | Notes |
| --- | --- | --- | --- |
| 128 K | ~11.5 GB | 22 – 30 | Interactive, full GPU load, RAM sufficient |
| 64 K | ~10.8 GB | 25 – 33 |   |
| 32 K | ~10.2 GB | 28 – 36 |   |
| 8 K | ~9.3 GB | 35 – 45 | (baseline) |

### Why This Speed?

| Factor | Impact |
| --- | --- |
| MoE (2.4B active) | Only 2.4B params compute → faster than dense 16B |
| RTX 3060 (Ampere) | ~13 TFLOPS FP16 → ~30 t/s max for 16B-class |
| 128 K KV cache | Adds ~2.
**Published:** 2025-11-03

### Result 6
**Title:** Best GPU for Local LLM[2025]: Complete Hardware Guide for Running Language Models Locally
**URL:** https://nutstudio.imyfone.com/llm-tips/best-gpu-for-local-llm/?utm_source=valyu.ai&utm_medium=referral
**Source:** web

**Content:**
Best GPU for Local LLM[2025]: Complete Hardware Guide for Running Language Models Locally

Home > LLM Tips

Aaron Smith

November 20, 2025

254 views , 10 mins read

Rated successfully!

You have already rated this article, please do not repeat scoring!

Have you seen headlines about private ChatGPT or Grok3 conversations leaking online? It's a real concern. When you use most popular AI tools, your data is processed on company servers, outside of your control. While you can run ChatGPT-quality AI on your own computer—privately, using the GPU you might already have.

This guide cuts through the technical jargon to provide a clear, straightforward path. You will learn how to evaluate your current graphics card (GPU), understand what kind of AI models it can handle, and ultimately choose the right setup to get the best performance for your budget. Our goal is to make running a private AI simple, putting you back in control of your data.

CONTENT:

- Understanding GPU Requirements for Local LLMs

- Our Top GPU Picks for Local LLMs in 2025

- Best Consumer Picks

- Professional and High-End Uses

- Budget-Conscious GPU Picks

- Best LLM Choices by GPU VRAM Capacity: What Can You Run?

- NVIDIA GPU Alternatives: More Options and Apple Silicon

- AMD GPUs

- Apple Silicon

- Intel and Huawei GPUs

- Frequently Asked Questions (FAQ)

- Conclusion

## Understanding GPU Requirements for Local LLMs

Before discussing specific GPU recommendations, it's crucial to understand the fundamental concepts that determine whether a GPU can effectively run a language model. These concepts will guide every hardware decision you make.

### VRAM (Video RAM)

VRAM is the GPU's dedicated memory—the workspace where the model resides during inference. For language models, VRAM is the foundation of LLM performance: the model must fit in VRAM or it won't load, and relying on system RAM will severely degrade performance.

Rule of thumb: roughly 2 GB of VRAM per billion parameters at FP16.

- A 7B model needs ~14 GB

- A 13B model needs ~26 GB

Quantization (below) can reduce these requirements substantially.

Don't have a high-end GPU? Run optimized models (under 5B) instantly. Nut Studio simplify the setup so you can pick and deploy LLMs without the expensive hardware upgrades or deep tech skills.

Free Download

### Memory Bandwidth

Memory bandwidth (GB/s) is how quickly a GPU can move data within VRAM. It directly affects token generation speed—how responsive the model feels. A GPU with ample VRAM but low bandwidth may still load models, but it will respond slowly.

However, older GPUs with generous VRAM can still perform well, as they keep both the full model and KV cache on-GPU—avoiding CPU offload that would negate bandwidth or architectural advantages.

Note

Modern GPUs like the RTX 4090 exceed 1000 GB/s; older or budget cards may offer 400–600 GB/s. For interactive use, aim for ≥600 GB/s to keep conversations fluid.

### Quantization

Quantization reduces weight precision (e.g., FP16 → INT8/INT4), shrinking the VRAM footprint and allowing models 2–4× larger to run on the same hardware—often with minimal or even imperceptible quality loss for typical use.

Example: a 13B model that needs ~26 GB at FP16 can often run in 8–10 GB when quantized to 4-bit. Fitting bigger models into smaller VRAM.

### VRAM Requirements by Model Size

Don't worry about manual configuration. Our tool auto-detects your GPU and sets up the best model for you in one click.

| Model Size | FP16 (Full Precision) | INT8 (8-bit Quantized) | INT4 (4-bit Quantized) | Minimum GPU | Action Now |
| --- | --- | --- | --- | --- | --- |
| 7B | 14GB | 7GB | 3.5GB | RTX 3060 12GB | Download |
| 7B | 14GB | 7GB | 3.5GB | RTX 3060 12GB | Download |
| 13B | 26GB | 13GB | 6.5GB | RTX 3080 10GB (INT4) | Download |
| 30B | 60GB | 30GB | 15GB | RTX 4090 24GB (INT4) | Download |
| 70B | 140GB | 70GB | 35GB | RTX 6000 Ada 48 GB(single GPU), 2× RTX 3090 with NVLink (INT4) | Download |

## Our Top GPU Picks for Local LLMs in 2025

Now that you understand the key metrics, here are our specific GPU recommendations for every budget and use case. NVIDIA's CUDA platform is the industry standard, making these cards the path of least resistance for local AI.

### 1 Best Consumer Picks: NVIDIA GPUs

NVIDIA's CUDA platform has become the industry standard for AI workloads, offering unmatched software support and optimization. Every major LLM framework—from PyTorch to TensorFlow—is built with CUDA in mind, making NVIDIA GPUs the path of least resistance for local deployment.

NVIDIA RTX 4090

- Pros: The largest VRAM (24GB) in the consumer lineup, enabling larger models and longer context windows. It provides the best performance-to-VRAM ratio for most users. You can comfortably run quantized 30B models or even experiment with 70B models.

- Cons: High cost.

NVIDIA RTX 4080

- Pros: Good performance for its price, handles quantized models up to 13B–33B comfortably.

- Cons: Lower VRAM (16GB) compared to the 4090, which can limit model size and context window length. You'll need to manage your memory more carefully.

### RTX 4090 vs 4080 vs 4070 Ti: Local LLM Reality Check

RTX 4090 (24GB VRAM)

Represents the easiest path to larger models and longer context windows with minimal workarounds. You can load 30B models at 8-bit quantization while maintaining 8K+ token contexts, or push to 70B models with 4-bit quantization. The extra 8GB over the 4080 eliminates constant VRAM anxiety and allows for comfortable experimentation. Token generation typically reaches 40-50 tokens/second on 13B models.

RTX 4080 (16GB VRAM)

Delivers strong throughput and handles 13B-33B quantized models comfortably. However, you'll need to watch context length and batch size carefully. Extended conversations or document analysis can push VRAM limits. Expect 30-35 tokens/second on 13B models—still excellent for interactive use but requiring more careful resource management.

RTX 4070 Ti (12GB VRAM)

Offers efficiency and competence for 7B and quantized 13B models, but you'll hit VRAM walls sooner than you'd like. Long context windows become problematic, and forget about experimenting with larger models without aggressive quantization. Token generation hovers around 25-30 tokens/second on 7B models—acceptable but limiting for advanced use cases.

If you value longer context windows, want to experiment with diverse models, and prefer avoiding constant memory optimization, the jump to 24GB VRAM is right.

### 2 Professional and High-End Uses

NVIDIA RTX 6000 Ada Generation

- Pros: A massive 48GB of VRAM, essential for training, fine-tuning, and running very large models without compromise. Supports advanced enterprise workflows.

- Cons: Very high cost, designed for workstations, not typical desktops.

NVIDIA A100

- Pros: Proven reliability for enterprise and cloud environments. Available with up to 80GB of VRAM for handling enormous models and datasets.

- Cons: Extremely expensive and designed for data centers, not local desktop use. Overkill for 99% of users.

### 3 Budget-Conscious GPU Picks

Not everyone can accept flagship GPU prices, and thankfully, with the fast updates of GPUs, the used market offers exceptional opportunities for budget-conscious LLM enthusiasts. For language model work, the key is that older GPUs with large VRAM pools often outperform newer GPU models with less memory.

NVIDIA RTX 3090 24GB

- Pros: Best budget option. Available for $700-900 used, it matches the RTX 4090's VRAM capacity while delivering 70-80% of its performance. This is the undisputed value champion, capable of running 30B models comfortably and even stretching to 70B with aggressive quantization.

- Cons: Used market availability can be inconsistent, and you're buying older hardware without warranty coverage in most cases.

RTX 4070 Ti Super 16 GB

- Pros: A practical sweet spot for 7B–13B models with longer contexts, offering excellent perf-per-watt without the heat and noise tax of older high-end cards.

- Cons: Costs more than older cards and still not enough VRAM for easy 30B.

### Professional Cards vs Consumer Cards

Professional cards (A100/H100) offer undeniable advantages: massive VRAM pools (40–80GB), NVLink for true multi-GPU scaling, ECC memory for production reliability, and data center-grade cooling solutions. These features matter for production inference servers handling thousands of requests or research institutions training custom models.

However, the downsides are equally significant. Prices start at $10,000+, power requirements often exceed standard PSUs, cooling solutions require a server chassis, and the complexity is too great for typical local deployments. Unless you are building production infrastructure or have specific enterprise requirements, these cards represent significant overkill.

Consumer RTX cards are the pragmatic choice for 99% of local LLM users. They fit standard desktop cases, work with regular power supplies, run quietly enough for office environments, and cost a fraction of professional cards.

### Price-to-Performance Analysis

When evaluating GPUs for local LLM deployment, start with a simple calculation: VRAM capacity divided by price.

When evaluating GPUs for LLM work, traditional gaming benchmarks become irrelevant. Instead, focus on VRAM per dollar—a metric that reveals surprising value propositions. A used RTX 3090 with 24GB of VRAM at $700-900 offers better value than a new RTX 4070 Ti with 12GB at similar prices, despite the older architecture. For LLM work, VRAM capacity trumps architectural improvements in most cases.

## Matching LLMs to Your GPU: What Can You Run?

Here are some of the best models you can run, categorized by the VRAM on your GPU.

Best LLMs for 8GB VRAM (2025)

| GPU VRAM | Model | Quantization | Why / Notes |
| --- | --- | --- | --- |
| 8GB | Mistral 7B | INT4 | Great balance of speed and quality for general use. |
| 8GB | Llama 3.2 7B | INT4 | Smooth on consumer GPUs; strong multilingual support. |
| 8GB | Phi-4 Mini | INT4 | Compact model from Microsoft; excellent for coding tasks than Phi-3. |
| 8GB | Gemma 7B | INT4 | Efficient Google model optimized for modest hardware. |

Best LLMs for 12GB VRAM (2025)

| GPU VRAM | Model | Quantization | Why / Notes |
| --- | --- | --- | --- |
| 12GB | Llama 3.1 13B | INT4 | Top choice for conversation and reasoning on mid-range GPUs. |
| 12GB | CodeLlama 13B | INT4 | Specialized for programming; solid code completion and Q&A. |
| 12GB | Mistral-Nemo 12B | INT4 / INT8 | Fits comfortably with room for context; good generalist. |
| 12GB | Yi-1.5 9B | INT8 | Strong long-context performance with stable 8-bit runs. |

Best LLMs for RTX 4090 (24GB VRAM)

| GPU VRAM | Model | Quantization | Why / Notes |
| --- | --- | --- | --- |
| 24GB (RTX 4090) | Llama 3.1 70B | INT4 | Flagship local performance for complex reasoning and depth. |
| 24GB (RTX 4090) | Mixtral 8x7B | INT4 (MoE) | Mixture-of-Experts with GPT-4-class results on many tasks. |
| 24GB (RTX 4090) | DeepSeek Coder 33B | INT4 | Superior for software development, debugging, and code synthesis. |
| 24GB (RTX 4090) | Qwen 2.5 32B | INT4 | Excellent multilingual and mathematical capabilities. |

For models under 7B parameters (Small Language Models), see our SLM and LLM comparison guide for tailored deployment recommendations.

Exploring Video Models: Once you have your local LLM running, you can use it to brainstorm creative ideas for other media. With the rapid rise of US and Chinese AI video generators, many users are now pairing their local models with video AIs. Check out our guide on how to access Veo 3 free to get started. You can even use your local LLM to draft detailed prompts for high-quality video generation.

Unsure what your current GPU can handle? Match models to your hardware in seconds with Nut Studio's compatibility check.

## NVIDIA GPU Alternatives: More Options and Apple Silicon

While NVIDIA offers the smoothest experience, other options exist for those willing to experiment or who have different priorities.

### 1 AMD GPUs: High VRAM, More Tinkering

AMD's flagship RX 7900 XTX offers strong hardware specifications—24GB of VRAM and ~960 GB/s bandwidth—often matching the RTX 3090/4090 at a lower price. However, its main drawback lies in software support. While ROCm, AMD's compute platform and CUDA alternative, has improved significantly, it still lags behind in framework compatibility and ease of use. It often requires manual configuration and lacks out-of-the-box support for many tools.

For users comfortable with Linux and troubleshooting, it can be a viable option, but Windows users are generally better served by NVIDIA.

### 2 Apple Silicon: A Unified Memory Powerhouse

Apple Silicon (M1 ~ M4 series) introduces a unique unified memory architecture where system RAM and VRAM are shared. Current Mac Studio models with an M3 Ultra support up to 512GB of unified memory and over 800GB/s bandwidth, enabling very large language models to run entirely in memory. On price, a base M3 Ultra Mac Studio ($3,999) with 96GB of unified memory costs less than a single high-end professional GPU.

However, token generation speeds lag behind dedicated GPUs—expect 5-15 tokens per second versus 30-50 on an RTX 4090. Apple Silicon excels for experimentation with large models and development work where response speed isn't critical. For production deployments requiring fast inference, dedicated GPUs remain superior.

### 3 The Experimental Zone: Intel and Regional Players

Intel Arc GPUs represent an interesting wildcard. The A770 (16GB VRAM) offers substantial memory at competitive prices, but software support remains embryonic. Intel's commitment to AI acceleration is clear, but the ecosystem needs time to mature. Consider Intel Arc only for experimentation, not production use.

Regional alternatives like Huawei GPUs face availability challenges outside their home markets. While technically capable and attracting a high level of attention and discussion, obtaining hardware and accessing documentation presents significant barriers for most users.

Nut Studio

- Automatically detects your GPU and recommends compatible models

- One-click deployment without manual configuration

- Optimizes model selection based on your hardware capabilities

- Supports all major GPU brands including NVIDIA, AMD, and Intel

Try It Free

## Frequently Asked Questions (FAQ)

### 1 What's the Minimum GPU for Running Local LLMs?

The absolute minimum for meaningful LLM work is a GPU with 8GB of VRAM. This allows you to run 7B parameter models with 4-bit quantization, providing ChatGPT-3.5-like capabilities. However, 12GB of VRAM (RTX 3060 12GB, RTX 4070) offers much better flexibility, allowing you to run 7B models at higher precision or experiment with 13B models. Below 8GB, you're limited to very small models. We also have a guide for SLM and LLM comparison.

### 2 Can I Run 70B Models on A Single Consumer GPU?

Running 70B models on a single consumer GPU requires aggressive optimization. The RTX 4090 or RTX 3090 (both with 24GB VRAM) can technically run 70B models using 4-bit quantization, which reduces the memory requirement to approximately 35GB. However, this requires techniques like offloading some layers to system RAM, which significantly impacts performance. For better 70B model deployment, consider dual-GPU setups or cloud solutions.

### 3 Is NVIDIA better than AMD for local AI models?

For most people, NVIDIA is the safer and smoother choice because of its mature CUDA ecosystem and near-universal framework support. AMD can be a great value (more VRAM per dollar) if you're on Linux, your card is on the ROCm support list, and you don't mind some tinkering.

If you want the least friction and widest software compatibility, choose NVIDIA. If you're Linux-savvy and chasing maximum VRAM per dollar while accepting some tinkering, AMD can be worthwhile.

### 4 Can Intel GPUs Run Local Language Models?

Intel Arc GPUs can technically run language models through frameworks like llama.cpp and IPEX-LLM, but support remains experimental. The Arc A770 with 16GB VRAM has sufficient memory for many models, but performance optimization lags behind NVIDIA and AMD. Driver updates are frequent but sometimes unstable, and community support is limited. Intel Arc represents an interesting future option as the ecosystem matures, but it's not recommended for users who need reliable LLM deployment today.

## Conclusion

Choosing the right GPU for running AI locally is a personal decision that balances performance, budget, and technical comfort. The NVIDIA RTX 4090 offers unmatched power for those who want the absolute best, while a used RTX 3090 provides excellent value with the same 24GB of memory for a lower price. Meanwhile, newcomers can find a capable and affordable entry point with the RTX 4070 Ti Super.

For users starting their local LLM journey who want to avoid the complexity of manual setup, Nut Studio offers automated deployment progress that detect hardware capabilities and optimize model selection accordingly.

Aaron brings over a decade of experience in crafting SEO-optimized content for tech-focused audiences. At Nut Studio, he leads the blog’s content strategy and focuses on the evolving intersection of AI and content creation. His work dives deep into topics like large language models (LLMs) and AI deployment frameworks, turning complex innovations into clear, actionable guides that resonate with both beginners and experts.

- Best Animes to Learn Japanese in 2025 Discover 14 anime perfect for learning Japanese, from beginner to advanced levels. Get practical tips on using anime and AI to improve your Japanese skills effectively. 10 mins read

Discover 14 anime perfect for learning Japanese, from beginner to advanced levels. Get practical tips on using anime and AI to improve your Japanese skills effectively.

- How ChatGPT Helps with Tests: 10 Methods for Preparation Learn 10 best ways to use ChatGPT for test and exam prep. Get personalized quizzes, instant feedback, and study smarter for SAT, TOEFL, university finals & more. 6 mins read

Learn 10 best ways to use ChatGPT for test and exam prep. Get personalized quizzes, instant feedback, and study smarter for SAT, TOEFL, university finals & more.

- How to Use ChatGPT to Learn a Language? 5 Free Ways Tested Unlock fluency faster with AI language learning. Get 5 powerful ChatGPT strategies and prompts for personalized vocabulary, grammar, and speaking practice. 10 mins read

Unlock fluency faster with AI language learning. Get 5 powerful ChatGPT strategies and prompts for personalized vocabulary, grammar, and speaking practice.

- 20 Things You Should Never Tell ChatGPT Stop letting ChatGPT waste your time. Discover 20 things that AI kill your focus and efficiency, while also learning the essential security rules to work safely. 10 mins read

Stop letting ChatGPT waste your time. Discover 20 things that AI kill your focus and efficiency, while also learning the essential security rules to work safely.

- Best ChatGPT Prompts for Academic Writing in 2025 [Templates Included] Discover best ChatGPT prompts for academic writing. Get templates for each step that actually work. Test locally with Nut Studio. 10 mins read

Discover best ChatGPT prompts for academic writing. Get templates for each step that actually work. Test locally with Nut Studio.

- Best LLMs for Resume Writing: Cloud vs. Local[2025 Tested] Unbiased 2025 review of the best LLMs for resume writing—Claude 4, Gemini 2.5 Pro, GPT-5, Llama 3.2, Mistral, Phi-4—plus prompts, advanced LLM tips, and local setup. 5 mins read

Unbiased 2025 review of the best LLMs for resume writing—Claude 4, Gemini 2.5 Pro, GPT-5, Llama 3.2, Mistral, Phi-4—plus prompts, advanced LLM tips, and local setup.

### 0 Comment(s)

Join the discussion!
**Published:** 2025-11-20

### Result 7
**Title:** 4 open‑source apps I use to run AI locally
**URL:** https://www.xda-developers.com/opensource-apps-i-use-to-run-ai-locally/?utm_source=valyu.ai&utm_medium=referral
**Source:** web

**Content:**
Sign in to your XDA account

No AdsNinja v10 Client!

No AdsNinja v10 Client!

No AdsNinja v10 Client!

No AdsNinja v10 Client!

When AI platforms started mushrooming out of nowhere, I wasn’t very fond of using them in my workflows. And well, that sentiment still hasn’t changed, especially with most software and hardware manufacturers slapping artificial intelligence onto their products. However, I wouldn’t group large language models and image generators under the same umbrella as AI apps that big corporations try to shove down everybody’s throats at every chance they get.

No AdsNinja v10 Client!

No AdsNinja v10 Client!

That’s because LLMs (and by extension, image generation tools) have their use cases, no matter how niche they may be. The problem is that online AI-hosting platforms are rife with privacy issues, with most of them restricting essential features behind paid subscriptions. Self-hosting my own AI tools turned out to be a neat solution, and here’s a collection of utilities I run on local servers (and even my daily driver) to integrate LLMs and image creation models into my everyday tasks.

No AdsNinja v10 Client!

## Ollama

### It aids plenty of services in my self-hosted stack

If you’ve read my articles on XDA, you may already know that I love running a bajillion services on my home lab. Although most of them are fairly self-sufficient and work well inside containerized environments while consuming minimal resources, others mesh well with external services – including LLMs.

While we’re on the subject, I use Ollama to deploy and manage the majority of my self-hosted LLMs. If you haven’t heard of it, Ollama is a FOSS tool that can harness the processing capabilities of your local hardware to run LLMs without involving external cloud platforms. Ollama supports a ton of models, ranging from simple 0.7B and 1B variants that can even run on SBCs and CPUs to hardcore 70B+ LLMs that can only be tamed by cutting-edge graphics cards. And the best part? Ollama’s API is compatible with many home lab services, so I can directly integrate it with my arsenal of containers and virtual machines.

Home Assistant, for instance, supports AI-powered queries, and even something as lightweight as 3B Ollama-based models can [answer most of my questions](https://www.xda-developers.com/i-use-this-tiny-llm-to-control-my-smart-home/) and perform the right smart home operations without issues. Likewise, Paperless-GPT utilizes my Ollama models to improve the document manager’s OCR and search capabilities. Then there’s [Karakeep](https://www.xda-developers.com/this-self-hosted-app-showed-me-been-using-bookmarks-wrong-all-life/), which uses LLMs to generate tags and summaries for my bookmarks. Heck, I’ve even armed the VS Code instances running on my dev VMs with LLMs using the Continue.Dev extension. And not for generating code, mind you. The models instead provide autocompletion, code review, and debugging support for my programming tasks. And I haven’t even mentioned using Ollama models with [Open Notebook](https://www.xda-developers.com/open-notebook-is-the-best-self-hosted-notebooklm-alternative/).

No AdsNinja v10 Client!

## KoboldCPP

### To run LLMs on my daily drivers

As much as I love my Ollama instance, I run it as a VM on my home server, and there are times when I can’t access the LLMs from my everyday machine. That’s because my old RTX 3080 Ti can only handle so many LLM workloads before hitting high utilization levels, and I wouldn’t want to tax it with extra tasks.

That’s where my KoboldCPP instances fit into the equation. I’ve got it running on both my MacBook and (bare-metal) Windows 11 PC. Coming from Ollama, it took a little while to get used to KoboldCPP, but I use it for everything from my D&D escapades to quickly checking the feasibility of my programming algorithms.

No AdsNinja v10 Client!

## Automatic1111

### Or rather, Stable Diffusion

Image generators may still produce inconsistencies when creating illustrations, but they’ve come a long way since the early days, when their creations were pretty much nightmare fuel. Similar to Ollama and KoboldCPP, Automatic1111 is a tool where I can feed the model files and play around with prompts to create images.

Personally, I tend to avoid using Automatic1111 (or rather, Stable Diffusion models) to generate illustrations, and creating custom character portraits for my D&D campaigns is the farthest I’m willing to go with it. Instead, I mostly use it to upscale low-resolution images from my early childhood days. The only caveat is that it requires way too much processing power – to the point where I’m already planning to upgrade to a used RTX 4090. And as weird as it may sound, I also use Automatic1111 with GIMP to add AI-powered inpainting and X/Y plotting support to the king of FOSS image editors.

No AdsNinja v10 Client!

## Faster-whisper

### For my audio transcription tasks

Faster-whisper is something I never really used until recently, but I’m really glad I came across this handy tool. Upon first glance, being able to transcribe audio may seem like a niche utility, but faster-whisper is more than worth the complicated setup. Running faster-whisper’s algorithms on meetings makes it easier to create notes, as I don’t have to constantly switch back and forth between different sections of the footage.

The same holds true for podcasts and interviews, and it can even generate subtitles for YouTube videos. Sure, it’s a bit of a pain to configure, but being able to archive long audio clips is quite handy – especially for content creators like yours truly.

### You’ll need fairly decent systems to self-host AI tools

Although LLMs-hosting utilities and image generators have become a lot more accessible, they need a lot of horsepower for the best results. Sure, the low-parameter models may run on budget hardware, but their utility is rather limited – especially for image upscaling and other tasks that require better accuracy. Their high-capacity counterparts can produce significantly better results, but you'll have to sacrifice your wallet for cutting-edge graphics cards if you don’t want to encounter performance issues.

Close
**Published:** 2025-11-11

### Result 8
**Title:** Run AI Models Locally: A New Laptop Era Begins - IEEE Spectrum
**URL:** https://spectrum.ieee.org/ai-models-locally?utm_source=valyu.ai&utm_medium=referral
**Source:** web

**Content:**
[Computing](https://spectrum.ieee.org/topic/computing/)[AI](https://spectrum.ieee.org/topic/artificial-intelligence/)[Magazine](https://spectrum.ieee.org/magazine/)[Feature](https://spectrum.ieee.org/type/feature/)

# Your Laptop Isn’t Ready for LLMs. That’s About to Change

Local AI is driving the biggest change in laptops in decades

[Matthew S. Smith](https://spectrum.ieee.org/u/matthew-s-smith)

17 Nov 2025

10 min read

Vertical

Dan Page

Blue

**Odds are the PC in**your office today isn’t ready to run AI [large language models](https://spectrum.ieee.org/large-language-model-performance) (LLMs).

Today, most users interact with LLMs via an online, browser-based interface. The more technically inclined might use an application [programming](https://spectrum.ieee.org/tag/programming) interface or command line interface. In either case, the queries are sent to a [data center](https://spectrum.ieee.org/dcflex-data-center-flexibility), where the model is hosted and run. It works well, until it doesn’t; a data-center outage can take a model offline for hours. Plus, some users might be unwilling to send [personal data](https://spectrum.ieee.org/tag/personal-data) to an anonymous entity.

Running a model locally on your computer could offer significant benefits: lower latency, better understanding of your personal needs, and the privacy that comes with keeping your data on your own machine.

However, for the average laptop that’s over a year old, the number of useful [AI models](https://spectrum.ieee.org/tag/ai-models) you can run locally on your PC is close to zero. This laptop might have a four- to eight-core processor ([CPU](https://en.wikipedia.org/wiki/Central_processing_unit)), no dedicated [graphics](https://spectrum.ieee.org/tag/graphics) chip ([GPU](https://en.wikipedia.org/wiki/Graphics_processing_unit)) or neural-processing unit ([NPU](https://en.wikipedia.org/wiki/Neural_processing_unit)), and 16 gigabytes of [RAM](https://en.wikipedia.org/wiki/Random-access_memory), leaving it underpowered for LLMs.

Even new, high-end PC [laptops](https://spectrum.ieee.org/tag/laptops), which often include an NPU and a GPU, can struggle. The largest AI models have over a trillion parameters, which requires memory in [the hundreds of gigabytes](https://snowkylin.github.io/blogs/a-note-on-deepseek-r1.html#:~:text=Note-,Models,Studio%20(%245.6k)!). Smaller versions of these models are available, even prolific, but they often lack the intelligence of larger models, which only dedicated AI [data centers](https://spectrum.ieee.org/tag/data-centers) can handle.

The situation is even worse when other AI features aimed at making the model more capable are considered. [Small language models (SLMs)](https://huggingface.co/blog/jjokah/small-language-model) that run on local hardware either scale back these features or omit them entirely. Image and video generation are difficult to run locally on laptops, too, and until recently they were reserved for high-end tower desktop PCs.

That’s a problem for AI adoption.

To make running AI models locally possible, the hardware found inside laptops and the software that runs on it will need an upgrade. This is the beginning of a shift in laptop design that will give engineers the opportunity to abandon the last vestiges of the past and reinvent the PC from the ground up.

## NPUs enter the chat

The most obvious way to boost a PC’s AI performance is to place a powerful NPU alongside the CPU.

An NPU is a specialized chip [designed for the matrix multiplication calculations](https://penntoday.upenn.edu/what-is-an-NPU-in-computing) that most AI models rely on. These matrix operations are highly parallelized, which is why [GPUs](https://spectrum.ieee.org/tag/gpus) (which were already better at highly parallelized tasks than CPUs) became the go-to option for AI data centers.

However, because NPUs are designed specifically to handle these matrix operations—and not other tasks, like 3D graphics—[they’re more power efficient than GPUs](https://www.ibm.com/think/topics/npu-vs-gpu). That’s important for accelerating AI on portable consumer technology. NPUs also tend to provide better support for low-precision arithmetic than laptop GPUs. AI models often use low-precision arithmetic to reduce computational and memory needs on portable hardware, such as laptops.

### Laptops Are Being Rebuilt to Run LLMs

Your laptop today is probably not equipped to run large language models. But future laptops might. Chasing the dream of locally run LLMs, laptop architects are rethinking many aspects of current designs, leading to changes that are only now starting to take hold.

iStockphoto

1. **Addition of NPUs.** Neural processing units (NPUs)—specialized accelerator chips that can run large language models (LLMs) and other AI models faster than CPUs and GPUs can—are being incorporated into laptops.

2. **Addition of more—and faster—memory.** The largest language models take up hundreds of gigabytes of memory. To host these models, and serve them quickly to the number-crunching processing units, laptops are increasing their memory capacity and speed.

3. **Consolidation of memory.** Most laptops today have a divided memory architecture, with a separate pool of memory to serve the GPUs. This made sense when the design first came out: GPUs needed faster memory access than could be supplied by the common bus. Now, to feed AI’s data appetite, laptop architects are rethinking this decision, and now they’re pooling memory together with faster [interconnects](https://spectrum.ieee.org/tag/interconnects).

4. **Combination of chips on the same silicon.** To help shorten the path to pooled memory, all the processing units—CPUs, GPUs, and NPUs—are now being integrated into the same silicon chip. This helps them connect to one another and to memory, but it will make maintenance more challenging.

5. **Power management.** AI models can see heavy use when they power always-on features like Microsoft’s Windows Recall, or the AI-powered Windows Search. Power-sipping NPUs help laptops run these models without excessive battery drain.

“With the NPU, the entire structure is really designed around the data type of tensors [a multidimensional array of numbers],” said [Steven Bathiche](https://www.microsoft.com/applied-sciences/people/steven-bathiche), technical fellow at [Microsoft](https://spectrum.ieee.org/tag/microsoft). “NPUs are much more specialized for that workload. And so we go from a CPU that can handle three [trillion] operations per second (TOPS), to an NPU” in [Qualcomm’s](https://www.qualcomm.com) [Snapdragon](https://spectrum.ieee.org/tag/snapdragon) X chip, which can power [Microsoft’s](https://www.microsoft.com/en-us/) [Copilot+](https://blogs.microsoft.com/blog/2024/05/20/introducing-copilot-pcs/) features. This includes [Windows Recall](https://support.microsoft.com/en-us/windows/retrace-your-steps-with-recall-aa03f8a0-a78b-4b3e-b0a1-2eb8ac48701c), which uses AI to create a searchable timeline of a user’s usage history by analyzing screenshots, and [Windows Photos’ Generative erase](https://blogs.windows.com/windows-insider/2024/02/22/windows-photos-gets-generative-erase-and-recent-ai-editing-features-now-available-on-arm64-devices-and-windows-10/), which can remove the background or specific objects from an image.

While [Qualcomm](https://qualcomm.com) was arguably the first to provide an NPU for Windows laptops, it kickstarted an NPU TOPS arms race that also includes [AMD](https://www.amd.com/en.html) and [Intel](https://www.intel.com/content/www/us/en/homepage.html), and the competition is already pushing NPU performance upward.

In 2023, prior to Qualcomm’s Snapdragon X, [AMD](https://spectrum.ieee.org/tag/amd) chips with NPUs were uncommon, and those that existed delivered about 10 TOPS. Today, AMD and [Intel](https://spectrum.ieee.org/tag/intel) have NPUs that are competitive with Snapdragon, [providing 40 to 50 TOPS](https://www.pcworld.com/article/2806864/intel-vs-amd-vs-qualcomm-which-copilot-pc-cpu-is-best-for-you.html).

[Dell’s upcoming Pro Max Plus AI PC](https://www.lifewire.com/dell-pro-max-plus-ai-laptop-11739880) will up the ante with a [Qualcomm](https://spectrum.ieee.org/tag/qualcomm) AI 100 NPU that promises up to 350 TOPS, improving performance by a staggering 35 times compared with that of the best available NPUs just a few years ago. Drawing that line up and to the right implies that NPUs capable of thousands of TOPS are just a couple of years away.

How many TOPS do you need to run state-of-the-art models with hundreds of millions of parameters? No one knows exactly. It’s not possible to run these models on today’s consumer hardware, so real-world tests just can’t be done. But it stands to reason that we’re within throwing distance of those capabilities. It’s also worth noting that LLMs are not the only use case for NPUs. [Vinesh Sukumar](https://www.qualcomm.com/news/onq/2024/05/from-olympic-table-tennis-to-ai-product-manager-meet-dr-vinesh-sukumar), Qualcomm’s head of AI and [machine learning](https://spectrum.ieee.org/tag/machine-learning) product management, says [AI image generation](https://spectrum.ieee.org/tag/ai-image-generation) and manipulation is an example of a task that’s difficult without an NPU or high-end GPU.

## Building balanced chips for better AI

Faster NPUs will handle more tokens per second, which in turn will deliver a faster, more fluid experience when using AI models. Yet there’s more to running AI on local hardware than throwing a bigger, better NPU at the problem.

[Mike Clark](https://ieeexplore.ieee.org/author/37089001134), corporate fellow design engineer at AMD, says that companies that design chips to accelerate AI on the PC can’t put all their bets on the NPU. That’s in part because AI isn’t a replacement for, but rather an addition to, the tasks a PC is expected to handle.

“We must be good at low latency, at handling smaller data types, at branching code—traditional workloads. We can’t give that up, but we still want to be good at AI,” says Clark. He also noted that “the CPU is used to prepare data” for AI workloads, which means an inadequate CPU could become a bottleneck.

NPUs must also compete or cooperate with GPUs. On the PC, that often means a high-end AMD or [Nvidia](https://spectrum.ieee.org/tag/nvidia) GPU with large amounts of built-in memory. The [Nvidia GeForce RTX 5090](https://signal65.com/research/ai/nvidia-geforce-rtx-5090-founders-edition-performance-analysis/)’s specifications quote an AI performance up to 3,352 TOPS, which leaves even the Qualcomm AI 100 in the dust.

That comes with a big caveat, however: power. Though extremely capable, the RTX 5090 is designed to draw up to [575 watts](https://signal65.com/research/ai/nvidia-geforce-rtx-5090-founders-edition-performance-analysis/) on its own. Mobile versions for laptops are more miserly but still draw up to [175 W](https://www.notebookcheck.net/Nvidia-GeForce-RTX-5090-Laptop-Benchmarks-and-Specs.934947.0.html), which can quickly drain a laptop battery.

[Simon Ng](https://www.linkedin.com/in/simonng39/?originalSubdomain=ca), client AI product manager at Intel, says the company is “seeing that the NPU will just do things much more efficiently at lower power.”[Rakesh Anigundi](https://www.linkedin.com/in/rakesh-s-anigundi/), AMD’s director of product management for Ryzen AI, agrees. He adds that [low-power](https://spectrum.ieee.org/tag/low-power) operation is particularly important because AI workloads tend to take longer to run than other demanding tasks, like encoding a video or rendering graphics. “You’ll want to be running this for a longer period of time, such as an AI personal assistant, which could be always active and listening for your command,” he says.

These competing priorities mean chip architects and system designers will need to make tough calls about how to allocate silicon and power in AI PCs, especially those that often rely on battery power, such as laptops.

“We have to be very deliberate in how we design our [system-on-a-chip](https://spectrum.ieee.org/tag/system-on-a-chip) to ensure that a larger [SoC](https://spectrum.ieee.org/tag/soc) can perform to our requirements in a thin and light form factor,” said[Mahesh Subramony](https://www.linkedin.com/in/mahesh-subramony-a0ba60/), senior fellow design engineer at AMD.

## When it comes to AI, memory matters

Squeezing an NPU alongside a CPU and GPU will improve the average PC’s performance in AI tasks, but it’s not the only revolutionary change AI will force on PC architecture. There’s another that’s perhaps even more fundamental: memory.

Most modern PCs have a divided memory architecture [rooted in decisions made over 25 years ago](https://www.electronicdesign.com/technologies/embedded/article/55300900/jon-peddie-research-what-came-before-pcie-the-evolution-of-pc-graphics-buses). Limitations in bus bandwidth led GPUs (and other add-in cards that might require high-bandwidth memory) to move away from accessing a PC’s system memory and instead rely on the GPU’s own dedicated memory. As a result, powerful PCs typically have two pools of memory, system memory and graphics memory, which operate independently.

That’s a problem for AI. Models require large amounts of memory, and the entire model must load into memory at once. The legacy PC architecture, which splits memory between the system and the GPU, is at odds with that requirement.

“When I have a discrete GPU, I have a separate memory subsystem hanging off it,” explained [Joe Macri,](https://www.linkedin.com/in/joseph-macri-9a288a55/) vice president and chief technology officer at AMD. “When I want to share data between our [CPU] and GPU, I’ve got to take the data out of my memory, slide it across the PCI Express bus, put it in the GPU memory, do my processing, then move it all back.” Macri said this increases power draw and leads to a sluggish [user experience](https://spectrum.ieee.org/tag/user-experience).

The solution is a unified memory architecture that provides all system resources access to the same pool of memory over a fast, interconnected memory bus. Apple’s in-house silicon is perhaps the most well-known recent example of a chip with a unified memory architecture. However, unified memory is otherwise rare in modern PCs.

AMD is following suit in the laptop space. The company announced a new line of APUs targeted at high-end laptops, [Ryzen AI Max](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-max-plus-395.html), at [CES](https://spectrum.ieee.org/tag/ces) ([Consumer Electronics](https://spectrum.ieee.org/topic/consumer-electronics/) Show) 2025.

Ryzen AI Max places the company’s Ryzen CPU cores on the same silicon as Radeon-branded GPU cores, plus an NPU rated at 50 TOPS, on a single piece of silicon with a unified memory architecture. Because of this, the CPU, GPU, and NPU can all access up to a maximum of [128 GB of system memory](https://www.amd.com/en/developer/resources/technical-articles/2025/amd-ryzen-ai-max-395--a-leap-forward-in-generative-ai-performanc.html), which is shared among all three. AMD believes this strategy is ideal for memory and performance management in consumer PCs. “By bringing it all under a single thermal head, the entire power envelope becomes something that we can manage,” said Subramony.

The Ryzen AI Max is already available in several laptops, including[the HP Zbook Ultra G1a](https://www.pcworld.com/article/2650073/hands-on-the-hp-zbook-ultra-g1a-smashes-the-work-laptop-paradigm.html) and the [Asus ROG Flow Z13](https://rog.asus.com/laptops/rog-flow/rog-flow-z13-2025/). It also powers the[Framework Desktop](https://frame.work/marketplace/desktops) and several mini desktops from less well-known brands, such as the [GMKtec EVO-X2 AI mini PC](https://www.gmktec.com/products/amd-ryzen%E2%84%A2-ai-max-395-evo-x2-ai-mini-pc?srsltid=AfmBOooME4uCrsnIh5mOf98eGHteIzsi-DAPl6E5xhNrTzG94qr3Tjf6).

Intel and Nvidia will also join this party, though in an unexpected way. In September, the former rivals announced an alliance to sell chips that pair Intel CPU cores with Nvidia GPU cores. While the details are still under wraps, the chip architecture will likely include unified memory and an Intel NPU.

Chips like these stand to drastically change PC architecture if they catch on. They’ll offer access to much larger pools of memory than before and integrate the CPU, GPU, and NPU into one piece of silicon that can be closely monitored and controlled. These factors should make it easier to shuffle an AI workload to the hardware best suited to execute it at a given moment.

Unfortunately, they’ll also make PC upgrades and repairs more difficult, as chips with a unified memory architecture typically bundle the CPU, GPU, NPU, and memory into a single, physically inseparable package on a PC mainboard. That’s in contrast with traditional PCs, where the CPU, GPU, and memory can be replaced individually.

## Microsoft’s bullish take on AI is rewriting Windows

MacOS is well regarded for its attractive, intuitive [user interface](https://spectrum.ieee.org/tag/user-interface), and Apple Silicon chips have a unified memory architecture that can prove useful for AI. However, Apple’s GPUs aren’t as capable as the best ones used in PCs, and its AI tools for developers are less widely adopted.

[Chrissie Cremers](https://www.linkedin.com/in/chrissiecremers/?originalSubdomain=nl), cofounder of the AI-focused marketing firm Aigency Amsterdam, told me earlier this year that although she prefers macOS, her agency doesn’t use Mac computers for AI work. “The GPU in my Mac desktop can hardly manage [our AI workflow], and it’s not an old computer,” she said. “I’d love for them to catch up here, because they used to be the creative tool.”

Dan Page

That leaves an opening for competitors to become the go-to choice for AI on the PC—and Microsoft knows it.

Microsoft launched [Copilot+ PCs](https://blogs.microsoft.com/blog/2024/05/20/introducing-copilot-pcs/) at the company’s 2024 Build developer conference. The launch had problems, most notably the [botched](https://www.theverge.com/2024/6/13/24178144/microsoft-windows-ai-recall-feature-delay) release of its key feature,[Windows Recall](https://spectrum.ieee.org/microsoft-copilot), which uses AI to help users search through anything they’ve seen or heard on their PC. Still, the launch was successful in pushing the PC industry toward NPUs, as AMD and Intel both introduced new laptop chips with upgraded NPUs in late 2024.

At Build 2025, Microsoft also revealed [Windows’ AI Foundry Local](https://devblogs.microsoft.com/foundry/foundry-local-a-new-era-of-edge-ai/), a “runtime stack” that includes a catalog of popular open-source [large language models](https://spectrum.ieee.org/tag/large-language-models). While Microsoft’s own models are available,[the catalog includes thousands of open-source models](https://azure.microsoft.com/en-us/products/ai-model-catalog#tabs-pill-bar-oc92d8_tab0) from [Alibaba](https://spectrum.ieee.org/tag/alibaba), DeepSeek, [Meta](https://spectrum.ieee.org/tag/meta), Mistral AI, Nvidia, [OpenAI](https://spectrum.ieee.org/tag/openai), Stability AI, xAI, and more.

Once a model is selected and implemented into an app, Windows executes AI tasks on local hardware through the Windows ML runtime, which automatically directs AI tasks to the CPU, GPU, or NPU hardware best suited for the job.

AI [Foundry](https://spectrum.ieee.org/tag/foundry) also provides APIs for local knowledge retrieval and low-rank adaptation (LoRA), advanced features that let developers customize the data an AI model can reference and how it responds. Microsoft also announced support for on-device semantic search and retrieval-augmented generation, features that help developers build AI tools that reference specific on-device information.

“[AI Foundry] is about being smart. It’s about using all the [processors](https://spectrum.ieee.org/tag/processors) at hand, being efficient, and prioritizing workloads across the CPU, the NPU, and so on. There’s a lot of opportunity and runway to improve,” said Bathiche.

### Toward AGI on PCs

The rapid evolution of AI-capable PC hardware represents more than just an incremental upgrade. It signals a coming shift in the PC industry that’s likely to wipe away the last vestiges of the PC architectures designed in the ’80s, ’90s, and early 2000s.

The combination of increasingly powerful NPUs, unified memory architectures, and sophisticated software-optimization techniques is closing the performance gap between local and cloud-based AI at a pace that has surprised even industry insiders, such as Bathiche.

It will also nudge chip designers toward ever-more-integrated chips that have a unified memory subsystem and to bring the CPU, GPU, and NPU onto a single piece of silicon—even in high-end laptops and desktops. AMD’s Subramony said the goal is to have users “carrying a mini workstation in your hand, whether it’s for AI workloads, or for high compute. You won’t have to go to the cloud.”

A change that massive won’t happen overnight. Still, it’s clear that many in the PC industry are committed to reinventing the computers we use every day in a way that optimizes for AI. Qualcomm’s Vinesh Sukumar even believes affordable consumer laptops, much like data centers, should aim for [AGI](https://spectrum.ieee.org/tag/agi).

“I want a complete [artificial general intelligence](https://spectrum.ieee.org/tag/artificial-general-intelligence) running on Qualcomm devices,” he said. “That’s what we’re trying to push for.”

From Your Site Articles

- [When AI Unplugs, All Bets Are Off ›](https://spectrum.ieee.org/personal-ai-assistant) - [Opera Includes AI Agents in Latest Web Browser ›](https://spectrum.ieee.org/agentic-ai-opera-mini)

Related Articles Around the Web

- [A Starter Guide for Playing with Your Own Local AI! : r/LocalLLaMA ›](https://www.reddit.com/r/LocalLLaMA/comments/16y95hk/a_starter_guide_for_playing_with_your_own_local_ai/) - [Why You Should Use Local Models. When building Gen AI ... ›](https://medium.com/@springrod/why-you-should-use-local-models-a3fce1124c94)

[large language models](https://spectrum.ieee.org/tag/large-language-models)[laptops](https://spectrum.ieee.org/tag/laptops)[amd](https://spectrum.ieee.org/tag/amd)[apple](https://spectrum.ieee.org/tag/apple)[microsoft](https://spectrum.ieee.org/tag/microsoft)

Matthew S. SmithMatthew S. Smith is a freelance consumer technology journalist with 17 years of experience and the former Lead Reviews Editor at Digital Trends. An IEEE Spectrum Contributing Editor, he covers consumer tech with a focus on display innovations, artificial intelligence, and augmented reality. A vintage computing enthusiast, Matthew covers retro computers and computer games on his YouTube channel, Computer Gaming Yesterday.

[Energy](https://spectrum.ieee.org/topic/energy/)[News](https://spectrum.ieee.org/type/news/)

## How to Spot a Counterfeit Lithium-Ion Battery

53m

5 min read

[AI](https://spectrum.ieee.org/topic/artificial-intelligence/)[Magazine](https://spectrum.ieee.org/magazine/)[Article](https://spectrum.ieee.org/type/article/)

## On Rereading Norbert Wiener’s The Human Use of Human Beings at 75

1h

1 min read

[The Institute](https://spectrum.ieee.org/topic/the-institute/)[IEEE Member News](https://spectrum.ieee.org/the-institute/collections/ieee-member-news/)[Article](https://spectrum.ieee.org/type/article/)[Spectrum Collections](https://spectrum.ieee.org/collections/)[Careers](https://spectrum.ieee.org/topic/careers/)[Tips on How to Elevate Your Career](https://spectrum.ieee.org/collections/tips-on-how-to-elevate-your-career/)

## Tips for How to Think Like an Entrepreneur

19h

2 min read
**Published:** 2025-11-19

### Result 9
**Title:** PRIMA.CPP: Speeding Up 70B-Scale LLM Inference on Low-Resource Everyday Home Clusters
**URL:** https://arxiv.org/abs/2504.08791?utm_source=valyu.ai&utm_medium=referral
**Source:** valyu/valyu-arxiv

**Content:**
# 1 Introduction

Current large language models (LLMs) are mostly cloud-based, but DeepSeek [DeepSeek-AI, 2025] changes this. Its R1 series, spanning from 1.5B to 70B, bring small models closer to frontier performance. Its 70B version even surpasses cloud-based models like GPT-4o and Claude 3.5 Sonnet. This has sparked interest in deploying LLMs locally on users' own devices, especially with the explosion of open-source LLMs. However, limited by weak chips and small RAM, user devices struggle to run anything beyond 10B, even with 4-bit quantization. For example, running Qwen 2.5-14B (Q4K) on a Mac M1 with 8 GiB RAM takes a staggering 10 seconds per token. As a result, most end-side LLM systems prefer smaller models, e.g., run 7B models on phones and browsers [MLC, 2023, Lugaresi et al., 2019] and 3.8B models on an Android device [Ghorbani, 2024].

That's not too bad, users have many devices, e.g., laptops, desktops, phones, and tablets. Some PCs have high-end GPUs like the NVIDIA 20/30/40 series, and Mac M-series have Apple Metal GPUs. By pooling the computing power and memory of home devices, it's possible to run larger models. In pipeline parallelism, the model is split into segments and assigned to devices. Exo [Exo, 2024] distributes model layers based on memory size, devices with more RAM/VRAM handle more layers. While this prevents OOM, it can slow speed if high-memory devices have weak CPUs/GPUs. This raises a question: *How should model layers be assigned?* A simple alternative is to assign model layers based on computing power, with stronger devices handling more layers, but also with high OOM risk. Ye et al. [2024] offers an idea: first, assign model layers based on computing power, then migrate layers from OOM devices to those with free memory. However, this also slows down inference, as weaker CPUs handle more layers.

So new questions arise: *Can stronger devices handle these overloaded layers instead?* If we require the cluster memory to meet the model's needs [Ye et al., 2024, Exo, 2024, Tadych, 2024, Zhang et al., 2025, Lee et al., 2024, Zhao et al., 2023, Zhang et al., 2024], the answer is no, as stronger devices have reached their OOM limits. But what if we relax this requirement? For example, we can free up processed layers on stronger devices and load the extra layers to continue computation. With a fast SSD, this could be more efficient than using weak-CPU devices. This adds complexity: *whose disks are faster than weak CPUs? And how many extra layers can be migrated to maximize inference speed?* This is tricky because disk I/O introduces a new bottleneck: disk loading latency, which depends on data size to be (re-)load and disk read speed. These two factors vary with hardware and OS differences. For example, macOS with Metal reclaims memory more aggressively than Linux, causing more reloads, while Linux optimizes sequential reads, making reloading faster than on macOS. This heterogeneity makes disk loading latency hard to estimate.

This paper introduces a device profiler to capture system heterogeneity across computation, memory, disk, communication, and OS. We mathematically model token latency from these factors and propose Halda, an efficient algorithm to solve this layer-to-device assignment (LDA) problem. Halda provides an optimal workload distribution across CPU and GPU (if available) for each device. It determines how many model layers each device should handle and how to allocate them between CPU and GPU. To hide disk loading, we design piped-ring parallelism, where devices form a ring and pass their results to the next for subsequent processing. Unlike existing systems, in our design, devices can complete a token with multiple rounds, and with prefetching, we overlap disk loading with other devices to hide latency. We call it *prima.cpp*, as it uses piped-ring parallelism and builts on llama.cpp [Gerganov, 2024]. The main contributions are summarized as follows:

- We propose prima.cpp, a distributed inference system designed for low-resource home clusters. It uses mmap to lazily load model weights, and piped-ring parallelism with prefetching to hide disk latency. It prevents OOM and reduces token latency.
- We model the LDA problem and develop a device profiler to capture the system heterogeneity. It minimizes token latency by modeling delays in computation, memory access, disk loading, and communication, while optimizing the use of RAM and VRAM.
- We propose the Halda algorithm to solve the LDA problem. Halda breaks the NP-hard problem into a set of simple ILPs, so we can find the optimal solution in polynomial time.
- We implement prima.cpp with 20K LoC modifications. Evaluation on a real home cluster shows that prima.cpp is 15× faster than llama.cpp on 70B models, with memory pressure below 6% per device. It also surpasses distributed alternatives like exo [Exo, 2024] and dllama [Tadych, 2024] in both speed and memory efficiency across all 7B-72B models.

In our experiments, a small, heterogeneous, and budget-friendly home cluster (2 laptops, 1 desktop, 1 phone) was used. Our prima.cpp achieves ∼600 milliseconds per token and a time-to-first-token (TTFT) below 2 seconds for a 70B model, making it accessible for voice chat apps like home Siri. For 45B-70B models, the speed matches those of audiobook apps. It now supports hot models including Llama 3, Qwen 2.5, QwQ, and DeepSeek R1 (distilled versions).
[]
**Published:** 2025-04-07

### Result 10
**Title:** The Complete Guide to Running LLMs Locally: Hardware, Software, and Performance Essentials
**URL:** https://www.ikangai.com/the-complete-guide-to-running-llms-locally-hardware-software-and-performance-essentials/?utm_source=valyu.ai&utm_medium=referral
**Source:** web

**Content:**
## Why Run LLMs Locally?

Before we dive into the mechanics, let's be clear about what you're gaining and what you're trading away.

Privacy and Data Control: Your prompts never leave your machine. This matters more than it sounds, especially for businesses handling sensitive documents, medical records, or proprietary code. No cloud logs. No terms-of-service concerns. No surprise data retention policies.

Cost and Autonomy: Once you've paid for your hardware, inference is free. You're not exposed to pricing changes. You won't wake up to find your favorite model deprecated in favor of a newer expensive version. You have complete control over what versions you run, how you modify them, and how you deploy them.

Latency: A round trip to a cloud API typically adds 200-500ms. Local inference eliminates that network overhead. For real-time applications or interactive chatbots, this difference is tangible.

Customization: You can fine-tune models on your own data. You can add retrieval-augmented generation (RAG) pipelines. You can integrate custom tools. You're not limited by what the API provider decided to expose.

The tradeoffs are hardware cost, power consumption, and the reality that you're now responsible for your own infrastructure. Cloud APIs remain superior for occasional use, extreme scale, or when you need frontier models that simply won't fit on consumer hardware. But for many workflows, local inference has crossed the threshold from experimental novelty to practical default.

## Understanding the Bottleneck: Memory Bandwidth Is Your Primary Performance Lever

When choosing hardware for running large language models locally, most people focus on processor speed or raw compute power. They shouldn't. Recent research makes it clear: for LLM inference, memory bandwidth—not compute power—is the primary performance limiter. Yet this remains poorly understood outside technical circles. Understanding why matters, because it completely changes how you should evaluate whether a machine is suitable for running LLMs.

### Why Memory Bandwidth Matters: The Arithmetic Intensity Problem

LLMs have a fundamental characteristic called low arithmetic intensity: they perform relatively few mathematical operations per byte of data fetched from memory. When your machine generates each token, it must retrieve billions of model weights from RAM while performing comparatively little computation. That data movement—not the raw computation—becomes the bottleneck.

A detailed 2025 NVIDIA Research paper, Efficient LLM Inference: Bandwidth, Compute, Synchronization, and Capacity Are All You Need, demonstrates that inference throughput scales primarily with memory bandwidth, since transformer decoding requires fetching billions of weights repeatedly, overwhelming data movement capacity rather than compute units. IBM's Mind the Memory Gap study (2025) found that even GPUs with vast unused computational headroom become bandwidth-saturated, leaving compute units idle during inference.

In practical terms: upgrading a machine's compute capacity often produces minimal speedup in token generation, but increasing memory bandwidth can produce dramatic improvements. Academic analysis quantifies this: increasing effective memory bandwidth from GDDR6 (~700 GB/s) to HBM3 (~3.5 TB/s) can nearly quadruple throughput for large models without changing compute power at all.

### The First Token vs. Subsequent Tokens Distinction

There's an important technical distinction worth understanding: the first token (when processing your prompt) can be somewhat compute-bound, since you're computing across the entire input sequence at once. But every subsequent token during generation is almost entirely memory-bound—because you're reusing the same model weights repeatedly while adding just one new token.

Databricks (2025) and Hathora (2025) research confirms this dynamic clearly: the first token is compute-bound, but all subsequent tokens are memory-bound. This means for interactive use—where you care most about token generation speed—bandwidth is nearly everything.

### Real-World Example: Why an M3 Max Outperforms a Newer M4 Pro for LLMs

This principle plays out in the real world in ways that might surprise you. Consider Apple's laptop lineup: an older M3 Max with 48GB of unified memory (400 GB/s bandwidth) will actually run LLMs faster during token generation than a newer M4 Pro, despite the M4 Pro being a newer, more powerful chip overall.

Why? The M3 Max's substantially higher memory bandwidth (400 GB/s vs. the M4 Pro's significantly lower bandwidth) means it moves model weights from memory to compute units far more efficiently. For LLM inference specifically, that bandwidth advantage overwhelms any generational compute improvements the M4 Pro brings. A two-year-old Max can outpace a current-generation Pro.

This scenario repeats across hardware ecosystems: higher-bandwidth systems consistently deliver better LLM inference performance than higher-compute alternatives, even when those alternatives are newer or more expensive.

### The Balanced Perspective: What This Means for Your Hardware Choices

So, while calling LLM performance "entirely determined" by memory bandwidth oversimplifies things slightly, the evidence is overwhelming: - Inference (token generation) ≈ strongly bandwidth-bound. - Training or first-token processing ≈ partially compute-bound. - Real-world performance ≈ min(memory bandwidth, compute throughput × arithmetic intensity).

For anyone running LLMs locally, here's what matters: When evaluating whether a machine is suitable for LLM workloads, prioritize memory bandwidth as your primary decision criterion. Memory capacity is important—you need enough to hold your model—but how fast your system can move that memory is what determines whether it runs smoothly or struggles. This is why machines with high-bandwidth memory systems outperform high-compute alternatives for LLM inference. It's also why many people are surprised to discover their "underpowered" older machine handles LLMs better than a newer system: they likely never checked the bandwidth specs.

## Hardware: Finding Your Sweet Spot

Let's be concrete about what you can actually run on different hardware configurations. The landscape in 2025 is broader than ever, with options ranging from sub-$250 entry-level cards to workstation-class accelerators.

Performance Methodology Note: The token-per-second (t/s) figures below represent ballpark estimates based on internal testing and third-party benchmarks. Actual throughput depends significantly on model, quantization format, context length, scheduler, batch size, and thermal state. Figures assume single-stream inference on Q4_K_M or equivalent quantization at typical batch sizes (1–8). For accurate performance modeling, test on your specific hardware with your actual workload.

### The Entry Level: Under $500

Intel Arc B580 ($249): The newest surprise entry. Intel's Arc GPUs have been gradually maturing, and the B580 offers genuinely impressive price-to-performance for small models. Twelve gigabytes of VRAM, reasonable bandwidth for the price point, and native oneAPI support. You're limited to 7B models, but if you're experimenting or prototyping, this is the most affordable path to local inference. The main caveat: software support is still developing, and community resources are thinner than NVIDIA's ecosystem.

NVIDIA RTX 4060 Ti ($499 new): A more conservative entry into NVIDIA's lineup. Sixteen gigabytes of VRAM, proper CUDA support, and mature tooling. You can comfortably run 7B–13B models, and squeeze into 30B territory with quantization. For a developer who wants guaranteed compatibility, this is a reasonable starting point. Performance lands in the 8-15 tokens per second range depending on the model.

### Budget-Conscious: $700–1500

Used RTX 3090 ($700-900): This is the king of value for serious work. On the used market, you can find RTX 3090s for $700-900—roughly one-third the original MSRP. It has 24GB of GDDR6X memory with around 935 GB/s of bandwidth, which is still competitive for inference despite being Ampere architecture (2020). You can run 30B models comfortably, even touch 70B with aggressive quantization. Real-world measurements show consistent 25-35 tokens per second on mid-range models. The catch: you're buying used hardware without warranty, and availability fluctuates. But the value proposition—performance per dollar—remains nearly impossible to beat. Many researchers still build multi-card rigs around used 3090s.

NVIDIA RTX 4070 Ti Super ($1000-1200 new): If you want a new card with warranty, this bridges the gap between entry and performance. Sixteen gigabytes of VRAM limits you to 7B–13B models comfortably, with 30B models requiring reduced context windows. Memory bandwidth is more constrained than the 3090, but it's still adequate for interactive use. You'll see 15-25 tokens per second depending on the model. It's also a capable gaming card, which matters if your GPU needs to do double duty.

CPU-Only Machines: If you have no GPU at all, don't despair. Modern CPUs with good VRAM (DDR5) can run small quantized models. A 7B model in 4-bit quantization fits in 4-5GB and delivers 2-5 tokens per second—enough for batch processing or non-interactive work. It's free to experiment with, but not practical for interactive chatbot use.

### The Practical Optimum: $1500–2500

NVIDIA RTX 4090 ($1600–2000 new): For several years, this was the unambiguous consumer choice for serious local work. Twenty-four gigabytes of GDDR6X with 1,010 GB/s of bandwidth and rock-solid CUDA support. It handles 30-32B models beautifully with full context windows. For 70B models, you'll need aggressive quantization (INT4 or lower). Real-world benchmarks consistently show 40-50 tokens per second. Power consumption runs around 450W peak. This card remains formidable, though its market position has shifted with newer alternatives.

NVIDIA RTX 5090 ($1999 new): NVIDIA's newest flagship, released in January 2025, represents a genuine leap forward. Thirty-two gigabytes of GDDR7 memory with ~1,792 GB/s of bandwidth—a 77% improvement over the 4090. On comparable mid-size models (30B and smaller in Q4), ballpark estimates suggest 60–70 tokens per second (vs. 40–50 on the 4090). Important caveat: 70B models in standard Q4_K_M quantization (~42–43 GB files) do not fit entirely on 32GB VRAM; you'll need aggressive 3-bit quantization, IQ-class compression, or CPU offload for full 70B models. For 30B–32B models with full context, the 5090 is exceptional. Higher power consumption (575W peak) than the 4090, but the bandwidth advantage justifies the premium for long-term purchases in 2025.

AMD Radeon RX 7900 XTX ($1200–1500): The AMD alternative with 24GB of VRAM and 960 GB/s bandwidth looks promising on paper. Performance is roughly comparable to the RTX 3090. The significant problem: software maturity. ROCm (AMD's CUDA equivalent) lags NVIDIA's ecosystem considerably. Framework support is inconsistent. On Windows, ROCm support is essentially nonexistent. Even on Linux, you'll face manual configuration and occasional incompatibilities. For Linux enthusiasts comfortable with troubleshooting, it can work. For everyone else, NVIDIA remains the safer choice.

### Apple Silicon: The Unified Memory Alternative

Apple's unified memory architecture deserves serious consideration for local LLMs, particularly because memory bandwidth and capacity directly translate to performance—exactly what LLM inference demands. Unlike discrete GPUs where you move data from system RAM to VRAM, Apple's unified architecture means the GPU, CPU, and neural engine all access the same pool of memory at full bandwidth. This architectural elegance has real performance implications for inference workloads.

MacBook Air M3 ($1,099–$1,499): Entry point for local LLM experimentation. Eight to 24GB unified memory. Realistically supports 7B models comfortably, running around 10–15 tokens per second on quantized models. Thermals are tight under sustained load, but for casual use or prototyping, it works. Best for: students and hobbyists exploring local inference without GPU investment.

MacBook Pro M3 Pro ($1,999–$2,599): The sweet spot for portable LLM development. Eighteen to 36GB unified memory. Handles 13B models smoothly at 15–22 tokens per second. Battery life remains reasonable even under load. This is where you can build practical local AI applications—RAG pipelines, small agents, prompt experimentation—without being desk-bound. Best for: developers who need portability and prefer not to maintain separate GPU hardware.

MacBook Pro M4 Max (2025, $3,999–$5,300): NVIDIA's launch timing actually highlights what Apple's doing well. Thirty-six to 128GB unified memory. Runs 33B–70B quantized models at 30–45 tokens per second using the optimized MLX backend. This is legitimate desktop-class performance in a laptop. The M4 Max brings significantly better thermal headroom than the M3 Pro while maintaining battery life. Best for: professional AI developers who travel or prefer a single powerful machine for all work.

Mac Studio M3 Ultra ($4,999–$8,999, 192–512GB): When you need to run multiple models simultaneously or work with truly large models. Eight hundred gigabytes per second of unified memory bandwidth—a figure that rivals high-end enterprise GPUs. Can handle 70B unquantized models or experimental 600B+ models in 4-bit quantization for research purposes. The performance ceiling is higher than anything consumer-grade except the newest NVIDIA enterprise cards, but the power efficiency is extraordinary. Best for: organizations, research groups, or power users running multi-LLM deployments or fine-tuning pipelines.

Software Matters: Unlike Windows with competing frameworks, the Mac ecosystem has converged on excellent tools. MLX (Apple's framework) and Ollama both efficiently exploit unified memory, allowing you to load quantized weights directly into RAM with minimal overhead. This is where Apple's architecture shines—the lack of discrete VRAM means no copying penalty between system and GPU memory.

The Honest Assessment: Mac performance trails high-end discrete NVIDIA by roughly 20–30% on raw tokens per second when comparing models of similar size. An RTX 5090 beats the M3 Ultra in absolute throughput. But the total cost of ownership—price, power consumption, noise, space, system integration—shifts the calculation significantly. A Mac Studio M4 Max with 128GB at $4,500 competes directly with a $2,000 RTX 5090 when you factor in the entire system cost. And if you're already in the Apple ecosystem for other work, the integration is seamless. Best for: developers and organizations already committed to macOS, researchers prioritizing efficiency and quiet operation, or anyone who values not maintaining separate hardware ecosystems.

### NVIDIA DGX Spark: The New Contender ($2,999–$3,999)

Released in October 2025, the NVIDIA DGX Spark represents something new: NVIDIA's answer to unified-memory inference workstations. It combines a Grace Blackwell GPU (128GB unified LPDDR5X memory at 273 GB/s bandwidth) with 20-core Grace ARM CPU cores in a single, quiet, 240W system.

Here's where the DGX Spark becomes a crucial case study for understanding LLM performance limitations: it perfectly demonstrates the prefill vs. decode bandwidth bottleneck in real-world benchmarks.

The Performance Story:

On prefill (prompt processing)—which is compute-heavy—the Spark is exceptional. Processing large prompts through a 120B model shows measured throughput around 1,700 tokens/sec in internal and third-party benchmarks. That's roughly 3× faster than three RTX 3090s in the same workload. For batched inference or applications that process large documents before generation, this is compelling.

But on decode (token generation)—which is memory-bound—the Spark hits a wall: ballpark estimates place it around 30–40 tokens per second on large models, compared to 100+ t/s from a well-tuned multi-GPU 3090 rig. Suddenly, the Spark's massive compute advantage evaporates.

Why? Memory bandwidth. The Spark's 273 GB/s bandwidth is respectable but insufficient for token generation at scale. The GPU has *more than enough compute power* to generate tokens faster, but it's starved for data. The decode phase is waiting for weights to stream from memory, not waiting for compute.

This is not a flaw—it's proof of our core thesis. The DGX Spark has approximately 80 TFLOPS of FP32 compute, roughly 3× what Apple's M3 Ultra provides. Yet decode performance barely improves over the M3 Ultra (which achieves 12–15 t/s on 70B models) because both systems are bandwidth-bound. You can't overcome a bandwidth bottleneck with more compute.

When the DGX Spark Makes Sense:

- Fine-tuning and training: The Spark finetunes Llama 8B LoRA at >53,000 tokens per second—exceptional for a desktop system. If you're doing active model development, not just inference, this is compelling. - Handling truly large models: With 128GB unified memory, you can work with models up to 200B parameters in FP4 quantization, something most consumer hardware cannot do. - Prefill-heavy workloads: Applications that process large documents, code, or context before generation benefit significantly. - Quiet, efficient operation: At 240W and an efficient thermal design, the Spark is quiet and power-efficient compared to multi-GPU rigs.

The Honest Comparison:

For pure token generation speed on mid-size quantized models, the RTX 5090 materially outpaces the DGX Spark. With ~1,792 GB/s bandwidth vs. the Spark's 273 GB/s, the 5090 scales token generation efficiency much better. Real-world throughput depends heavily on model size, quantization, and batch size, but the bandwidth gap is the fundamental limiting factor. Spark's appeal lies in model capacity (128GB) and prefill throughput, not decode speed.

Conversely, if you're bandwidth-saturated on a single Spark and need higher decode throughput, adding more units helps: bandwidth scales linearly with GPU count (though coordination overhead applies). Two networked Sparks or a multi-Spark cluster can reportedly achieve proportionally higher aggregate throughput, although this is something that we haven't seen in real world testing.

Bottom line: The DGX Spark is not for maximum token throughput. It's for organizations that need model capacity (128GB unified memory), don't want to manage multi-GPU complexity, and care about power efficiency. It's also the clearest evidence that once you're bandwidth-bound, more compute is just wasteful.

### Workstation and Enterprise Grade: $4,000+

NVIDIA RTX A6000 ($4,000–5,000): Enterprise-class card with 48GB of VRAM. Handles up to 70B quantized models smoothly. CUDA-optimized and reliable. Overkill for most hobbyists, but standard for organizations running production local inference.

NVIDIA H100 (80 GB, $25,000–40,000): The data-center gold standard. Eighty gigabytes of VRAM, HBM3 memory with exceptional bandwidth, and NVLink support for multi-GPU scaling. Can handle 175B+ models. Only relevant for organizations serving inference to many concurrent users, not local experimentation.

### Cost-Effectiveness: When Does Local Make Sense?

The ROI calculation depends on your usage. Local LLM operations achieve cloud cost parity within 6–12 months for anyone spending $500/month or more on API access. Electricity and cooling add roughly $50–200 monthly depending on location. This means:

- For $1000 spent on hardware (e.g., used RTX 3090), you reach parity with cloud APIs in approximately 6 months at moderate usage levels ($500/month API spend). - Across a 3-5 year hardware lifespan, local deployment can save $10,000–50,000 compared to continuous cloud API usage for heavy users. - For small teams, a single RTX 5090 ($2000) can handle what would cost $30,000+ annually in cloud API spending.

The key insight: bandwidth remains the limiting factor across all price tiers. Even enterprise hardware like H100s becomes bandwidth-saturated during inference. This is why the RTX 5090 competes with the much pricier H100 on pure inference throughput—the newer architecture and superior memory bandwidth matter more than raw compute capacity.

### Portable & Ultra-Compact: The AMD Ryzen AI Max+ 395 Category

There's a newer class of systems worth mentioning: portable mini-PCs and laptops built around AMD's Ryzen AI Max+ 395 (Strix Halo architecture). These are genuinely interesting for a specific use case—developers and researchers who need local LLM capability without being tethered to a desk.

What makes them compelling: The Ryzen AI Max+ 395 integrates a high-performance Zen 5 CPU, Radeon 8060S GPU, and a dedicated XDNA 2 NPU—all in a power-efficient package. More importantly for LLMs, these systems support up to 128GB of LPDDR5X unified memory with over 300 GB/s bandwidth. That bandwidth is respectably close to where you'd see discrete NVIDIA cards, and it's enough to run 7B–13B models smoothly.

Mini-PC examples: Devices like the Beelink GTR9 Pro (~$1,399), AOOSTAR NEX395 (~$1,699–$2,099), and PELADN YO1 ($2,000) offer the full desktop-class experience in a compact form factor. You get dual Ethernet, USB4, proper cooling—everything you'd expect from a mini-PC. These compete directly with the RTX 5090 approach on price and portability, though with slightly lower absolute performance.

Laptop options: If you need actual portability, ASUS ROG Flow Z13 (2025) ($2,499–$3,499) and HP ZBook Ultra G1 ($3,200–$8,000) bring workstation-class capability to 13–16 inch form factors. The ROG Flow is particularly interesting for mobile AI development—it's a convertible tablet with serious compute behind it.

The tradeoff: These systems excel at efficiency and portability but fall slightly short of discrete GPU peak performance. An RTX 5090 will edge them out on raw tokens-per-second, but the 395-based systems integrate NPU support, better thermal characteristics, and the entire system is purpose-built for AI workloads. They're also quieter and consume less power than a desktop GPU rig.

Best for: Developers who travel, researchers prototyping models on the move, or organizations deploying local LLMs across multiple compact workstations without datacenter infrastructure. If you value quiet operation, low power consumption, and portability, these represent a genuine alternative to traditional GPUs.

## Key Metrics: What to Look For

When evaluating hardware, focus on three numbers:

VRAM (Video RAM): Directly determines the largest model you can run. The common rule of thumb ("1/8th of parameters") is dangerously wrong. Here's the reality:

- FP32 precision: 1 byte per parameter. A 30B model = 120 GB just for weights (before KV cache). - FP16/BF16: 2 bytes/param → 60 GB for 30B. - Q8 (8-bit quant): ~1 byte/param → 30 GB for 30B. - Q4 (4-bit quant): ~0.5 bytes/param + metadata → 15–18 GB for 30B; typical Q4_K_M files are 10–15% smaller.

For a 70B model in Q4: expect 35–43 GB (typical Q4_K_M files run ~42–43 GB, which does not fit on a 32GB RTX 5090 without aggressive 3-bit quantization or offload). KV cache adds 5–25 GB depending on context length and batch size—longer prompts and larger batches mean more memory overhead.

Memory Bandwidth: Measured in GB/s. This is your primary performance lever. For interactive use, aim for at least 300 GB/s. The RTX 3090 (~936 GB/s) and 4090 (~1,008 GB/s) both exceed this significantly; the RTX 5090 pushes ~1,792 GB/s. Newer integrated systems like the M4 Max achieve >0.5 TB/s through unified memory, demonstrating that bandwidth matters as much as VRAM capacity.

Power Consumption: Particularly relevant if you're running 24/7. A 450W GPU running continuously costs roughly $500–750 annually in electricity (depending on local rates). Factor this into total cost of ownership over 3–5 years.

## The Software Stack: Tools for Running Local LLMs

The ecosystem has matured dramatically. You have choices, and they're all genuinely good.

### llama.cpp: The Foundation

At the bedrock of nearly everything is llama.cpp, a plain C/C++ implementation of LLaMA inference created by Georgi Gerganov. It's the engine that powers most of what you'll use. Its key innovation was demonstrating that LLMs could run efficiently on consumer CPUs and GPUs through intelligent quantization and layer offloading.

Unless you're specifically interested in low-level optimization or fine-grained control, you won't interact with llama.cpp directly. But understand that when you use Ollama or LM Studio, they're building on top of llama.cpp's inference engine. It's the reliable, battle-tested foundation that made local inference practical.

### Ollama: The Developer-Friendly Tool

Ollama (ollama.com) is arguably the most important tool in the modern local LLM ecosystem.
**Published:** 2025-10-26
