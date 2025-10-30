import pygame
import random
import math
import sys

class ParticleSystem:
    def __init__(self):
        pygame.init()
        self.width, self.height = 1000, 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Happy Vinayaka Chavithi 2023")
        self.clock = pygame.time.Clock()
        
        self.particles = []
        self.modaks = []
        self.font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 32)
        
        # Create initial particles
        self.create_particles()
        self.create_modaks()
    
    def create_particles(self):
        # Create floating particles (representing blessings)
        for _ in range(200):
            particle = {
                'x': random.randint(0, self.width),
                'y': random.randint(0, self.height),
                'size': random.randint(2, 6),
                'speed': random.uniform(0.5, 2),
                'color': random.choice([(255, 215, 0), (255, 165, 0), (218, 165, 32)]),
                'angle': random.uniform(0, 2 * math.pi)
            }
            self.particles.append(particle)
    
    def create_modaks(self):
        # Create floating modaks
        for _ in range(15):
            modak = {
                'x': random.randint(100, self.width - 100),
                'y': random.randint(100, self.height - 100),
                'size': random.randint(20, 40),
                'speed': random.uniform(0.5, 1.5),
                'angle': random.uniform(0, 2 * math.pi),
                'rotation': 0
            }
            self.modaks.append(modak)
    
    def draw_ganesha_silhouette(self, x, y, size):
        # Draw a simple Ganesha silhouette
        points = [
            (x, y - size),  # Top of head
            (x - size//2, y - size//3),  # Left ear
            (x - size//3, y + size//3),  # Left shoulder
            (x, y + size//2),  # Bottom
            (x + size//3, y + size//3),  # Right shoulder
            (x + size//2, y - size//3),  # Right ear
        ]
        
        # Draw body
        pygame.draw.polygon(self.screen, (218, 165, 32), points)
        
        # Draw trunk
        trunk_points = [
            (x, y - size//4),
            (x - size//8, y),
            (x, y + size//8),
            (x + size//8, y)
        ]
        pygame.draw.polygon(self.screen, (139, 69, 19), trunk_points)
    
    def draw_modak(self, x, y, size, rotation):
        # Draw a modak (sweet)
        points = []
        for i in range(5):
            angle = rotation + i * 2 * math.pi / 5
            px = x + size * math.cos(angle)
            py = y + size * math.sin(angle)
            points.append((px, py))
        
        pygame.draw.polygon(self.screen, (255, 215, 0), points)
        pygame.draw.circle(self.screen, (255, 165, 0), (x, y), size//2)
    
    def run(self):
        running = True
        time = 0
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            # Clear screen with gradient background
            for y in range(self.height):
                color_value = int(100 + 50 * math.sin(time * 0.01 + y * 0.01))
                pygame.draw.line(self.screen, (color_value, color_value, 150), 
                               (0, y), (self.width, y))
            
            time += 1
            
            # Update and draw particles
            for particle in self.particles:
                particle['x'] += math.cos(particle['angle']) * particle['speed']
                particle['y'] += math.sin(particle['angle']) * particle['speed']
                
                # Wrap around screen
                if particle['x'] < 0: particle['x'] = self.width
                if particle['x'] > self.width: particle['x'] = 0
                if particle['y'] < 0: particle['y'] = self.height
                if particle['y'] > self.height: particle['y'] = 0
                
                pygame.draw.circle(self.screen, particle['color'], 
                                 (int(particle['x']), int(particle['y'])), 
                                 particle['size'])
            
            # Update and draw modaks
            for modak in self.modaks:
                modak['x'] += math.cos(modak['angle']) * modak['speed']
                modak['y'] += math.sin(modak['angle']) * modak['speed']
                modak['rotation'] += 0.02
                
                # Bounce off walls
                if modak['x'] < modak['size'] or modak['x'] > self.width - modak['size']:
                    modak['angle'] = math.pi - modak['angle']
                if modak['y'] < modak['size'] or modak['y'] > self.height - modak['size']:
                    modak['angle'] = -modak['angle']
                
                self.draw_modak(int(modak['x']), int(modak['y']), 
                              modak['size'], modak['rotation'])
            
            # Draw Ganesha silhouette in center
            self.draw_ganesha_silhouette(self.width // 2, self.height // 2, 150)
            
            # Draw text messages with animation
            text_color = (255, 255, 255)
            glow_color = (255, 215, 0)
            
            # Main title with glow effect
            main_text = self.font.render("Happy Vinayaka Chavithi 2023", True, text_color)
            glow_text = self.font.render("Happy Vinayaka Chavithi 2023", True, glow_color)
            
            text_rect = main_text.get_rect(center=(self.width//2, 50))
            glow_offset = 2 * math.sin(time * 0.1)
            
            self.screen.blit(glow_text, (text_rect.x + glow_offset, text_rect.y + glow_offset))
            self.screen.blit(main_text, text_rect)
            
            # Subtitle
            sub_text = self.small_font.render("May Lord Ganesha remove all obstacles from your life", True, text_color)
            sub_rect = sub_text.get_rect(center=(self.width//2, 100))
            self.screen.blit(sub_text, sub_rect)
            
            # Blessings text
            blessings = [
                "Wisdom & Prosperity",
                "Success & Happiness",
                "Peace & Harmony"
            ]
            
            for i, blessing in enumerate(blessings):
                blessing_text = self.small_font.render(blessing, True, 
                                                     (255, 255 - i*30, 100 + i*50))
                blessing_rect = blessing_text.get_rect(center=(self.width//2, 600 + i*40))
                self.screen.blit(blessing_text, blessing_rect)
            
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

# Run the particle system
if __name__ == "__main__":
    greeting = ParticleSystem()
    greeting.run()