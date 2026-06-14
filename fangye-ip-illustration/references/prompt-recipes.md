# Fangye Prompt Recipes

Use these as prompt building blocks. Adapt scene, props, emotion, and text to the article.

## Opening State Image

```text
Create a 16:9 WeChat article illustration for the Fangye wellness brand.
Main subject: the Fangye deer IP, soft watercolor, modern casual home pajamas, sitting on the edge of a bed/sofa at night, holding a phone, slight frown and tired eyes, still thinking about work after getting home.
Scene: simple warm bedroom/living room, bedside lamp, one cup of water, small note on table, moon outside window, large blank space on the left for Chinese copy.
Style: young, friendly, non-preachy, clean off-white background, hand-drawn outline, sage green and warm beige palette, lots of white space.
Text on image, left side, exact Chinese:
躺下了，又摸回来
明天的事还在脑子里转。
Avoid: ornate background, corner flowers, traditional robe, complex decorations, teacher-like pose, extra Chinese words.
```

## Mechanism As Comic

```text
Create a quiet 16:9 comic-like Fangye illustration with one Fangye IP as the only character.
Show a night of sleep being interrupted several times: lamp light, coffee cup, unfinished work note, phone notification. Use simple visual beats around the character rather than a scientific chart.
The character should look sleepy and mildly confused, not exaggerated.
Background: mostly blank, no detailed bedroom, no decorative corners.
Text labels, if any, are short: 亮光 / 咖啡 / 待办
Avoid: ugly comic panels, dense infographic, scary medical feeling, long labels.
```

## Action Demo Image

```text
Create a 16:9 Fangye article illustration.
Show the Fangye hamster IP doing one clear action: writing three short lines in a notebook beside a dim bedside lamp.
Modern home clothes, simple desk or bedside table, large blank background.
The action should be readable without explanatory text.
No role names, no speech bubble, no teaching pose.
```

## Vertical Step Card

Use deterministic rendering for text cards. Prepare a JSON spec and run `scripts/render_vertical_steps_card.py`.

```json
{
  "title": "试三晚，选两件就行",
  "subtitle": "不用全做。看早上有没有一点变化。",
  "chips": ["从容易的开始", "三晚后再看"],
  "steps": [
    {"tag": "下午", "heading": "那杯咖啡早一点", "body": "如果晚上 11 点睡，咖啡、浓茶、能量饮料先放到 15:00 前。"},
    {"tag": "睡前", "heading": "屋里暗一点", "body": "关大灯，留一盏小灯；手机还在也没关系，内容慢一点。"}
  ]
}
```

## Existing Image Edit

```text
Edit the provided Fangye illustration. Keep the same main character, palette, and layout.
Change only: [specific change].
Preserve: [what should not move].
Remove: [unwanted text/box/background/details].
Style remains soft watercolor, minimal background, modern clothing, large blank space.
```
