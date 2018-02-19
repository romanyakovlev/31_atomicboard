import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re

WAITING_TIME = 10


class TestOne(unittest.TestCase):

    def change_element_data(self, parent, keys_to_send, form_tag_name, form_element_tag_name,
    child_tag_name, is_textarea_in_form, *textarea_string):
        parent.find_element_by_tag_name(child_tag_name).click()
        form = parent.find_element_by_class_name(form_tag_name)
        form_element = form.find_element_by_tag_name(form_element_tag_name)
        form_element.send_keys(keys_to_send)
        if is_textarea_in_form:
            form_element.send_keys(textarea_string)
        form_element.submit()
        return parent.find_element_by_tag_name(child_tag_name).text

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
        self.driver.implicitly_wait(WAITING_TIME)
        driver = self.driver
        selected_ticket = driver.find_element_by_class_name('ticket__selected')

        ticket_title = selected_ticket.find_element_by_class_name('panel-heading-no-padding')
        title_to_check = self.change_element_data(
            ticket_title, Keys.CONTROL + "a", 'form-inline',
            'input', 'span', True, 'Хэй, это работает!'
        )

        ticket_description = selected_ticket.find_element_by_class_name('ticket_description')
        description_to_check = self.change_element_data(
            ticket_description, Keys.CONTROL + "a", 'form-inline',
            'textarea', 'div', True, 'Хэй, это работает опять!'
        )

        ticket_category = ticket_description.find_elements_by_tag_name('div')[1]
        category_to_check = self.change_element_data(
            ticket_category, Keys.DOWN, 'form-inline',
            'select', 'span', False,
        )

        difficulty_ticket = ticket_description.find_elements_by_tag_name('div')[2]
        difficulty_to_check = self.change_element_data(
            difficulty_ticket, Keys.DOWN, 'form-inline',
            'select', 'span', False,
        )

        ticket_class = selected_ticket.get_attribute('class')
        changed_ticket_class = re.search(r'js-ticket-(\d{1,})', ticket_class).group()

        driver.get("http://atomicboard.devman.org/")
        driver.implicitly_wait(WAITING_TIME)
        selected_ticket = driver.find_element_by_class_name('ticket__selected')
        selected_ticket.click()

        ticket_title = selected_ticket.find_element_by_class_name('panel-heading-no-padding')
        self.assertEqual(ticket_title.find_element_by_tag_name('span').text, title_to_check)

        ticket_description = selected_ticket.find_element_by_class_name('ticket_description')
        self.assertEqual(ticket_description.find_element_by_tag_name('div').text, description_to_check)

        ticket_category = ticket_description.find_elements_by_tag_name('div')[1]
        self.assertEqual(ticket_category.find_element_by_tag_name('span').text, category_to_check)

        difficulty_ticket = ticket_description.find_elements_by_tag_name('div')[2]
        self.assertEqual(difficulty_ticket.find_element_by_tag_name('span').text, difficulty_to_check)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
