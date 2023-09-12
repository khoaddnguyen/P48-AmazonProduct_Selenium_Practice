from selenium import webdriver
from selenium.webdriver.common.by import By

ITEM_LINK="https://www.amazon.com/Breville-BES870XL-Barista-Express-Espresso/dp/B00CH9QWOU/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=8FfYN&content-id=amzn1.sym.225b4624-972d-4629-9040-f1bf9923dd95%3Aamzn1.symc.40e6a10e-cbc4-4fa5-81e3-4435ff64d03b&pf_rd_p=225b4624-972d-4629-9040-f1bf9923dd95&pf_rd_r=8M2Q5XKB2CR6RMJAHT3R&pd_rd_wg=101qg&pd_rd_r=cee8a935-9eb8-4d52-a8ab-c71e8c23583f&pd_rd_i=B00CH9QWOU&th=1"

# Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(ITEM_LINK)

# Search by locator: CLASS_NAME
price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#print(f"The price is {price_dollar.text}.{price_cents.text}")

# Search by name
add_to_cart = driver.find_element(By.NAME, value="submit.add-to-cart")
# print(add_to_cart.tag_name)  # result is input

# Search by id
button = driver.find_element(By.ID, value="add-to-cart-button")
# print(button.value)

# Search by CSS_SELECTOR
store_link = driver.find_element(By.CSS_SELECTOR, value=".a-section a")
# print(store_link.text)

# Search by XPATH (right click to copy xpath of the element
info_link = driver.find_element(By.XPATH, value='//*[@id="navFooter"]/div[1]/div/div[5]/ul/li[1]/a')
print(info_link.text)


# driver.close()  # close tab
driver.quit()  # quit entire browser