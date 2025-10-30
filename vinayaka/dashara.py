import pygame
import sys
import math

def pygame_ganesha_blessings():
    pygame.init()
    width, height = 1000, 700
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Lord Ganesha Blessings - English")
    clock = pygame.time.Clock()
    
    # Colors
    GOLD = (255, 215, 0)
    RED = (139, 0, 0)
    BLUE = (30, 30, 60)
    WHITE = (255, 255, 255)
    
    # Blessings
    blessings = [
        "Lord Ganesha Blessings",
        "May all obstacles be removed from your path",
        "Wishing you wisdom and prosperity",
        "Success in all your endeavors",
        "Peace and harmony in your life",
        "Divine guidance always"
    ]
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Fill background
        screen.fill(BLUE)
        
        # Draw simple Ganesha
        center_x, center_y = width // 2, height // 2
        
        # Body
        pygame.draw.circle(screen, GOLD, (center_x, center_y), 80)
        
        # Head
        pygame.draw.circle(screen, GOLD, (center_x, center_y - 60), 60)
        
        # Trunk
        points = [
            (center_x, center_y - 50),
            (center_x + 40, center_y - 80),
            (center_x + 30, center_y - 30),
            (center_x, center_y - 20),
            (center_x - 30, center_y - 30),
            (center_x - 40, center_y - 80)
        ]
        pygame.draw.polygon(screen, (139, 69, 19), points)
        
        # Draw blessings text
        font_large = pygame.font.Font(None, 48)
        font_small = pygame.font.Font(None, 32)
        
        for i, blessing in enumerate(blessings):
            if i == 0:
                text = font_large.render(blessing, True, GOLD)
            else:
                text = font_small.render(blessing, True, WHITE)
            
            text_rect = text.get_rect(center=(center_x, 100 + i * 50))
            screen.blit(text, text_rect)
        
        # Draw decorative elements
        pygame.draw.circle(screen, RED, (center_x, center_y - 60), 15)  # Bindi
        
        # Om symbol
        om_font = pygame.font.Font(None, 72)
        om_text = om_font.render("🕉️", True, GOLD)
        om_rect = om_text.get_rect(center=(center_x, height - 100))
        screen.blit(om_text, om_rect)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

# Run the PyGame version
pygame_ganesha_blessings()