
import re

#TODO: Use a more efficient sort than selection sort
def mySort(data):
    #First sort the list alphabetically
    data.sort()

    #Use selection sort to sort by length
    for x in range(len(data)):
        min = x;

        for y in range(x+1, len(data)):
            if (len(data[y]) < len(data[min])):
                min = y

        #Instead of swapping the values, the displaced element is inserted at the
        #front of the unsorted partition to retain the alphabetical sorting
        if (min != x):
            temp = data[x]
            data[x] = data.pop(min)
            data.insert(x+1, temp)

    return data


data = []

#TODO: Add check to see if file exists
with open('Sort Me.txt') as f:
    #Add all of the data to a list
    for line in f:
        #Cut off any spaces, numbers, or newline characters
        x = re.search("([A-Z]|[a-z]){2,}", line)
        if (x and x.group()):
            data.append(x.group())


data = mySort(data)

while True:
    choice = input("Sort in reverse order? (y/n) --> ")

    if choice[0] == "y":
        data.reverse()
        break
    if choice[0] == "n":
        break

    print("Please enter either yes or no.")


for x in data:
    print(x)

