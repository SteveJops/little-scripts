res = [num*1 for num in range(1, 11)]
print(f'1 * 1 = {res[0]}', f'2 * 1 = {res[1]}', f'3 * 1 = {res[2]}', sep='\n')


for i in range(1, 10):
    for j in range(1, 11):
        print(f'{i}*{j}={i*j}\t', end=' ')
    print('')
