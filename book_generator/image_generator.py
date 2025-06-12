import os
from typing import List
import requests
from config import IMAGE_API_KEY, IMAGE_OUTPUT_DIR

def generate_image(prompt: str, page_number: int) -> str:
    """
    Generate an image using the Stability AI image generation API (v2beta).
    """
    print(f"🎨 Generating image for page {page_number}...")

    url = "https://api.stability.ai/v2beta/stable-image/generate/core"

    headers = {
        "Authorization": f"Bearer {IMAGE_API_KEY}",
        "Accept": "image/*",  # Must explicitly request image response
    }

    # Must be multipart/form-data
    files = {
        "prompt": (None, prompt),
        "output_format": (None, "png"),
        "aspect_ratio": (None, "1:1"),
    }

    response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        file_path = os.path.join(IMAGE_OUTPUT_DIR, f"page_{page_number}.png")
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Image saved to {file_path}")
        return file_path
    else:
        print(response.text)
        raise Exception(f"Image generation failed: {response.status_code} {response.text}")

def generate_images_for_story(pages: List[str]) -> List[str]:
    """
    Generate and save images for each page of the story.
    Returns a list of image file paths.
    """
    image_paths = []
    for i, page_text in enumerate(pages, 1):
        image_path = generate_image(prompt=page_text, page_number=i)
        image_paths.append(image_path)
    return image_paths
