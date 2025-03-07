from random import choice
capital = "João Pessoa"
passaro = "Galo de Campina"
flor = "Margarida"
musica = "Vital e sua moto"

def fatoengracadoaleatorio():
    fatosengracados = ["O paraibano é o povo mais feliz do Brasil.", "Terra de muita cultura e inovação.", "O paraibano é um povo muito acolhedor."]
    index = choice("0123")
    print(fatosengracados[int(index)])
if __name__ == "__main__":
    fatoengracadoaleatorio()