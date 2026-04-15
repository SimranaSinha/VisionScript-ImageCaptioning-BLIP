# Generative Project: VisionScript-ImageCaptioning - BLIP

---
### 🗃️ Drive 
https://drive.google.com/drive/folders/1J0A9taJg-t7_dRZdi8k8j4CDILQ9oZwl?usp=sharing

### 🔗 Live Link
https://huggingface.co/spaces/Simi2407/VisionScript

---

## Milestone 1 : Automatic Image Captioning Baseline (BLIP + CLIP)
### 📌 Overview
Milestone 1 focuses on building the baseline pipeline for automatic image captioning using BLIP. The system uses CLIP to extract image embeddings and BLIP to generate a single, fluent natural-language caption per image.
This milestone establishes the baseline caption generation before fine-tuning in later milestones.

### 🎯 Milestone 1 Tasks
- Flickr30k dataset selection and preprocessing
- Caption filtering and dataset subset creation (1k pairs)
- CLIP embedding extraction (512-dim, L2-normalized)
- GPT-2 tokenizer setup for caption analysis
- BLIP baseline caption generation (unconditional)
- 5 sample image:caption test runs
- Repository setup and documentation

### 🧠 Model Pipeline
**Image → CLIP Encoder → 512-dim Embedding**
**Image → BLIP Processor → BLIP Decoder → Generated Caption**

**Models Used:**
- CLIP ViT-B/32 (Image Encoder)
- BLIP blip-image-captioning-base (Caption Generation)
- GPT-2 Tokenizer (Caption Preprocessing Only)

### 📊 Milestone 1 Results
- Baseline captions generated successfully using BLIP
- Captions are fluent and image-grounded out of the box
- CLIP embeddings extracted and cached (512-dim)
- GPT-2 tokenizer used to analyze caption length distribution
- Fine-tuning on Flickr30k will be implemented in Milestone 2

## 📁 Files Included

```
🗂️ Milestone 1/
│
├── 📄 Milestone_1_Prj2.ipynb
│
├── 📄 Project_Proposal.pdf
│
├── 🖼️ baseline_captions.png
│
└── 📘 README.md                    
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

### 📊 Milestone 3 Results

* Fine-tuned model produced more descriptive captions
* Style differences clearly visible in generated captions (single/paragraph)
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

## Milestone 4 : Multi-Mode Captioning and Visual Question Answering

### 📌 Overview

Milestone 4 extends the image captioning system by introducing **multi-mode caption generation** and **visual question answering (VQA)** using the BLIP model. This milestone enhances the system’s ability to generate both concise and detailed captions, while also enabling interactive question-based understanding of images.

This milestone represents the transition from static caption generation to a more flexible and interactive vision-language system.

### 🎯 Milestone 4 Tasks
* Implementation of BLIP-based caption generation
* Multi-mode captioning (Single + Paragraph)
* Visual Question Answering (VQA) integration
* Caption comparison across modes
* Qualitative evaluation of generated outputs
* Result visualization and documentation
* Final system testing and validation


### 🧠 Model Pipeline
**Image → BLIP Encoder-Decoder → Caption / Answer Generation**

**Modes Implemented:**
* Single Caption (Concise Output)
* Paragraph Caption (Detailed Output)
* Visual Question Answering (Q&A Output)

### 📊 Milestone 4 Results

* Paragraph mode generated richer and more descriptive captions
* Single mode produced short and efficient summaries
* VQA successfully answered context-based questions from images
* Model demonstrated strong understanding of objects, scenes, and spatial relationships
* System supports flexible output formats for different use cases
* Final system successfully integrates captioning and reasoning capabilities


### 📁 Files Included

```
🗂️ Milestone 4
│
├── 📑 Results/
│   │
│   ├── 🖼️ VisionScript_paragraph_20260409_160452.png   # Lion – Paragraph
│   │
│   ├── 🖼️ VisionScript_paragraph_20260410_003347.png   # Group Scene – Paragraph
│   │
│   ├── 🖼️ VisionScript_paragraph_20260410_003722.png   # Sand Dune – Paragraph
│   │
│   ├── 🖼️ VisionScript_single_20260409_160448.png      # Lion – Single Caption
│   │
│   └── 🖼️ VisionScript_vqa_20260410_003730.png         # VQA Output
│
├── 📄 Final_Prj2.ipynb
│
├── 📄 Final_Prj2NNDL.ipynb
│
└── 📘 README.md
```

---

