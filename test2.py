def verificar_gol(x_bola, y_bola, raio_bola):
    # Supondo que o gol esteja na posição (x_gol, y_gol) com uma largura e altura específicas
    x_gol = 1100
    y_gol = 360
    largura_gol = 100
    altura_gol = 60

    if (x_gol <= x_bola + raio_bola <= x_gol + largura_gol) and (y_gol <= y_bola + raio_bola <= y_gol + altura_gol):
        return True
    return False

placar = 0

def atualizar_placar():
    global placar
    placar += 1
    
class TesteGol(unittest.TestCase):
    def teste_bola_no_gol(self):
        global placar
        placar = 0  # Reseta o placar antes do teste

        # Simula a posição da bola
        x_bola = 1150  # Posição X da bola dentro do gol
        y_bola = 400   # Posição Y da bola dentro da área do gol
        raio_bola = 22  # Raio da bola

        # Verifica se a bola entrou no gol
        if verificar_gol(x_bola, y_bola, raio_bola):
            atualizar_placar()  # Atualiza o placar

        # Espera que o placar tenha sido atualizado para 1
        self.assertEqual(placar, 1)

    def teste_bola_fora_do_gol(self):
        global placar
        placar = 0  # Reseta o placar antes do teste

        # Simula a posição da bola
        x_bola = 900  # Posição X da bola fora do gol
        y_bola = 400   # Posição Y da bola fora da área do gol
        raio_bola = 22  # Raio da bola

        # Verifica se a bola entrou no gol
        if verificar_gol(x_bola, y_bola, raio_bola):
            atualizar_placar()  # Não deve atualizar

        # Espera que o placar ainda seja 0
        self.assertEqual(placar, 0)
