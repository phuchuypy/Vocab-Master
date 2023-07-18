import csv
import random
from difflib import SequenceMatcher

def similarity_between(first_str, second_str):
    return SequenceMatcher(None, first_str, second_str).ratio()

print("Hei hei / Welcome")

while True:
    print("To practice, press 1")
    print("To add new words, press 2")
    print("To exit, press 3")
    mode = input("What would you like to do? [1/2/3] ")
    if mode == "1":
        read_data = []
        with open("wordbank.csv","r",encoding="UTF-8") as csv_file_read:
            csv_reader = csv.DictReader(csv_file_read)
            for row in csv_reader:
                read_data.append(row)

        while True:
            random_pick = random.choice(read_data)
            word = random_pick["Word"].strip().lower()
            meaning = random_pick["Meaning"].strip().lower()
            print(f"Hva er '{word}' på Engelsk?")
            answer = input("Ditt svar: ").strip().lower()
            if answer == meaning:
                print("Det stemmer!")
            elif answer in meaning or similarity_between(answer,meaning) >= 0.8:
                print(f"Great! It means '{meaning}'")  
            else:
                print(f"Nei, det er '{meaning}'")
            continue_play = input("Continue? [y/n] ")
            if continue_play == "n":
                break
            else:
                continue
        continue
    elif mode == "2":
        with open("wordbank.csv","a",encoding="UTF-8",newline="") as csv_file_write:
            csv_writer = csv.writer(csv_file_write)

            while True:
                word = input("Word: ")
                meaning = input("Meaning: ")
                csv_writer.writerow([word,meaning])
                continue_write = input("Continue? [y/n] ")
                if continue_write == "n":
                    break
                elif continue_write == "y":
                    continue
                else:
                    print("------------- INPUT ERROR -------------")
                    print("Invalid input! Only y or n is accepted!")
        continue
    elif mode == "3":
        print("Ha det bra!")
        break
    else:
        print("------------- INPUT ERROR ----------------")
        print("Invalid input! Only 1, 2 or 3 is accepted!")
        continue

