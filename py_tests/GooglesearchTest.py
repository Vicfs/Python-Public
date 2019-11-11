from selenium import webdriver
import unittest
import HtmlTestRunner

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver.exe')
        cls.browser.implicitly_wait(10)
        cls.browser.maximize_window()

    def test_google_search(self):
        self.browser.get('https://www.google.com/')
        self.browser.find_element_by_name('q').send_keys('busca teste')
        self.browser.find_element_by_name('btnK').click()

    def test_google_search_corinthians(self):
        self.browser.get('https://www.google.com/')
        self.browser.find_element_by_name('q').send_keys('corinthians')
        self.browser.find_element_by_name('btnK').click()

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
        print('Test completed.')

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Victor\\Desktop\\Python\\reports'))