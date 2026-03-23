# 🎨 MuseumCaption – Milestone 1

## Style-Conditioned Image Captioning using CLIP + GPT-2

## 📌 Overview

Milestone 1 focuses on building the baseline pipeline for a style-conditioned image captioning system. The system generates captions for images in different styles using a CLIP image encoder and GPT-2 language model.

In this milestone, captions are generated using **prompt-based style conditioning only**. CLIP embeddings are extracted but not yet injected into GPT-2. This milestone establishes the baseline for later improvements.

---

## 🎯 Objective

The goal of this project is to generate image captions in different styles for the same image.

The three caption styles used in this project:

* 🖼️ Art Critic
* 🙂 Casual Visitor
* 🧒 Children’s Guide

Milestone 1 focuses on:

* Dataset preparation
* CLIP embedding extraction
* GPT-2 caption generation
* Style prompt conditioning
* Baseline caption generation

---

## 🗂️ Dataset

**Dataset Used:** Flickr30k
**Source:** HuggingFace dataset

### Dataset Processing

* Selected ~1000 image–caption pairs
* Removed captions with fewer than 5 words
* Images converted to RGB format
* Dataset cached for faster loading
* Images processed using PIL
* CLIP embeddings extracted and stored

---

## 🧠 Model Pipeline

The baseline captioning pipeline:

**Image → CLIP Encoder → Style Prompt → GPT-2 → Generated Caption**

### Components

| Component      | Model            |
| -------------- | ---------------- |
| Image Encoder  | CLIP ViT-B/32    |
| Language Model | GPT-2 Base       |
| Style Control  | Prompt Prefix    |
| Decoding       | Nucleus Sampling |

---

## ✍️ Style Prompt Prefixes

| Style            | Prompt                                             |
| ---------------- | -------------------------------------------------- |
| Art Critic       | "An art critic observes this painting:"            |
| Casual Visitor   | "A museum visitor says about this painting:"       |
| Children’s Guide | "A tour guide explains this painting to children:" |

---

## ⚙️ Caption Generation Parameters

* Top-p = 0.92
* Temperature = 0.85
* Repetition penalty = 1.2
* Max tokens = 60

---

## 📊 Results – Milestone 1

Baseline captions were generated successfully using GPT-2 with style prompts.

### 🔍 Observations

* GPT-2 generates fluent captions
* Style prompts successfully change caption tone
* Captions are not image-grounded yet
* CLIP embeddings extracted but not injected into GPT-2
* Embedding injection will be implemented in Milestone 2

---

## 📁 Repository Structure

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

## ✅ Milestone 1 Summary

Milestone 1 completed:

* Dataset selection and preprocessing
* Flickr30k subset creation
* CLIP embedding extraction
* GPT-2 caption generation baseline
* Style prompt conditioning
* Baseline caption test runs
* Repository setup and documentation



