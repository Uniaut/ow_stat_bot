import requests

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR")

driver = webdriver.Chrome('C:/chromedriver', chrome_options=options)
print('Selenium Ready')

def quit_sele():
    global driver
    driver.quit()
    print('Selenium Quit')

import atexit
atexit.register(quit_sele)

soup = BeautifulSoup(requests.get('https://google.com').text, 'html.parser')

def alert_check():
    global driver
    try:
        WebDriverWait(driver, 7).until(
            expected_conditions.alert_is_present(),
                'Timed out waiting for PA creation ' +
                'confirmation popup to appear.'
        )
        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")
        return True
    except TimeoutException:
        print("no alert")
        return False


def read(name, code):
    global driver

    try:
        driver.switch_to_alert().accept()
    except:
        pass

    driver.implicitly_wait(2)
    driver.get(
        'https://overwatch.op.gg/search/?playerName=' + name + '%23' + code)
    html = driver.page_source
    global soup
    soup = BeautifulSoup(html, 'html.parser')

def update(name, code):
    global driver
    driver.find_element_by_xpath(
        '//*[@id="PlayerLayoutHeader"]/div/div[2]/ul/li[1]/button'
    ).click()

def valid():
    global soup
    prof = soup.select('#PlayerLayoutHeader > div > div.PlayerInfo')
    if len(prof) == 0:
        return False
    else:
        return True

def get_score():
    global soup
    score = soup.select(
        '#PlayerLayoutContent > div > div:nth-child(1) > div:nth-child(1) >'
        + ' div > div.SkillRating > h2 > b'
        )[0]
    return score.string

def get_tier_ai():
    global soup
    ai = soup.select(
        '#PlayerLayoutContent > div > div:nth-child(1) > div:nth-child(1) >'
        + ' div > div.SkillRating > img'
    )[0]
    return ai['src']
def get_rank():
    global soup
    rank = soup.select(
        '#PlayerLayoutContent > div > div:nth-child(1) > div:nth-child(1) >'+
        ' div > div.SkillRating > em'
    )[0]
    return rank.string
def get_pt():
    global soup
    pt = soup.select(
        '#PlayerLayoutContent > div > div:nth-child(1) > div:nth-child(1) > div >' +
        ' div.PlayerSummaryStats > div:nth-child(3) > span'
    )[0]
    return pt.string


def get_hero_pic(index):
    global soup
    icon = soup.select(
        '#PlayerLayoutContent > div > div.MainContent > div.ChampionStatsTable >'+
        ' table > tbody > tr > td.ContentCell.ContentCell-Hero > div > img'
    )[index]
    return icon['src']

def get_hero_name(index):
    global soup
    name = soup.select(
        '#PlayerLayoutContent > div > div.MainContent > div.ChampionStatsTable >'+
        ' table > tbody > tr > td.ContentCell.ContentCell-Hero'
    )[index]
    return ''.join(name.text.split())

def get_hero_pt(index):
    global soup
    pt = soup.select(
        '#PlayerLayoutContent > div > div.MainContent > div.ChampionStatsTable >'+
        ' table > tbody > tr > td:nth-child(8)'
    )[index]
    return pt.string

def get_hero_pp(index):
    portion = pt_to_min(get_hero_pt(index)) / pt_to_min(get_pt())
    return str(round(portion * 100, 1)) + '%'

def get_hero_vd(index):
    global soup
    vd = soup.select(
        '#PlayerLayoutContent > div > div.MainContent > div.ChampionStatsTable >'+
        ' table > tbody > tr > td:nth-child(4)'
    )[index]
    return ''.join(vd.text.split())

def get_hero_kd(index):
    global soup
    kd = soup.select(
        '#PlayerLayoutContent > div > div.MainContent > div.ChampionStatsTable >'+
        ' table > tbody > tr > td.ContentCell.ContentCell-KD > b'
    )[index]
    return kd.string

def pt_to_min(pt = ''):
    if pt.endswith('시간'):
        return int(pt.replace('시간', '')) * 60
    elif pt.endswith('분'):
        return int(pt.replace('분', ''))
    else:
        return 0

def get_last_up():
    global soup
    last_up = soup.select(
        '#PlayerLayoutHeader > div > div.PlayerInfo > div.LastUpdated > b'
    )[0]
    return last_up.string
