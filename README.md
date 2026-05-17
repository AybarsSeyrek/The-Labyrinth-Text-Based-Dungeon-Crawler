# The-Labyrinth-Text-Based-Dungeon-Crawler
A Python text-based dungeon crawler using dice rolls, turn-based combat, inventory, random encounters, and score tracking.

## Python Concepts Demonstrated

This project was built to practice and demonstrate Python concepts in one complete terminal-based program.

### Core Python Syntax
- Variables for tracking lives, gold, stats, room choices, and dice rolls
- Constants such as `MAX_LIVES` and `MAX_STAT`
- `if`, `elif`, and `else` statements for game decisions
- Comparison operators for checking dice roll success
- String formatting with f-strings

### Data Structures
- Dictionaries for character stats, enemy stats, inventory, and score tracking
- Lists for random room descriptions, room types, hints, and treasure drops
- Nested dictionaries for organizing character and inventory data

### Functions
The program is divided into functions to keep the code organized and reusable.

Examples:
- `choose_character()` handles character selection
- `fight_enemy()` handles combat
- `play_floor()` controls each dungeon floor
- `handle_room()` resolves room events
- `show_final_score()` prints the end summary

### Loops
- `for` loops are used to control the 8 rooms on each floor
- `while` loops are used for menus and repeated input validation

### User Input and Validation
- `input()` is used for player commands
- `.lower()` makes commands case-insensitive
- `.strip()` prevents extra spaces from breaking input
- Invalid commands are handled safely without crashing the program

### Random Module
The built-in `random` module is used for:
- Dice rolls
- Random room encounters
- Random treasure amounts
- Random item drops
- Random room flavor text

### Game Logic
The project implements several connected gameplay systems:
- Turn-based combat
- Dice-roll success checks
- Perception checks
- Trap detection and disarming
- Inventory item usage
- Temporary stat bonuses
- Gold collection
- Score tracking
- Final boss encounter

### State Tracking
The game tracks changing state throughout the program, including:
- Player lives
- Inventory items
- Gold collected
- Rooms explored
- Enemies defeated
- Traps disarmed or triggered
- Floors cleared
- Player path through the dungeon

### Defensive Programming
The game includes checks to prevent common issues:
- Stats are capped at 6 because the game uses a 6-sided dice system
- Lives are capped at 5
- Invalid input does not terminate the program
- Inventory items are checked before use
