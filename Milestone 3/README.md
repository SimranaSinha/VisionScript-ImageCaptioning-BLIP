Here is a **README for Milestone 3** similar to your Milestone 2 style, with emojis and sections you usually use.

---

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

### Test 1

![Image](https://www.researchgate.net/publication/236651620/figure/fig2/AS%3A341356196188165%401458397067394/Test-1-comparison-of-the-reference-line-and-numerical-I-order-BULLET-II.png)

![Image](https://www.researchgate.net/publication/331277700/figure/fig1/AS%3A11431281177558209%401690547071922/Test-1-Comparison-between-diffusion-naive-first-and-fourth-order-explicit-AP-and-first.png)

### Test 2

![Image](https://www.researchgate.net/profile/Ray-Berry-2/publication/333881584/figure/fig3/AS%3A771594955804672%401560973981194/Test-2-Comparison-between-analytical-and-numerical-solutions-for-the-general-Riemann.png)

![Image](https://www.researchgate.net/publication/267046557/figure/fig1/AS%3A360996515401736%401463079685109/Test-2-Comparison-of-the-normal-contact-force-at-the-right-foot-when-walking.png)

### Test 3

![Image](https://www.researchgate.net/publication/234838911/figure/fig4/AS%3A299813053714435%401448492410443/Test-3-Comparison-of-experimental-data-and-numerical-results-rain-duration-t-14-10.png)

![Image](https://www.researchgate.net/publication/329705199/figure/fig1/AS%3A704667755487232%401545017293425/Test-3-Comparison-of-the-rate-of-convergence-of-f-e-m-f-MM-2-g-for-different-values-of.png)

### Test 4

![Image](https://www.researchgate.net/publication/380223509/figure/fig2/AS%3A11431281239950640%401714569963267/Test-4-Comparison-Error-Cost-N-between-the-particle-stochastic-Galerkin-scheme-MC-sG.png)

![Image](https://www.researchgate.net/publication/332897812/figure/fig3/AS%3A755762104127488%401557199135605/Test-4-Comparison-of-POD-and-DMD-errors-Local-truncation-error-and-global-error-for-DMD.png)

---

## 📊 Observations

* Prefix Tuning sometimes produced incorrect or unrelated captions.
* LoRA generated more relevant captions compared to Prefix Tuning.
* Full Fine-Tuning produced more descriptive captions but sometimes overfitted.
* BLIP produced the most accurate and consistent captions across test images.
* Parameter-efficient methods (Prefix, LoRA) require less training but may reduce caption quality.

---

## 📁 Project Structure

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


