"""VALIDATION"""
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    if re.fullmatch(regex, email):
      print("Valid email")
    else:
      print("Invalid email")
isValid("ast@hfk.bbb")

# importing re library
import re


def main():
    passwd = 'Geek12@'
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

    # compiling regex
    pat = re.compile(reg)

    # searching regex
    mat = re.search(pat, passwd)

    # validating conditions
    if mat:
        print("Password is valid.")
    else:
        print("Password invalid !!")


"""POSTAL CODE VALIDATION"""
def postalValidate(S):
    S = S.upper().replace(" ", "")
    if len(S) == 6:
            for i in range(len(S)):
                if i % 2 == 0:
                    # Even index (0, 2, 4, 6...) , has to be 'letter'
                     if not (S[i].isalpha()):
                        return False
    else:
        # Odd index (1, 3, 5, 7...), must be 'number'
            if not (S[i].isdigit()):
                return False

        else:
            # You can save some cpu ticks here... at this point, the string has to be of length 6 or you know it's not a zip
              return False
        return S