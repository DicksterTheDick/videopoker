# 🎰 Video Poker (Python Terminal Game)

A fun, retro-style **video poker** game built in Python — complete with ASCII art, card logic, and a sound effect at the end using `aplay`.

---

## 🃏 Features

- Fully randomized 52-card deck
- Bet system with credit tracking
- Card holding and redrawing
- Hand evaluation (Royal Flush, Straight, etc.)
- ASCII menu and paytable
- Plays a `bye.wav` sound when exiting

---

## 🛠 Requirements

- Python 3.6+
- Linux with `aplay` for sound playback

---

## ▶️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/USERNAME/video-poker.git
   cd video-poker
   ```

2. Run the game:
   ```bash
   python3 videopoker.py
   ```

3. Make sure `bye.wav` is in the **same folder** as the script.

---

## 🎧 Sound

At the end of the game, `bye.wav` is played using the `aplay` command. Make sure it's available on your system. If you're on Windows or macOS, this can be replaced with another sound command if needed.

---

## 📸 Preview

```
▓▒░▒▓▒░▒▓▒░▒▓▒░▒▓▒▓
▓▒░ WELCOME TO  ░▒▓
▓▒░ VIDEO POKER ░▒▓
▓▒░▒▓▒░▒▓▒░▒▓▒░▒▓▒▓
```

---

## 📄 License

MIT — use it, share it, modify it!
