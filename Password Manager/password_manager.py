from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            print(f"User: {user} | Password: {fer.decrypt(pwd.encode()).decode()}")


def add():
    name = input("Account Name: ")
    password = input("Password: ")

    # with allows us to add a file that will close automatically
    # followed by open(filename, append(a), read(r,), or write(w))
    # follow by as to name it in the code
    with open("passwords.txt", "a") as f:
        f.write(f"{name} | {fer.encrypt(password.encode()).decode()} \n")

while True:
    mode = input("Would you like to add a new password or view existing ones? (add/view) (press q to exit): ")
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Mode")
        continue