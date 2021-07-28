from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")
elem = driver.find_element_by_name("q") # 크롬 검색 element 네임
elem.send_keys("조코딩")  # 검색하는 값 넣는것
elem.send_keys(Keys.RETURN) # 자동으로 엔터값 넣어줘서 위의 값을 검색해줌


images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd") # elements 리스트로 저장, 작은 이미지들
count = 1
for image in images:
    try:
        image.click() # 큰 이미지 클릭
        time.sleep(1)
        imgUrl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img").get_attribute("src") # 큰이미 주소 가져옴
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg") # 이미지 다운받는 코드를 이러한 이름으로 저장하겠다고함.
        count = count +1 # 
    except:
        break