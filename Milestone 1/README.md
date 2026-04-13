# 🖼️ VisionScript – Milestone 1
## Automatic Image Captioning using BLIP

---

## 📌 Overview
Milestone 1 establishes the baseline pipeline for VisionScript — an automatic image captioning system built on BLIP. The system takes an image as input and generates a single, fluent natural-language caption.

In this milestone, captions are generated using **BLIP (Salesforce/blip-image-captioning-base)** with unconditional generation. CLIP embeddings are extracted for image representation. This milestone establishes the baseline for fine-tuning in later milestones.

---

## 🎯 Objective
The goal of this project is to automatically generate accurate, natural-language captions for images using a pretrained BLIP model fine-tuned on Flickr30k.

Milestone 1 focuses on:
- Dataset preparation and preprocessing
- CLIP embedding extraction pipeline
- GPT-2 tokenizer setup for caption analysis
- BLIP baseline caption generation
- 5 sample image:caption test runs

---

## 🗂️ Dataset
- **Dataset Used:** Flickr30k
- **Source:** HuggingFace (`clip-benchmark/wds_flickr30k`)

### Dataset Processing
- Selected ~1000 image–caption pairs
- Removed captions with fewer than 5 words
- Images converted to RGB format
- Dataset cached to Google Drive for faster reloading
- CLIP embeddings extracted and stored as `.pt` file

---

## 🧠 Model Pipeline

**Image → CLIP Encoder → 512-dim Embedding**
**Image → BLIP Processor → BLIP Decoder → Generated Caption**

### Components

| Component       | Model                                    |
|-----------------|------------------------------------------|
| Image Encoder   | CLIP ViT-B/32                            |
| Caption Model   | BLIP (blip-image-captioning-base)        |
| Tokenizer       | GPT-2 (caption preprocessing only)      |
| Decoding        | Beam Search (num_beams=4)                |

---

## ⚙️ Caption Generation Parameters
- Num beams = 4
- Max new tokens = 50
- Early stopping = True
- Unconditional generation (no style prompts)

---

## 📊 Results – Milestone 1
Baseline captions were generated successfully using BLIP on 5 sample Flickr30k images.

### 🔍 Observations
- BLIP generates fluent, image-grounded captions
- Captions are semantically accurate without any fine-tuning
- CLIP embeddings successfully extracted (512-dim, L2-normalized)
- GPT-2 tokenizer used to analyze caption length distribution
- Fine-tuning on full Flickr30k subset will be done in Milestone 2

---

### 🖼️ Baseline Caption Results

![Baseline Captions](baseline_captions.png)

---

## 📁 Repository Structure

```
🗂️ Milestone 1/
│
├── 📄 Milestone_1_Prj2.ipynb
│
├── 📄 Project_Proposal.pdf
│
├── 🖼️ baseline_captions.png
│
├── 📘 README.md
```

---

## ✅ Milestone 1 Summary
Milestone 1 completed:
- Dataset selection and preprocessing (Flickr30k, 1k pairs)
- CLIP embedding extraction pipeline (512-dim)
- GPT-2 tokenizer setup for caption analysis
- BLIP baseline caption generation (unconditional)
- 5 sample image:caption test runs
- Repository setup and documentation



