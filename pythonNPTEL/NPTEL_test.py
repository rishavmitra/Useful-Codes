import string


Dict = {}
data = ""
file = open("encrypted_text.txt", "w")
for i in range(len(string.ascii_letters)):
    Dict[string.ascii_letters[i]] = string.ascii_letters[i-1]
print(Dict)

with open("real_message.txt", "r") as F:
    while True:
        c = F.read(1)
        if not c:
            print("End of File")
            break
        if c in Dict:
            data = Dict[c]
        else:
            data = c
        file.write(data)
        print(data)
file.close()
