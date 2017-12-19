from selenium.webdriver.firefox.webdriver import WebDriver
from model.contact import Contact
from selenium.common.exceptions import NoSuchElementException
import re
class ContactHelper:


    def __init__(self, app):
        self.app = app

    def open_new_contact_page(self):
        # open new contact page
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def add_new_contact(self, contact):
        # create new contact
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.telephone_home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.telephone_mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.telephone_work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email_1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email_2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email_3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % contact.birthday_option_1).is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % contact.birthday_option_1).click()
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % contact.birthday_option_2).is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % contact.birthday_option_2).click()
        # wd.find_element_by_name("byear").click()
        # wd.find_element_by_name("byear").clear()
        # wd.find_element_by_name("byear").send_keys(contact.birthday_year)
        # wd.find_element_by_name("theform").click()
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % contact.anniversary_option_1).is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % contact.anniversary_option_1).click()
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % contact.anniversary_option_2).is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % contact.anniversary_option_2).click()
        # wd.find_element_by_name("ayear").click()
        # wd.find_element_by_name("ayear").clear()
        # wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        # wd.find_element_by_name("theform").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.secondary_address)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.home)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.select_contact_by_index(index)
        # wd.find_element_by_value("Delete").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        wd.implicitly_wait(4)
        self.open_contact_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def open_contact_page(self):
        # open contacts page
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        # wd.find_element_by_link_text("groups").click()
        # self.select_first_contact()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[%s]/td[8]/a/img" % index).click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.open_contact_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field("firstname", contact.name)
        self.change_field("lastname", contact.last_name)
        self.change_field("address", contact.address)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text != None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    contact_cache = None

    # def get_contact_list(self):
    #     if self.contact_cache is None:
    #
    #         wd = self.app.wd
    #         self.open_contact_page()
    #         self.contact_cache = []
    #         for element in wd.find_elements_by_css_selector("td.center"):
    #             test = self.if_element_present(element)
    #             if test == True:
    #                 name = element.find_element_by_name("selected[]").get_attribute("title")
    #                 id = element.find_element_by_name("selected[]").get_attribute("value")
    #                 lastname = element.find_element_by_name("selected[]").get_attribute("alt")
    #                 self.contact_cache.append(Contact(name=name, last_name = lastname, id = id))
    #     return list(self.contact_cache)

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                name = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                #print(address)
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(name = name, last_name=lastname, address=address, all_telephones_from_home_page=all_phones, all_emails_from_home_page=all_emails, id=id))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def if_element_present(self, element):
        wd = self.app.wd
        try:
            element.find_element_by_name("selected[]")
        except NoSuchElementException:
            return False
        return True

    def get_contact_info_from_edit_page(self, index):
        wd= self.app.wd
        self.open_contact_to_edit_by_index(index)
        name = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        telephone_home = wd.find_element_by_name("home").get_attribute("value")
        telephone_mobile = wd.find_element_by_name("mobile").get_attribute("value")
        telephone_work = wd.find_element_by_name("work").get_attribute("value")
        telephone_fax = wd.find_element_by_name("fax").get_attribute("value")
        address = wd.find_element_by_name("address").text
        email_1 = wd.find_element_by_name("email").get_attribute("value")
        email_2 = wd.find_element_by_name("email2").get_attribute("value")
        email_3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(name=name, last_name=lastname, telephone_home=telephone_home, address=address, email_1=email_1, email_2=email_2, email_3=email_3,
                       telephone_work=telephone_work, telephone_mobile=telephone_mobile, fax=telephone_fax, id= id)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        telephone_home = re.search("H: (.*)", text).group(1)
        telephone_work = re.search("W: (.*)", text).group(1)
        telephone_mobile = re.search("M: (.*)", text).group(1)
        telephone_fax = re.search("F: (.*)", text).group(1)
        return Contact(telephone_home=telephone_home, telephone_work=telephone_work,
                       telephone_mobile=telephone_mobile, fax=telephone_fax)
