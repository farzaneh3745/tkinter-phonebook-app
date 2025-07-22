class Contact:
    def __init__(self,id,firstname,lastname,phone):
        self.id=id
        self.first_name=firstname
        self.last_name=lastname
        self.phone_number=phone

    def edit(self,new_firstname,new_lastname,new_phone):
        self.first_name=new_firstname
        self.last_name=new_lastname
        self.phone_number=new_phone

    def object_to_string(self):
        return f"{self.id},{self.first_name},{self.last_name},{self.phone_number}"