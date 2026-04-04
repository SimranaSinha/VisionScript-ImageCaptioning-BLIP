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

- Test 1
Observation: BLIP generated the most accurate caption. Prefix Tuning produced an incorrect description. LoRA and Full Fine-Tuning generated partially correct captions related to soccer.

- Test 2
Observation: BLIP correctly identified the dog on a beach. LoRA and Full Fine-Tuning generated action-based captions but were not fully accurate. Prefix Tuning again produced an incorrect caption.

- Test 3
Observation: BLIP correctly described two people sitting on a bench in the woods. LoRA and Full Fine-Tuning produced incorrect scene descriptions. Prefix Tuning output was unrelated to the image.

- Test 4
Observation: BLIP correctly identified a lion in the grass. Prefix Tuning, LoRA, and Full Fine-Tuning generated incorrect captions unrelated to the lion image.

---

## 📊 Observations

* Prefix Tuning sometimes produced incorrect or unrelated captions.
* LoRA generated more relevant captions compared to Prefix Tuning.
* Full Fine-Tuning produced more descriptive captions but sometimes overfitted.
* BLIP produced the most accurate and consistent captions across test images.
* Parameter-efficient methods (Prefix, LoRA) require less training but may reduce caption quality.

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


