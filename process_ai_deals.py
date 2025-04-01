import json
from datetime import datetime
from pathlib import Path
from shutil import copyfile

# Load JSON data
with open('ai_deals.json', 'r', encoding='utf-8') as f:
    try:
        deals = json.load(f)
    except json.JSONDecodeError:
        print("❌ Error: ai_deals.json is empty or malformed.")
        deals = []

if not deals:
    print("⚠️ No deals found. Please check ai_deals.json.")
    exit()

# Build HTML blocks
html_blocks = []
for deal in deals:
    title = deal.get('title', 'Untitled')
    type_ = deal.get('type') or deal.get('platform', '')
    description = deal.get('description', '')
    discount_price = deal.get('discount_price') or deal.get('deal_price', '')
    original_price = deal.get('original_price', '')
    discount_percent = deal.get('discount_percent', '')
    tags = ', '.join(deal.get('tags', []))
    deal_url = deal.get('url') or deal.get('deal_url', '#')
    #image_url = deal.get('image_url') or "https://via.placeholder.com/800x300?text=No+Image"
    image_url = deal.get('image_url', '').strip()
    if not image_url:
        if "udemy.com/course/" in deal.get('url', ''):
            image_url = "https://img-c.udemycdn.com/course/480x270/default_course_image.jpg"
        else:
            image_url = "https://via.placeholder.com/800x300?text=No+Image"

    
    html_blocks.append(f"""
    <div class="deal-card">
        <img src="{image_url}" alt="{title}" class="deal-img" />
        <h2>{title}</h2>
        <p><strong>{type_}</strong></p>
        <p>{description}</p>
        <p><strong>Price:</strong> {discount_price} 
            {"<del>" + original_price + "</del>" if original_price else ''}</p>
        <p><strong>Discount:</strong> {str(discount_percent) + "%" if discount_percent else "–"}</p>
        <a href="{deal_url}" target="_blank">Check Deal →</a>
        <p class="tags">{tags}</p>
    </div>
    """)

# Full HTML page
html_output = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Daily AI Deals</title>
    <style>
        body {{ font-family: Arial, sans-serif; padding: 20px; max-width: 800px; margin: auto; }}
        h1 {{ color: #2b2b2b; }}
        .last-updated {{ font-size: 0.85em; color: #666; margin-top: -12px; margin-bottom: 20px; }}
        .deal-card {{ border: 1px solid #ddd; border-radius: 12px; padding: 16px; margin: 20px 0; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }}
        .deal-img {{ max-width: 100%; height: auto; border-radius: 8px; }}
        .tags {{ font-size: 0.85em; color: #555; margin-top: 10px; }}
        a {{ color: #0077cc; text-decoration: none; }}
    </style>
</head>
<body>
    <h1>🧠 Top AI Tool & Course Deals – {datetime.now().strftime("%B %d, %Y")}</h1>
    <p class="last-updated">Last updated: {datetime.now().strftime('%B %d, %Y – %H:%M')}</p>
    {''.join(html_blocks)}
</body>
</html>
"""

# Ensure output folders exist
Path("public").mkdir(parents=True, exist_ok=True)
Path("docs").mkdir(parents=True, exist_ok=True)

# Save main file
with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(html_output)

# Also copy to docs/ for GitHub Pages
copyfile('public/index.html', 'docs/index.html')

print("✅ public/index.html generated and copied to docs/index.html successfully.")
