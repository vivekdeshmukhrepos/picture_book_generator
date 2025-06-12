# book_generator/story_generator.py

from typing import List
from openai import OpenAI
from config import OPENAI_API_KEY, LLM_MODEL, STORY_OUTPUT_FILE

# Initialize the OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)


def generate_story_outline(title: str, num_pages: int) -> List[str]:
    """
    Generate a children's picture book outline using an LLM.
    Each element represents one page summary.
    """
    prompt = (
        f"Create a magical and fun story outline for a children's picture book titled '{title}'.\n"
        f"Break the story into {num_pages} short page-wise descriptions (2-3 sentences each)."
    )
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": "You are a creative children's book writer."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.8,
        max_tokens=1000,
    )
    outline_raw = response.choices[0].message.content
    pages = [line.strip() for line in outline_raw.split("\n") if line.strip()]
    return pages[:num_pages]


def expand_page_text(page_text: str) -> str:
    """
    Expand a short page outline into a full paragraph of narrative text.
    """
    prompt = (
        f"Expand this children's story outline into a short description, imaginative page (maximum 2 sentences):\n\n{page_text}"
    )
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=500,
    )
    return response.choices[0].message.content.strip()


def generate_full_story(title: str, num_pages: int) -> List[str]:
    """
    Generate the full story from title and number of pages.
    Returns list of full page texts.
    """
    outline = generate_story_outline(title, num_pages)
    full_pages = [expand_page_text(summary) for summary in outline]

    with open(STORY_OUTPUT_FILE, "w", encoding="utf-8") as f:
        for i, page in enumerate(full_pages, 1):
            f.write(f"--- Page {i} ---\n{page}\n\n")

    return full_pages
