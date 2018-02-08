import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestOne(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS(executable_path='phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
        self.driver.set_window_size(1120, 550)

    def test_create_user(self):
        self.driver.get("http://atomicboard.devman.org/create_test_user/")
        self.driver.find_element_by_tag_name('button').click()
        correct_response = self.driver.find_elements_by_tag_name('p')[1].text
        self.assertEqual(correct_response, 'Сделано. Пользователь создан и авторизован')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
