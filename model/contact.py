#helper class for add contact page
from sys import maxsize

class Contact:

    def __init__(self, name=None, middle_name=None, last_name=None, nickname=None, title=None, company=None, address=None, telephone_home=None, telephone_mobile=None,
                 telephone_work=None, fax=None, email_1=None, email_2=None, email_3=None, homepage=None, secondary_address=None, home=None, notes=None, id=None,
                 all_telephones_from_home_page=None, all_emails_from_home_page=None):

        self.name = name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.telephone_home = telephone_home
        self.telephone_mobile = telephone_mobile
        self.telephone_work = telephone_work
        self.fax = fax
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        # self.birthday_option_1 = birthday_option_1
        # self.birthday_option_2 = birthday_option_2
        # self.birthday_year = birthday_year
        # self.anniversary_option_1 = anniversary_option_1
        # self.anniversary_option_2 = anniversary_option_2
        # self.anniversary_year = anniversary_year
        self.secondary_address = secondary_address
        self.home = home
        self.notes = notes
        self.id = id
        self.all_telephones_from_home_page = all_telephones_from_home_page
        self.all_emails_from_home_page=all_emails_from_home_page


    def __repr__(self):
        return "%s:%s%s:%s:%s" % (self.id, self.name, self.last_name, self.address, self.email_1)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id  == other.id) or self.name == other.name or self.last_name == other.last_name, self.address == other.address)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

