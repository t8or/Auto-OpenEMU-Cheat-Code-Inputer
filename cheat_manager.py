import csv # for reading the csv file
import pyautogui # for mouse automation
import time # for timing
import os # for file operations
import json # for saving the calibration
import pyperclip  # For clipboard operations
import keyboard  # For ESC key monitoring
import sys

# Add a small pause between actions to ensure OpenEMU can keep up
pyautogui.PAUSE = 0.25  # Set to 250ms, adjust if script is too fast or slow

# Enable failsafe
pyautogui.FAILSAFE = True

CALIBRATION_FILE = "config.json"
GAMES_DIR = "game_cheats"

def countdown(message, seconds=5): # countdown for the calibration, adjust if setup is too fast or slow
    print(f"\n{message}") 
    for i in range(seconds, 0, -1):
        print(f"{i}...")
        time.sleep(1)

def check_for_exit():
    if keyboard.is_pressed('esc'):
        print("\nESC pressed - Stopping script!")
        sys.exit(0)

class Coordinates:
    def __init__(self):
        self.gear_icon = None
        self.cheats_menu = None
        self.add_cheat_button = None
        self.enable_checkbox = None
        self.save_button = None
    
    def to_dict(self):
        return {
            'gear_icon': {'x': self.gear_icon.x, 'y': self.gear_icon.y} if self.gear_icon else None,
            'cheats_menu': {'x': self.cheats_menu.x, 'y': self.cheats_menu.y} if self.cheats_menu else None,
            'add_cheat_button': {'x': self.add_cheat_button.x, 'y': self.add_cheat_button.y} if self.add_cheat_button else None,
            'enable_checkbox': {'x': self.enable_checkbox.x, 'y': self.enable_checkbox.y} if self.enable_checkbox else None,
            'save_button': {'x': self.save_button.x, 'y': self.save_button.y} if self.save_button else None
        }
    
    @classmethod
    def from_dict(cls, data):
        coords = cls()
        if data.get('gear_icon'):
            coords.gear_icon = pyautogui.Point(data['gear_icon']['x'], data['gear_icon']['y'])
        if data.get('cheats_menu'):
            coords.cheats_menu = pyautogui.Point(data['cheats_menu']['x'], data['cheats_menu']['y'])
        if data.get('add_cheat_button'):
            coords.add_cheat_button = pyautogui.Point(data['add_cheat_button']['x'], data['add_cheat_button']['y'])
        if data.get('enable_checkbox'):
            coords.enable_checkbox = pyautogui.Point(data['enable_checkbox']['x'], data['enable_checkbox']['y'])
        if data.get('save_button'):
            coords.save_button = pyautogui.Point(data['save_button']['x'], data['save_button']['y'])
        return coords

def save_calibration(coords):
    with open(CALIBRATION_FILE, 'w') as f:
        json.dump(coords.to_dict(), f)
    print(f"\nCalibration saved to {CALIBRATION_FILE}")

def load_calibration():
    try:
        with open(CALIBRATION_FILE, 'r') as f:
            data = json.load(f)
            coords = Coordinates.from_dict(data)
            if all([coords.gear_icon, coords.cheats_menu, coords.add_cheat_button, coords.enable_checkbox, coords.save_button]):
                return coords
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return None

def get_mouse_position():
    # Give user time to move mouse
    time.sleep(3)
    return pyautogui.position()

def calibrate_coordinates():
    coords = Coordinates()
    
    print("\n=== Calibration Mode ===")
    print("You'll need to point your mouse to five locations.")
    
    # Initial countdown before starting calibration
    countdown("Get ready to move your mouse to the first position. Calibration starting in:")
    
    # Gear Icon calibration
    print("\n1. Move your mouse to the GEAR ICON in OpenEMU")
    countdown("Recording gear icon position in:")
    coords.gear_icon = get_mouse_position()
    print(f"Gear icon position recorded: {coords.gear_icon}")
    
    # Cheats Menu calibration
    print("\n2. Move your mouse to where the CHEATS item appears in the dropdown menu")
    countdown("Recording cheats menu position in:")
    coords.cheats_menu = get_mouse_position()
    print(f"Cheats menu position recorded: {coords.cheats_menu}")
    
    # Add Cheat Button calibration
    print("\n3. Move your mouse to where the ADD CHEAT... button appears")
    countdown("Recording add cheat button position in:")
    coords.add_cheat_button = get_mouse_position()
    print(f"Add Cheat button position recorded: {coords.add_cheat_button}")
    
    # Enable Checkbox calibration
    print("\n4. Move your mouse to where the ENABLE NOW checkbox appears")
    countdown("Recording enable checkbox position in:")
    coords.enable_checkbox = get_mouse_position()
    print(f"Enable checkbox position recorded: {coords.enable_checkbox}")
    
    # Save Button calibration
    print("\n5. Move your mouse to where the ADD CHEAT button appears")
    countdown("Recording save button position in:")
    coords.save_button = get_mouse_position()
    print(f"Save button position recorded: {coords.save_button}")
    
    print("\nCalibration complete! ")
    
    # Save calibration
    save_calibration(coords)
    
    return coords

def add_cheat(name, code, coords):
    try:
        print(f"\nAttempting to add cheat: {name}")
        
        check_for_exit()
        # Click the gear icon
        print(f"Clicking gear icon at position: ({coords.gear_icon.x}, {coords.gear_icon.y})")
        pyautogui.click(x=coords.gear_icon.x, y=coords.gear_icon.y)
        time.sleep(0.5)  # Longer delay for menu to appear
        
        check_for_exit()
        # Move to Cheats menu
        print(f"Moving to Cheats menu at position: ({coords.cheats_menu.x}, {coords.cheats_menu.y})")
        pyautogui.moveTo(x=coords.cheats_menu.x, y=coords.cheats_menu.y)
        time.sleep(0.25)
        
        check_for_exit()
        # Click "Add Cheat..." button
        print(f"Clicking Add Cheat button at position: ({coords.add_cheat_button.x}, {coords.add_cheat_button.y})")
        pyautogui.click(x=coords.add_cheat_button.x, y=coords.add_cheat_button.y)
        time.sleep(0.35)  # Slightly longer for dialog
        
        check_for_exit()
        # Paste cheat name
        print(f"Pasting cheat name: {name}")
        pyperclip.copy(name)
        pyautogui.hotkey('command', 'v')
        time.sleep(0.25)
        
        check_for_exit()
        print("Moving to code field")
        pyautogui.press('tab')
        time.sleep(0.25)
        
        check_for_exit()
        # Paste cheat code
        print(f"Pasting cheat code: {code}")
        pyperclip.copy(code)
        pyautogui.hotkey('command', 'v')
        time.sleep(0.25)
        
        check_for_exit()
        # Click enable checkbox
        print(f"Clicking enable checkbox at position: ({coords.enable_checkbox.x}, {coords.enable_checkbox.y})")
        pyautogui.click(x=coords.enable_checkbox.x, y=coords.enable_checkbox.y)
        time.sleep(0.25)
        
        check_for_exit()
        # Click save button
        print(f"Clicking save button at position: ({coords.save_button.x}, {coords.save_button.y})")
        pyautogui.click(x=coords.save_button.x, y=coords.save_button.y)
        time.sleep(0.35)  # Slightly longer for save
        
        check_for_exit()
        # Return to start position (gear icon)
        print("Returning to start position")
        pyautogui.moveTo(x=coords.gear_icon.x, y=coords.gear_icon.y)
        time.sleep(0.25)
        
        print(f"Successfully added cheat: {name}")
        
    except Exception as e:
        print(f"Error while adding cheat {name}: {str(e)}")
        raise

def get_available_games():
    """Get list of game directories in the game_cheats folder"""
    if not os.path.exists(GAMES_DIR):
        print(f"Creating {GAMES_DIR} directory...")
        os.makedirs(GAMES_DIR)
        return []
    
    games = [d for d in os.listdir(GAMES_DIR) 
             if os.path.isdir(os.path.join(GAMES_DIR, d))]
    return sorted(games)

def get_game_csv_files(game_dir):
    """Get list of CSV files in the game directory"""
    game_path = os.path.join(GAMES_DIR, game_dir)
    csv_files = [f for f in os.listdir(game_path) 
                 if f.endswith('.csv')]
    return sorted(csv_files)

def select_game():
    """Select a game folder"""
    games = get_available_games()
    
    if not games:
        print("\nNo game directories found!")
        print("Please create a directory in 'game_cheats' folder with your CSV files.")
        sys.exit(1)
    
    print("\nAvailable games:")
    for index, game in enumerate(games, 1):
        print(f"{index}. {game}")
    
    while True:
        try:
            choice = int(input("\nSelect a game by typing the number of the folder(1-{}): ".format(len(games))))
            if 1 <= choice <= len(games):
                return games[choice-1]
            else:
                print(f"Please enter a number between 1 and {len(games)}")
        except ValueError:
            print("Please enter a valid number")

def select_csv_file(game_dir):
    """Select a CSV file from the game directory"""
    csv_files = get_game_csv_files(game_dir)
    
    if not csv_files:
        print(f"\nNo CSV files found in {game_dir}!")
        print("Please add CSV files to the game directory.")
        sys.exit(1)
    
    print("\nAvailable cheat collections:")
    for index, filename in enumerate(csv_files, 1):
        print(f"{index}. {filename}")
    
    while True:
        try:
            choice = int(input("\nSelect a cheat collection (1-{}): ".format(len(csv_files))))
            if 1 <= choice <= len(csv_files):
                return os.path.join(GAMES_DIR, game_dir, csv_files[choice-1])
            else:
                print(f"Please enter a number between 1 and {len(csv_files)}")
        except ValueError:
            print("Please enter a valid number")

def startup_menu():
    existing_calibration = load_calibration()
    
    if existing_calibration:
        print("\n=== OpenEMU Cheat Code Adder ===")
        print("\nExisting calibration found:")
        print(f"Gear Icon: ({existing_calibration.gear_icon.x}, {existing_calibration.gear_icon.y})")
        print(f"Cheats Menu: ({existing_calibration.cheats_menu.x}, {existing_calibration.cheats_menu.y})")
        print(f"Add Cheat Button: ({existing_calibration.add_cheat_button.x}, {existing_calibration.add_cheat_button.y})")
        print(f"Enable Checkbox: ({existing_calibration.enable_checkbox.x}, {existing_calibration.enable_checkbox.y})")
        print(f"Save Button: ({existing_calibration.save_button.x}, {existing_calibration.save_button.y})")
        
        while True:
            choice = input("\nDo you want to:\n1. Use existing calibration\n2. Recalibrate\nChoice (1 or 2): ").strip()
            if choice == "1":
                return existing_calibration
            elif choice == "2":
                return calibrate_coordinates()
            else:
                print("Please enter 1 or 2")
    else:
        print("\nNo existing calibration found. Starting calibration...")
        return calibrate_coordinates()

def main():
    print("=== OpenEMU Cheat Code Adder ===")
    print("Press ESC at any time to stop the script")
    
    # First select the game
    selected_game = select_game()
    print(f"\nSelected game: {selected_game}")
    
    # Get coordinates through startup menu
    coords = startup_menu()
    
    if not coords or not all([coords.gear_icon, coords.cheats_menu, coords.add_cheat_button, coords.enable_checkbox, coords.save_button]):
        print("Error: Invalid coordinates. Please try calibrating again.")
        return
    
    # Select CSV file from game directory
    csv_file = select_csv_file(selected_game)
    
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found!")
        return
    
    print(f"\nUsing {csv_file} for cheats.")
    print("Press ESC at any time to stop the script")
    countdown("Starting cheat addition in:")
    
    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            total_cheats = sum(1 for row in csv_reader)
            file.seek(0)  # Reset file pointer to start
            csv_reader = csv.reader(file)
            
            for index, row in enumerate(csv_reader, 1):
                check_for_exit()
                if len(row) >= 2:  # Ensure we have both name and code
                    name, code = row[0].strip(), row[1].strip()
                    print(f"\nProcessing cheat {index}/{total_cheats}")
                    print(f"Name: {name}")
                    print(f"Code: {code}")
                    add_cheat(name, code, coords)
                    time.sleep(0.25)  # Delay between cheats
                    
        print("\nFinished adding all cheats!")
        
    except FileNotFoundError:
        print("Error: CSV file not found!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    except KeyboardInterrupt:
        print("\nScript stopped by user!")
        sys.exit(0)

if __name__ == "__main__":
    main() 