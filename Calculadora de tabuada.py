n = 0
while n >= 0:
    n = float(input('Insira um número (maior que 0): '))
    if n < 0:
        break
    carac_n = len(f'Insira um número (maior que 0): {n}')
    carac_t = len(f'{n} X 10 = {n*10}')-2
    print('=' * carac_n if carac_n > carac_t else '='*carac_t)

    for m in range(1,11):
        print(f'{n} X {m} = {n*m}')

    print('=' * carac_n if carac_n > carac_t else '='*carac_t)