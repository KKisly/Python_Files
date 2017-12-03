from model.group import Group

class GroupHelper:


    def __init__(self, app):
        self.app = app

    def retrun_to_groups_page(self):
        # return to group page
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def open_groups_page(self):
        # open group page
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        # init group creation
        wd = self.app.wd
        wd.find_element_by_name("new").click()
        # fill group firm
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.group_cache = None

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field("group_name", group.name)
        self.change_field("group_header", group.header)
        self.change_field("group_footer", group.footer)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text != None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_group_by_index(self, index):
        # open group page
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        #wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("delete").click()
        self.retrun_to_groups_page()
        self.group_cache = None

    def select_group_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def delete_first_group(self):
        self.delete_group_by_index(0)

    def modify_first_group(self, new_group_data):
        self.modify_group_by_index(0, new_group_data)


    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        #wd.find_element_by_link_text("groups").click()
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        wd.find_element_by_name("update").click()
        self.retrun_to_groups_page()
        self.group_cache = None


    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)


