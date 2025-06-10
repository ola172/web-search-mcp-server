from typing import List
import validators


def validate_url(url: str):
    if not validators.url(url):
        raise ValueError("Provided url is not valid.")


def validate_urls(urls: List[str]):
    for url in urls:
        if not validators.url(url):
            raise ValueError(f"Provided url: {url} is not valid.")
