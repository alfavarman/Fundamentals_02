is_in_thailand = False
likes_male = False

if is_in_thailand or likes_male:
    print("You like males or You are in Thailand")
elif is_in_thailand and likes_male:
    print("You are in Thailand and You like man")
elif not(is_in_thailand) and likes_male:
    print("You re not in Thailand but You like male")
else:
    print("You Re not in Thailand and You dont like man")