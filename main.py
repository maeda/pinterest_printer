import tempfile
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def extract(url):
    driver = webdriver.Chrome()
    driver.get(url)

    try:
        sleep(3)
        elem = driver.find_elements(By.TAG_NAME, 'img')
        pin = [item for item in elem if item.get_attribute('class') == ""]
        url = pin[0].get_attribute('src')

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
        'https://pin.it/66Ete1s',
        'https://pin.it/53EfAmi',
    ]

    for url in urls:
        print(url)
        run(url)


