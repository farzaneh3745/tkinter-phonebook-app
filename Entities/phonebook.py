from Entities.contact import Contact

class Phonebook:
    def __init__(self,contact_list):
        self.contact_list=contact_list
        self.show_contact_list=self.contact_list.copy()

    def create(self,firstname,lastname,phone):
        new_id=len(self.contact_list)+1
        new_contact=Contact(new_id,firstname,lastname,phone)
        self.contact_list.append(new_contact)
        self.show_contact_list.append(new_contact)

    def delete(self,id):
        for contact in self.contact_list:
            if contact.id==id:
                self.contact_list.remove(contact)

        self.show_contact_list.clear()
        self.show_contact_list=self.contact_list.copy()

    def search(self,term):
        self.show_contact_list.clear()
        for contact in self.contact_list:
            if term in contact.first_name or term in contact.last_name or term in contact.phone_number:
                self.show_contact_list.append(contact)

    def get_contact_by_id(self,id):
        for contact in self.show_contact_list:
            if contact.id==id:
                return contact
