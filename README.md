# UGC Video Creator Creative Brief & Storyboard Factory

> Stop getting bad creator videos. Deliver structured, shot-by-shot 9:16 UGC storyboards that direct-response video creators understand instantly.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: TEMPLATE_FRAMEWORK](https://img.shields.io/badge/Format-TEMPLATE--FRAMEWORK-green.svg)](#)
[![Tier: 1](https://img.shields.io/badge/Tier-1-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**PRO** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Build an open-source UGC creator brief and storyboard system: 1) 10 vertical video narrative formulas (Hook, Problem, Demonstration, Social Proof, CTA), 2) Visual storyboard wireframe templates with exact camera angle notations (POV, Close-up, Selfie), 3) Scriptwriting template with timed audio cues (0-3s, 4-15s, 16-25s, 26-30s), 4) Creator deliverable agreement and QA checklist.

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `briefs/10-direct-response-video-formulas.md`
- `checklists/creator-deliverable-qa.md`
- `examples/beauty_ecommerce_sample_brief.md`
- `examples/perfume_skincare_hooks.md`
- `LICENSE`
- `playbooks/3-second-retention-playbook.md`
- `README.md`
- `scripts/hook_randomizer.py`
- `templates/creator-storyboard-template.md`
- `templates/hook_matrix_ar.json`
- `templates/shot-list-worksheet.md`
- `tests/test_hook_randomizer.py`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run CLI Script
```bash
python scripts/hook_randomizer.py --help
```

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "content",
  "repository": "ugc-creator-video-brief-factory",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **Native 9:16 Storyboard Structure:** Briefs structure scripts into 3-second hook, problem/relatability, product demonstration, and single clear CTA.
- **Regional Dialect Alignment:** Distinguishes between Egyptian energetic casual tone and Saudi authentic conversational Gulf dialect.
- **B-Roll Safe Zone Layout:** Creator shooting instructions specify keeping text overlays away from platform UI icons (heart, comment, share buttons).

---

## 📚 Primary Documentation & Verifiable References

- [TikTok Creative Center: Creator Scripting & Storyboards](https://ads.tiktok.com/business/creativecenter/) - Platform guidelines for creator-led video advertising and pacing.
- [Meta Creative Hub: Mobile-First Video Production](https://www.facebook.com/business/help/101650893847953) - Best practices for vertical video formatting and sound-on storytelling.
- [YouTube Shorts Creator Academy](https://creatoracademy.youtube.com/) - Video production fundamentals for high-retention short-form clips.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
