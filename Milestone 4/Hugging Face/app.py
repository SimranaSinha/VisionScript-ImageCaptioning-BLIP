import os
import json
import textwrap
from datetime import datetime

import torch
import gradio as gr
import matplotlib.pyplot as plt
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration, BlipForQuestionAnswering

# ── Device ────────────────────────────────────────────────────
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# ── Load Captioning Model ─────────────────────────────────────
CAP_MODEL_ID = "Salesforce/blip-image-captioning-base"
processor = BlipProcessor.from_pretrained(CAP_MODEL_ID)
model = BlipForConditionalGeneration.from_pretrained(CAP_MODEL_ID).to(device)
model.eval()
print("✓ BLIP captioning model ready.")

# ── Load VQA Model ────────────────────────────────────────────
VQA_MODEL_ID = "Salesforce/blip-vqa-base"
vqa_processor = BlipProcessor.from_pretrained(VQA_MODEL_ID)
vqa_model = BlipForQuestionAnswering.from_pretrained(VQA_MODEL_ID).to(device)
vqa_model.eval()
print("✓ BLIP VQA model ready.")

# ── Output Directory (local, within Space) ───────────────────
DEMO_DIR = "demo_results"
os.makedirs(DEMO_DIR, exist_ok=True)


# ── Core Functions ────────────────────────────────────────────
def run_caption(img, mode="single", temperature=1.0):
    if img is None:
        return "⚠️ No image provided."
    inputs = processor(images=img, return_tensors="pt").to(device)
    use_sampling = temperature != 1.0
    with torch.no_grad():
        if mode == "single":
            out = model.generate(
                **inputs,
                max_new_tokens=50, min_new_tokens=8,
                num_beams=5 if not use_sampling else 1,
                do_sample=use_sampling,
                temperature=temperature if use_sampling else 1.0,
                no_repeat_ngram_size=4,
                length_penalty=1.0
            )
        else:
            out = model.generate(
                **inputs,
                max_new_tokens=120, min_new_tokens=30,
                num_beams=5 if not use_sampling else 1,
                do_sample=use_sampling,
                temperature=temperature if use_sampling else 1.0,
                no_repeat_ngram_size=4,
                length_penalty=2.0,
                repetition_penalty=2.0
            )
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption


def run_vqa(img, question):
    if img is None:
        return "⚠️ Please provide an image."
    if not question or not question.strip():
        return "⚠️ Please enter a question."
    inputs = vqa_processor(images=img, text=question, return_tensors="pt").to(device)
    with torch.no_grad():
        out = vqa_model.generate(**inputs, max_new_tokens=20)
    answer = vqa_processor.decode(out[0], skip_special_tokens=True)
    return answer.strip() if answer.strip() else "Could not determine an answer."


def save_result(img, caption, mode="caption"):
    try:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        save_name = f"VisionScript_{mode}_{ts}"
        fig, axes = plt.subplots(1, 2, figsize=(14, 6),
                                  gridspec_kw={"width_ratios": [1, 1.3]})
        axes[0].imshow(img)
        axes[0].set_title("Input Image", fontsize=12, fontweight="bold")
        axes[0].axis("off")
        axes[1].axis("off"); axes[1].set_xlim(0, 1); axes[1].set_ylim(0, 1)
        axes[1].add_patch(plt.Rectangle((0.03, 0.08), 0.94, 0.84,
                          facecolor="#e6ffe6", edgecolor="#4ade80", linewidth=2))
        axes[1].text(0.5, 0.78, "Generated Caption", ha="center", va="center",
                     fontsize=12, fontweight="bold", color="#2e7d32")
        axes[1].text(0.5, 0.45, "\n".join(textwrap.wrap(caption, width=32)),
                     ha="center", va="center", fontsize=13,
                     linespacing=1.9, color="#1a1a1a")
        axes[1].text(0.5, 0.14, "Model: BLIP | VisionScript",
                     ha="center", va="center", fontsize=9,
                     color="#888", style="italic")
        plt.suptitle(f"VisionScript — {ts}", fontsize=13, fontweight="bold")
        plt.tight_layout()
        plt.savefig(f"{DEMO_DIR}/{save_name}.png", dpi=150, bbox_inches="tight")
        plt.close()
        with open(f"{DEMO_DIR}/{save_name}.json", "w") as jf:
            json.dump({"timestamp": ts, "caption": caption,
                        "mode": mode, "model": "BLIP"}, jf, indent=2)
        print(f"✓ Saved: {save_name}")
    except Exception as e:
        print(f"Save error: {e}")


def on_caption(img, mode, temperature):
    cap = run_caption(img, mode, temperature)
    if img is not None and "⚠️" not in cap:
        save_result(img, cap, mode)
    return cap


def on_vqa(img, question):
    ans = run_vqa(img, question)
    if img is not None and "⚠️" not in ans:
        save_result(img, f"Q: {question}\nA: {ans}", "vqa")
    return ans


# ── CSS ───────────────────────────────────────────────────────
css = """
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');
* { font-family: 'Plus Jakarta Sans', sans-serif; }

.gradio-container {
    background-color: #030712 !important;
    max-width: 1100px !important;
    margin: 40px auto !important;
}
.header-box {
    background: linear-gradient(135deg, #0d1117 0%, #161b27 50%, #0d2137 100%);
    border-radius: 20px; padding: 36px 32px; text-align: center;
    margin-bottom: 24px; border: 1px solid #1e3a5f;
    box-shadow: 0 0 60px rgba(34,211,238,0.07);
}
.header-title {
    font-size: 2.8rem; font-weight: 900; letter-spacing: -1px;
    background: linear-gradient(90deg, #4ade80, #22d3ee, #818cf8);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.badge {
    display: inline-block;
    background: rgba(255,255,255,0.04); border: 1px solid #1e3a5f;
    border-radius: 20px; padding: 4px 14px;
    color: #94a3b8; font-size: 0.82rem; margin: 3px;
}
.custom-card {
    background: rgba(17, 24, 39, 0.7) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 20px !important;
    padding: 20px; margin-bottom: 10px;
}
.action-btn {
    background: linear-gradient(135deg, #4ade80, #22d3ee) !important;
    color: #0d1117 !important; font-weight: 800 !important;
    border-radius: 12px !important; border: none !important;
    font-size: 1rem !important; padding: 14px !important;
    width: 100% !important; text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
}
.section-label { color: #4ade80; font-weight: 700; font-size: 1rem; margin-bottom: 8px; }
textarea, input[type=text] {
    background: #0d1a2e !important; color: #e2e8f0 !important;
    border: 1px solid #1e3a5f !important; border-radius: 10px !important;
    font-size: 0.95rem !important;
}
.footer { text-align:center; color:#334155; font-size:0.8rem; padding:20px; }
"""

# ── Gradio UI ─────────────────────────────────────────────────
with gr.Blocks(css=css, theme=gr.themes.Soft(), title="VisionScript") as demo:

    gr.HTML("""
    <div class="header-box">
        <div class="header-title">🔭 VisionScript</div>
        <div style="color:#94a3b8; font-size:0.95rem; margin:4px 0 8px 0;">
            BLIP Image Captioning System
        </div>
        <div style="color:#64748b; font-size:0.88rem; line-height:1.6; margin:8px 0;">
            VisionScript is an AI-powered image captioning system that generates accurate captions
            for any image using BLIP — a vision-language model pretrained on 129M image-text pairs.
            Built comparing CLIP+GPT2, LoRA, Full Fine-tuning, and BLIP strategies.
        </div>
        <div style="margin:6px 0;">
            <span class="badge">👥 Group 5</span>
            <span class="badge">🎓 IE 7615 Deep Learning for AI</span>
            <span class="badge">🏫 Northeastern University</span>
        </div>
        <div style="margin:8px 0;">
            <a href="https://www.linkedin.com/in/simranasinha/" target="_blank"
               style="display:inline-block;margin:3px;background:linear-gradient(135deg,#4ade80,#22d3ee);
                      color:#0d1117!important;font-weight:700;font-size:0.82rem;
                      padding:6px 16px;border-radius:20px;text-decoration:none!important;">
                🔗 Simran Abhay Sinha</a>
            <a href="https://www.linkedin.com/in/sushmitha-sudharsan-2101/" target="_blank"
               style="display:inline-block;margin:3px;background:linear-gradient(135deg,#4ade80,#22d3ee);
                      color:#0d1117!important;font-weight:700;font-size:0.82rem;
                      padding:6px 16px;border-radius:20px;text-decoration:none!important;">
                🔗 Sushmitha Sudharsan</a>
            <a href="https://www.linkedin.com/in/aditya-kumar9512/" target="_blank"
               style="display:inline-block;margin:3px;background:linear-gradient(135deg,#4ade80,#22d3ee);
                      color:#0d1117!important;font-weight:700;font-size:0.82rem;
                      padding:6px 16px;border-radius:20px;text-decoration:none!important;">
                🔗 Aditya Kumar</a>
            <a href="https://www.linkedin.com/in/meghana-rao0109/" target="_blank"
               style="display:inline-block;margin:3px;background:linear-gradient(135deg,#4ade80,#22d3ee);
                      color:#0d1117!important;font-weight:700;font-size:0.82rem;
                      padding:6px 16px;border-radius:20px;text-decoration:none!important;">
                🔗 Meghana Rao</a>
        </div>
        <a style="display:inline-block;margin-top:14px;background:linear-gradient(135deg,#4ade80,#22d3ee);
                  color:#0d1117!important;font-weight:800;font-size:0.85rem;
                  padding:8px 20px;border-radius:20px;text-decoration:none!important;"
           href="https://github.com/SimranaSinha/VisionScript-ImageCaptioning-BLIP"
           target="_blank">⭐ View on GitHub</a>
    </div>
    """)

    with gr.Row():

        # LEFT COLUMN
        with gr.Column(scale=1):
            with gr.Group(elem_classes="custom-card"):
                gr.HTML("<p class='section-label'>📸 Image Source</p>")
                input_img = gr.Image(
                    type="pil", label=None, show_label=False,
                    sources=["upload", "webcam", "clipboard"],
                    height=300
                )
                gr.HTML("<p class='section-label' style='margin-top:15px;'>⚙️ Caption Settings</p>")
                gr.HTML("""<span style='display:inline-block; background:#6d28d9; color:#e9d5ff;
                            border-radius:8px; padding:3px 12px; font-size:0.8rem;
                            font-weight:700; margin-bottom:6px;'>Detail Level</span>""")
                cap_mode = gr.Radio(
                    choices=["single", "paragraph"],
                    value="single", label="",
                    info="single = one sentence | paragraph = detailed description"
                )
                gr.HTML("""<span style='display:inline-block; background:#6d28d9; color:#e9d5ff;
                            border-radius:8px; padding:3px 12px; font-size:0.8rem;
                            font-weight:700; margin-top:10px; margin-bottom:6px;'>🌡️ Temperature</span>""")
                temperature_slider = gr.Slider(
                    minimum=0.5, maximum=2.0, value=1.0, step=0.1,
                    label="",
                    info="1.0 = beam search (best quality) | <1.0 = focused | >1.0 = creative/varied"
                )
                gen_cap_btn = gr.Button("✨ GENERATE CAPTION", elem_classes="action-btn")

        # RIGHT COLUMN
        with gr.Column(scale=1):

            with gr.Group(elem_classes="custom-card"):
                gr.HTML("<p class='section-label'>💡 AI Analysis</p>")
                gr.HTML("""<span style='display:inline-block; background:#6d28d9; color:#e9d5ff;
                            border-radius:8px; padding:3px 12px; font-size:0.8rem;
                            font-weight:700; margin-bottom:8px;'>Caption Output</span>""")
                out_caption = gr.Textbox(
                    label="", show_label=False, lines=6,
                    placeholder="Caption will appear here...",
                    interactive=False
                )

            with gr.Group(elem_classes="custom-card"):
                gr.HTML("<p class='section-label' style='color:#22d3ee;'>❓ Visual Q&A</p>")
                gr.HTML("""<span style='display:inline-block; background:#6d28d9; color:#e9d5ff;
                            border-radius:8px; padding:3px 12px; font-size:0.8rem;
                            font-weight:700; margin-bottom:8px;'>Ask a question about the image</span>""")
                vqa_msg = gr.Textbox(
                    label="", show_label=False,
                    placeholder="e.g. What color is the car? / How many people?",
                    lines=2
                )
                vqa_btn = gr.Button("🔍 Query Model", variant="secondary")
                gr.HTML("""<span style='display:inline-block; background:#6d28d9; color:#e9d5ff;
                            border-radius:8px; padding:3px 12px; font-size:0.8rem;
                            font-weight:700; margin:8px 0;'>Answer</span>""")
                out_vqa = gr.Textbox(
                    label="", show_label=False,
                    interactive=False, lines=2,
                    placeholder="Answer will appear here..."
                )

    gr.HTML("""
    <div class="footer">
        © 2026 VisionScript Team &nbsp;·&nbsp; Built with Gradio &amp; Salesforce BLIP &nbsp;·&nbsp;
        <a href="https://github.com/SimranaSinha/VisionScript-ImageCaptioning-BLIP"
           target="_blank" style="color:#4ade80; text-decoration:none;">GitHub ↗</a>
    </div>
    """)

    # ── Event Handlers ─────────────────────────────────────────
    gen_cap_btn.click(fn=on_caption, inputs=[input_img, cap_mode, temperature_slider], outputs=out_caption)
    vqa_btn.click(fn=on_vqa, inputs=[input_img, vqa_msg], outputs=out_vqa)

if __name__ == "__main__":
    demo.launch()
