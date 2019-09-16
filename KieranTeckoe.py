#Kieran Teckoe python assessment

print("Welcome to this program, please input what you would like to do today?")
#Menu


menu_loop = 'true'
while menu_loop == 'true':

    #functions = [display, add_new, remove, information, copy, update] - could not work out how to get functions working in a loop

    print("To work this program. Type in one of the following programs: 'd' to display current records. "
          "'a' to add a new record. 'remove' to remove a particular person. 'k' to bring up specific "
          "information. 'c' to copy our info to a new txt file. 'u' to update an existing record")

    choice = input("What would you like to do today? ")
    choice.lower()

    if choice == 'd': # display the records
            #def display():
                display_records = 'true'
                while display_records == 'true':
                    show_records = input("Would you like to view all records(y/n): ")
                    show_records.lower()
                    records = open("list.txt", "r")
                    if show_records == "y":
                        contents = records.read()
                        print(contents)
                        display_records = 'false'
                    elif show_records == "n":
                        print("This program wil not display the records")
                        break
                    else:
                        print("Invalid input. Please try again?")

                records.close()

    elif choice == 'a':
        #def add_new():
            records = open("list.txt", "a")
            print("please add a new record, answering the questions below")
            new_record1 = str(input("Please Enter a number: "))
            new_record2 = str(input("Please Enter a First Name: "))
            new_record3 = str(input("Please Enter a Last Name: "))
            new_record4 = str(input("please enter first line of address: "))
            new_record5 = str(input("Please enter second line of address: "))
            new_record6 = str(input("please enter your post code: "))
            new_record7 = str(input("please enter your phone number: "))

            records.write(new_record1)
            records.write(new_record2)
            records.write(new_record3)
            records.write(new_record4)
            records.write(new_record5)
            records.write(new_record6)
            records.write(new_record7)

            records.close()

            records = open("list.txt", "r")
            contents = records.read()
            print(contents)
            print("New Record has been created.")

            records.close()

    elif choice == 'r': # function to remove a person from the text file
        #def remove():
            records = open("list.txt", "r+")
            contents = records.read
            print(contents)

            delete_record = input("please enter the id number of the person you wish to delete")

            records = open("list.txt", "w")

            #Could not get this one to work in time. My plan was to use the user input number match up with the number of
            #the iD number on the ID number. then from there I would ask the program to write that line and subsequent 7 lines
            #underneath as blank.

    elif choice == "k": # Function that lists info about a specific person
        #def information ():
            info_loop = 'True'
            while info_loop == 'True':
                info_records = str(input("Please input the ID number of the person you wish to view: "))
                records = open("list.txt", "r")
                if records == info_records():
                    records.seek(info_records)
                    print("Here is your records: ")
                    print(records.readline(info_records))
                    info_loop = 'False'
                else:
                    print("Invalid input")
            records.closed()

    elif choice == 'c': #copy the txt.file in a separate file
        #def copy():
            copyrecords = 'True'
            while copyrecords == 'True':
                print("This where we copy over the txt.file to a new one")
                select_copy = input("Would you like to save this file to a new .txt file (y/n): ")
                select_copy.lower()
                if select_copy == 'y':
                    with open("list.txt") as records:
                        with open("copylist.txt", "w") as copy_records:
                            for line in records:
                                copy_records.write(line)
                                print("The Program has copied over to copylist.txt")
                elif select_copy == 'no':
                    print("The program will not copy over")
                    copyrecords = 'False'
                else:
                    print("Invalid input")

    elif choice == 'u': # Function to update a specific record
        #def update():
            update_loop = 'True'
            while update_loop == 'True':
                records = open("list.txt", "r+")
                lines = records.readlines()
                update_record = input("Please give the line number of the file you wish to update: ")
                if update_record == lines[1, 100]:
                    new_line = str(input("What would you like to update this too: "))
                    records.write(new_line)
                    records.close()
                    print("File updated")
                    view_changes = input("Would you like to view the changes(y/n)")
                    view_changes.lower()
                    if view_changes == "y":
                        records = open("list.txt", "r")
                        contents = records
                        print(contents)
                        update_loop = 'False'
                    elif view_changes == "n":
                        print("Not opening updated list. hading back to menu")
                        update_loop = 'False'
                    else:
                        print("Invalid answer, try again")


    else:
        print("Invalid answer, try again")
