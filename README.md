⚔️ Jogo de RPG em Python
Um jogo de RPG simples desenvolvido em Python utilizando os conceitos de Orientação a Objetos.
🎮 Como Funciona
O jogo é uma batalha por turnos entre um herói e um inimigo. O jogador controla o herói e pode escolher entre dois tipos de ataque para derrotar o adversário.
🎯 Mecânica do Jogo

Início da Batalha: O jogo apresenta os detalhes dos personagens (vida, nível, habilidades)
Turnos: O jogador escolhe entre ataque normal ou especial
Combate: Após o ataque do herói, o inimigo automaticamente contra-ataca
Vitória: A batalha continua até que um dos personagens tenha a vida reduzida a zero

💥 Tipos de Ataque

Ataque Normal: Causa dano baseado no nível do personagem (2x a 4x o nível)
Ataque Especial: Causa dano maior (5x a 8x o nível) usando a habilidade especial do herói

🧬 Orientação a Objetos
O projeto foi desenvolvido utilizando os principais conceitos de Programação Orientada a Objetos:
🏗️ Classes Implementadas

Personagem: Classe base com atributos e métodos comuns (nome, vida, nível)
Heroi: Herda de Personagem, adiciona habilidade especial
Inimigo: Herda de Personagem, adiciona tipo de criatura
Jogo: Classe orquestradora que gerencia a batalha

🎓 Conceitos de OOP Utilizados

Encapsulamento: Atributos privados (usando __) com métodos getters
Herança: Classes Heroi e Inimigo herdam de Personagem
Polimorfismo: Método exibir_detalhes() é sobrescrito nas classes filhas
Abstração: Interface simples para o usuário interagir com o jogo

🚀 Como Executar
bashpython jogo_rpg.py
👥 Personagens Padrão

Herói: Vida 100, Nível 5, Habilidade "Superforça"
Inimigo: Morcego, Vida 80, Nível 5, Tipo "Voador"
