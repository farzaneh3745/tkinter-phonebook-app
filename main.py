from tkinter import Tk,Label,Entry,Button
from tkinter.ttk import Treeview
from Entities.phonebook import Phonebook

phonebook=Phonebook([])
phonebook.create("Sara","Jackson",phone="09129083490")
phonebook.create("Maria","White",phone="09111082200")
phonebook.create("Liana","Wilson",phone="09102081190")
phonebook.create("Mark","Smith",phone="09142080090")

window=Tk()
window.title("Phone Book Application")
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)
window.grid_rowconfigure(2, weight=1)

search_label=Label(window,text="Search")
search_label.grid(row=0,column=0,padx=10,pady=10,sticky="w")

search_entry=Entry(window,width=50)
search_entry.grid(row=0,column=1,columnspan=3,padx=(0,10),pady=10,sticky="ew")

def search_button_clicked():
    term=search_entry.get()
    phonebook.search(term)
    load_treeview()

search_button=Button(window,text="Search",command=search_button_clicked)
search_button.grid(row=0,column=4,padx=(0,10),pady=10,sticky="e")

def show_contact_form(update_id=None):
    contact_form=Tk()
    contact_form.title("Update Contact" if update_id else "Create Contact")

    firstname_label=Label(contact_form,text="First Name")
    firstname_label.grid(row=0,column=0,padx=10,pady=10,sticky="w")

    firstname_entry=Entry(contact_form,width=30)
    firstname_entry.grid(row=0,column=1,padx=10,pady=10,sticky="ew")

    lastname_label = Label(contact_form, text="Last Name")
    lastname_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    lastname_entry=Entry(contact_form,width=30)
    lastname_entry.grid(row=1, column=1, padx=10,pady=10,sticky="ew")

    phone_label = Label(contact_form, text="Phone Number")
    phone_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    phone_entry=Entry(contact_form,width=30)
    phone_entry.grid(row=2, column=1, padx=10,pady=10,sticky="ew")

    if update_id:
        update_contact=phonebook.get_contact_by_id(update_id)
        firstname_entry.insert(0,update_contact.first_name)
        lastname_entry.insert(0,update_contact.last_name)
        phone_entry.insert(0,update_contact.phone_number)

    def submit_button_clicked():
        firstname=firstname_entry.get()
        lastname=lastname_entry.get()
        phone=phone_entry.get()

        if update_id:
            update_contact.edit(firstname,lastname,phone)
        else:
            phonebook.create(firstname,lastname,phone)

        load_treeview()
        contact_form.destroy()


    submit_button=Button(contact_form,text="Submit",command=submit_button_clicked)
    submit_button.grid(row=3,column=1,padx=10, pady=10,sticky="w")

    contact_form.mainloop()

create_button=Button(window,text="Create",command=show_contact_form)
create_button.grid(row=1,column=1,padx=(0,10),pady=(0,10),sticky="ew")

def update_button_clicked():
    update_id=int(phonebook_treeview.selection()[0])
    show_contact_form(update_id)

update_button=Button(window,text="Update",command=update_button_clicked)
update_button.grid(row=1,column=2,padx=(0,10),pady=(0,10),sticky="ew")

def delete_button_clicked():
    row_selected=int(phonebook_treeview.selection()[0])
    phonebook.delete(row_selected)
    load_treeview()

delete_button=Button(window,text="Delete",command=delete_button_clicked)
delete_button.grid(row=1,column=3,padx=(0,10),pady=(0,10),sticky="ew")

phonebook_treeview=Treeview(window,columns=("firstname","lastname","phone"))
phonebook_treeview.grid(row=2,column=1,columnspan=3,padx=(0,10),pady=10,sticky="ewns")

phonebook_treeview.heading("#0",text="Row")
phonebook_treeview.heading("firstname",text="First Name")
phonebook_treeview.column("firstname", anchor="center")
phonebook_treeview.heading("lastname",text="Last Name")
phonebook_treeview.column("lastname", anchor="center")
phonebook_treeview.heading("phone",text="Phone Number")
phonebook_treeview.column("phone", anchor="center")
phonebook_treeview.column("#0",width=50)

def load_treeview():
    for item in phonebook_treeview.get_children():
        phonebook_treeview.delete(item)

    row_number=1
    for contact in phonebook.show_contact_list:
        phonebook_treeview.insert("",
                                  "end",
                                  iid=contact.id,
                                  text=row_number,
                                  values=(contact.first_name,contact.last_name,contact.phone_number))
        row_number+=1

load_treeview()
window.mainloop()