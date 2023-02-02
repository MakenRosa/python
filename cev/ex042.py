primeiro_segmento = int(input('Digite o primeiro segmento: '))
segundo_segmento = int(input('Digite o segundo segmento: '))
terceiro_segmento = int(input('Digite o terceiro segmento: '))
if primeiro_segmento < segundo_segmento + terceiro_segmento and segundo_segmento < primeiro_segmento + terceiro_segmento and terceiro_segmento < primeiro_segmento + segundo_segmento:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if primeiro_segmento == segundo_segmento == terceiro_segmento:
        print('EQUILÁTERO!')
    elif primeiro_segmento != segundo_segmento != terceiro_segmento != primeiro_segmento:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')