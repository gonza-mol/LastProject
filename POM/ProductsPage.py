from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class ProductsPageLocators:
    searchBox = (By.ID, "search_product")
    menTshirtbox = (By.CSS_SELECTOR, "div>div:nth-child(4)>div")
    sliderColorForBox = (By.CSS_SELECTOR, "div:nth-child(4)>div div.product-overlay")
    titleTshirtbox = (By.CSS_SELECTOR, "div:nth-child(4)>div div.productinfo.text-center>p")
    linkBrandsPolo = (By.CSS_SELECTOR, "div.brands_products>div li:nth-child(1)")
    womenCategoryLink = (By.CSS_SELECTOR, "div:nth-child(1)>div.panel-heading>h4>a>span>i")
    dressCategoryLink = (By.CSS_SELECTOR, "#Women>div>ul>li:nth-child(1)>a")
    btnAddCart1 = (By.CSS_SELECTOR, "div:nth-child(3)>div>div.single-products>div.product-overlay>div>a")
    btnAddCart2 = (By.CSS_SELECTOR, "div:nth-child(4)>div>div.single-products>div.product-overlay>div>a")
    btnAddCart3 = (By.CSS_SELECTOR, "div:nth-child(5)>div>div.single-products>div.product-overlay>div>a")
    btnContinueShoppingPopUp = (By.CSS_SELECTOR, "#cartModal>div>div>div.modal-footer>button")
    listOfDresses = (By.CSS_SELECTOR, "#cart_info_table>tbody>tr")



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

    def addProductsToCart(self):
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(By.CSS_SELECTOR, "div.col-sm-9.padding-right>div>div:nth-child(3)>div"))
        hover.perform()
        self.driver.find_element(*ProductsPageLocators.btnAddCart1).click()
        self.driver.find_element(*ProductsPageLocators.btnContinueShoppingPopUp).click()
        time.sleep(2)
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(By.CSS_SELECTOR, "div.col-sm-9.padding-right>div>div:nth-child(4)>div"))
        hover.perform()
        self.driver.find_element(*ProductsPageLocators.btnAddCart2).click()
        self.driver.find_element(*ProductsPageLocators.btnContinueShoppingPopUp).click()
        time.sleep(2)
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(By.CSS_SELECTOR, "div.col-sm-9.padding-right>div>div:nth-child(5)>div"))
        hover.perform()
        self.driver.find_element(*ProductsPageLocators.btnAddCart3).click()
        self.driver.find_element(*ProductsPageLocators.btnContinueShoppingPopUp).click()
        time.sleep(2)



    def selectWomenCategoryIcon(self):
        self.driver.find_element(*ProductsPageLocators.womenCategoryLink).click()

    def selectDressWomenCategory(self):
        self.driver.find_element(*ProductsPageLocators.dressCategoryLink).click()

    def getQuantityLoadedDresses(self):
        return len(self.driver.find_elements(*ProductsPageLocators.listOfDresses))




