# main.py

from config import DEFAULT_NUM_PAGES
from book_generator.story_generator import generate_full_story
from book_generator.image_generator import generate_images_for_story
from book_generator.book_assembler import assemble_book


def main():
    # Step 1: User Input
    title = "The Thirsty Crow"
    num_pages = DEFAULT_NUM_PAGES

    print(f"\n📚 Starting book generation: '{title}' with {num_pages} pages")

    # Step 2: Generate Story Text
    print("\n✏️ Generating story text...")
    story_pages = generate_full_story(title, num_pages)

    # Step 3: Generate Images
    print("\n🖼️ Generating images for each page...")
    image_paths = generate_images_for_story(story_pages)

    # Step 4: Assemble Book
    print("\n📘 Assembling final picture book...")
    assemble_book(story_pages, image_paths)

    print("\n🎉 Picture book generation complete!")


if __name__ == "__main__":
    main()
