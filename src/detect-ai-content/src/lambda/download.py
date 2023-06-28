import re

from bs4 import BeautifulSoup
import requests

def lambda_handler(event, context):
    r = requests.get(event['url'])

    soup = BeautifulSoup(r.text, 'html.parser')

    article = soup.find('article')

    for code in article.find_all('code'):
        code.replace_with('')
    for li in article.find_all('li'):
        li.replace_with('* ' + li.text)

    article_text = article.get_text()

    article_text = re.sub(r'\n{2,}', ' ', article_text)
    article_text = re.sub(r'[ ]+', ' ', article_text)
    article_text = re.sub(r'\.{2,}', ' ', article_text)

    result = ""

    for line in article_text.split('\n'):
        if len(line) > 20:
            result += line + '\n'

    return {
        "input": result
    }