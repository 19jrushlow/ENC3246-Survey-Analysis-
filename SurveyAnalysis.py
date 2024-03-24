def parse_line(stringy):
    checking = True
    pos = 0
    arr = []
    for i in range(len(stringy)):
        if stringy[i] == '"':
            checking = not checking
        if checking and (stringy[i] == ","):
            arr.append(stringy[pos:i])
            pos = i
    arr.pop(13)
    arr.pop(6)
    arr.pop(4)
    arr.pop(2)
    for i in range(1, len(arr)):
        arr[i] = arr[i][1::]
    for i in range(len(arr)):
        if arr[i] == "":
            arr[i] = "NONE"
        if arr[i][-1] == "\"":
            arr[i] = arr[i][1:-1]
    return arr


def print_all():
    for i in response_list:
        for j in i:
            print(j)
        print("\n")


with open("SurveyResults.csv", "r") as file:
    listy = file.readlines()

# organizes each response into an array, NONE means no answer given
response_list =[]
for i in listy:
    response_list.append(parse_line(i))

print_all()
