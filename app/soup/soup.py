from bs4 import BeautifulSoup
from urllib.request import urlopen
from re import compile
from config import FILETYPE


def check_for_duplicates(files):
    seen = set()
    for file in files:
        if file not in seen:
            seen.add(file)
    return seen


def make_soup(url):
    try:
        website = urlopen(url)
    except ValueError:
        return
    soup = BeautifulSoup(website, "html.parser")

    files = []
    for file in soup.findAll('a', href=compile(str(FILETYPE))):
        files.append(file['href'])

    files = check_for_duplicates(files)

    return files
