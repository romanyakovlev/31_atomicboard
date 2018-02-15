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

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re

WAITING_TIME = 10

class TestOne(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS(executable_path='phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
        self.driver.set_window_size(1120, 550)
        self.driver.implicitly_wait(WAITING_TIME)
        self.driver.get("http://atomicboard.devman.org/create_test_user/")
        self.driver.find_element_by_tag_name('button').click()
        correct_response = self.driver.find_elements_by_tag_name('p')[1].text
        self.assertEqual(correct_response, 'Сделано. Пользователь создан и авторизован')

    def test_load_page_and_tasks(self):
        self.driver.get("http://atomicboard.devman.org/")
        self.remember_page = self
        tickets_count = len(self.driver.find_elements_by_class_name('js-ticket'))
        self.assertTrue(tickets_count is not 0)

    def test_load_page_and_tasks(self):
        self.driver.get("http://atomicboard.devman.org/")
        ticket_for_editing = self.driver.find_element_by_class_name('js-ticket')
        print(tick)

    def tearDown(self):
        self.driver.quit()


#if __name__ == '__main__':
#    unittest.main()


def change_element_data(parent, keys_to_send, form_tag_name, form_element_tag_name,
child_tag_name, is_textarea_in_form, *textarea_string):
    parent.find_element_by_tag_name(child_tag_name).click()
    form = parent.find_element_by_class_name(form_tag_name)
    form_element = form.find_element_by_tag_name(form_element_tag_name)
    form_element.send_keys(keys_to_send)
    if is_textarea_in_form:
        form_element.send_keys(textarea_string)
    form_element.submit()


driver = webdriver.PhantomJS(executable_path='phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
driver.set_window_size(1120, 550)
driver.get("http://atomicboard.devman.org/create_test_user/")
driver.find_element_by_tag_name('button').click()
driver.get("http://atomicboard.devman.org/")
driver.implicitly_wait(WAITING_TIME)
selected_ticket = driver.find_element_by_class_name('ticket__selected')
driver.save_screenshot("screenshot.png")

# нажимаем на заголовок тикета и изменяем его
ticket_title = selected_ticket.find_element_by_class_name('panel-heading-no-padding')
change_element_data(
    ticket_title, Keys.CONTROL + "a", 'form-inline', 
    'input', 'span', True, 'Хэй, это работает!'
)


# нажимаем на описание тикета и изменяем его
ticket_description = selected_ticket.find_element_by_class_name('ticket_description')
change_element_data(
    ticket_description, Keys.CONTROL + "a", 'form-inline', 
    'textarea', 'div', True, 'Хэй, это работает опять!'
)

# нажимаем на категорию тикета и изменяем её
ticket_category = ticket_description.find_elements_by_tag_name('div')[1]
change_element_data(
    ticket_category, Keys.DOWN, 'form-inline', 
    'select', 'span', False,
)

# нажимаем на сложность тикета и изменяем её
difficulity_ticket = ticket_description.find_elements_by_tag_name('div')[2]
change_element_data(
    difficulity_ticket, Keys.DOWN, 'form-inline', 
    'select', 'span', False,
)


ticket_class = selected_ticket.get_attribute('class')
changed_ticket_class = re.search(r'js-ticket-(\d{1,})', ticket_class).group()

driver.get("http://atomicboard.devman.org/")
driver.implicitly_wait(WAITING_TIME)
selected_ticket = driver.find_element_by_class_name('ticket__selected')
selected_ticket.click()
driver.save_screenshot("screenshot.png")

# проверка заголовка
ticket_title = selected_ticket.find_element_by_class_name('panel-heading-no-padding')


if __name__ == '__main__':
    unittest.main()
