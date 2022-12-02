import re


# using regular expression to check string entered is URL
# returns True if URL is valid
def validate_url(url_string):

    # set the regex to check string
    regex = ("((http|https)://)?(www.)?"
             + "[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]"
             + "{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)")

    # compiling the regex into a regex object is more efficient
    compiled_regex = re.compile(regex)

    # search through string return True when "match object" is found
    if re.search(compiled_regex, url_string):
        return True
    elif url_string is None:
        return False
    else:
        return False


#  checks email for at least 1 '@' and at least 1 '.' and continues to ask until prerequisites are met
def check_email(email):
    while True:
        at, period = False, False

        for ch in email:
            if ch == '@':
                at = True
            if ch == '.':
                period = True

        if at and period is True:
            break
        else:
            print("Please ensure your email is valid (it must contain @ and .)")
            email = input("Enter your email: \n")
    return email
