i = sum = 0
while i <= 0:
 sum += i
 i = i+1
print(sum)

for char in 'PYTHON STRING':
    if char == ' ':
        break
    print(char, end='')
    if char == 'O':
        continue
    print('*', end='')


