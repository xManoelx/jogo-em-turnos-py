import random

# Personagem: classe mãe
# Heroi: controlado pelo usuario
# Inimigo: adversario do usuario

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    ## Recupera o nome do personagem
    def get_nome(self): 
        return self.__nome
    
    ## Recupera a vida do personagem
    def get_vida(self): 
        return self.__vida
    
    ## Recupera o nivel do personagem
    def get_nivel(self): 
        return self.__nivel
    
    ## Exibe detalhes dos personagens 
    def exibir_detalhes(self): 
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNivel: {self.get_nivel()}"
    
    ## Calcula a vida após receber um ataque
    def receber_ataque(self, dano): 
        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0

    ## Gera o dano de ataque
    def atacar(self, alvo): 
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4) # Baseado no nível
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")
    
## Informações do Herói
class Heroi(Personagem): 
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}"
    
    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8) ## Dano aumentado
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!")

## Informações do inimigo    
class Inimigo(Personagem): 
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}"

### Classe orquestradora do jogo ###    
class Jogo: 
    def __init__(self):
        ## INFORMÇÕES DOS PERSONAGENS
        self.heroi = Heroi(nome = "Herói", vida = 100, nivel = 5, habilidade = "Superforça")
        self.inimigo = Inimigo(nome = "Morcego", vida = 80, nivel = 5, tipo = "Voador")

    ### Faz a gestão da batalha em turnos ###
    def iniciar_batalha(self): 
        print("Iniciando batalha!")
        
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos personagens:")
            print(self.heroi.exibir_detalhes())
            print("")
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar...")
            escolha = input("Escolha: (1- Ataque Normal, 2- Ataque Especial): ")

            if escolha == '1':
                self.heroi.atacar(self.inimigo)
            elif escolha == '2':
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha inválida, escolha novamente.")

            if self.inimigo.get_vida() > 0: ## Inimigo ataca o herói
                self.inimigo.atacar(self.heroi)

        if self.heroi.get_vida() > 0:
            print("\nParabéns, você venceu a batalha!")
        else:
            print("\nVocê perdeu!")
            
# Criar instancia do jogo e iniciar a batalha
jogo = Jogo()
jogo.iniciar_batalha()