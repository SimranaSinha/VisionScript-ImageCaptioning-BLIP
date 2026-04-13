# 🖼️ VisionScript - Milestone 4

**Multi-Mode Captioning + VQA**

## 📌 Overview

Milestone 4 extends the VisionScript Image Captioning system by introducing **multi-mode caption generation** and **visual question answering (VQA)** capabilities using the BLIP model.

This milestone focuses on making the system more flexible and interactive by allowing different caption styles and enabling question-based reasoning on images.

---

## 🎯 Objectives

* Extend caption generation beyond a single output style
* Implement multiple captioning modes:

  * Single-line caption
  * Paragraph-style caption
* Add **Visual Question Answering (VQA)** capability
* Evaluate qualitative improvements across different scenarios
* Improve usability and interpretability of outputs

---

## 🧠 Model & Approach

* **Model Used:** BLIP (Bootstrapping Language Image Pretraining) – Salesforce
* **Framework:** VisionScript Interface
* **Core Enhancements:**

  * Mode-based caption generation
  * Structured outputs (single vs paragraph)
  * Question-driven inference (VQA)

---

## ⚙️ Modes Implemented

### 🟢 1. Single Caption Mode

* Generates a short, concise description
* Best for quick summaries

📌 Example:

> “a lion laying in the grass with a blue sky in the background”

---

### 🟢 2. Paragraph Caption Mode

* Generates a detailed, descriptive caption
* Captures context, background, and relationships

📌 Example:

> “a lion laying on the ground with its head turned to the side and it's looking at the camera, with a blue sky behind it in the background of a field of grass and a few trees”

---

### 🟢 3. Visual Question Answering (VQA)

* Answers questions based on image content
* Enables interactive understanding

📌 Example:

> Q: Where is the man standing?
> A: The man is standing on top of the sand dune

---

## 🖼️ Results

### 🦁 Lion – Paragraph Caption

![Lion Paragraph](https://github.com/SimranaSinha/VisionScript-ImageCaptioning-BLIP/blob/main/Milestone%204/Results/VisionScript_paragraph_20260409_160452.png)

---

### 🦁 Lion – Single Caption

![Lion Single](https://github.com/SimranaSinha/VisionScript-ImageCaptioning-BLIP/blob/main/Milestone%204/Results/VisionScript_single_20260409_160448.png)

---

### 👨‍👩‍👧 Group Scene – Paragraph Caption

![Group Paragraph](https://github.com/SimranaSinha/VisionScript-ImageCaptioning-BLIP/blob/main/Milestone%204/Results/VisionScript_paragraph_20260410_003347.png)

---

### 🏜️ Sand Dune – Paragraph Caption

![Sand Paragraph](https://github.com/SimranaSinha/VisionScript-ImageCaptioning-BLIP/blob/main/Milestone%204/Results/VisionScript_paragraph_20260410_003722.png)

---

### ❓ Visual Question Answering (VQA)

![VQA](https://github.com/SimranaSinha/VisionScript-ImageCaptioning-BLIP/blob/main/Milestone%204/Results/VisionScript_vqa_20260410_003730.png)

---

## 📊 Observations

* **Paragraph mode** provides richer and more context-aware descriptions
* **Single mode** is faster and more concise but less detailed
* **VQA** demonstrates strong spatial understanding (e.g., location, actions)
* Model performs well on:
  * Clear subjects
  * Outdoor scenes
* Slight verbosity and repetition observed in paragraph mode

---

## 📁 Repository Structure

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

## 🔗 Results Drive Link

📂 Full Results Folder:
👉 [https://drive.google.com/drive/folders/1EB2NIj_HIOR3XTDXXPqo5fGJEWEFNfUH](https://drive.google.com/drive/folders/1EB2NIj_HIOR3XTDXXPqo5fGJEWEFNfUH)

---

## 🚀 Key Improvements from Milestone 3

| Feature      | Milestone 3 | Milestone 4           |
| ------------ | ----------- | --------------------- |
| Caption Type | Single      | Single + Paragraph    |
| Flexibility  | Limited     | Multi-mode            |
| Interaction  | None        | VQA Added             |
| Output Depth | Basic       | Detailed + Contextual |

---

## ✅ Conclusion

This milestone successfully enhances VisionScript into a **multi-functional vision-language system**. The addition of paragraph captions and VQA significantly improves usability, making the system more interactive and closer to real-world applications like assistive AI, smart search, and visual storytelling.


