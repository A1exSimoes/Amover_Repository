
def desenhar_tabuleiro(tabuleiro):
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")


def verificar_vencedor(tabuleiro, jogador):
    combinacoes_vencedoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]  
    ]
    
    for combinacao in combinacoes_vencedoras:
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] == jogador:
            return True
    return False


def jogo_do_galo():
    tabuleiro = [' ' for _ in range(9)]
    jogador_atual = 'X'
    jogo_ativo = True
    jogadas = 0
    
    while jogo_ativo:
        desenhar_tabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual}, escolha uma posição (1-9):")
        
        
        try:
            posicao = int(input()) - 1
            if tabuleiro[posicao] == ' ':
                tabuleiro[posicao] = jogador_atual
                jogadas += 1
            else:
                print("Esta posição já está ocupada! Tente outra.")
                continue
        except (IndexError, ValueError):
            print("Escolha uma posição válida entre 1 e 9.")
            continue
        
        # Verificar se há um vencedor
        if verificar_vencedor(tabuleiro, jogador_atual):
            desenhar_tabuleiro(tabuleiro)
            print(f"Parabéns, Jogador {jogador_atual}! venceu!")
            jogo_ativo = False
            continue
        
        # Verificar empate
        if jogadas == 9:
            desenhar_tabuleiro(tabuleiro)
            print("Empate!")
            jogo_ativo = False
            continue
        
        # Alternar entre os jogadores
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

# Executar o jogo
if __name__ == "__main__":
    jogo_do_galo()