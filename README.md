
# Banking Application
A simple command-line banking application written in Python that supports balance management and KYC (Know Your Customer) document tracking. Designed for learning purposes, it demonstrates basic financial logic, input validation, and in-memory state management.

## Features
1.Balance Management
View your current account balance at any time
Deposit any positive amount into your account
Withdraw funds with built-in validation — the app rejects zero/negative amounts and prevents overdrafts

2.KYC (Know Your Customer)
Store identity documents as flexible key-value pairs (e.g. name: John Doe, id_number: AB123456)
View all stored KYC records in a formatted list
Update or add new KYC entries at any time — existing keys are overwritten, new ones are appended

3.Input Validation
Deposits: rejects zero and negative amounts with a clear error message
Withdrawals: rejects invalid amounts and blocks transactions that would overdraw the account
Menu: handles unrecognised input gracefully and re-displays the menu

## How to Run
Step 1 — Make sure Python 3.13 is installed
Step 2 — Save the source code to a file named banking_app.py.
Step 3 — Run the application: 'python code.py'

## Algorithm
The application runs on a single while True loop that reads user input and routes it to the appropriate function. Below is the step-by-step logic for each operation.

### 1.Main Loop
  1. Print welcome banner
  2. LOOP forever:
     a. Display menu options 1–6
     b. Read user choice
     c. Route to matching operation (see below)
     d. If choice is 6  →  break loop
     e. If choice is unrecognised  →  print error, continue
  3.  Print farewell message
  4.  END
   
### 2.Deposit Algorithm
  1. Prompt the user for amount
  2. IF amount > 0:
     a. balance = balance + amount
     b. Print "Amount deposited: {amount}"
  3. IF amount > 0:
     a. balance = balance + amount
     b. Print "Amount deposited: {amount}"
  4. END 
### 3.Withdrawal Algorithm
  1. Prompt user for amount
  2. IF amount <= 0:
     a. Print "Cannot withdraw negative or zero amount"
     b. END
  3.  ELSE IF amount > balance:
     a. Print "Cannot withdraw. Insufficient funds"
     b. END
  4. ELSE:
     a. balance = balance - amount
     b. Print "Amount withdrawn: {amount}"
  5. END

### 4. Balance Check Algorithm
   1. Print "Your balance is {balance}"
   2. END

### 5.KYC Check Algorithm
  1. IF kyc_document is empty:
     a. Print "No KYC document"
  2. ELSE:
     a. FOR each key in kyc_document:
          i. Print "KYC {key}: {value}"
   3. END

### 6.KYC Update Algorithm
  1. Prompt user for number of documents (n)
  2. FOR i in range(n):
     a. Prompt for key
     b. Prompt for value
     c. Store key-value pair in temporary dict
  3. Merge temporary dict into kyc_document
     (existing keys are overwritten; new keys are added)
  4. Print "KYC updated"
  5. END

## limitations 
   1. All balance and KYC data is held in memory. Quitting the app erases everything.There is no data persistence
   2. Completed deposits and withdrawals are not logged or retrievable.
   3. Deposit and withdrawal amounts are parsed with int(). Entering 50.5 will raise a ValueError and crash the app.
   4. There is no concept of accounts, sessions, or authentication. One balance and one KYC store exist for the lifetime of the process.
