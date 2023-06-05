-> The script reads passwords from the file "top-20-common-SSH-passwords.txt" and iterates over each password. 
-> It tries to establish an SSH connection to the target host (127.0.0.1) using the current password and the specified username (kali).

-> If the connection is successful (response.connected()), it prints the valid password and breaks out of the loop. 
-> If the authentication fails (paramiko.ssh_exception.AuthenticationException), it prints "Invalid password!" and continues to the next password.

-> The script keeps track of the number of attempts made (attempts variable) and displays the attempt number and current password being tried for each iteration.
