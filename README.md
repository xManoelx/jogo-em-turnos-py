# ⚔️ RPG Battle System - Turn-Based Combat Game

A complete turn-based RPG battle system built in Python using Object-Oriented Programming principles. Features hero vs enemy combat with special abilities, inheritance-based character classes, and an engaging terminal-based gaming experience.

## 📸 Preview

```
Iniciando batalha!

Detalhes dos personagens:
Nome: Herói
Vida: 100
Nivel: 5
Habilidade: Superforça

Nome: Morcego
Vida: 80
Nivel: 5
Tipo: Voador

Pressione Enter para atacar...
Escolha: (1- Ataque Normal, 2- Ataque Especial): 2
Herói usou a habilidade especial Superforça em Morcego e causou 28 de dano!
Morcego atacou Herói e causou 12 de dano!
```

## 📋 About This Project

This project is a complete RPG-style battle system that demonstrates advanced Object-Oriented Programming concepts through game development. The system features inheritance-based character classes, turn-based combat mechanics, and strategic gameplay elements with normal and special attacks.

### Game Features:
- **Turn-Based Combat**: Strategic hero vs enemy battles
- **Character Classes**: Hero and Enemy with unique abilities
- **Special Attacks**: Enhanced damage abilities for the hero
- **Random Damage System**: Level-based damage calculations
- **Battle Management**: Complete game loop with win/lose conditions
- **Interactive Combat**: Player choice between attack types

## 🛠️ Technologies Used

- **Python 3** - Core programming language with advanced OOP
  - **Inheritance**: Base Personagem class with Hero and Enemy subclasses
  - **Encapsulation**: Private attributes with getter methods
  - **Polymorphism**: Method overriding for specialized behaviors
  - **Random Module**: Dynamic damage calculation system
  - **Strategic Game Logic**: Turn-based combat mechanics

## 🎯 Features

- ✅ **Object-Oriented Architecture** - Inheritance and encapsulation
- ✅ **Turn-Based Combat System** - Strategic gameplay mechanics
- ✅ **Character Specialization** - Hero abilities and enemy types
- ✅ **Dynamic Damage System** - Level-based random damage calculation
- ✅ **Special Abilities** - Enhanced attacks with increased damage
- ✅ **Game State Management** - Health tracking and battle resolution
- ✅ **Interactive Interface** - Player choice and real-time feedback

## 🔧 Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/xManoelx/python-rpg-battle.git
   cd python-rpg-battle
   ```

2. **Run the game**
   ```bash
   python rpg_battle.py
   ```

3. **Playing the game**
   - Press Enter to start each turn
   - Choose between Normal Attack (1) or Special Attack (2)
   - Monitor character health and strategic timing
   - Battle continues until one character's health reaches 0

## 🏗️ Class Architecture

### Base Class - `Personagem`:
- **Attributes**: Name, health, level (private with getters)
- **Methods**: Display details, receive damage, basic attack
- **Foundation**: Common functionality for all characters

### Hero Class - `Heroi`:
- **Inherits**: All Personagem functionality
- **Special Attribute**: Unique ability name
- **Special Method**: Enhanced special attack with increased damage
- **Player Controlled**: Interactive combat choices

### Enemy Class - `Inimigo`:
- **Inherits**: All Personagem functionality  
- **Special Attribute**: Enemy type classification
- **AI Controlled**: Automatic attack behavior
- **Varied Types**: Different enemy classifications

### Game Controller - `Jogo`:
- **Battle Management**: Turn-based combat orchestration
- **Game Loop**: Continuous battle until victory/defeat
- **User Interface**: Input handling and feedback display

## ⚔️ Combat Mechanics

### Damage Calculation:
- **Normal Attack**: `random.randint(level * 2, level * 4)`
- **Special Attack**: `random.randint(level * 5, level * 8)`
- **Level-Based**: Higher level = more damage potential

### Battle Flow:
1. Display character stats
2. Player chooses attack type
3. Hero attacks enemy
4. Enemy counter-attacks (if alive)
5. Check victory conditions
6. Repeat until battle ends

## 📚 What I Learned

This project advanced my understanding of:

- **Advanced OOP Concepts**: Inheritance, encapsulation, and polymorphism
- **Game Development Logic**: Turn-based systems and state management
- **Strategic Programming**: Balancing game mechanics and player choice
- **Code Architecture**: Designing extensible class hierarchies
- **User Interaction**: Creating engaging command-line interfaces
- **Random Systems**: Implementing fair but varied game mechanics

## 🌟 Technical Highlights

- **Inheritance Hierarchy**: Clean base class with specialized subclasses
- **Encapsulation**: Private attributes with controlled access via getters
- **Method Overriding**: Specialized behavior in subclasses
- **Game State Management**: Health tracking and battle condition logic
- **Strategic Mechanics**: Risk/reward balance between attack types

## 🎮 Gameplay Strategy

- **Normal Attacks**: Consistent damage, good for sustained combat
- **Special Attacks**: High risk/high reward, use strategically
- **Health Management**: Monitor both hero and enemy health
- **Timing**: Save special attacks for critical moments

## 🔄 Future Improvements

- [ ] Add multiple enemy types with different abilities
- [ ] Implement hero classes (Warrior, Mage, Archer)
- [ ] Add inventory system with potions and equipment
- [ ] Create multiple battle scenarios and levels
- [ ] Implement experience points and character progression
- [ ] Add status effects (poison, stun, buff/debuff)
- [ ] Create save/load game functionality

## 👨‍💻 Author

**Manoel Antonio**
- Junior Robot Programmer transitioning to Full Stack Development
- GitHub: [@xManoelx](https://github.com/xManoelx)
- Location: Caxias do Sul, RS, Brasil

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*From industrial robotics to game development - applying OOP principles to create engaging interactive experiences! 🤖⚔️*
