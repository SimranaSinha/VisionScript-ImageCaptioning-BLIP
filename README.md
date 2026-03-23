# Generative Project: Museum Canvas Caption - CLIP - GPT2

---

## 🎨 MuseumCaption – Milestone 1 : Style-Conditioned Image Captioning (CLIP + GPT-2)

### 📌 Overview

Milestone 1 focuses on building the baseline pipeline for a style-conditioned image captioning system. The system uses CLIP to extract image embeddings and GPT-2 to generate captions in different styles using prompt prefixes.

This milestone establishes the baseline caption generation before embedding injection and fine-tuning in later milestones.

---

### 🎯 Milestone 1 Tasks

* Flickr30k dataset selection and preprocessing
* Caption filtering and dataset subset creation
* CLIP embedding extraction
* GPT-2 caption generation baseline
* Style prompt conditioning
* Baseline caption test runs
* Repository setup and documentation

---

### 🧠 Model Pipeline

**Image → CLIP Encoder → Style Prompt → GPT-2 → Generated Caption**

**Models Used:**

* CLIP ViT-B/32 (Image Encoder)
* GPT-2 Base (Language Model)

**Styles Implemented:**

* Art Critic
* Casual Visitor
* Children’s Guide

---

### 📊 Milestone 1 Results

* Baseline captions generated successfully
* Style prompts changed tone of captions
* Captions were fluent but not image-grounded
* CLIP embeddings extracted but not injected yet
* Embedding injection will be implemented in Milestone 2

---

## 📁 Files Included

```
Milestone 1/
│
├── Baseline_code.ipynb
├── Project_Proposal.pdf
├── README.md
```

---


If you keep all milestones like this, your repo will look very clean and structured.
