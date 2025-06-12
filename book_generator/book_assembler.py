# book_generator/book_assembler.py

from fpdf import FPDF
import os
from typing import List
from config import FINAL_BOOK_FILE, IMAGE_OUTPUT_DIR

class PictureBook(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_auto_page_break(auto=True, margin=15)
        self.set_font("Arial", size=12)

    def add_page_with_text_and_image(self, text: str, image_path: str):
        self.add_page()

        # Add image (centered)
        if os.path.exists(image_path):
            self.image(image_path, x=35, y=20, w=140)

        # Add text below the image
        self.set_xy(20, 200)
        self.multi_cell(0, 10, text, align="L")

def assemble_book(pages: List[str], image_paths: List[str], output_file: str = FINAL_BOOK_FILE):
    """
    Combine story text and images into a final PDF picture book.
    """
    book = PictureBook()
    for page_text, image_path in zip(pages, image_paths):
        book.add_page_with_text_and_image(page_text, image_path)

    book.output(output_file)
    print(f"📕 Book saved to {output_file}")
