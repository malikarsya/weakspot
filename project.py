import math

def main():
    while True:
        password = input("What's your password? ")
        pass_list = list(password)
        for i in pass_list:
            if ' ' in pass_list:
                print("Spaces are not allowed.")
            else:
                break

def calculate_entropy(pass_list):
    count = 0
    entropy = 0
    pass_length = len(pass_list)
    non_capitals = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    capital = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in pass_list:
        if pass_list[count] in (capital or non_capitals):
            entropy += 26
        else:
            entropy += 32

    bit = float(int(len(pass_list)) * math.log(entropy,2))
    return bit

def common_password(password):
    with open("100k-most-used-passwords-NCSC.txt","r") as file:
        for passes in file:
            if passes.rstrip() == password:
                return("Password is common.")
    return True

def sequential_number(pass_list):
    nums = [0,1,2,3,4,5,6,7,8,9]
    max_sequential_order = 3
    count = 0
    i = 0
    while i < len(pass_list):
        if pass_list[i] in str(nums):
            j = i
            if pass_list[j+1] == pass_list[j] + 1:
                while j < j + 4:
                    if pass_list[j+1] == pass_list[j] + 1:
                        j += 1
                        count += 1
                    else:
                        j = 0
                        i += 1
                        break
            
            elif pass_list[j+1] == pass_list[j] - 1:
                while j < j + 4:
                    if pass_list[j+1] == pass_list[j] - 1:
                        j += 1
                        count += 1
                    else:
                        j = 0
                        i += 1
                        break
        else:
            i += 1
    if count >= max_sequential_order:
        return("Password is sequential.")
    else:
        return("Password udah aman")
        



   
if __name__ == "__main__":
    main()