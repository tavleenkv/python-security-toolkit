#create 2 variables to keep track of logins.
failed = 0
successful = 0

#dictionary for tracking failed attempts
failed_users = {}

#opens the file in read mode
with open("sample.log", "r") as logfile:

  #read every line in the file
  for line in logfile:
    
    #splits the line
    parts = line.strip().split()
    
    #stores the values
    event = parts[1]
    username = parts[2]

    #checks for any failed logins
    if event == "FAILED_LOGIN":
      #adds 1 to the failed login count for each one
      failed += 1
      
      # Creates user entry if necessary
      if username not in failed_users:
      failed_users[username] = 0
      
      # Increment counter
      failed_users[username] += 1

    #checks for successful logins
    elif event == "SUCCESS_LOGIN":
      #adds 1 to the successful login count for each one
      successful += 1

#displays all logins
print("\nSecurity Report")
print("-" * 20)

print(f"Failed Logins: {failed}")
print(f"Successful Logins: {successful}")

print("\nUser Statistics")
print("-" * 20)

for user, attempts in failed_users.items():
    print(f"{user}: {attempts} failed")

print("\nThreat Analysis")
print("-" * 20)

#returns a warning if the amount of repeated failed logins exceed a specific limit
for user, attempts in failed_users.items():
    if attempts >= 3:
        print(
            f"WARNING: Possible brute force attack against {user}"
        )
