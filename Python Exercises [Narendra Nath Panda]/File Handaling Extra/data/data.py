#name of file to store addresses
file_save = open("adresses.txt", 'a')

with open('data.txt', 'r') as file_to_open:
    data = file_to_open.read().rsplit(":",1)

    file_save.write(data[-1])

    print(data) #for testing only

file_to_open.close()