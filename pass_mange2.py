import csv

class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

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
        return f"{self.fname}{self.age}{self.lname}_passfile.csv"
    
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
    try:
        fname, lname = input("Enter your first and last name: ").strip().split()
        age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid input. Please enter the correct details.")
        return

    person = Person(fname, lname, age)
    while True:
        choice = input("Do you want to 'see' the passwords or 'add' a new one (or 'quit' to exit): ").strip().lower()
        if choice == "see":
            person.view()
        elif choice == "add":
            person.add()
        elif choice == "quit":
            break
        else:
            print("Invalid choice. Please enter 'see', 'add', or 'quit'.")

if __name__ == "__main__":
    main()
