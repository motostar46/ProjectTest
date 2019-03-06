import unittest
from selenium import webdriver


class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        cls.driver.get("https://www.dotabuff.com/players/93746209")

    def test_search_by_category(self):
        self.matches = self.driver.find_elements_by_xpath("//div[@class='r-fluid r-40 r-icon-text']"
                                                          "/div[@class='r-body']/a")
        self.array = []
        for every in self.matches:
            self.array.append(every.get_attribute("pathname")[9:])
        print('\n\n')
        for every in self.array:
            print('Match number:  ', every)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
