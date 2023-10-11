import time

from testcases.Config.config import TestData
from testcases.objects.bookTicket import BookTicket
from testcases.testScenarios.test_base import BaseTest


class Test_book(BaseTest):
    def test_bookticket(self):
        self.book = BookTicket(self.driver)
        self.book.bookTicket()
        self.book.fillEmailInfo(TestData.User_email, TestData.User_contact)
        self.book.fillAdultInfo(TestData.Adult_fname, TestData.Adult_lname)
        time.sleep(2)
        self.book.fillChildInfo(TestData.Child_fname, TestData.Child_lname)
        time.sleep(5)
        self.book.confirmBook()
        time.sleep(10)
