import time
import random
import os
from colorama import init, Fore, Back, Style

init(autoreset=True)

class ASCIIGanesha:
    def __init__(self):
        self.frames = self.create_frames()
        self.blessings = [
            "✨ May Lord Ganesha bless you with wisdom and prosperity! ✨",
            "🎉 Wishing you a joyful Vinayaka Chavithi! 🎉",
            "🙏 May all obstacles be removed from your path! 🙏",
            "🌟 Success and happiness in all your endeavors! 🌟",
            "🕉️ Peace and harmony to you and your family! 🕉️"
        ]
    
    def create_frames(self):
        # Multiple ASCII frames for animation
        frames = []
        
        # Frame 1
        frame1 = r"""
           /\_/\
          ( o.o )
           > ^ <
          /     \
         /       \
        /         \
       ╱╲         ╱╲
      ╱  ╲_______╱  ╲
     ╱   ________   ╱
    ╱   ╱        ╲  ╲
   ╱   ╱          ╲  ╲
  ╱   ╱            ╲  ╲
 ╱   ╱              ╲  ╲
╱   ╱                ╲  ╲
"""
        frames.append(frame1)
        
        # Frame 2
        frame2 = r"""
           /\_/\
          ( -.- )
           > ^ <
          /     \
         /       \
        /         \
       ╱╲         ╱╲
      ╱  ╲_______╱  ╲
     ╱   ________   ╱
    ╱   ╱        ╲  ╲
   ╱   ╱          ╲  ╲
  ╱   ╱            ╲  ╲
 ╱   ╱              ╲  ╲
╱   ╱                ╲  ╲
"""
        frames.append(frame2)
        
        return frames
    
    def animate_ganesha(self):
        colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.MAGENTA, Fore.WHITE]
        
        for i in range(50):  # Animation duration
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Random color for each frame
            color = random.choice(colors)
            
            # Alternate between frames
            frame = self.frames[i % len(self.frames)]
            
            print(color + "=" * 60)
            print(Fore.YELLOW + "🎊 HAPPY VINAYAKA CHAVITHI 2023 🎊".center(60))
            print(color + "=" * 60)
            print()
            
            print(color + frame)
            print()
            
            # Display random blessing
            blessing = random.choice(self.blessings)
            print(Fore.CYAN + blessing.center(60))
            print()
            
            # Floating modaks
            modak_line = " " * (i % 30) + "○" * 5
            print(Fore.GREEN + modak_line.center(60))
            
            print()
            print(Fore.WHITE + "Press Ctrl+C to exit".center(60))
            
            time.sleep(0.3)
    
    def create_flower_pattern(self):
        """Create a beautiful floral pattern around the text"""
        flowers = ["🌸", "🌺", "🌼", "🌷", "💮", "🏵️"]
        patterns = []
        
        for i in range(5):
            pattern = " ".join([random.choice(flowers) for _ in range(10)])
            patterns.append(pattern)
        
        return patterns

def main():
    try:
        ascii_ganesha = ASCIIGanesha()
        
        print(Fore.YELLOW + "\nInitializing Vinayaka Chavithi Greetings...")
        time.sleep(2)
        
        # Display floral pattern first
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.MAGENTA + "🌸" * 30)
        print(Fore.CYAN + "WELCOME TO VINAYAKA CHAVITHI CELEBRATIONS 2023".center(60))
        print(Fore.MAGENTA + "🌸" * 30)
        time.sleep(3)
        
        # Start animation
        ascii_ganesha.animate_ganesha()
        
    except KeyboardInterrupt:
        print(Fore.GREEN + "\n\nThank you for celebrating Vinayaka Chavithi!")
        print(Fore.YELLOW + "May Lord Ganesha bless you! 🙏")

if __name__ == "__main__":
    main()