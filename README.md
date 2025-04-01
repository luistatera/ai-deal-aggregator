# 🧠 AI Deal Aggregator

This is a fully automated, daily-updated web page that showcases top deals on AI tools and courses. It scrapes the web, summarizes deal details using AI, and updates a clean static page hosted on GitHub Pages.

---

## 🚀 Live Site

👉 [https://luistatera.github.io/ai-deal-aggregator/](https://luistatera.github.io/ai-deal-aggregator/)

---

## ⚙️ How It Works

1. **Search & Extract (Manual or Automated):**
   - `.cline` prompt (`ai-deals-daily.cline`) uses Brave MCP to search for deals
   - Extracts text and markdown for product info & images
   - Saves result to `ai_deals.json`

2. **Process & Render:**
   - `process_ai_deals.py` reads the JSON and generates `public/index.html`

3. **Publish via GitHub Pages:**
   - GitHub Pages serves content from `public/`
   - A GitHub Action (`.github/workflows/daily-deals.yml`) runs daily to auto-update the site

---

## 🛠️ How to Run It Locally

### ✅ Step 1: Install Requirements
```bash
pip install -r requirements.txt  # (optional if you need parsing libs)
