def validemail(email):
    counting = email.count(".")
    return ("@" in email) and (counting > 0)


user_email = str(input("please enter a valid email address :"))

if validemail(user_email):
    print("user email address is a valid email.")
else:
    print("user email address is not a valid email.")



