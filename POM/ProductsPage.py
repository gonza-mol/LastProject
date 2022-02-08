from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ProductsPageLocators:
    searchBox = (By.ID, "search_product")
    menTshirtbox = (By.CSS_SELECTOR, "div>div:nth-child(4)>div")
    sliderColorForBox = (By.CSS_SELECTOR, "div:nth-child(4)>div div.product-overlay")
    titleTshirtbox = (By.CSS_SELECTOR, "div:nth-child(4)>div div.productinfo.text-center>p")
    linkBrandsPolo = (By.CSS_SELECTOR, "div.brands_products>div li:nth-child(1)")


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver


    def verify_SearchBox(self):
        return self.driver.find_element(*ProductsPageLocators.searchBox)


    def select_MenTshirtProduct(self):
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*ProductsPageLocators.menTshirtbox))
        hover.perform()

    def show_HoverMenTshirtProduct(self):
        return self.driver.find_element(*ProductsPageLocators.sliderColorForBox)


    def show_Title_TshirtBox(self):
        return self.driver.find_element(*ProductsPageLocators.titleTshirtbox).text


    def totalNumberBrandsPolo(self):
        return self.driver.find_element(*ProductsPageLocators.linkBrandsPolo).text

    def selectBrandsPolo(self):
        self.driver.find_element(*ProductsPageLocators.linkBrandsPolo).click()

