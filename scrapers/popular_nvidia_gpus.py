from bs4 import BeautifulSoup
from utils import start_session, end_session

URL = "https://www.techpowerup.com/gpu-specs/"


def scrap_nvidia_popular_gpus():
    driver = start_session(URL)

    end_session(driver)


scrap_nvidia_popular_gpus()
