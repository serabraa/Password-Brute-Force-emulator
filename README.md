# BruteSystem
This project is a Python-based program to emulate a password brute-force attack using a dictionary of potential passwords. The program includes two main functionalities:

Password Storage: Securely stores a user password by hashing it with SHA-256 and saving the hash in a JSON file.
Brute-Force Attack: Loads a dictionary file and attempts to brute-force the stored password by hashing each entry and comparing it to the stored hash.
Features

Password Hashing: Uses SHA-256 to hash passwords, ensuring that plain passwords are not stored.
Dictionary-Based Attack: Loads a dictionary of common passwords and attempts to match the stored hash.
Error Handling: Handles missing files and encoding issues gracefully.

**How to Use It?**

1. **Password Storage**: Begin by running the `loginEmulation.py` script. When prompted, enter a username and password of your choice. This script will create a JSON file, securely storing your data by associating your username with the SHA-256 hashed version of the password. This method ensures that the actual password is not stored in plaintext, enhancing security.

2. **Brute-Force Simulation**: Next, run the `bruteForce.py` script. When prompted, enter the same username as before and specify the file path to the dictionary (a text file containing common passwords or phrases for testing, for example famous [rockyou.txt]([url](https://github.com/ohmybahgosh/RockYou2021.txt))). The brute-force script will iterate through the dictionary, hashing each entry and comparing it to the stored hash associated with your username. If a match is found, the original password is revealed, demonstrating the efficacy and limitations of dictionary-based brute-force attacks.


