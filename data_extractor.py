import numpy as np
import requests

from utils import STR_TO_REMOVE
from bs4 import BeautifulSoup
from time import sleep
from tqdm import tqdm


def get_links(batch_size):
    webpage = requests.get(
        f"https://www.rbc.ru/v10/ajax/get-news-by-filters/?category=economics&offset={batch_size}&limit={batch_size}").json()
    webpage = BeautifulSoup(webpage["html"])
    lines = webpage.find_all("a", href=True)
    return [line["href"] for line in lines]


def extract_text(link, max_pause):
    sleep(np.random.randint(max_pause))
    content = BeautifulSoup(requests.get(link).text)
    header = content.find_all("title")[0].text
    for pattern in STR_TO_REMOVE:
        header = header.replace(pattern, "")
    text = content.find_all("p")
    text = [line.text.replace("\n", "").strip() for line in text]
    return header, text


def get_texts(batch_size, max_pause):
    links = get_links(batch_size)
    texts = []
    for link in tqdm(links, position=0, leave=True):
        output = extract_text(link, max_pause)
        texts.append(output)
    return texts

