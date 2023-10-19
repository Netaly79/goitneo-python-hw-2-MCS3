from collections import UserDict

class UnknownUserName(Exception):
    def __init__(self, username):
        self.message = f"Unknown username: {username}"
        super().__init__(self.message)
        print(self.message)

class UnvalidPhoneNumber(Exception):
    def __init__(self, phone):
        self.message = f"Incorrect phone number: {phone}"
        super().__init__(self.message)
        print(self.message)

class Field():
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        self.value = name

    def __str__(self):
        return str(self.value)

class Phone(Field):
    def __init__(self, phone):
        if phone.isdigit() and len(phone) == 10:
            self.value = phone
        else:
            raise UnvalidPhoneNumber(phone)

    def __str__(self):
        return self.value

class Record():
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone):
        try:
            self.remove_phone(old_phone)
            self.phones.append(Phone(new_phone))
        except TabError:
            print("Error deleting")

    def remove_phone(self, phone):
        phones = []
        for i in self.phones:
            if not i.value == phone:
                phones.append(i)
        self.phones = phones

    def find_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                return phone
        return "Not found"

class AddressBook(UserDict):

    def add_record(self, record: Record):
        name = record.name.value
        self[name] = record.phones

    def find(self, name):
        try:
            phone = self.data[name]
            record = Record(name)
            record.phones = phone
            return record
        except KeyError:
            raise UnknownUserName(name)

    def delete(self, name):
        records = []
        for i in self.data.keys():
            if not i == name:
                records.append({i: self.data[i]})
        self.data = records

def main():
    book = AddressBook()

    # Creating a record for John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    try:
        john_record.add_phone("555555555")
    except UnvalidPhoneNumber:
        print("Phone hasn't been added to address book")

    # Adding John's record to the address book
    book.add_record(john_record)

    # Creating and adding a new record for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Printing all records in the book
    for name, record in book.data.items():
        for i in record:
            print(name, i)

    # Finding and editing John's phone
    try:
        john = book.find("John")
        john.edit_phone("1234567890", "1112223333")
    except UnknownUserName:
        print("This user is not present in the Address Book")

    print(john)  # Output: Contact name: John, phones: 1112223333; 5555555555

    # Finding a specific phone in John's record
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Output: 5555555555

    # Deleting Jane's record
    book.delete("Jane")

if __name__ == "__main__":
    main()
