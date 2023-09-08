"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuario. O pro
grama será interrompido quando o número solicitado for negativo """

while True:
    num = int(input('\033[31mQuer ver a tabuada de qual valor?\033[0m '))
    print('\033[36m=\033[0m' * 37)
    if num < 0:
        break
    for c in range(1, 11):
        print(f"{num} x {c} = \033[32m{num * c}\033[0m")
    print('\033[36m=\033[0m' * 37)
print('\033[33mPROGRAMA DE TABUADA FINALIZADO!\033[0m Volte sempre!')
