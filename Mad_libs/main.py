# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fomanca <fomanca@student.42porto.com>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/21 15:00:36 by fomanca           #+#    #+#              #
#    Updated: 2025/11/21 16:01:07 by fomanca          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def main():
    # --- Inputs organizados em blocos ---
    tipo_de_lugar = input("Escolhe um tipo de lugar (ex.: vila, floresta, deserto): ")
    profissao = input("Escolhe uma profissão (ex.: guerreiro, cozinheira, mago): ")
    nome = input("Escolhe um nome para o personagem: ")

    objeto = input("Escolhe um objeto qualquer (ex.: mochila, bússola, pedra): ")
    lugar_magico = input("Escolhe um lugar mágico (ex.: Reino Perdido, Caverna de Cristal): ")

    objeto_engracado = input("Escolhe um objeto engraçado (ex.: pato de borracha, chinelo voador): ")
    animal = input("Escolhe um animal (ex.: dragão, vaca, polvo): ")
    coisa_perigosa = input("Escolhe algo perigoso (ex.: lava, armadilha, poção explosiva): ")
    coisa_absurda_plural = input("Escolhe uma coisa absurda no plural (ex.: gelados falantes, sapos saltitantes): ")

    objeto_brilhante = input("Escolhe um objeto brilhante (ex.: cristal dourado, coroa reluzente): ")
    poder_magico = input("Escolhe um poder mágico (ex.: tornar invisível, controlar o fogo): ")
    acao_inesperada = input("Escolhe uma ação inesperada (ex.: dançar até cair, dar o tesouro a um estranho): ")

    print()
    print("=== A TUA HISTÓRIA ===\n")

    # --- História ---
    print(f"Num(a) {tipo_de_lugar}, muito longe daqui, vivia um(a) {profissao} chamado(a) {nome}.")
    print(f"Um dia, enquanto procurava {objeto}, encontrou um mapa misterioso que levava ao lendário {lugar_magico}.")

    print(f"\nSem pensar duas vezes, {nome} pegou o seu {objeto_engracado} e partiu na aventura. "
          f"O caminho era perigoso:")
    print(f"Primeiro teve de atravessar um(a) {animal} gigante que guardava a {coisa_perigosa}.")
    print(f"Depois, enfrentou uma tempestade de {coisa_absurda_plural} que quase o(a) fez desistir.")

    print(f"\nMas nada o(a) parava! Finalmente, ao chegar ao {lugar_magico}, descobriu um tesouro: "
          f"um(a) {objeto_brilhante} capaz de {poder_magico}.")
    print(f"Em vez de ficar com ele, {nome} decidiu {acao_inesperada}.")

    print(f"\nDesde esse dia, todos no(a) {tipo_de_lugar} contam a lenda de {nome}, "
          f"o(a) {profissao} que teve coragem de mudar o destino de todo o reino.")

main()

