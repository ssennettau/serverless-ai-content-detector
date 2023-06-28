from bs4 import BeautifulSoup
import requests

def lambda_handler(event, context):
    r = requests.get(event['url'])

    soup = BeautifulSoup(r.text, 'html.parser')

    article = soup.find('article')
    article_text = article.get_text()

    split = []

    for a in article_text.split('\n\n'):
        a = a.replace('\n', ' ')
        a = ' '.join(a.split())

        if a == '':
            print("emptyone")
        elif len(a.split(' ')) < 6:
            print("short ")
            print(a)
            continue
        else:
            print("living " + str(len(a)))
            split.append(a)

    # chop shop time
    split_consolidated = []
    current_element = ''
    for s in split:
        if len(current_element) + len(s) > 500:
            current_element = current_element.replace('\n', ' ')
            split_consolidated.append(current_element)
            current_element = ''
        current_element += s
    
    return {
        "chunks": split_consolidated
    }