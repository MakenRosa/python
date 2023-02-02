def mostrar_maior(*nums):
    print('-=' * 30)
    if len(nums) == 0:
        print('Não foram informados valores.')
        return
    print('Analizando os valores passados...')
    for num in nums:
        print(num, end=' ')
    print(f'Foram informados {len(nums)} valores ao todo.')
    print(f'O maior valor informado foi {max(nums)}')


mostrar_maior(2, 9, 4, 5, 7, 1)
mostrar_maior(4, 7, 0)
mostrar_maior(1, 2)
mostrar_maior(6)
mostrar_maior()