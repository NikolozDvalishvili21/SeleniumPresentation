from selenium import webdriver
from selenium.webdriver.common.keys import By

# ვებდრაივერის ინიცილიაზაცია 
driver = webdriver.Chrome()  

# ხსნის tkt.ge-ს
driver.get("https://tkt.ge/") 

# აfull-screen-ებს window-ს
driver.maximize_window()

# ეძებს და აკლიკებს "კონცერტების" ბათონს
concerts_link = driver.find_element(By.LINK_TEXT, "კონცერტები")  
concerts_link.click()         


print("Page Title:", driver.title)  

driver.quit()
