# 🎨 Museum Canvas Caption — Milestone 3

**CLIP + GPT-2 Fine-Tuning Methods Comparison**

## 📌 Overview

Milestone 3 focuses on comparing different fine-tuning strategies for image caption generation using CLIP embeddings and GPT-2. The goal is to evaluate how different training methods affect caption quality and image understanding.

The models compared in this milestone:

* Prefix Tuning
* LoRA (Low-Rank Adaptation)
* Full Fine-Tuning
* BLIP (Baseline model)

This milestone evaluates which method generates the most accurate and descriptive captions.

---

## 🧠 Methods Compared

| Method         | Description                                                   |
| -------------- | ------------------------------------------------------------- |
| Prefix Tuning  | Only prefix embeddings are trained while GPT-2 remains frozen |
| LoRA           | Low-rank adaptation layers added to GPT-2                     |
| Full Fine-Tune | Entire GPT-2 model is fine-tuned                              |
| BLIP           | Pretrained image captioning baseline model                    |

---
## 🖼️ Results Comparison
## Test 1
![Test 1](https://raw.githubusercontent.com/SimranaSinha/Museum-Canvas-Caption-CLIP-GPT2/main/Milestone%203/Results/Test_1_comparison.png)

**Observation:**  
BLIP generated the most accurate caption describing a person standing on a soccer ball. Prefix Tuning produced an incorrect caption, while LoRA and Full Fine-Tuning generated partially relevant soccer-related descriptions.

---

## Test 2
![Test 2](https://raw.githubusercontent.com/SimranaSinha/Museum-Canvas-Caption-CLIP-GPT2/main/Milestone%203/Results/Test_2_comparison.png)

**Observation:**  
BLIP correctly identified a brown and white dog standing on a beach. LoRA and Full Fine-Tuning described a dog action scene but were not fully accurate. Prefix Tuning again generated an incorrect caption.

---

## Test 3
![Test 3](https://raw.githubusercontent.com/SimranaSinha/Museum-Canvas-Caption-CLIP-GPT2/main/Milestone%203/Results/Test_3_comparison.png)

**Observation:**  
BLIP correctly described a man and a woman sitting on a bench in the woods. LoRA and Full Fine-Tuning generated incorrect scene descriptions. Prefix Tuning produced an unrelated caption.

---

## Test 4
![Test 4](https://raw.githubusercontent.com/SimranaSinha/Museum-Canvas-Caption-CLIP-GPT2/main/Milestone%203/Results/Test_4_comparison.png)

**Observation:**  
BLIP correctly identified a lion lying in the grass. Prefix Tuning, LoRA, and Full Fine-Tuning generated incorrect captions unrelated to the lion image.

---

## 📊 Observations

* Prefix Tuning sometimes produced incorrect or unrelated captions.
* LoRA generated more relevant captions compared to Prefix Tuning.
* Full Fine-Tuning produced more descriptive captions but sometimes overfitted.
* BLIP produced the most accurate and consistent captions across test images.
* Parameter-efficient methods (Prefix, LoRA) require less training but may reduce caption quality.

---

## 📊 Results Summary Table

The table below compares different fine-tuning methods using evaluation metrics such as BLEU, METEOR, CIDEr, and ROUGE-L, along with the number of trainable parameters.

![Results Summary](https://raw.githubusercontent.com/SimranaSinha/Museum-Canvas-Caption-CLIP-GPT2/main/Milestone%203/Summary.png)

---

## 📁 Repository Structure

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

## 🛠️ Tools & Technologies

* Python
* PyTorch
* HuggingFace Transformers
* CLIP
* GPT-2
* LoRA
* Prefix Tuning
* BLIP
* Google Colab

---

## ✅ Conclusion

This milestone demonstrates that different fine-tuning strategies significantly impact image caption quality. Parameter-efficient methods like Prefix Tuning and LoRA are computationally efficient, while Full Fine-Tuning and BLIP generally produce more accurate captions. The comparison helps understand the trade-off between performance and training cost in vision-language models.


