registered = {"riya@gmail.com", "arjun@scmirt.com"}
domains=("gmail.com","scmirt.org")
print("WELCOME TO SCMIRT E MAIL CHECKING PORTAL")
email=input("\nEnter your email:")
email=email.strip().lower()
if "@" not in email:
     print("Invalid format")
elif not email.endswith(domains):
     print("Invalid")
elif email in registered:
     print("Email is alredy registered!")
else:
    registered.add(email)
    print(f"Your email {email} is sucessfully registered ")