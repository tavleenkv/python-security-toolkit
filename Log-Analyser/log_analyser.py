#create 2 variables to keep track of logins.
failed = 0
successful = 0

#opens the file in read mode
with open("sample.log", "r") as logfile:

  #read every line in the file
  for line in logfile:

    #checks if any line contains a failed login
    if "FAILED_LOGIN" in line:
      #adds 1 to the failed login count
      failed += 1

    #checks if any line contains a successful login
    elif "SUCCESS_LOGIN" in line:
      #adds 1 to the successful login count
      successful += 1

#displays all logins
print("\nSecurity Report")
print("-" * 20)

print(f"Failed Logins: {failed}")
print(f"Successful Logins: {successful}")

#returns a warning if the amount of repeated failed logins exceed a specific limit
if failed >= 3:
  print("\nWARNING")
  print("Possible Brute Force Activity Detected")

