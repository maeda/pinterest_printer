import tempfile
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from wordcloud import WordCloud


def extract(url):
    elem = None
    driver = webdriver.Chrome()
    driver.get(url)

    try:
        sleep(3)
        elem = driver.find_elements(By.TAG_NAME, 'img')
        pin = [item for item in elem if item.get_attribute('class') == ""]
        url = pin[0].get_attribute('src')

        # Make a copy of relevant data, because Selenium will throw if
        # you try to access the properties after the driver quit
    finally:
        driver.close()

    return url


def download(url):
    import requests
    r = requests.get(url, allow_redirects=True)
    fp = tempfile.NamedTemporaryFile(delete=False)
    fp.write(r.content)

    return fp.name


def send_to_printer(file):
    import subprocess

    subprocess.run(['lp', file])


def run(url):
    url = extract(url)
    file = download(url)
    send_to_printer(file)


if __name__ == "__main__":
    urls = [
        # 'https://pin.it/66Ete1s',
        # 'https://pin.it/53EfAmi',
        'https://pin.it/1adMt7h',
        'https://pin.it/4aLPWDl',
        'https://pin.it/5xcUa7O',
        'https://pin.it/1wpnKMn',
        'https://pin.it/2p07vCA',
        'https://pin.it/21vOWFd',
        'https://pin.it/1tOLWRI',
        'https://pin.it/6HWscpV',
        'https://pin.it/2yAoSLo',
        'https://pin.it/71Zf2Hn',
        'https://pin.it/6a8Pdhu',
        'https://pin.it/1EZqdfs',
        'https://pin.it/5BWxDVw',
        'https://pin.it/7yfGCbf',
        'https://pin.it/63uwxmf',
        'https://pin.it/2r1jorV',
        'https://pin.it/2Ydo6Y1',
        'https://pin.it/2kRrNIO',
        'https://pin.it/11z4ZaV',
        'https://pin.it/2hNYWfK',
        'https://pin.it/1XaOH5e',
        'https://pin.it/2VdnSzR',
        'https://pin.it/3ZiCyzG',
        'https://pin.it/43p1S9M',
        'https://pin.it/5szztKA',
        'https://pin.it/36w58cj',
        'https://pin.it/1wOgYci',
        'https://pin.it/6ZCYuL4',
        'https://pin.it/79jDWbn',
        'https://pin.it/3YsXzvL',
        'https://pin.it/5Ak9WPq',
        'https://pin.it/7yYL6wP',
        'https://pin.it/3M9LDPD',
        'https://pin.it/2oEV3QU',
        'https://pin.it/36yrJh0',
        'https://pin.it/3pjyXMN',
        'https://pin.it/31EzyTB',
        'https://pin.it/7882XsI',
        'https://pin.it/26jwt7n',
        'https://pin.it/1WQYi5m',
        'https://pin.it/4oinQCN',
        'https://pin.it/4o6xiM2',
        'https://pin.it/7FYhJAt',
        'https://pin.it/24BYXBe',
        'https://pin.it/5uPzy3V',
        'https://pin.it/5WXlbXT',
        'https://pin.it/10tiPbM',
        'https://pin.it/5ApyzjD',
        'https://pin.it/2E3ex1a',
        'https://pin.it/4QZiBh2',
        'https://pin.it/6488Lcg',
        'https://pin.it/2tYgKsM',
        'https://pin.it/zL4YdX1',
        'https://pin.it/110D8wc',
        'https://pin.it/110Bdct',
        'https://pin.it/2pP3KCh',
        'https://pin.it/3W4mTTF',
        'https://pin.it/3MJNY8v',
        'https://pin.it/3mTcaDM',
        'https://pin.it/5QkV76d',
        'https://pin.it/4hzlhC4',
        'https://pin.it/1xDG8yi',
        'https://pin.it/3MWfswa',
        'https://pin.it/YkSmO26',
        'https://pin.it/5WnbyS6',
        'https://pin.it/6IioWhA',
        'https://pin.it/6vTNkzr',
        'https://pin.it/7I8ixxa',
        'https://pin.it/4JPcU4w',
        'https://pin.it/6RRyDZC',
        'https://pin.it/4rFvsYR',
        'https://pin.it/4MxZsa1',
        'https://pin.it/15b2Ac8',
        'https://pin.it/5E3P0kB',
        'https://pin.it/4GtvtZk',
        'https://pin.it/4cwbwz5',
        'https://pin.it/2G9670Z',
        'https://pin.it/6Gq8XY0',
        'https://pin.it/32K7Epx',
        'https://pin.it/6lW3n3h',
        'https://pin.it/1JsLc6X',
        'https://pin.it/64IjV2Q',
        'https://pin.it/2vbIVX9',
        'https://pin.it/520Q4sT',
        'https://pin.it/O7u8gsx',
        'https://pin.it/3uBA5Lr',
        'https://pin.it/j5hj6lI',
        'https://pin.it/24SlhpR',
        'https://pin.it/u75YAHw',
        'https://pin.it/7G38wIa',
        'https://pin.it/7oU6nIB',
        'https://pin.it/7wSvot0',
        'https://pin.it/5Jqgava',
        'https://pin.it/4N6AUw5',
        'https://pin.it/2nn2Nfk',
        'https://pin.it/5Dt6NHA',
        'https://pin.it/4WRS3Iw',
        'https://pin.it/6GDfLcV',
        'https://pin.it/8F1FDnW',
        'https://pin.it/4coUIhx',
        'https://pin.it/59is3ad',
        'https://pin.it/6wsXNA9',
        'https://pin.it/1ePS1IY',
        'https://pin.it/5KpFTKr',
        'https://pin.it/WK6HPZU',
        'https://pin.it/3CgNHwK',
        'https://pin.it/YYvYoLy',
        'https://pin.it/4KxcuKw',
        'https://pin.it/4kY8lbj',
        'https://pin.it/4NPV5es',
        'https://pin.it/3hA2yAQ',
        'https://pin.it/m2lnPXi',
        'https://pin.it/8reLvO9',
        'https://pin.it/7HEW2LK',
        'https://pin.it/6ipwthx',
        'https://pin.it/1N1TcAZ',
        'https://pin.it/2Wdb0WP',
        'https://pin.it/4pTOV8F',
        'https://pin.it/5R1x7wV',
        'https://pin.it/18XVsET',
        'https://pin.it/58FqlxX',
    ]

    for url in urls:
        print(url)
        run(url)


