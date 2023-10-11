import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from testcases.Config.config import TestData
from testcases.objects.utilities import utilities
from selenium.webdriver.support.ui import Select


class BookTicket(utilities):
    depart = (By.ID, "depart_city")
    destination = (By.ID, "dest_city")
    date = (By.ID, "depart_date")
    fromdate = (By.LINK_TEXT, "29")
    traveller = (By.ID, "traveller")
    nationality = (By.ID, "nationality")
    adultadd = (By.XPATH, "//button[contains(@class , 'button-plus') and contains( @ data-field, 'adults')]")
    childadd = (By.XPATH, "//button[contains(@class , 'button-plus') and contains( @ data-field, 'children')]")
    childminus = (By.XPATH, "//button[contains(@class , 'button-minus') and contains( @ data-field, 'children')]")
    economy = (By.XPATH, "//label[@for='M']")
    search_flight = (By.ID, "btnFlightSearch")
    view_details = (By.XPATH, "//button[contains(@class, 'btn-book-now') and @data-flight-collapse-button='2']")
    book_now = (By.XPATH, "//button[contains(@class, 'btn-book-now') and @data-booking-num='2']")
    guest_login = (By.ID, "btnGuestBooking")
    baggage_info = (By.LINK_TEXT, "baggage information")
    guest_email = (By.ID, "emergency_email")
    guest_phone = (By.XPATH, "//input[@name='emergency_contact']")
    popup_confirm = (By.ID, "btnConfirmBookingSpecial")
    adult_fname = (By.XPATH, "//input[@name='adult_given_name[0]']")
    adult_lname = (By.XPATH, "//input[@name = 'adult_surname[0]']")
    child_fname = (By.XPATH, "//input[@name = 'child_given_name[0]']")
    child_lname = (By.XPATH, "//input[@name = 'child_surname[0]']")
    terms_agree = (By.XPATH, "//label[@for ='checkbox-iagree']")
    continue_booking = (By.XPATH, "//button[@class ='btn btn-danger btnConfirmBooking']")
    confirm = (By.ID, "btnConfirmBookingModal")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BaseUrl)
        self.driver.maximize_window()


    def bookTicket(self):
        self.click(self.depart)

        self.sendkeys(self.depart, Keys.ARROW_DOWN)
        self.sendkeys(self.depart, Keys.ARROW_DOWN)
        self.sendkeys(self.depart, Keys.RETURN)

        self.sendkeys(self.destination, Keys.ARROW_DOWN)
        self.sendkeys(self.destination, Keys.RETURN)

        self.click(self.fromdate)
        self.click(self.nationality)

        element = self.driver.find_element(*self.nationality)
        select = Select(element)
        select.select_by_visible_text('Nepalese')

        self.click_js(self.childadd)
        self.click_js(self.economy)
        self.click(self.search_flight)

        time.sleep(2)
        self.sendkeys(self.view_details, Keys.PAGE_DOWN)
        self.click_js(self.view_details)
        self.click_js(self.book_now)

        self.click(self.guest_login)
        self.click(self.popup_confirm)

    def fillEmailInfo(self, email, contact):
        self.sendkeys(self.guest_email, email)
        self.sendkeys(self.guest_phone, contact)

    def fillAdultInfo(self, adultfname, adultlname):
        self.sendkeys(self.adult_fname, adultfname)
        self.sendkeys(self.adult_lname, adultlname)

    def fillChildInfo(self, childFname, childLname):
        self.sendkeys(self.child_fname, childFname)
        self.sendkeys(self.child_lname, childLname)

    def confirmBook(self):
        self.click_js(self.terms_agree)
        self.click_js(self.continue_booking)
        self.click_js(self.confirm)

