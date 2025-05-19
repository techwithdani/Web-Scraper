from bs4 import BeautifulSoup
from utils import start_session, end_session

URL = "https://www.techpowerup.com/gpu-specs/"


def scrap_nvidia_popular_gpus():
    driver = start_session(URL)

    the_soup = BeautifulSoup(driver.page_source, "html.parser")

    header = the_soup.find("thead", class_="colheader")
    header_child = header.find_next("tr")
    attributes = header_child.find_all("th")

    cleaned_attributes = []

    for th in attributes:
        text = th.string
        cleaned_attributes.append(text)

    del attributes

    end_session(driver)


scrap_nvidia_popular_gpus()
