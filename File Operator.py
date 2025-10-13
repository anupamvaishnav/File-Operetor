import os
from datetime import datetime

class Journal:
    def __init__(self, file="journal.txt"):
        self.file = file

    def add(self):
        entry = input("Write your journal entry:\n")
        time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        with open(self.file, "a") as f:
            f.write(f"{time}\n{entry}\n\n")
        print("Entry added!\n")

    def view(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                print("\n--- All Entries ---")
                print(f.read())
        else:
            print("No journal found.\n")

    def search(self):
        if not os.path.exists(self.file):
            print("No journal found.\n")
            return
        key = input("Enter keyword to search: ").lower()
        found = False
        with open(self.file, "r") as f:
            for block in f.read().split("\n\n"):
                if key in block.lower():
                    print(block + "\n")
                    found = True
        if not found:
            print("No match found.\n")

    def delete(self):
        if os.path.exists(self.file):
            if input("Delete all entries? (yes/no): ").lower() == "yes":
                os.remove(self.file)
                print("All entries deleted.\n")
            else:
                print("Cancelled.\n")
        else:
            print("No journal found.\n")


def main():
    j = Journal()
    while True:
        print("Personal Journal")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Search Entry")
        print("4. Delete All")
        print("5. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                j.add()
            case "2":
                j.view()
            case "3":
                j.search()
            case "4":
                j.delete()
            case "5":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
