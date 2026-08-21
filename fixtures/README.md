# Sample Fixtures

这里的图片均为 2026-08-21 使用 Codex harness 内置 ImageGen 生成或编辑的合成素材，不来自真实人物、地点或第三方摄影作品。生成模式为 `photorealistic-natural`，未做手工图像后处理。

## 01 — Architecture café

- File: `01-architecture-cafe.png`
- Size: 1536 × 1024
- Purpose: 建筑线条、显著色块、物件数量、左右关系和照片保真。
- Invariants: teal awning、coral door、one red bicycle、three terracotta pots、one black streetlamp、no people、no text。

Prompt:

```text
Generate a photorealistic natural editorial benchmark photograph.
Use case: photorealistic-natural.
Asset type: neutral benchmark input for testing image-editing skills.
Scene: a quiet modern neighborhood corner café exterior with a distinctive teal fabric awning, a coral-orange wooden door, one red step-through bicycle leaning against the left wall, three terracotta plant pots, and a slim black streetlamp.
Composition: horizontal 3:2 landscape photograph, eye-level, all objects fully visible, clear geometric lines and spatial relationships.
Lighting: soft mid-morning daylight with gentle realistic shadows.
Constraints: exactly one bicycle, exactly three pots, no people, no readable text, no logos, no watermark, no collage, no illustration, no stylization.
```

## 02 — Mountain lake

- File: `02-mountain-lake.png`
- Size: 1536 × 1024
- Purpose: 复杂植被压缩、远近层次、水面反射和小型高饱和主体。
- Invariants: turquoise lake、wooden bridge、one red umbrella、misty mountains、no people。

Prompt:

```text
Generate a photorealistic natural landscape benchmark photograph.
Use case: photorealistic-natural.
Asset type: neutral benchmark input for testing image-editing skills.
Scene: a deep turquoise mountain lake surrounded by dense evergreen forest; a narrow wooden footbridge crosses the lower third; one vivid red umbrella rests open near the right end of the bridge; layered misty mountains and pale clouds in the distance.
Composition: horizontal 3:2 landscape photograph, wide view, clear foreground bridge, complex foliage, strong depth, the red umbrella is small but unmistakable.
Lighting: cool overcast daylight after rain, realistic water reflections and wet wood texture.
Constraints: exactly one red umbrella, no people, no buildings, no readable text, no logos, no watermark, no collage, no illustration, no stylization.
```

## 03 — Editorial portrait duo with camera

- File: `03-portrait-camera-duo.png`
- Size: 1024 × 1536
- Purpose: 双人物身份与年龄表达、四只手、服装层次、产品几何、协作关系和竖图路由。
- Invariants: exactly two fictional professionals；一位年轻白人男性；一位 40–50 岁、非老年化的中国职场女性；mustard jacket；navy blazer；striped shirt；one turquoise camera；one cobalt mug；one contact sheet；four visible hands。
- Provenance: 由早期单人版 `03-portrait-camera.png` 经两次 ImageGen 编辑得到；第二次仅修正女方第二只手的可见性。单人版保留用于回溯，但不再列入当前示例输入。

Prompt:

```text
Create a photorealistic natural editorial studio portrait with exactly two fictional professionals collaborating at one wooden worktable beside a large window.
Use case: photorealistic-natural.
Asset type: neutral benchmark input for testing identity-preserving image-editing skills.
People: one young white man with wavy brown hair, a mustard-yellow rain jacket, and a navy-and-white striped shirt; one middle-aged Chinese professional woman, clearly about 40–50 rather than elderly, with shoulder-length dark hair, a tailored deep-navy blazer, and a warm ivory blouse. They read as equal creative colleagues reviewing images, not as a romantic pair.
Interaction: the man holds one turquoise compact camera naturally while the woman points to one small printed contact sheet. Exactly four anatomically plausible hands are visible: her second hand rests beside one cobalt-blue mug, and his second hand rests near the contact sheet.
Composition: vertical 2:3 environmental waist-up two-shot; both faces, clothing, hands, camera, contact sheet, mug, table, window, and softly blurred studio details remain readable.
Lighting: soft directional window daylight with realistic skin, fabric, paper, ceramic, and camera materials.
Constraints: exactly two people, exactly one camera, exactly one mug, exactly one contact sheet, exactly four visible hands, no extra or duplicated objects, no readable text, no logos, no watermark, no collage, no illustration, no stylization.
```

## 04 — Cat and dog with yarn

- File: `04-animal-cat-dog.png`
- Size: 1536 × 1024
- Purpose: 动物身份、细密毛发、眼睛与爪部结构、动态互动、遮挡和单一物件数量约束。
- Invariants: exactly one orange tabby cat、exactly one black-and-white border collie、exactly one red yarn ball、cream rug、moss-green sofa、one mustard cushion、no people、playful rather than aggressive interaction。

Prompt:

```text
Generate a photorealistic natural editorial benchmark photograph.
Use case: photorealistic-natural.
Asset type: neutral benchmark input for testing image-generation and image-transformation skills.
Scene: inside a warm contemporary living room, exactly one orange tabby cat and exactly one medium-sized black-and-white border collie playfully compete over exactly one vivid red wool yarn ball on a textured cream rug. The cat hooks one loose strand with a front paw while the dog gently holds another short strand in its mouth. The intact red ball remains clearly visible between them. Their body language is energetic and curious, not aggressive or distressed.
Composition: horizontal 3:2 action photograph at animal eye level. Show both animals fully enough to read species, coat pattern, faces, eyes, front paws, and interaction. Keep the single red yarn ball unobstructed near the lower center. Include a moss-green sofa, one mustard cushion, a light oak side table, and soft window curtains as stable indoor anchors.
Lighting: soft late-afternoon window daylight with realistic fur, whiskers, paw anatomy, wool fibers, rug texture, and gentle shadows; freeze the motion without motion blur.
Constraints: exactly one cat, exactly one dog, exactly one red yarn ball; no extra animals, no people, no collars, no toys besides the yarn ball, no food bowls, no readable text, no logos, no watermark, no collage, no illustration, no stylization; no fighting, fear, injury, or aggression.
```
