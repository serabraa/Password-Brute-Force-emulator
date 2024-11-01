import hashlib
import json

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_stored_hash(username):
    try:
        with open("passoword_store.json","r") as file:
            data = json.load(file)
            return data.get(username)
    except FileNotFoundError:
        print("password storage file not found.")
        return None

def brute_force(username, dictionary_file):
    target_hash = load_stored_hash(username)


    if not target_hash:
        print("no stored password for the given username.")
        return

    try:
        with open(dictionary_file,"r", encoding="ISO-8859-1") as file:
            for line in file:
                word = line.strip()
                hashed_word = hash_password(word)

                if hashed_word == target_hash:
                    print(f"Passoword found! The passoword is : {word}")
                    return
                print("Password not found in the dictionary")
    except FileNotFoundError:
        print("Dictionary file not found.")

def main():
    username = input("Enter the username for the brute-force: ")
    dictionary_file = input("Enter the dictionary file path: ")
    brute_force(username,dictionary_file)

if __name__ == "__main__":
    main()