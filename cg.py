import os
from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup

HTML_FILE = "partc.html"
TEMPLATE_FILE = "wcld25-template.jpg"
FONT_FILE = "/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf"

OUTPUT_FOLDER = "certificates"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

processed = set()

TEXT_COLOR = "#0a1d41"

# Adjusted perfect position
TARGET_CENTER_Y = 648   # << corrected placement
MAX_WIDTH_PERCENT = 0.60

with open(HTML_FILE, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

rows = soup.select("tbody tr")

for row in rows:
    cols = row.find_all("td")
    if len(cols) < 2:
        continue

    name = cols[0].get_text(strip=True)
    email = cols[1].get_text(strip=True)

    key = (name.lower(), email.lower())
    if key in processed:
        print(f"⚠ Skipped duplicate: {name}")
        continue

    processed.add(key)
    username = email.split("@")[0]

    img = Image.open(TEMPLATE_FILE)

    if img.mode == "RGBA":
        img = img.convert("RGB")

    draw = ImageDraw.Draw(img)
    img_w, img_h = img.size

    max_width = int(img_w * MAX_WIDTH_PERCENT)
    font_size = 110

    # Auto-resize
    while True:
        font = ImageFont.truetype(FONT_FILE, font_size)
        bbox = draw.textbbox((0, 0), name, font=font)
        text_width = bbox[2] - bbox[0]

        if text_width <= max_width or font_size <= 55:
            break

        font_size -= 3

    bbox = draw.textbbox((0, 0), name, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Center
    x = (img_w - text_width) // 2
    y = TARGET_CENTER_Y - (text_height // 2)

    draw.text((x, y), name, font=font, fill=TEXT_COLOR)

    output_file = os.path.join(OUTPUT_FOLDER, f"{username}.jpg")
    img.save(output_file)

    print(f"✔ Saved: {output_file}")

print("\n🎉 Certificates generated successfully.")

