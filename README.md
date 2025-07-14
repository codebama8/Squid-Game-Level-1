
 Red Light, Green Light (Console Game – Python)
This is a simple console-based game inspired by the famous “Red Light, Green Light” from Squid Game.
The player must press Enter only when the light is green. If you press during red light, you're eliminated!

 Game Rules:
You must reach step 10 within 60 seconds.

In each round:

If the light is 🟢 green, press Enter to move forward.

If the light is 🔴 red, do not press Enter.

If you press Enter during red light, you lose immediately.

If you don’t press Enter during green light in time, you’re also eliminated.

Wait patiently when it's red, and react quickly when it's green!

🛠 How it Works:
The game randomly chooses green/red light (green is more likely).

A background thread listens for your input (Enter).

You must press Enter within 3 seconds of green light or lose the game.

The game uses threading, time, and random modules.
