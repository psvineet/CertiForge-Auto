# CertiForge-Auto
### Certificate Generation Tool (Bulk Image Renderer)

A Python-based automation tool to generate personalized certificates in bulk by extracting user data from an HTML file and rendering names onto a predefined image template.

---

## Overview

This tool automates certificate creation by:

- Parsing participant data (name, email) from an HTML table
- Rendering names dynamically onto a certificate template image
- Adjusting font size automatically to fit long names
- Center-aligning text for clean visual output
- Avoiding duplicate certificate generation
- Saving certificates as individual image files

It is designed for bulk operations such as events, workshops, or competitions.

---

## Input Requirements

### 1. HTML File

- Must contain a table structure (`<tbody><tr><td>...</td></tr></tbody>`)
- First column → Name
- Second column → Email
- Each row represents one participant

---

### 2. Template Image

- Certificate background image (JPG/PNG)
- Text will be rendered on top of this image

---

### 3. Font File

- TrueType font (`.ttf`) file required
- Used for rendering participant names

---

## ⚠️ What You Need to Replace Before Running

Update these variables in the script:

### 1. HTML Input File

Replace:
```
HTML_FILE = "partc.html"
```

With:
```
HTML_FILE = "your_file.html"
```

---

### 2. Template Image

Replace:
```
TEMPLATE_FILE = "wcld25-template.jpg"
```

With:
```
TEMPLATE_FILE = "your_template.jpg"
```

---

### 3. Font Path

Replace:
```
FONT_FILE = "/path/to/font.ttf"
```

With your system font path:
```
FONT_FILE = "your_font.ttf"
```

---

### 4. Output Folder (Optional)

Replace:
```
OUTPUT_FOLDER = "certificates"
```

With:
```
OUTPUT_FOLDER = "your_output_folder"
```

---

## Dependencies

```
pip install pillow beautifulsoup4
```

---

## Usage

Run the script:

```
python cg.py
```

---

## Output

- Certificates are saved as image files (`.jpg`)
- File naming format:
  - Based on email username (before `@`)
- Stored in the output folder

Example:
```
certificates/john_doe.jpg
```

---

## Processing Flow

1. Load HTML file  
2. Parse table rows using BeautifulSoup  
3. Extract name and email  
4. Remove duplicates using a set  
5. Load certificate template  
6. Dynamically adjust font size to fit name  
7. Center-align text on image  
8. Render name onto template  
9. Save output image  

---

## Customization

- Adjust text position:
  ```
  TARGET_CENTER_Y = <value>
  ```

- Control text width:
  ```
  MAX_WIDTH_PERCENT = 0.60
  ```

- Change text color:
  ```
  TEXT_COLOR = "#000000"
  ```

- Modify font scaling logic if needed

---

## Project Structure

```
.
├── cg.py
└── README.md
```

---

## Notes

- Duplicate entries (same name + email) are automatically skipped
- Long names are resized to fit within the template
- Works with standard HTML table structure
- Supports batch generation efficiently

---

## License

Free to use and modify.
