# Veda Discord Bot

A simple Discord bot built with **discord.py** that provides useful utility commands such as reminders, giveaways, random number generation, and more.

## Features

- Ping command
- Greeting command
- Repeat (say) command
- Random number generator
- Reminder system
- Giveaway system with:
  - Countdown timer
  - 🎉 reaction entry
  - Automatic winner selection
  - Random participant selection
- Input validation
- Asynchronous command handling

## Requirements

- Python 3.10+
- discord.py
- python-dotenv

## Installation

Install the required dependencies:

```bash
pip install discord.py python-dotenv
```

## Setup

Create a `.env` file in the project directory:

```env
DISCORD_TOKEN=YOUR_BOT_TOKEN
```

Replace `YOUR_BOT_TOKEN` with your Discord bot token.

## Run

```bash
python3 veda_discord_bot.py
```

## Commands

| Command | Description |
|---------|-------------|
| `!ping` | Replies with `Pong!` |
| `!hello` | Greets the user |
| `!say <message>` | Makes the bot repeat your message |
| `!roll <lower> <upper>` | Generates a random integer within the given range |
| `!rem <seconds> [message]` | Sends a reminder after the specified time |
| `!giveaway <minutes> <prize>` | Starts a giveaway with a live countdown |

## Examples

```text
!ping
```

```text
!hello
```

```text
!say Hello everyone!
```

```text
!roll 1 100
```

```text
!rem 300 Drink water
```

```text
!giveaway 5 Discord Nitro
```

## Giveaway

When a giveaway starts:

- The bot posts the giveaway message.
- Users enter by reacting with 🎉.
- A live countdown updates every second.
- When the timer ends:
  - A random participant is selected.
  - If nobody entered, the giveaway ends with no winner.

## Project Structure

```text
veda_discord_bot/
├── veda_discord_bot.py
├── .env
└── README.md
```

## Concepts Practiced

- Object-Oriented Programming (OOP)
- Discord API
- Event-driven programming
- Asynchronous programming (`async` / `await`)
- Background tasks (`asyncio.create_task`)
- Regular expressions
- Random number generation
- Environment variables
- Reaction handling
- Message editing
- User mentions
- Input validation

## Future Improvements

- Slash commands
- Persistent reminders after bot restart
- Giveaway reroll command
- Multiple simultaneous giveaways
- Giveaway IDs
- Permission checks
- Embed messages
- Custom command prefix
- Configuration file
- Logging system
- Better error handling

## Author

Sabal