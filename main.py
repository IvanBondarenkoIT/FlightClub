import sheety


WELCOME_TEXT = "Welcome to Flight Club.\nWe find the best flight deals and email you."

def welcome(text):
    print(text)
    first_name = input("What is your first name?")
    last_name = input("What is your last name?")
    while True:
        email1 = input("What is your email?")
        email2 = input("Type your email again")
        if email1 == email2:
            print("Ypu're in the club!")
            return first_name, last_name, email1
        else:
            print("Emails does not match, try again")
    
    

def main():
    first_name, last_name, email = welcome(WELCOME_TEXT)
    sheety.post_new_row(first_name, last_name, email)
    


if __name__ == "__main__":
    main()