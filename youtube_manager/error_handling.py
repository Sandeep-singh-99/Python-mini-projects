file = open('youtube.txt', 'w')


try:
    file.write('sandeep singh')
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write('ben 10')