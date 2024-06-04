

file = open('youtube.txt', 'w') 

try :
    file.write('Khushi Sharma')
finally :
    file.close()



# same as above
with open('youtube.txt', 'w') as file :
    file.write('Khushi Jangid')