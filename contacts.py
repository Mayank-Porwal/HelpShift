import os
import re
import argparse
import sys


class Contacts:

    def __init__(self, contact_dir_path, contact_list_file):
        if not os.path.exists(contact_dir_path):
            os.mkdir(contact_dir_path)

        self.file_name = contact_dir_path + '/' + contact_list_file


    def add_contact(self, name):
        add_name = name.strip()

        if not os.path.exists(self.file_name):
            write = 'w+'
        else:
            write = 'a+'

        with open(self.file_name, write) as file_handler:
            file_handler.write(add_name + '\n')


    def search_contact(self, name):
        search_name = name.strip()
        matches = list()

        with open(self.file_name, 'r') as file_handler:
            for line in file_handler:
                line = line.rstrip()
                if re.search(r'(?i){}'.format(search_name), line):
                    matches.append(line)

        # Rating exact match higher than other matches
        matches_dict = dict()
        for match in matches:
            if match.lower() == search_name.lower():
                matches_dict[match] = 1
            else:
                matches_dict[match] = 0

        sorted_dict = sorted(matches_dict.items(), key=lambda kv: kv[1])
        sorted_dict.reverse()

        for match in sorted_dict:
            print(match[0])



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", dest="contact_dir", help="""Directory where Contacts App would run""")
    parser.add_argument("--file", dest="input_file", help="The list of contacts with their names")
    args = parser.parse_args()

    contact = Contacts(args.contact_dir, args.input_file)

    while True:
        choice = input("1)Add Contact  2)Search  3)Exit \n")
        choice = choice.strip()

        if choice == '1':
            add_name = input("Enter Name:")
            add_name = add_name.strip()
            contact.add_contact(add_name)
        elif choice == '2':
            search_name = input("Enter Name:")
            search_name = search_name.strip()
            contact.search_contact(search_name)
        elif choice == '3':
            print("Happy Searching..!")
            sys.exit()
        else:
            print("Oops..Wrong Choice!!\n Please choose between (1-3)!!")
