import math
import sys
import string


def main():
    while True:
        if len(sys.argv) == 2:
            pass_list = list(sys.argv[1])
            password = sys.argv[1]

            if ' ' in pass_list:    
                sys.exit("Spaces are not allowed.")
            else:
                if is_common(password) == False and calculate_entropy(pass_list) >= 60 and has_sequential_number(pass_list) == False:
                    print("Password is Safe")
                    break

                elif is_common(password) == True and calculate_entropy(pass_list) >= 60 and has_sequential_number(pass_list) == False:
                    print("Password is common")
                    break

                elif is_common(password) == True and calculate_entropy(pass_list) < 60 and has_sequential_number(pass_list) == False:
                    print("Password is common and <60 bit")
                    break

                elif is_common(password) == True and calculate_entropy(pass_list) >= 60 and has_sequential_number(pass_list) == True:
                    print("Password is common and has sequential number")
                    break

                elif is_common(password) == True and calculate_entropy(pass_list) < 60 and has_sequential_number(pass_list) == True:
                    print("Password is common, <60 bit, and has sequential numbers")
                    break

                elif is_common(password) == False and calculate_entropy(pass_list) < 60 and has_sequential_number(pass_list) == False:
                    print("Password has <60 bit")
                    break

                elif is_common(password) == False and calculate_entropy(pass_list) < 60 and has_sequential_number(pass_list) == True:
                    print("Password has <60 bit and has sequential number")
                    break

                elif is_common(password) == False and calculate_entropy(pass_list) >= 60 and has_sequential_number(pass_list) == True:
                    print("Password has sequential number")
                    break

        else:
            sys.exit("Format is project.py [password]")
        
        


def calculate_entropy(pass_list : list) -> int:
    # calculating the difficulty of a password to bruteforce in bits
    pool = 0
    has_lower = False
    has_upper = False
    has_digits = False
    has_punctuation = False

    for i in pass_list:
        if (i in string.ascii_lowercase and has_lower == False):
            pool += 26
            has_lower = True
        elif (i in string.ascii_uppercase and has_upper == False):
            pool += 26
            has_upper = True
        elif (i in string.digits and has_digits == False):
            pool += 10
            has_digits = True
        elif (i in string.punctuation and has_punctuation == False):
            pool += 32
            has_punctuation = True
    if pool == 0 :
        return 0
    else:
        bit = len(pass_list) * math.log2(pool)
        return bit

def is_common(password : str) -> bool:
    # check if a password is common in the 100k-most-used-passwords-NCSC.txt
    with open("100k-most-used-passwords-NCSC.txt","r") as file:
        for passes in file:
            if passes.rstrip() == password:
                return True
    return False


def has_sequential_number(pass_list : list) -> bool:
    # deciding if a password is sequentially ordered numerically or not
    max_sequential_order = 3
    count = 0
    i = 0
    while i < len(pass_list) - 1:
        if pass_list[i] in (string.digits):
            j = i
            if pass_list[j+1] in string.digits:
                if int(pass_list[j+1]) == int(pass_list[j]) + 1:
                # ascending
                    while (j < len(pass_list) - 1) and (pass_list[j + 1] in string.digits) and (int(pass_list[j+1]) == int(pass_list[j]) + 1):
                        j += 1
                        count += 1
                    if count + 1 >= max_sequential_order:
                        return True
                    else:
                        count = 0
                        i += 1
                        
            
                elif int(pass_list[j+1]) == int(pass_list[j]) - 1:
                # descending
                    while (j < len(pass_list) - 1) and (pass_list[j + 1] in string.digits) and (int(pass_list[j+1]) == int(pass_list[j]) - 1):
                        j += 1
                        count += 1
                    if count + 1 >= max_sequential_order:
                        return True
                    else:
                        count = 0
                        i += 1
                    
                else:
                    i += 1
            else:
                i += 1
        else:
            i += 1
    
    return False
        



   
if __name__ == "__main__":
    main()