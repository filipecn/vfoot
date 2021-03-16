import pandas as pd
import random


def generate_teams(n_teams=128, n_countries=3, csv_file="times.csv"):
    times = pd.DataFrame(columns=['nome', 'estadio', 'nacionalidade', 'score'])
    for i in range(n_teams):
        times = times.append({
            'nome': 'Time ' + str(i),
            'estadio': random.randint(1000, 50000),
            'nacionalidade': random.randint(0, n_countries),
            'score': random.randint(0, 20),
        }, ignore_index=True)
    times.to_csv(csv_file)
    return times


def generate_players(n_teams=128, n_countries=3, csv_file="jogadores.csv"):
    """
        gerar os jogadores
        0 - sarrafeiro
        1 - caceteiro
        2 - cordeirinho
        3 - cavalheiro
        4 - fair play

        0 - goleiro       3
        1 - defensor      7
        2 - meio          7
        3 - atacante      7
    :param n_teams:
    :param n_countries:
    :param csv_file:
    :return:
    """
    jogadores = pd.DataFrame(
        columns=['nome', 'nacionalidade', 'idade', 'estrela', 'time', 'posicao', 'comportamento', 'forca'])

    numero_por_posicao = [3, 7, 7, 7]
    k = 0
    for i in range(n_teams):
        for p in range(4):
            for j in range(numero_por_posicao[p]):
                jogadores = jogadores.append({
                    'nome': 'Jogador ' + str(k),
                    'nacionalidade': random.randint(0, n_countries),
                    'idade': random.randint(18, 45),
                    'estrela': random.randint(1, 100) > 95,
                    'time': i,
                    'posicao': p,
                    'comportamento': random.randint(0, 4),
                    'forca': random.randint(1, 50),
                }, ignore_index=True)
                k = k + 1
    jogadores.to_csv(csv_file)
    return jogadores


def generate_coaches(n_teams=128, csv_file="tecnicos.csv"):
    tecnicos = pd.DataFrame(columns=['nome', 'time', 'idade', 'comportamento'])
    for i in range(n_teams):
        tecnicos = tecnicos.append({
            'nome': 'Tecnico ' + str(i),
            'time': i,
            'idade': random.randint(30, 70),
            'comportamento': random.randint(0, 4),
        }, ignore_index=True)
    tecnicos.to_csv(csv_file)


if __name__ == "__main__":
    generate_teams(csv_file="../../data/times.csv")