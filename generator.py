# Encryption code generator
import string
import random
import csv

alphanumeric_characters = list(string.ascii_letters + string.digits)
special_characters = list("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")

all_characters = alphanumeric_characters + special_characters
all_characters2 = alphanumeric_characters + special_characters

for i in all_characters:
    ran = random.choice(all_characters2)
    with open("enc2.csv", "a", newline="") as file:
        write = csv.writer(file)
        write.writerow([i, ran])
    all_characters2.remove(ran)
