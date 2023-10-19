def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me a name and phone, please."
        except KeyError:
            return "Unknown name"
        except IndexError:
            return "Incorrect number of arguments"
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise IndexError
    name, phone = args
    if name in contacts:
        answer = input("This contact already exists. Do you want to rewrite this contact? Press 1 if yes, 0 if no\n")
        if answer == '0':
            return "Contact hasn't been modified"
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        raise IndexError
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    if len(args) < 1:
        raise IndexError
    name = args[0]
    return contacts.get(name, "Name not found in contacts.")

def show_all(contacts):
    return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
