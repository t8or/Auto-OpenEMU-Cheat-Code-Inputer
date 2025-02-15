# OpenEMU Cheat Manager

A Python script to automate adding cheat codes to OpenEMU games. This script uses mouse automation to quickly add lots of cheat codes from CSV files.

## Prerequisites

- macOS with OpenEMU installed
- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone or download this repository to your local machine
2. Open Terminal and navigate to the script directory
3. Create a Python virtual environment:
   ```bash
   python3 -m venv venv
   ```
4. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
5. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Directory Structure

```
.
├── cheat_manager.py        # Main script
├── requirements.txt        # Python dependencies
├── config.json            # Saved mouse positions
└── game_cheats/           # Directory containing game-specific cheats
    └── zelda_majoras_mask/  # Example game directory
        ├── all_cheats.csv        # Complete cheat collection
        ├── essential_cheats.csv  # Most useful cheats
        ├── basic_cheats.csv      # Simple cheats
        ├── equipment_cheats.csv  # Equipment-related cheats
        ├── mask_cheats.csv       # Mask-related cheats
        └── dungeon_cheats.csv    # Dungeon-specific cheats
```

## CSV File Format

Create your cheat CSV files with the following format:
```Example csv
Cheat Name,Cheat Code
Infinite Health,ABCD-1234
Max Money,EFGH-5678
```

## Usage

1. Make sure OpenEMU is open with your game loaded
2. Activate the virtual environment if not already active:
   ```bash
   source venv/bin/activate
   ```
3. Run the script:
   ```bash
   python3 cheat_manager.py
   ```

### First-Time Setup

1. The script will guide you through a calibration process to record mouse positions
2. You'll need to point your mouse to five locations:
   - The gear icon (⚙️) in OpenEMU's game window
   - The "Cheats >" menu item that appears when clicking the gear
   - The "Add Cheat..." button
   - The "Enable Now" checkbox in the cheat dialog
   - The "Add Cheat" button in the cheat dialog

### Calibration Process

1. When prompted, move your mouse to each required position
2. A 5-second countdown will occur in the Terminal before each position is recorded
3. Move to the target, and stay still during the countdown
4. The script saves these positions in `config.json`
5. You can recalibrate anytime by choosing option 2 when prompted

### Adding Cheats to a Game

1. Run the script in Terminal (make sure you are in the right directory)
2. Select your game from the available directories
3. Choose to use existing calibration or recalibrate
4. Select the CSV file containing your cheats
5. The script will automatically:
   - Click the gear icon
   - Navigate to the Cheats menu
   - Click "Add Cheat..."
   - Paste the cheat name and code
   - Enable the cheat
   - Save and repeat for each cheat

### Failsafe Features

- Press ESC at any time to stop the script
- Move your mouse to any corner of the screen to trigger the failsafe
- The script includes built-in delays to ensure OpenEMU can keep up

## Adding New Games

1. Create a new directory/folder in `game_cheats/` with your game's name (use underscores for spaces)
2. Add your CSV files using descriptive names (e.g., `basic_cheats.csv`, `all_cheats.csv`, etc.)
3. Follow the CSV format shown above (2 columns: Cheat Name, GameShark Code)

## Troubleshooting

1. If cheats aren't being added correctly:
   - Ensure OpenEMU is the active window
   - Try recalibrating the mouse positions
   - Increase the script's timing (currently set to 0.25 seconds)

2. If the script isn't finding your cheats:
   - Verify your CSV files are in the correct game directory
   - Check the CSV file format matches the example above
   - Ensure file names follow the `.csv` extension

## Notes

- Keep OpenEMU window visible and active while the script runs
- Don't move the OpenEMU window after calibration (or else you'll have to recalibrate)
- If the list of cheats gets too long, the script may break and click the wrong things
- The script uses clipboard operations for faster input
- Each game's cheats should be organized in its own directory 
- Use a + sign in between GameShark codes for multiple cheats in the same entry

## Credits

- [OpenEMU](https://openemu.org/)
- [GameShark](https://en.wikipedia.org/wiki/GameShark)
- [pyautogui](https://pyautogui.readthedocs.io/)
- [pyperclip](https://pyperclip.readthedocs.io/)

## Created by

- [@t8or](https://github.com/t8or)

## Buy me a (digital)coffee

- [Stripe](https://donate.stripe.com/3cs00LadmfgB6Dm9AB)
- [Bitcoin] (https://www.blockchain.com/btc/address/3PUnci5ZZ9czF8TM2RZCgcodoiuqwhrURn)
