import csv

class Member:
    def __init__(self,username):
    #   self.fname = fname
    #   self.age = age
    #   self.lname = lname
      self.username = username
    #   self.master_password = master_password
      
    def new_user(self, usernamee):
        self.username = usernamee
        self.fname, self.lname = input("Enter your name: ").strip().split()
        self.age = input("Enter your age: ")
        self.master_password = self._encrypt_(input("Enter your master password: "))
        with open("users.csv", "a", newline='') as file:
            write = csv.writer(file)
            write.writerow([self.username, self.master_password, self.fname, self.lname, self.age])
        
      
    def view(self):
        file_name = self._get_file_name()
        try:
            with open(file_name, "r") as file:
                reader = csv.reader(file)
                passwords = list(reader)
                if not passwords:
                    print("No passwords saved yet.")
                else:
                    for row in passwords:
                        if len(row) == 2:
                            row[1] = self._decrypt(row[1])
                            row[0] = self._decrypt(row[0])
                            print(f"Website: {row[0]}, Password: {row[1]}")
                        else:
                            print("Invalid row detected.")
        except FileNotFoundError:
            print("No passwords saved yet.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def add(self):
        file_name = self._get_file_name()
        website = input("Enter a website name: ").strip()
        website = self._encrypt_(website)
        password = input("Enter your password: ").strip()
        password = self._encrypt_(password)
        with open(file_name, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([website, password])

    def _get_file_name(self):
        return f"{self.username}_passfile.csv"
    def _encrypt_(self, passs):
        pasw = ""
        for letters in passs:
            
            with open("enc2.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if str(row[0]) == letters:
                        pasw = pasw + str(row[1])
                    else: pass
                    
        return pasw
            
    
    def _decrypt(self, passss):
        pasw = ""
        for letters in passss:
            
            with open("enc2.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[1] == letters:
                        pasw = pasw + row[0]
                    else: pass
        return pasw
    
def main():
    
    user_type= input("You are a new user or existing user?(n/ex) ")
    if user_type == "ex":
        user_name = input("Enter you username: ").strip()
        master_pass,fname, lname, age = check_user(user_name)
        name = fname, lname
        if master_pass == None or name == None:
            print("User not found, creating new user")
            mem = Member(user_name)
            mem.new_user(user_name)
        else: 
            user = Member(user_name)
            master_pass = user._decrypt(master_pass)
            find_userpass(name, master_pass)
            while True:
                choice = input("Do you want to 'see' the passwords or 'add' a new one (or 'quit' to exit): ").strip().lower()
                if choice == "see":
                    user.view()
                elif choice == "add":
                    user.add()
                elif choice == "quit":
                    break
                else:
                    print("Invalid choice. Please enter 'see', 'add', or 'quit'.")
    elif user_type == "n":
        user_name = input("Enter you username: ").strip()
        mem = Member(user_name)
        mem.new_user(user_name)
        while True:
            choice = input("Do you want to 'see' the passwords or 'add' a new one (or 'quit' to exit): ").strip().lower()
            if choice == "see":
                mem.view()
            elif choice == "add":
                mem.add()
            elif choice == "quit":
                break
            else:
                print("Invalid choice. Please enter 'see', 'add', or 'quit'.")
def find_userpass(name, master_pass):
    print(f"Hello {name},")
    while True:
        mpass = input("Enter your master password: ").strip()
        if mpass == master_pass:
            return True
        else: print("Incorrect password!")
def check_user(username):
    with open("users.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0]== username:
                return row[1], row[2], row[3], row[4]
            else: pass
if __name__ == "__main__":
    main()