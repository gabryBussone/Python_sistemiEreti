string = "sdknfvdsnfndsknfkdsnklv"
vocali = "aeiouAEIOU"

string_no_vocali = [k for k in string if(k not in vocali)]

print("".join(string_no_vocali))
