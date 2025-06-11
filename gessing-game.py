import random
import datetime
import pandas as pd
import matplotlib.pyplot as plt

class GuessingGame:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0
        self.resultados_file = "resultados.csv"

    def play(self):
        print("\nBem-vindo ao Jogo da Adivinhação!")
        self.loop()

    def loop(self):
        while True:
            try:
                palpite = int(input("\nDigite seu palpite (1-100): "))
            except ValueError:
                print("\nPor favor, digite um número válido.")
                continue

            self.tentativas += 1

            if palpite < self.numero_secreto:
                print("\nTente um número MAIOR.")
            elif palpite > self.numero_secreto:
                print("\nTente um número MENOR.")
            else:
                print(f"\nParabéns! Você acertou o número {self.numero_secreto} em {self.tentativas} tentativas.")
                self.salvar_resultado()
                self.mostrar_estatisticas()
                break

    def salvar_resultado(self):
        agora = datetime.datetime.now()
        dados = {
            "data": [agora],
            "tentativas": [self.tentativas]
        }
        try:
            df = pd.read_csv(self.resultados_file)
            df = pd.concat([df, pd.DataFrame(dados)], ignore_index=True)
        except FileNotFoundError:
            df = pd.DataFrame(dados)
        df.to_csv(self.resultados_file, index=False)
        print("Resultado salvo!")

    def mostrar_estatisticas(self):
        try:
            df = pd.read_csv(self.resultados_file)
            df['data'] = pd.to_datetime(df['data'])
            plt.plot(df['data'], df['tentativas'], marker='o')
            plt.title('Tentativas ao longo do tempo')
            plt.xlabel('Data')
            plt.ylabel('Número de Tentativas')
            plt.grid(True)
            plt.show()
        except Exception as e:
            print("Não foi possível mostrar as estatísticas:", e)


if __name__ == "__main__":
    game = GuessingGame()
    game.play()
