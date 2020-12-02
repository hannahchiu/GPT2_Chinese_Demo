import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/56.0.2924.87 Safari/537.36'}


def crawl(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    div = soup.select(".mw-parser-output")[0]
    # for elm in div.find_all(recursive=False):
    #     if elm.name in ['p', 'dl']:
    #         print(elm.text, end='')
    content = div.text
    start_index = content.find("第")
    end_index = content.find("\n返回頁首")
    content = content[start_index:end_index]
    content = content.replace("全書終\n\n\n\n\n\n\n", "").replace("下一回▶\n\n\n\n\n\n\n", "")
    content = content.strip()
    return content


if __name__ == '__main__':
    with open("data/sanguoyanyi.txt", "w") as w:
        for i in tqdm(range(1, 121)):
            url = f"https://zh.wikisource.org/wiki/三國演義/第{i:03d}回"
            content = crawl(url)
            print(content, end='\n\n\n', file=w)
