from os import write

from Entities.contact import Contact
data_list=[]

def load_from_file():
    with open('PhoneBookData.txt') as file:
        for line in file.readlines():
            line_replaced=line.replace("\n","")
            line_splited=line_replaced.split(',')
            line_splited[0]=int(line_splited[0])
            contact=Contact(*line_splited)
            data_list.append(contact)

        return data_list

def save_to_file(string_file):
    with open('PhoneBookData.txt','w') as file:
        file.write(string_file)