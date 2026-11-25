import time


secret = "Adamu@001"
wrong_attempts = 0
lockouts = [60, 10 * 60, 60 * 60]  # 1 minute, 10 minutes, 1 hour
lockout_number = 0

while True:
    password = input("Enter your password: ")

    if password == secret:
        print("Access granted!")
        break

    wrong_attempts += 1
    attempts_left = 3 - wrong_attempts

    if attempts_left > 0:
        print(f"Wrong password. {attempts_left} tries left.")
        continue

    wait_seconds = lockouts[min(lockout_number, len(lockouts) - 1)]
    print(f"Three wrong tries. Wait {wait_seconds // 60} minute(s) before trying again.")
    time.sleep(wait_seconds)

    wrong_attempts = 0
    lockout_number += 1
