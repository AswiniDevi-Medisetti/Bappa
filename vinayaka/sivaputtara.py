import tkinter as tk
from tkinter import messagebox
import random

class SimpleCardGrid:
    def __init__(self, root):
        self.root = root
        self.root.title("Ganesha Blessing Cards Grid")
        self.root.geometry("1000x700")
        self.root.configure(bg='#1a1a2e')
        
        self.blessings = [
            "Obstacles removed from your path",
            "Wisdom and prosperity",
            "Success in endeavors", 
            "Peace and harmony",
            "Health and happiness",
            "Spiritual growth",
            "Divine guidance",
            "Wealth and abundance"
        ]
        
        self.create_card_grid()
    
    def create_card_grid(self):
        # Header
        header = tk.Frame(self.root, bg='#1a1a2e')
        header.pack(pady=20)
        
        tk.Label(header, text="🎴 Ganesha Blessing Cards 🎴", 
                font=('Arial', 20, 'bold'),
                fg='#FFD700', bg='#1a1a2e').pack()
        
        tk.Label(header, text="Click any card for blessings",
                font=('Arial', 12),
                fg='white', bg='#1a1a2e').pack(pady=5)
        
        # Cards container
        self.cards_frame = tk.Frame(self.root, bg='#1a1a2e')
        self.cards_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        self.create_cards()
        
        # Control buttons
        control_frame = tk.Frame(self.root, bg='#1a1a2e')
        control_frame.pack(pady=20)
        
        tk.Button(control_frame, text="🎲 Random Card", 
                 command=self.random_card,
                 bg='#FFD700', fg='#1a1a2e',
                 font=('Arial', 12, 'bold'),
                 padx=20, pady=10).pack(side=tk.LEFT, padx=10)
        
        tk.Button(control_frame, text="🔄 Reset All", 
                 command=self.reset_all,
                 bg='#8B0000', fg='white',
                 font=('Arial', 12, 'bold'),
                 padx=20, pady=10).pack(side=tk.LEFT, padx=10)
    
    def create_cards(self):
        # Create 8 cards in 2x4 grid
        self.card_widgets = []
        
        for i in range(8):
            row = i // 4
            col = i % 4
            
            # Different colors for variety
            colors = ['#8B0000', '#2c1b0d', '#4B0082', '#2c3e50',
                     '#8B4513', '#2F4F4F', '#800020', '#36454F']
            
            card = tk.Frame(self.cards_frame, 
                          bg=colors[i],
                          relief='raised',
                          bd=3,
                          width=200,
                          height=150)
            card.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')
            card.pack_propagate(False)
            
            # Card content
            icon_label = tk.Label(card, text=["🕉️","✨","🌟","💫","🎯","💖","🔮","🎉"][i],
                                font=('Arial', 20),
                                bg=colors[i],
                                fg='#FFD700')
            icon_label.pack(pady=10)
            
            title_label = tk.Label(card, text=f"Card {i+1}",
                                 font=('Arial', 12, 'bold'),
                                 bg=colors[i],
                                 fg='white')
            title_label.pack()
            
            blessing_label = tk.Label(card, text="",
                                    font=('Arial', 9),
                                    bg=colors[i],
                                    fg='#CCCCCC',
                                    wraplength=180,
                                    justify='center')
            blessing_label.pack(expand=True, fill='both', padx=10, pady=10)
            
            # Store reference
            self.card_widgets.append((card, blessing_label))
            
            # Bind click event
            card.bind("<Button-1>", lambda e, idx=i: self.reveal_blessing(idx))
            for widget in [icon_label, title_label, blessing_label]:
                widget.bind("<Button-1>", lambda e, idx=i: self.reveal_blessing(idx))
        
        # Configure grid weights
        for i in range(2):
            self.cards_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.cards_frame.grid_columnconfigure(i, weight=1)
    
    def reveal_blessing(self, card_index):
        card, blessing_label = self.card_widgets[card_index]
        blessing = random.choice(self.blessings)
        blessing_label.config(text=blessing)
        
        # Visual feedback
        original_color = card.cget('bg')
        card.config(bg='#34495e')
        card.after(300, lambda: card.config(bg=original_color))
    
    def random_card(self):
        card_index = random.randint(0, len(self.card_widgets)-1)
        self.reveal_blessing(card_index)
        messagebox.showinfo("Random Blessing", 
                          f"Blessing revealed on Card {card_index+1}!\n\n"
                          f"May Lord Ganesha bless you! 🕉️")
    
    def reset_all(self):
        for card, blessing_label in self.card_widgets:
            blessing_label.config(text="")
        messagebox.showinfo("Reset", "All cards have been reset!")

# Run the simple grid
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCardGrid(root)
    root.mainloop()