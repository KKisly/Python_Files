
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
        wd.find_element_by_name("fax").send_keys(contact.fax_work)
        #wd.find_element_by_name("email").click()
        #wd.find_element_by_name("email").clear()
        #wd.find_element_by_name("email").send_keys(group.email_1)
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
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % contact.birthday_option_1).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % contact.birthday_option_1).click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % contact.birthday_option_2).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % contact.birthday_option_2).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birthday_year)
        wd.find_element_by_name("theform").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % contact.anniversary_option_1).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % contact.anniversary_option_1).click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % contact.anniversary_option_2).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % contact.anniversary_option_2).click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        wd.find_element_by_name("theform").click()
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

    def delete_first_contact(self):
        # open group page
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_name("selected[]").click()
        #wd.find_element_by_value("Delete").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()