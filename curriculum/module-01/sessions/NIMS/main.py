import datetime

current_year = datetime.date.today().year

print("Welcome to NIMC Registration")

# Store registered users
users = []

while True:
    print("\n--- User Registration ---")

    name = input("First name: ")
    surname = input("Surname: ")

    dob = int(input("Enter your year of birth (YYYY): "))
    age = current_year - dob

    state = input("State of origin: ")
    local_government = input("Local government: ")
    area = input("Area of residence: ")
    phone_number = input("Phone number: ")
    email_address = input("Email address: ")

    next_of_kin = input("Next of kin: ")
    relationship_with_next_of_kin = input("Relationship with next of kin: ")
    next_of_kin_address = input("Next of kin address: ")
    next_of_kin_phone_number = input("Next of kin phone number: ")

    # Store the user's information
    user = {
        "name": name,
        "surname": surname,
        "age": age,
        "state": state,
        "local_government": local_government,
        "area": area,
        "phone_number": phone_number,
        "email_address": email_address,
        "next_of_kin": next_of_kin,
        "relationship_with_next_of_kin": relationship_with_next_of_kin,
        "next_of_kin_address": next_of_kin_address,
        "next_of_kin_phone_number": next_of_kin_phone_number
    }

    users.append(user)

    # Display registered user
    print("\n--- Registration Summary ---")
    print(f"Full Name: {name} {surname}")
    print(f"Age: {age}")
    print(f"State of Origin: {state}")
    print(f"Local Government: {local_government}")
    print(f"Area of Residence: {area}")
    print(f"Phone Number: {phone_number}")
    print(f"Email Address: {email_address}")
    print(f"Next of Kin: {next_of_kin}")
    print(f"Relationship with Next of Kin: {relationship_with_next_of_kin}")
    print(f"Next of Kin Address: {next_of_kin_address}")
    print(f"Next of Kin Phone Number: {next_of_kin_phone_number}")

    again = input("\nRegister another user? (yes/no): ")

    if again.strip().lower() != "yes":
        break

print(f"\nTotal users registered: {len(users)}")



