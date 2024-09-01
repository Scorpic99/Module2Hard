num = 0
capls_div = []

while True:
    num = int(input('Введите число от 4 до 20: '))
    if num > 20 or num < 4:
        print('Вы ввели не правельную цифру, попробуте еще раз')
        continue
    else:
        break

for i in range(1, num // 2 + 1):
    for j in range(1, num):
        if i != j:
            if num % (i + j) == 0:
                is_Replay = False
                for a in range(0, len(capls_div), 2):
                    if capls_div[a] == j and capls_div[a + 1] == i:
                        is_Replay = True
                        break
                    else:
                        is_Replay = False

                if not is_Replay:
                    capls_div.append(i)
                    capls_div.append(j)

print(capls_div)
result = ''
for i in range(len(capls_div)):
    f = str(capls_div[i])
    result += f

print(result)
