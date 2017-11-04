#helper class for add contact page

class Contact:

    def __init__(self, name, middle_name, last_name, nickname, title, company, address, telephone_home, telephone_mobile,
                 telephone_work, fax_work, email_1, email_2, email_3, homepage, birthday_option_1, birthday_option_2,
                 birthday_year, anniversary_option_1, anniversary_option_2, anniversary_year, secondary_address, home, notes):

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
        self.fax_work = fax_work
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.birthday_option_1 = birthday_option_1
        self.birthday_option_2 = birthday_option_2
        self.birthday_year = birthday_year
        self.anniversary_option_1 = anniversary_option_1
        self.anniversary_option_2 = anniversary_option_2
        self.anniversary_year = anniversary_year
        self.secondary_address = secondary_address
        self.home = home
        self.notes = notes
