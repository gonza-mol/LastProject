import time
import pytest
import unittest
import sys
import os

from selenium.webdriver.common import alert
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from POM.ContactUsPage import ContactUsPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from Utils.BaseClass import BaseClass

@pytest.mark.usefixtures("test_setup")
class TestContactUsForm(BaseClass):

    def test_ContactUs_Form(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.select_ContactUs()
        self.driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(3)
        cp = ContactUsPage(driver)
        assert "GET IN TOUCH" == cp.getTitleContactUsForm()
        print("Estamos en el formulario de ContactUs")
        cp.completeForm("pedro", "pedro.molina@hotmail.com", "Example", "Esto es para ver si se completa o no")
        time.sleep(3)
        alertpop = driver.switch_to.alert
        time.sleep(3)
        alerttext = alertpop.text
        assert "Press OK to proceed!" == alerttext
        print("Se puede visualizar el texto del pop up " + alerttext)
        alertpop.accept()
        time.sleep(3)
        assert "Success! Your details have been submitted successfully." == cp.getAlertSuccess()
        print("Se pudo enviar correctamente el formulario")
        cp.selectBtnReturnHomePage()
        time.sleep(3)
