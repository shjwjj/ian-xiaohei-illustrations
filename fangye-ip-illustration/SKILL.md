---
name: fangye-ip-illustration
description: Generate and edit Fangye brand IP illustrations for WeChat articles and health-culture content. Use when Codex needs to plan image slots, create prompts, generate or revise Fangye deer/hamster IP images, make clean action-demo illustrations, or render text-heavy WeChat graphics with Fangye's young, friendly, non-preachy style.
---

# Fangye IP Illustration

## Overview

Create Fangye article illustrations that feel young, close, and useful. The two IP characters appear as visual subjects only; do not turn them into narrators in the article body.

This skill adapts the `ian-xiaohei-illustrations` idea of "find the article's cognitive anchor, then draw one clear visual action" to Fangye's health-culture account.

## Load When Needed

- Read `references/style-guide.md` before planning or generating Fangye images.
- Read `references/prompt-recipes.md` when writing image prompts or editing an existing image.
- Run `scripts/lint_image_copy.py` before finalizing image text.
- Use `scripts/render_vertical_steps_card.py` for text-heavy vertical step cards where Chinese text must be exact.
- Use `assets/reference/` only as visual reference; do not copy old clothing or layouts mechanically.

## Workflow

### 1. Read The Article

Identify the lived moment, not just the topic. Look for:

- a physical state: tired eyes, clenched shoulders, lying down but checking the phone
- a small action: pulling curtains, writing three lines, dimming a lamp
- a mechanism worth visualizing: interruption, rhythm, light, caffeine timing
- one useful method the reader can try today

Do not distribute images evenly. Put images where the reader needs a pause, a concrete scene, or a clearer method.

### 2. Choose Image Types

Use 3-5 images for a normal WeChat article:

- **Opening state image**: one Fangye IP in a modern daily scene, with large blank space and at most one short caption.
- **Mechanism image**: a comic or simple visual metaphor. Prefer a character being interrupted over abstract curves when the reader needs empathy.
- **Action demo**: show the IP doing the exact movement or habit. Keep the outfit modern and the background minimal.
- **Method card**: a vertical steps card, rendered with deterministic text layout if there is more than a few words.

Skip an image if it repeats what the paragraph already explains.

### 3. Write Image Copy

Keep image text direct and ordinary:

- Good: `躺下了，又摸回来`, `那杯咖啡早一点`, `屋里暗一点`
- Good: `试三晚，选两件就行`, `看早上有没有一点变化`
- Avoid: `方也版做法`, `把研究翻译成行动`, `递信号`, `不是 A 而是 B`
- Avoid putting `鹿也` or `粟也` into body copy. The IP can appear in the picture, not as a speaking character.

Run:

```bash
python scripts/lint_image_copy.py --text "试三晚，选两件就行" --text "屋里暗一点"
```

### 4. Generate Or Render

For painterly scene images, use `image_gen` with:

- Fangye deer or hamster as the central action subject
- modern casual or office clothing unless the user asks for traditional clothing
- clean warm off-white background, large white space
- simple props that reveal the situation
- no decorative corner flowers, no ornate backgrounds, no role-name labels
- no long Chinese text inside model-generated imagery

For exact Chinese text graphics, render with a script, HTML/SVG, Remotion, or PIL. Do not rely on image generation to typeset long Chinese copy.

### 5. Save And Wire Into The Article

Save final images in the active project, usually:

```text
assets/content/wechat/<article-slug-or-number>-<short-topic>-vN.png
```

If replacing an image, create a new `vN` file instead of overwriting the old one. Update the Markdown and preview HTML references after visual inspection.

### 6. Verify

Before final delivery:

- view the image at real size
- check text legibility on WeChat-width preview
- confirm the IP is doing the main action
- confirm the picture has enough blank space
- remove images that do not add meaning
- refresh the WeChat preview when available

## Editing Existing Images

When revising a generated image, keep the user's selected element as the source of truth:

- If the user says "delete this image", remove it from the article and preview, not just from the asset folder.
- If the user says "remove the bottom box, keep the logo", produce a new asset version and preserve the rest of the layout.
- If the user criticizes clothing or background, simplify first: modern clothing, fewer props, more blank space.

## Output

Finish with:

- what image assets changed
- where they are saved
- which article or preview was rewired
- any remaining image that still feels optional
