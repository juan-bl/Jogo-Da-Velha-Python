import time
import os

def enter():
    print('\033[m=\033[m' * 50)
    
cor = '\033[1;35m'

tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
jogador = ['\033[1;35mX', '\033[1;33mO']
cont = 0

print(f''' 
 {tabela[0][0]} \033[0;32m|\033[m {tabela[0][1]} \033[0;32m|\033[m {tabela[0][2]}
\033[0;32m---|---|---\033[m
 {tabela[1][0]} \033[0;32m|\033[m {tabela[1][1]} \033[0;32m|\033[m {tabela[1][2]}
\033[0;32m---|---|---\033[m
 {tabela[2][0]} \033[0;32m|\033[m {tabela[2][1]} \033[0;32m|\033[m {tabela[2][2]}
''')

while True:
    enter()
    time.sleep(0.5)
    print(f'\033[1;36mJOGADOR {jogador[cont]}\033[m')
    jogada = str(input('Informe a posição da jogada: '))
    
    if jogada not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print('\033[1;31mDigite uma posição valida. Tente novamente!\033[m')
        continue
    
    if jogada == '1':
        if tabela[0][0] in [jogador[0], jogador[1]]:
            print('\033[1;31mPosição oculpada. Tente novamente.\033[m')
            continue
        tabela[0][0] = jogador[cont]
        
    elif jogada == '2':
        if tabela[0][1] in [jogador[0], jogador[1]]:
            print('\033[1;31mPosição oculpada. Tente novamente.\033[m')
            continue
        tabela[0][1] = jogador[cont]
        
    elif jogada == '3':
        if tabela[0][2] in [jogador[0], jogador[1]]:
            print('\033[1;31mPosição oculpada. Tente novamente.\033[m')
            continue
        tabela[0][2] = jogador[cont]
        
    elif jogada == '4':
        if tabela[1][0] in [jogador[0], jogador[1]]:
            print('\033[1;31mPosição oculpada. Tente novamente.\033[m')
            continue
        tabela[1][0] = jogador[cont]
        
    elif jogada == '5':
        if tabela[1][1] in [jogador[0], jogador[1]]:
            print('\033[1;31mPosição oculpada. Tente novamente.\033[m')
            continue
        tabela[1][1] = jogador[cont]
        
    elif jogada == '6':
        if tabela[1][2] in [jogador[0], jogador[1]]:
            print('\033[1;31mPosição oculpada. Tente novamente.\033[m')
            continue
        tabela[1][2] = jogador[cont]
        
    elif jogada == '7':
        if tabela[2][0] in [jogador[0], jogador[1]]:
            print('\033[1;31mPosição oculpada. Tente novamente.\033[m')
            continue
        tabela[2][0] = jogador[cont]
        
    elif jogada == '8':
        if tabela[2][1] in [jogador[0], jogador[1]]:
            print('\033[1;31mPosição oculpada. Tente novamente.\033[m')
            continue
        tabela[2][1] = jogador[cont]
        
    elif jogada == '9':
        if tabela[2][2] in [jogador[0], jogador[1]]:
            print('\033[1;31mPosição oculpada. Tente novamente.\033[m')
            continue
        tabela[2][2] = jogador[cont]
    
    os.system('cls')
    time.sleep(0.5)

    print(f''' 
 {tabela[0][0]} \033[0;32m|\033[m {tabela[0][1]} \033[0;32m|\033[m {tabela[0][2]}
\033[0;32m---|---|---\033[m
 {tabela[1][0]} \033[0;32m|\033[m {tabela[1][1]} \033[0;32m|\033[m {tabela[1][2]}
\033[0;32m---|---|---\033[m
 {tabela[2][0]} \033[0;32m|\033[m {tabela[2][1]} \033[0;32m|\033[m {tabela[2][2]}
''')
    
    time.sleep(1)
    
    # mudar de jogador
    if cont == 0:
        cont += 1
    else:
        cont = 0
        
    # fim de jogo
    if (tabela[0][0] == '\033[1;35mX' and tabela[0][1] == '\033[1;35mX' and tabela[0][2] == '\033[1;35mX') or (tabela[1][0] == '\033[1;35mX' and tabela[1][1] == '\033[1;35mX' and tabela[1][2] == '\033[1;35mX') or (tabela[2][0] == '\033[1;35mX' and tabela[2][1] == '\033[1;35mX' and tabela[2][2] == '\033[1;35mX') or (tabela[0][0] == '\033[1;35mX' and tabela[1][0] == '\033[1;35mX' and tabela[2][0] == '\033[1;35mX') or (tabela[0][1] == '\033[1;35mX' and tabela[1][1] == '\033[1;35mX' and tabela[2][1] == '\033[1;35mX') or (tabela[0][2] == '\033[1;35mX' and tabela[1][2] == '\033[1;35mX' and tabela[2][2] == '\033[1;35mX') or (tabela[0][0] == '\033[1;35mX' and tabela[1][1] == '\033[1;35mX' and tabela[2][2] == '\033[1;35mX') or (tabela[0][2] == '\033[1;35mX' and tabela[1][1] == '\033[1;35mX' and tabela[2][0] == '\033[1;35mX'):
        print('\033[1;32mJOGADOR X VENCEU!!!\033[m')
        break
    elif (tabela[0][0] == '\033[1;33mO' and tabela[0][1] == '\033[1;33mO' and tabela[0][2] == '\033[1;33mO') or (tabela[1][0] == '\033[1;33mO' and tabela[1][1] == '\033[1;33mO' and tabela[1][2] == '\033[1;33mO') or (tabela[2][0] == '\033[1;33mO' and tabela[2][1] == '\033[1;33mO' and tabela[2][2] == '\033[1;33mO') or (tabela[0][0] == '\033[1;33mO' and tabela[1][0] == '\033[1;33mO' and tabela[2][0] == '\033[1;33mO') or (tabela[0][1] == '\033[1;33mO' and tabela[1][1] == '\033[1;33mO' and tabela[2][1] == '\033[1;33mO') or (tabela[0][2] == '\033[1;33mO' and tabela[1][2] == '\033[1;33mO' and tabela[2][2] == '\033[1;33mO') or (tabela[0][0] == '\033[1;33mO' and tabela[1][1] == '\033[1;33mO' and tabela[2][2] == '\033[1;33mO') or (tabela[0][2] == '\033[1;33mO' and tabela[1][1] == '\033[1;33mO' and tabela[2][0] == '\033[1;33mO'):
        print('\033[1;32mJOGADOR O VENCEU!!!\033[m')
        break
    elif tabela[0][0] in ['\033[1;35mX', '\033[1;33mO'] and tabela[0][1] in ['\033[1;35mX', '\033[1;33mO'] and tabela[0][2] in ['\033[1;35mX', '\033[1;33mO'] and tabela[0][0] in ['\033[1;35mX', '\033[1;33mO'] and tabela[1][0] in ['\033[1;35mX', '\033[1;33mO'] and tabela[1][1] in ['\033[1;35mX', '\033[1;33mO'] and tabela[1][2] in ['\033[1;35mX', '\033[1;33mO'] and tabela[2][0] in ['\033[1;35mX', '\033[1;33mO'] and tabela[2][1] in ['\033[1;35mX', '\033[1;33mO'] and tabela[2][2] in ['\033[1;35mX', '\033[1;33mO']:
        print('\033[1;31mDEU VELHA!!!\033[m')
        break
