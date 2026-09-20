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

    total = float(len(pass_list) + math.log(entropy,2))
    return total


def weak_pattern(password):
    with open("100k-most-used-passwords-NCSC.txt") as file:
        for i in file:
            if password


if __name__ == "__main__":
    main()