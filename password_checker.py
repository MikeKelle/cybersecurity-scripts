import datetime

MIN_LENGTH = 6
MAX_LENGTH = 10
PASSWORD_LOG_FILE = "password_log.txt"

def log_invalid_attempt(reason):
    with open(PASSWORD_LOG_FILE, "a") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        log_file.write(f"{timestamp} - Invalid password: {reason}\n")

def check_password(password):
    if len(password) < MIN_LENGTH:
        log_invalid_attempt("password < 6")
        return False
    elif len(password) > MAX_LENGTH:
        log_invalid_attempt("password > 10")
        return False
    return True

def main():
    print("Password Checker Program")
    
    while True:
        password = input("Please enter your password for checking: ")
        if check_password(password):
            print(f"Valid password. Length: {len(password)}")
            break
        else:
            print("Invalid password. Try again.")
    
    print("\nPassword log contents:")
    with open(PASSWORD_LOG_FILE, "r") as log_file:
        print(log_file.read())

if __name__ == "__main__":
    main()