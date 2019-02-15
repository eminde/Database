
from Bank import Bank
import os


# a function to clear the terminal
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


 
def get_client_console(bank):
    print("Adding client:")
    fname = input("Pleas enter clients first name:")

    lname = input("Pleas enter clients last name:")

    #make sure deposit is positive float number
    deposit = None
    while deposit is None:
        try:
            val = float(input("Pleas enter clients Deposit:"))
            if(val < 0):
                raise ValueError
            deposit = val
        except ValueError:
                print("Deposit Input Is Invalid, Please Enter a Positive number")
                
    bank.add_client(fname,lname,deposit)
    print("Client Added!")


def get_user_input_console():
    print("1 - Add a client")
    print("2 - Delete a client")
    print("3 - Print Banks Records(Sorted By ID)")
    print("4 - Print Banks Records(Sorted By Name)")
    print("5 - Print Banks Records(Sorted By Balance)")
    print("6 - Print Banks Assets")
    print("7 - Exit")
    user_input= int(input("Enter a Number:"))
    return user_input

def delete_client_console(bank):
    id = None
    while id is None:
        try:
            val = int(input("Please enter Clients ID:"))
            val -=1
            if val < 0:
                raise ValueError
            if val> len(bank.get_clients())-1:
                raise ValueError
            id = val
        except ValueError:
                print("ID Input Is Invalid, Please Enter a Positive number")

    client_name =bank.get_clients()[id].get_fname()+" "+bank.get_clients()[id].get_lname()

    msg = "Are You Sure You Want to Delete Client "+client_name+"\n"
    yes = {'yes','y','are','bale'}
    no = {'no','n','na'}

    ans = None

    while ans==None:
        try :
            ans = input(msg).lower()
            if ans in yes:
                bank.del_client(id)
                print("Client " , client_name ,"has Been Deleted!")
                
            elif ans in no :
                print("Process Been Canceled")
            else:
                ans =None
                raise ValueError
        except:
                print("Invalid Input!! Please Enter Yes/No")

   
                

def print_clients_console(bank ,key):
    client_list = bank.get_clients(sort_by = key)

    id_indent = len(str(max(client_list,key=lambda x : len(str(x.get_id()))).get_id()))

    if id_indent<4:
        id_indent =4

    max_name =max(client_list,key=lambda x : len(x.get_lname()+x.get_fname()))
    name_indent = len(max_name.get_fname())+len(max_name.get_lname())+1
    balance_indent = len(str(max(client_list,key=lambda x : len(str(x.get_balance())))))

    row_delimeter = "-"*(id_indent+2)+"-|-"+"-"*(name_indent+3) + "-|-"+ "-"*(balance_indent+3)+"-|"


    id_header = " ID "
    name_header = " Name "
    balance_header = " Balance "
    
    print("_"*len(row_delimeter))
    print(id_header," "*(id_indent-len(id_header))," | ",name_header," "*(name_indent-len(name_header))," | ",balance_header,
        " "*(balance_indent-len(balance_header))," |")

    for client in client_list:
        print(row_delimeter)

        id = str(client.get_id())
        name = client.get_lname() + " " + client.get_fname()
        balance = str(client.get_balance())

        print(" ",id," "*(id_indent-len(id)-2)," | ",name," "*(name_indent-len(name))," | ",balance,
        " "*(balance_indent-len(balance))," | ")
    print(row_delimeter)


def print_bank_assets_console (bank):
    print("Total Assets Of Bank Is : " ,end="")
    print(round(bank.get_assets(),4))


def main():
   
    bank = Bank()

    ###-------------------#####
    ### This part is for tests we just create some costumers 
    #delete this after in final release

    bank.add_client("Amin","Dehghan",23.45)
    bank.add_client("ali","Rezaii",234)
    bank.add_client("Hissein","Abalfathi",354)
    bank.add_client("Reza","Irani",234.45)
    bank.add_client("Mohammad ","Esfehani",237.45)

    ###--------------------#####

    t=1
    while(t):
        user_input = get_user_input_console()

        if (user_input==1):
            
            # Add a client
            cls()
            get_client_console(bank)
            
            dummy = input("\nPress Enter to continue...")
            cls()

        elif (user_input==2):
            #Delete a client
            cls()
            delete_client_console(bank)

            dummy = input("\nPress Enter to continue...")
            cls()



        elif (user_input==3):
            #Print Banks Records(Sorted By ID)
            cls()
            print("Print Clients Records Sorted By ID")
            print_clients_console(bank ,key = "id")
            dummy = input("\nPress Enter to continue...")
            cls()
            pass
        elif (user_input==4):
            #Print Banks Records(Sorted By Name)
            cls()
            print("Print Clients Records Sorted By Name")
            print_clients_console(bank,key = "name")
            dummy = input("\nPress Enter to continue...")
            cls()
            pass

        elif (user_input==5):
            #Print Banks Records(Sorted By Balance)
            cls()
            print("Print Clients Records Sorted By Balance")
            print_clients_console(bank,key = "balance")
            dummy = input("\nPress Enter to continue...")
            cls()
            pass

        elif (user_input==6):
            #Print Banks Assets
            cls()
            print_bank_assets_console(bank)
            dummy = input("\nPress Enter to continue...")
            cls()
        elif (user_input==7):
            #Exit
            cls()
            t=0
        else:
            #Handel Invalid User Inputs
            cls()
            print("InValid User Input, Please Try Again...")


if __name__ == "__main__":
    main()
