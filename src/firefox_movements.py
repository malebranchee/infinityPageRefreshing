from selenium import webdriver
import time

def page_refresh():
    driver = webdriver.Firefox()
    driver.get("https://m.avito.ru/omsk/kvartiry/3-k._kvartira_634m_510et._2920538390?context=H4sIAAAAAAAA_0q0MrSqLrYytFKqULIutjI2tFLKNKs0K8-tLDBLsSizSE5OT8zIrywoyky3NC0qyiw1U7KuBQQAAP__7KxayDUAAAA")
    while True: #infinity page refreshing
        driver.refresh()
        time.sleep(10)

