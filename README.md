# Game-of-Life

## Requirements

You will need: `pygame` and `random`.

## Rules

This "game" is not really a game. All you can do is choose the starting situation. There is a grid with cells, which can be either alive or dead. Any cell can survive, die, or be born the next turn

#### Survival {S}

A cell can survive if it has 2 or 3 neighbours.

It dies the next turn if there are less than 2 or more than 3 neighbours

#### Birth {B}

A cell can be born the next turn if there are exactly 3 neighbours
