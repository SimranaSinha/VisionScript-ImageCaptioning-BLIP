# Generative Project: VisionScript-ImageCaptioning - BLIP

---
### 🗃️ Drive 
https://drive.google.com/drive/folders/1J0A9taJg-t7_dRZdi8k8j4CDILQ9oZwl?usp=sharing

---

## Milestone 1 : Style-Conditioned Image Captioning (CLIP + GPT-2)

### 📌 Overview

Milestone 1 focuses on building the baseline pipeline for a style-conditioned image captioning system. The system uses CLIP to extract image embeddings and GPT-2 to generate captions in different styles using prompt prefixes.

This milestone establishes the baseline caption generation before embedding injection and fine-tuning in later milestones.

### 🎯 Milestone 1 Tasks

* Flickr30k dataset selection and preprocessing
* Caption filtering and dataset subset creation
* CLIP embedding extraction
* GPT-2 caption generation baseline
* Style prompt conditioning
* Baseline caption test runs
* Repository setup and documentation

### 🧠 Model Pipeline

**Image → CLIP Encoder → Style Prompt → GPT-2 → Generated Caption**

**Models Used:**

* CLIP ViT-B/32 (Image Encoder)
* GPT-2 Base (Language Model)

**Styles Implemented:**

* Art Critic
* Casual Visitor
* Children’s Guide

### 📊 Milestone 1 Results

* Baseline captions generated successfully
* Style prompts changed tone of captions
* Captions were fluent but not image-grounded
* CLIP embeddings extracted but not injected yet
* Embedding injection will be implemented in Milestone 2


## 📁 Files Included

```
🗂️ Milestone 1/
│
├── 📄 Baseline_code.ipynb
│
├── 📄 Project_Proposal.pdf
│
├── 📘 README.md
```

---

## Milestone 2 : CLIP Embedding Injection into GPT-2

### 📌 Overview

Milestone 2 focuses on integrating CLIP image embeddings directly into the GPT-2 caption generation process. Instead of only using style prompts, this milestone injects visual embeddings into the language model to improve image grounding and caption relevance.

This milestone transitions the project from prompt-based captioning to embedding-conditioned caption generation.

### 🎯 Milestone 2 Tasks

* CLIP embedding extraction for images
* Embedding projection layer implementation
* Injection of CLIP embeddings into GPT-2 input embeddings
* Modified caption generation pipeline
* Comparison with baseline captions from Milestone 1
* Evaluation of caption relevance and grounding
* Documentation and result analysis

### 🧠 Model Pipeline

**Image → CLIP Encoder → Embedding Projection → GPT-2 → Generated Caption**

**Models Used:**

* CLIP ViT-B/32 (Image Encoder)
* GPT-2 Base (Language Model)
* Projection Layer (Embedding Alignment)

### 📊 Milestone 2 Results

* Captions became more image-relevant
* Reduced generic caption generation
* Visual grounding improved compared to Milestone 1
* Style prompts still influence caption tone
* Embedding injection successfully implemented
* Model ready for fine-tuning and evaluation in Milestone 3

### 📁 Files Included

```
🗂️ Milestone 2/
│
├── 📄 Milestone_2_Pri_2.ipynb      – CLIP + GPT-2 caption generation notebook
│
├── 📄 Milestone_2_Group_5.pdf      – Milestone report
│
├── 🎞️ demo_Test_1_(1).png          – Caption output example
│
├── 🎞️ demo_Test_4.png              – Caption output example
│
├── 🎞️ demo_test3.png               – Caption output example
│
├── 🎞️ training_loss_v2.png         – Training loss plot
│
└── 📘 README.md                    – Documentation
```

---

## Milestone 3 : Fine-Tuning and Style Comparison

### 📌 Overview

Milestone 3 focuses on fine-tuning the caption generation pipeline and analyzing how different styles affect caption generation. This milestone evaluates the final system by comparing captions generated in multiple styles and analyzing model performance and caption quality.

This milestone represents the final system evaluation and comparison stage of the project.

### 🎯 Milestone 3 Tasks

* Fine-tuning GPT-2 with image-conditioned captions
* Style-conditioned caption generation experiments
* Parameter tuning and caption comparison
* Caption quality evaluation
* Style comparison analysis
* Result visualization and documentation
* Final pipeline testing

### 🧠 Model Pipeline

**Image → CLIP Encoder → Embedding Injection → Fine-Tuned GPT-2 → Styled Caption**

**Styles Evaluated:**

* Art Critic
* Casual Visitor
* Children’s Guide

### 📊 Milestone 3 Results

* Fine-tuned model produced more descriptive captions
* Style differences clearly visible in generated captions
* Art Critic captions were formal and technical
* Casual Visitor captions were conversational
* Children’s Guide captions were simple and playful
* Final system successfully generates style-conditioned captions

### 📁 Files Included

```
🗂️ Milestone 3
│
├── 📑 Results/
│   │
│   ├── 🎞️ Test_1_comparison.png
│   │
│   ├── 🎞️ Test_2_comparison.png
│   │
│   ├── 🎞️ Test_3_comparison.png
│   │
│   └── 🎞️ Test_4_comparison.png
│
├── 📄 Milestone3_Prj2.ipynb
│
└── 📘 README.md
```

---

