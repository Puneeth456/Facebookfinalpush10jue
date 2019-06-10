
from selenium import webdriver
from selenium.webdriver.support.select import Select

Chunk=webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/chromedriver.exe")
Chunk.get("https://www.facebook.com/")

Chunk.find_element_by_name("firstname").send_keys("Puneeth")
Chunk.find_element_by_name("lastname").send_keys("B S")
Chunk.find_element_by_name("reg_email__").send_keys("9535468206")
Chunk.find_element_by_name("reg_passwd__").send_keys("preethiaunty")

day=Chunk.find_element_by_name("birthday_day")
s1=Select(day)
s1.select_by_visible_text("23")

month=Chunk.find_element_by_name("birthday_month")
s2=Select(month)
s2.select_by_value("9")

Year=Chunk.find_element_by_id("year")
s3=Select(Year)
s3.select_by_index("29")

Chunk.find_element_by_name("websubmit").click()

Chunk.quit()



