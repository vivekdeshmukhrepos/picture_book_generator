# AI Picture Book Generator

Turn a story idea into a fully illustrated picture book using Generative AI (LLMs + Text-to-Image models). This Python project lets you input a story title and number of pages — and outputs a beautiful PDF with AI-generated images and text on each page.

Powered by:
- OpenAI (for story generation)
- Stability AI (for image generation)
- FPDF (for PDF creation)

## ✨ Features

- 🧠 **Story Generation**: Uses OpenAI GPT to generate a unique story outline and detailed text for each page.
- 🎨 **Image Generation**: Uses Stability AI's Core API to generate high-quality illustrations for each story page.
- 📄 **PDF Compilation**: Automatically combines all text and images into a neatly formatted printable PDF book.
- 🛠️ **Modular Codebase**: Clean, well-structured modules for text generation, image creation, and PDF generation.
- 🧪 **Customizable**: Easily change the number of pages, story themes, or swap out AI providers.

## 🗂 Project Structure

```
├── picture_book_generator/
│   config.py
│   main.py
│   README.md
│   requirements.txt
├───assets
│   └───images
│           page_1.png
├───book_generator
│       book_assembler.py
│       image_generator.py
│       story_generator.py
└───outputs
        final_book.pdf
        story_pages.txt
```
## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/vivekdeshmukhrepos/picture_book_generator.git

pip install -r requirements.txt
```

### Configure API Keys
```
# config.py
OPENAI_API_KEY = "your-openai-key"

IMAGE_API_KEY = "your-stability-ai-key"

IMAGE_OUTPUT_DIR = "images"

PDF_OUTPUT_PATH = "generated_book.pdf"

LLM_MODEL = "gpt-3.5-turbo"  # or "gpt-4" if available
```
📝 You can get your keys from:

OpenAI: https://platform.openai.com/account/api-keys

Stability AI: https://platform.stability.ai/account/keys

## 🚀 How to Run the App

Once setup is complete, Modify the user input from `main.py` and run the main script:

```bash
python main.py
```

You can print it, share it, or turn it into a real children's book!
 

