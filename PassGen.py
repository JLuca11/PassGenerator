import random
def basepass():
    while True:
        base_pass = input("Enter base word for password:")
        if len(base_pass) < 5:
            print("Make the password at least 5 characters")
        elif len(base_pass) > 20:
            print("Make the password less than 20 characters")
        else:

            return createpass(base_pass)
def createpass(basepass):

    strong_pass = basepass
    random_num = random.randint(0,1)
    if random_num == 0:
        strong_pass = strong_pass.capitalize()
    if random_num == 1:
        strong_pass = strong_pass[0].lower() + strong_pass[1:].upper()
    rand_pass_digits = random.randint(0,9) + random.randint(0,9) + random.randint(0,9)
    strong_pass = strong_pass + str(rand_pass_digits)
    special_char = ["!", "?", "#", "$", "%", "&"]
    strong_pass = strong_pass + special_char[random.randint(0,5)]
    print(strong_pass)
    #add random sequence of numbers after password
    #change either first letter capital rest lowercase or inverse
    #add special character (?,!,$,ect)

basepass()
