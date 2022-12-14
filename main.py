"""
The program was made by Yaroslav Zahorodnyi.
If you like this program, and you want to add something or suggest some changes,
you can write to my email address - zahorodnyi.yaroslav.work@gmail.com

--- STELLAR MIND ---

This game is made in the strategy genre.
This game is about a civilization of robots who have realized that their planet will not survive in this space. 
The main goal is to move between planets, develop and preserve their civilization.

--- Author: Yaroslav Zahorodnyi ---
--- Version: alpha 0.0.1 ---
"""

# Import main app
from data.scripts.app.app import App

if __name__ == "__main__":
    # Create main window
    app = App()
    
    # Main loop of application
    while True:
        app.loop()