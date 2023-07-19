from datetime import datetime

bin_pass = ''
passwd = ''

with open("log.txt") as fin:
    lines = fin.readlines()
fin.close()

time_objects = []
for line in lines:
    date_string = line.split(" ")[3].split("[")[-1]
    time_objects.append(datetime.strptime(date_string, "%d/%b/%Y:%H:%M:%S"))

for i in range(1, len(time_objects)):
    dif = (time_objects[i] - time_objects[i - 1]).seconds
    if i % 4 in [1, 2, 3]:
        if dif == 0:
            bin_pass += '00'
        elif dif == 2:
            bin_pass += '01'
        elif dif == 4:
            bin_pass += '10'
        elif dif == 6:
            bin_pass += '11'
    else:
        if dif == 2:
            bin_pass += '0'
        elif dif == 4:
            bin_pass += '1'
        passwd += chr(int(bin_pass, 2))
        bin_pass = ''

print(passwd)
