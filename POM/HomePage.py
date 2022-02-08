from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePageLocators:
    signInlink = (By.CSS_SELECTOR, "#header ul>li:nth-child(4)>a")
    logoutLink = (By.CSS_SELECTOR, "div.col-sm-8>div>ul>li:nth-child(4)>a")
    loggedLink = (By.CSS_SELECTOR, "li:nth-child(9)>a")
    footerSubscriptionTitle = (By.CSS_SELECTOR, "div.col-sm-3.col-sm-offset-1>div>h2")
    footerSubscriptionSubtitle = (By.CSS_SELECTOR, "div>form>p")
    alertSubscriptionSuccess = (By.CSS_SELECTOR, "#success-subscribe>div")
    boxSubscription = (By.ID, "susbscribe_email")
    btnSubscription = (By.ID, "subscribe")
    productsLink = (By.CSS_SELECTOR, "#header ul>li:nth-child(2)>a")
    brandProductsList = (By.CSS_SELECTOR, "div.brands_products>div>ul>li")
    brandsTitle = (By.CSS_SELECTOR, "div.brands_products>h2")
    contactUsLink = (By.CSS_SELECTOR, "div.col-sm-8>div>ul>li:nth-child(7)>a")
    categoryWomenLink = (By.CSS_SELECTOR, "div:nth-child(1)>div.panel-heading>h4>a>span>i")
    categoryWomenTopsLink = (By.CSS_SELECTOR, "#Women>div>ul>li:nth-child(2)>a")
    sliderWithPriceAndProduct = (By.CSS_SELECTOR, "div:nth-child(3)>div>div.single-products>div.product-overlay>div")


class HomePage:

    def __init__(self, driver):
        self.driver = driver


    def select_SignIn(self):
        self.driver.find_element(*HomePageLocators.signInlink).click()

    def select_Logout(self):
        self.driver.find_element(*HomePageLocators.logoutLink).click()

    def verify_Logged(self):
        return self.driver.find_element(*HomePageLocators.loggedLink).text

    def show_FooterTitle(self):
        return self.driver.find_element(*HomePageLocators.footerSubscriptionTitle).text

    def show_FooterSubTitle(self):
        return self.driver.find_element(*HomePageLocators.footerSubscriptionSubtitle).text

    def show_Alert_SubscriptionSuccess(self):
        return self.driver.find_element(*HomePageLocators.alertSubscriptionSuccess).text

    def sendEmailBoxSubscription(self, email):
        self.driver.find_element(*HomePageLocators.boxSubscription).send_keys(email)
        self.driver.find_element(*HomePageLocators.btnSubscription).click()


    def select_Products(self):
        self.driver.find_element(*HomePageLocators.productsLink).click()

    def scrollDownUntilBrandProducts(self):
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*HomePageLocators.brandsTitle))
        hover.perform()

    def getAllBrandProducts(self):
        return self.driver.find_elements(*HomePageLocators.brandProductsList)


    def select_ContactUs(self):
        self.driver.find_element(*HomePageLocators.contactUsLink).click()


    def selectCategoryWomen(self):
        self.driver.find_element(*HomePageLocators.categoryWomenLink).click()


    def selectCategoryWomenTops(self):
        self.driver.find_element(*HomePageLocators.categoryWomenTopsLink).click()

    def verifyLoggedOut(self):
        return self.driver.find_element(*HomePageLocators.signInlink)


