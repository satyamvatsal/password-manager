import sys,os,string,random,csv,getpass
def main():
  count = 1
  while count <= 3:
    master_passwd_user = get_master_password()
    if checkMaster(master_passwd_user) == True:
      authenticated()
      sys.exit(0)
    else :
      print("You have entered wrong master password. Please try again")
      count += 1
  else :
    print("Too many wrong attempts")
    sys.exit(0)

def get_master_password():
  master_password = getpass.getpass("Enter the master password")
  return master_password

def authenticated():
  while True:
    choice = input("""l: list,n: new entry,s: search,q: quit\n""")
    if choice == 'l':
      listPasswords()
    elif choice == 'n':
      add_entry()
    elif choice == 's':
      search_term= input("Search for the user-id: ")
      searchUser(search_term)
    elif choice == 'q':
      print("exitting...")
      sys.exit(0)


  else:
    print("Exiting...")
    sys.exit(0)

def checkMaster(user_passwd):
  with open("data.csv","r") as file:
    reader = csv.DictReader(file)
    first_row = next(reader)
    if first_row["password"] == user_passwd:
      return True
    else:
      return False
      

def listPasswords() :
  with open("data.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
      print(f"\033[1m{row['userid']:5}      {row['password']:5}\033[01m")


def add_entry():
  user_id = input("Enter new user-id: ")
  choice = input("g: Generate , w: Write the password yourself, s:")
  
  if choice == 'g':
    while True:
      length = int(input("Enter lenght of password to be generated: "))
      passwd = ''.join(random.choices
      (string.ascii_letters+
      string.ascii_uppercase+
      string.digits,k=length)
      )
      print(f"Your generated password is \033[1m{passwd}\033[0m")
      print("Do you want to keep it or generate a new one(k/g)")
      isNew = input('')
      if isNew == 'k':
        break

  elif choice == 'w':
    passwd = input("Enter the password: ")

  else :
    print("You have entered incorrect character.\nExitting...")
    sys.exit(0)

  with open("data.csv","a") as file:
    fieldName = ["userid","password"]
    writer = csv.DictWriter(file,fieldnames=fieldName)
    writer.writeheader()
    writer.writerow({'userid':user_id,'password':passwd})


def searchUser(userid):
  with open("data.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
      if row['userid'] == userid:
        print(f"\033[1m Found Password for {userid} is {row['password']}\033[0m")
        return
    else:
      print("Not found.")
      again = input("Do you want to search again(y/n)")
      if again == 'y':
        userid_for_search= input("Search for the user-id: ")
        searchUser(user-id_for_search)
      
        



main()
