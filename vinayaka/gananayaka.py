import time
import random
import os
from colorama import init, Fore, Back, Style

init(autoreset=True)

class AndhraGaneshaASCII:
    def __init__(self):
        self.frames = self.create_telugu_frames()
        self.telugu_blessings = [
            "🎊 వినాయక చవితి శుభాకాంక్షలు! 🎊",
            "🙏 శ్రీ గణేశాయ నమః 🙏",
            "🍯 మోదక ప్రియాయ నమః 🍯",
            "🌟 విఘ్నేశ్వరాయ వరదాయ 🌟",
            "💫 సకల సిద్ధి ప్రదాయకాయ నమః 💫"
        ]
        
    def create_telugu_frames(self):
        frames = []
        
        # Frame 1 - Traditional Andhra Ganesha
        frame1 = r"""
         &&&&&&&&&&&&&&&&&&&&&         
       &&&&&&&&&&&&&&&&&&&&&&&&&       
      &&&&&&&&&&&&&&&&&&&&&&&&&&&      
     &&&&&&&%############%&&&&&&&     
    &&&&&##                 /##&&&&    
   &&&&#                       #&&&&   
   &&&%                         %&&&   
   &&&      #####      #####     &&&   
   &&&     %&&&&&%    %&&&&&%    &&&   
   &&&     %&&&&&%    %&&&&&%    &&&   
   &&&%     #####      #####     %&&&  
   &&&&#                       #&&&&   
    &&&&&##                 ##&&&&&    
     &&&&&&&%############%&&&&&&&     
      &&&&&&&&&&&&&&&&&&&&&&&&&&&      
       &&&&&&&&&&&&&&&&&&&&&&&&&       
         &&&&&&&&&&&&&&&&&&&&&         
"""
        frames.append(frame1)
        
        # Frame 2 - Ganesha with Modak
        frame2 = r"""
         🕉️ ANDHRA STYLE VINAYAKA CHAVITHI 🕉️
         
              .-""-.
             /      \
            |        |
             \      /
              `-..-'
               _||_
              /____\
             /      \
            |  MODAK |
            |   🍯   |
             \      /
              `----`
        """
        frames.append(frame2)
        
        return frames
    
    def draw_traditional_rangoli(self):
        """Draw traditional Andhra rangoli pattern"""
        rangoli_patterns = [
            "✨ ✨ 🌺 🌺 ✨ ✨",
            "🌺 🪔 🪔 🪔 🌺", 
            "✨ 🍯 🍯 🍯 ✨",
            "🌼 🌼 💫 🌼 🌼",
            "🪔 ✨ 🌺 ✨ 🪔"
        ]
        return random.choice(rangoli_patterns)
    
    def animate_festival(self):
        colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.MAGENTA, Fore.CYAN]
        andhra_colors = [Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTGREEN_EX]
        
        for i in range(100):
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Traditional Andhra header
            print(Fore.RED + "═" * 70)
            print(Fore.YELLOW + "🪔 ఆంధ్ర ప్రదేశ్ వినాయక చవితి శుభాకాంక్షలు 🪔".center(70))
            print(Fore.RED + "═" * 70)
            print()
            
            # Animated Ganesha
            color = random.choice(andhra_colors)
            frame = self.frames[i % len(self.frames)]
            print(color + frame)
            print()
            
            # Traditional blessings in Telugu
            blessing = self.telugu_blessings[i % len(self.telugu_blessings)]
            print(Fore.CYAN + blessing.center(70))
            print()
            
            # Rangoli pattern
            rangoli = self.draw_traditional_rangoli()
            print(Fore.MAGENTA + rangoli.center(70))
            print()
            
            # Traditional offerings
            offerings = ["🍯 పూరణ పోళి", "🍌 అరటి పండు", "🥥 కొబ్బరి", "🌺 మల్లె పువ్వు", "🪔 దీపం"]
            offering_line = " | ".join(random.sample(offerings, 3))
            print(Fore.GREEN + offering_line.center(70))
            
            # Floating elements
            floating = " " * (i % 50) + "🪔🍯🌺💫🌟"
            print(Fore.YELLOW + floating)
            
            print()
            print(Fore.WHITE + "ప్రేమతో మీ కుటుంబ సభ్యులతో ఈ పండుగను ఆచరించండి".center(70))
            print(Fore.LIGHTBLACK_EX + "Ctrl+C నొక్కి నిష్క్రమించండి".center(70))
            
            time.sleep(0.4)

def main():
    try:
        andhra_ganesha = AndhraGaneshaASCII()
        
        print(Fore.YELLOW + "\nఆంధ్ర సంప్రదాయ వినాయక చవితి శుభాకాంక్షలు...")
        time.sleep(2)
        
        andhra_ganesha.animate_festival()
        
    except KeyboardInterrupt:
        print(Fore.GREEN + "\n\nధన్యవాదాలు! శ్రీ గణపతి మీకు సకల సిద్ధులు ప్రసాదించాలి! 🙏")
        print(Fore.YELLOW + "వినాయక చవితి శుభాకాంక్షలు! 🪔")

if __name__ == "__main__":
    main()