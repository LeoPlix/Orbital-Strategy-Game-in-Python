# Órbito — Orbital Strategy Game

Órbito is a turn-based strategy game played on a square board made of concentric orbits. Players place stones and the board rotates after each move, creating dynamic positions and tactical depth. This repository contains a Python implementation of the game, including AI opponents.

## Features

- Configurable board with 2 to 5 orbits (board side length: 4×4 up to 10×10)
- Three stone types:
  - Black stone (1)
  - White stone (-1)
  - Neutral stone (0)
- Automatic counter-clockwise rotation of the board after every move
- Automatic detection of winning lines (horizontal, vertical and diagonal)
- Adjacency rules that include orthogonal and diagonal neighbors
- Game modes:
  - Singleplayer (with AI)
  - Multiplayer (two human players)
- AI with two difficulty levels: Easy and Normal

## Project Structure

Everything is implemented in a single file:

- `FP2425P2.py`

This file contains the Abstract Data Types (ADTs), game functions and the AI implementation.

## Implemented ADTs

1. ADT Position
   - Represents board coordinates as tuples (column, row)
   - Construction, validation, conversion and comparison functions
   - Functions to obtain adjacent positions (orthogonal and full 8-direction adjacency)

2. ADT Stone
   - Stones are represented as integers
   - Factory, predicate, comparison and conversion functions (converted to characters `X`, `O`, or space)

3. ADT Board
   - Generate empty or pre-filled boards
   - Selectors for horizontal, vertical and diagonal lines
   - Functions to find positions that contain a specific stone
   - Place and remove stones
   - Rotate the board
   - Detect consecutive lines and game end conditions

## Game Mechanics

- A player (human or AI) chooses an empty position.
- The chosen stone is placed on the board.
- The board rotates counter-clockwise automatically.
- The game checks for a winner or for a full board.
- A player wins by forming a consecutive line whose length equals the board side (n × 2).

## Artificial Intelligence

Easy level
- Attempts to play a position that, after rotation, becomes adjacent to one of its own stones.
- If that is not possible, plays the first available position in a predefined order.

Normal level
- Simulates moves including the rotation to try to win on the current turn.
- If it cannot win immediately, it attempts to block the opponent's imminent win.
- Uses forward simulation of future moves to decide the best position.

## Game Modes

Singleplayer
- The human chooses to play as `X` or `O`.
- The computer plays at the chosen difficulty (easy or normal).
- Turns alternate between human and computer; the board rotates at the end of every turn.

Multiplayer
- Two human players alternate turns.
- Rules, including automatic rotation, are the same as singleplayer.

## How to Run

Make sure you have Python installed. Then run:

python FP2425P2.py

The program will ask for:
- Number of orbits (board size)
- Game mode (easy, normal, or two-player)
- Starting player's stone (`X` or `O`)

