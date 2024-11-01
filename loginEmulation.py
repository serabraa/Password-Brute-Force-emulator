import hashlib
import json

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def store_password(username,password):
    hashed_password = hash_password(password)

    data = {username: hashed_password}

    with open("passoword_store.json", "w")as file:
        json.dump(data,file)

    print("password stored securely.")
def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    store_password(username,password)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
