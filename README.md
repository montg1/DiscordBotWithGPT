# DiscordBotWithGPT

A Python-based Discord bot that integrates OpenAI's GPT for intelligent chat responses and includes music playback capabilities.

## 🚀 Features

* **AI Chat**: Uses OpenAI's GPT models to generate human-like responses to user messages.
* **Music Player**: dedicated functionality to play songs in voice channels (via `playsong.py`).
* **Discord Integration**: Built using the `discord.py` library for seamless interaction with Discord servers.

## 🛠️ Technologies Used

* **Python 3.x**
* **[discord.py](https://discordpy.readthedocs.io/)**: For Discord bot interaction.
* **[openai](https://github.com/openai/openai-python)**: For accessing GPT API.
* **Voice Support**: Likely requires `PyNaCl` and `FFmpeg` for audio playback.

## 📋 Prerequisites

Before running the bot, ensure you have the following installed:

1. **Python 3.8+**
2. **FFmpeg** (Required for music playback):
* **Windows**: [Download FFmpeg](https://ffmpeg.org/download.html) and add it to your system PATH.
* **Linux**: `sudo apt install ffmpeg`
* **Mac**: `brew install ffmpeg`



## ⚙️ Installation

1. **Clone the repository**:
```bash
git clone https://github.com/montg1/DiscordBotWithGPT.git
cd DiscordBotWithGPT

```


2. **Install the required libraries**:
```bash
pip install discord.py openai

```


*Note: For voice support, you might also need:*
```bash
pip install PyNaCl

```



## 🔑 Configuration

You need API keys to make the bot work.

1. **Discord Bot Token**: Get it from the [Discord Developer Portal](https://www.google.com/search?q=https://discord.com/developers/applications).
2. **OpenAI API Key**: Get it from [OpenAI Platform](https://platform.openai.com/account/api-keys).

*Tip: It is best practice to store these in a `.env` file or environment variables rather than hardcoding them in the script.*

## 🎮 How to Run

1. Open `bot.py` (or the main configuration area) and ensure your **API Keys** are inserted where required.
2. Run the bot script:
```bash
python bot.py

```


3. Invite the bot to your server and start chatting!

## 📂 Project Structure

* `bot.py`: The main script that initializes the bot, handles events, and connects to OpenAI.
* `playsong.py`: Module handling music playback logic and voice channel connections.
* `README.md`: Documentation for the project.

## ⚠️ Disclaimer

* **API Costs**: Using the OpenAI API may incur costs depending on your usage. Check your quota on the OpenAI dashboard.
* **Bot Permissions**: Ensure your bot has the "Message Content" intent enabled in the Discord Developer Portal.
