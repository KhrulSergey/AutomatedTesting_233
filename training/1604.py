# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import unittest
import requests
import datetime
import locale
import pytils
from enum import Enum



class new (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_(self):
        driver = self.driver
        driver.get("https://gisp.gov.ru/ns-1604/collection/default")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Форма 2.10. Информация о производимой продукции и ее характеристиках'])[1]/following::a[1]").click()
        driver.find_element_by_link_text(u"Добавить продукцию").click()
        driver.find_element_by_id("form2-servicename").clear()
        driver.find_element_by_id("form2-servicename").send_keys(u"Тестовое наименование №1")
        driver.find_element_by_id("form2-servicenameen").clear()
        driver.find_element_by_id("form2-servicenameen").send_keys("test name #1")
        driver.find_element_by_id("form2-description").clear()
        driver.find_element_by_id("form2-description").send_keys("full text of product")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Единица измерения продукта / услуги'])[1]/following::span[5]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Подробное превью'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Подробное превью'])[1]/following::input[1]").send_keys(
            "796")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Подробное превью'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Код по ОКПД2'])[1]/following::span[5]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Подробное превью'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Подробное превью'])[1]/following::input[1]").send_keys(
            u"производст")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Код по ТН ВЭД (до шестого знака)'])[1]/following::span[5]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Подробное превью'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Подробное превью'])[1]/following::input[1]").send_keys(
            u"оливки")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Страна происхождения'])[1]/following::span[5]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Подробное превью'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Подробное превью'])[1]/following::input[1]").send_keys(
            u"Гре")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Подробное превью'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Отрасль, к которой принадлежит продукт'])[1]/following::input[2]").clear()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Отрасль, к которой принадлежит продукт'])[1]/following::input[2]").send_keys(
            u"пи")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Отрасль, к которой принадлежит продукт'])[1]/following::input[2]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Применимые технологические направления'])[1]/following::input[2]").clear()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Применимые технологические направления'])[1]/following::input[2]").send_keys(
            u"олив")
        driver.find_element_by_id("form2-opkproduct").click()
        driver.find_element_by_id("form2-opkproduct").click()
        driver.find_element_by_id("form2-thematiccatalogueid").click()
        Select(driver.find_element_by_id("form2-thematiccatalogueid")).select_by_visible_text(u"Каталоги Арктики")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Ключевые слова'])[1]/following::input[3]").click()
        driver.find_element_by_id("form2-industrialplatformtext").click()
        driver.find_element_by_id("form2-industrialplatformtext").click()
        driver.find_element_by_id("form2-industrialplatformtext").clear()
        driver.find_element_by_id("form2-industrialplatformtext").send_keys(u"адрес производства")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Добавить: Производимая продукция предприятия (Формы 2.10 и 2.11)'])[2]/following::a[2]").click()
        driver.find_element_by_id("form211-0-namedescription").click()
        driver.find_element_by_id("form211-0-namedescription").clear()
        driver.find_element_by_id("form211-0-namedescription").send_keys(u"супер характиристика")
        driver.find_element_by_id("select2-form211-0-okeiid-container").click()
        driver.find_element_by_id("form211-0-significance").click()
        driver.find_element_by_id("form211-0-value").clear()
        driver.find_element_by_id("form211-0-value").send_keys("4")
        driver.find_element_by_id("form211-0-significance").click()
        Select(driver.find_element_by_id("form211-0-significance")).select_by_visible_text(
            u"Дополнительная характеристика")
        driver.find_element_by_id("form211-0-significance").click()
        driver.find_element_by_id("form211-0-description").clear()
        driver.find_element_by_id("form211-0-description").send_keys(u"тест")
        driver.find_element_by_link_text(u"Сведения о стандартизации").click()
        driver.find_element_by_id("form2-designationstandard").click()
        driver.find_element_by_id("form2-designationstandard").clear()
        driver.find_element_by_id("form2-designationstandard").send_keys(u"Гост ХХ-454-5454545-4545")
        driver.find_element_by_id("form2-designationtechservice").click()
        driver.find_element_by_id("form2-designationtechservice").clear()
        driver.find_element_by_id("form2-designationtechservice").send_keys(u"ТУ-4566-4545-343434")
        driver.find_element_by_id("form2-techdocumenttitle").click()
        driver.find_element_by_id("form2-techdocumenttitle").clear()
        driver.find_element_by_id("form2-techdocumenttitle").send_keys(u"нормативный документ")
        driver.find_element_by_id("form2-techdocumentdescription").clear()
        driver.find_element_by_id("form2-techdocumentdescription").send_keys(u"документ")
        driver.find_element_by_id("form2-unspc").click()
        driver.find_element_by_id("form2-unspc").clear()
        driver.find_element_by_id("form2-unspc").send_keys("45345")
        driver.find_element_by_id("form2-gpc").click()
        driver.find_element_by_id("form2-gpc").clear()
        driver.find_element_by_id("form2-gpc").send_keys("1111111111")
        driver.find_element_by_id("form2-ean13").clear()
        driver.find_element_by_id("form2-ean13").send_keys("131313131313")
        driver.find_element_by_link_text(u"Спецификация продукта").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Закупочная цена'])[1]/following::div[1]").click()
        driver.find_element_by_id("form211spec-0-product").click()
        driver.find_element_by_id("form211spec-0-product").clear()
        driver.find_element_by_id("form211spec-0-product").send_keys(u"компонент")
        driver.find_element_by_id("select2-form211spec-0-okeiid-container").click()
        driver.find_element_by_id("form211spec-0-quantity").click()
        driver.find_element_by_id("form211spec-0-quantity").clear()
        driver.find_element_by_id("form211spec-0-quantity").send_keys("56")
        driver.find_element_by_id("form211spec-0-price").clear()
        driver.find_element_by_id("form211spec-0-price").send_keys("3453534")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Спецификация продукта'])[1]/following::a[1]").click()
        driver.find_element_by_id("form2-minimalquantity").clear()
        driver.find_element_by_id("form2-minimalquantity").send_keys("500")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Регионы поставки'])[1]/following::input[2]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='×'])[4]/following::input[1]").click()
        driver.find_element_by_id("form2-pricewithvat").click()
        driver.find_element_by_id("form2-pricewithvat").clear()
        driver.find_element_by_id("form2-pricewithvat").send_keys("7878")
        driver.find_element_by_id("form2-vatrate").click()
        driver.find_element_by_id("form2-vatrate").clear()
        driver.find_element_by_id("form2-vatrate").send_keys("13")
        driver.find_element_by_id("form2-availablequantity").click()
        driver.find_element_by_id("form2-availablequantity").clear()
        driver.find_element_by_id("form2-availablequantity").send_keys("999")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Доступное количество'])[1]/following::button[1]").click()
        # ERROR: Caught exception [unknown command []]

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
