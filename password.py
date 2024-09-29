def is_valid_password(password):

    if not (8 < len(password) < 20):
        return False

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    special_char = "!$%^&*()_+|~=`{}[]:\";'<>?,./"

    for text in password:
        if text.islower():
            has_lower = True
        elif text.isupper():
            has_upper = True
        elif text.isdigit():
            has_digit = True
        elif text in special_char:
            has_special = True

    if has_lower and has_upper and has_digit and has_special:
        return True
    else:
        return False

password =input("Enter Your Password : ")
if is_valid_password(password):
    print("MATCHED")
else:
    print("NOT MATCHED")
