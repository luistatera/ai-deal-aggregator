#!/bin/bash

echo "🚀 Running Cline to fetch fresh deals..."
cline ai-deals-daily.cline > ai_deals.json

echo "🧠 Converting to HTML..."
python process_ai_deals.py

echo "📦 Committing and pushing to GitHub..."
git add docs/index.html
git commit -m "🔁 Auto-update from Cline on $(date +'%Y-%m-%d %H:%M')"
git push
