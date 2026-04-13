# 🖼️ VisionScript  – Milestone 2

##  CLIP + GPT-2 Caption Generation

## 📌  Overview

This milestone focuses on integrating the CLIP image encoder with the GPT-2 language model to generate captions for artwork images. The CLIP model converts images into embeddings, and GPT-2 generates captions conditioned on those embeddings. Different decoding strategies were tested and caption outputs were analyzed.

---

## 🎯 Objectives

* Integrate CLIP image encoder with GPT-2 language model
* Inject image embeddings into GPT-2 for caption generation
* Generate captions for sample museum artwork images
* Compare decoding strategies
* Analyze caption quality and generation behavior

---

## 📁 Repository Structure

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

## 📑 Methodology

1. Images are passed through the CLIP image encoder.
2. CLIP generates image embeddings.
3. The embeddings are injected into GPT-2 as prefix embeddings.
4. GPT-2 generates captions based on the image embeddings.
5. Different decoding strategies were tested:
   * Greedy Decoding
   * Beam Search
   * Nucleus Sampling (Top-p Sampling)

---

##  📊 Results

* The model successfully generated captions from artwork images.
* Training loss decreased over time indicating learning.
* Caption quality varied depending on decoding strategy.
* Nucleus sampling produced more natural captions compared to greedy decoding.
* Beam search produced more structured captions but sometimes repetitive.

---

### 📉 Training Loss

Training loss plot is included in:

```
training_loss_v2.png
```

This shows the model learning trend during training.

---

## ✅ Conclusion

Milestone 2 successfully integrates CLIP and GPT-2 for image caption generation. The model is able to generate captions from images, and decoding strategy plays an important role in caption quality. This milestone forms the foundation for style-conditioned caption generation in the next milestone.

