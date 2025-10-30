import pygame
import random
import math
import sys

class AndhraVinayakaChavithi:
    def __init__(self):
        pygame.init()
        self.width, self.height = 1200, 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("ఆంధ్ర ప్రదేశ్ స్టైల్ వినాయక చవితి శుభాకాంక్షలు")
        self.clock = pygame.time.Clock()
        
        # Traditional Andhra colors
        self.colors = {
            'gold': (255, 215, 0),
            'red': (139, 0, 0),
            'saffron': (255, 140, 0),
            'yellow': (255, 255, 0),
            'green': (0, 128, 0),
            'maroon': (128, 0, 0)
        }
        
        self.flowers = []
        self.modaks = []
        self.diyas = []
        
        self.create_festival_scene()
    
    def create_festival_scene(self):
        # Create floating flowers
        for _ in range(50):
            flower = {
                'x': random.randint(0, self.width),
                'y': random.randint(0, self.height),
                'size': random.randint(10, 25),
                'speed': random.uniform(0.5, 2),
                'color': random.choice([self.colors['saffron'], self.colors['yellow'], self.colors['red']]),
                'angle': random.uniform(0, 2 * math.pi),
                'type': random.choice(['marigold', 'rose', 'lotus'])
            }
            self.flowers.append(flower)
        
        # Create floating modaks
        for _ in range(20):
            modak = {
                'x': random.randint(100, self.width - 100),
                'y': random.randint(100, self.height - 100),
                'size': random.randint(15, 30),
                'speed': random.uniform(0.3, 1),
                'angle': random.uniform(0, 2 * math.pi)
            }
            self.modaks.append(modak)
    
    def draw_traditional_ganesha(self, x, y, size):
        # Draw Andhra style Ganesha
        # Body
        pygame.draw.ellipse(self.screen, self.colors['gold'], 
                          (x - size//2, y - size//3, size, size//1.2))
        
        # Head
        head_radius = size // 3
        pygame.draw.circle(self.screen, self.colors['gold'], (x, y - size//6), head_radius)
        
        # Crown (Andhra style big crown)
        crown_points = [
            (x - head_radius, y - size//6),
            (x, y - size//2),
            (x + head_radius, y - size//6)
        ]
        pygame.draw.polygon(self.screen, self.colors['red'], crown_points)
        
        # Ears
        pygame.draw.ellipse(self.screen, self.colors['gold'], 
                          (x - head_radius - 20, y - size//6 - 15, 30, 50))
        pygame.draw.ellipse(self.screen, self.colors['gold'], 
                          (x + head_radius - 10, y - size//6 - 15, 30, 50))
        
        # Eyes
        pygame.draw.circle(self.screen, (0, 0, 0), (x - 15, y - size//6 - 5), 8)
        pygame.draw.circle(self.screen, (0, 0, 0), (x + 15, y - size//6 - 5), 8)
        
        # Trunk
        trunk_points = [
            (x, y - size//6 + 5),
            (x + 30, y - size//6 - 20),
            (x + 20, y - size//6 + 10),
            (x, y - size//6 + 20),
            (x - 20, y - size//6 + 10),
            (x - 30, y - size//6 - 20)
        ]
        pygame.draw.polygon(self.screen, (139, 69, 19), trunk_points)
    
    def draw_modak(self, x, y, size):
        # Draw traditional modak shape
        points = []
        for i in range(5):
            angle = i * 2 * math.pi / 5
            px = x + size * math.cos(angle)
            py = y + size * math.sin(angle)
            points.append((px, py))
        
        pygame.draw.polygon(self.screen, (255, 222, 173), points)  # Wheat color
        pygame.draw.circle(self.screen, (210, 180, 140), (x, y), size//1.5)
    
    def draw_flower(self, x, y, size, color, flower_type):
        if flower_type == 'marigold':
            # Marigold flower (traditional)
            pygame.draw.circle(self.screen, color, (x, y), size)
            pygame.draw.circle(self.screen, self.colors['red'], (x, y), size//2)
        elif flower_type == 'lotus':
            # Lotus flower
            for i in range(8):
                angle = i * math.pi / 4
                px1 = x + size * math.cos(angle)
                py1 = y + size * math.sin(angle)
                px2 = x + (size//2) * math.cos(angle + math.pi/8)
                py2 = y + (size//2) * math.sin(angle + math.pi/8)
                pygame.draw.polygon(self.screen, color, [(x, y), (px1, py1), (px2, py2)])
    
    def draw_telugu_text(self, text, x, y, size, color):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)
    
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
            
            # Traditional Andhra background gradient
            for y in range(self.height):
                color_shift = int(100 + 30 * math.sin(time * 0.01 + y * 0.005))
                pygame.draw.line(self.screen, (color_shift, color_shift, 100), 
                               (0, y), (self.width, y))
            
            time += 1
            
            # Update and draw flowers
            for flower in self.flowers:
                flower['x'] += math.cos(flower['angle']) * flower['speed']
                flower['y'] += math.sin(flower['angle']) * flower['speed']
                
                # Wrap around screen
                if flower['x'] < -50: flower['x'] = self.width + 50
                if flower['x'] > self.width + 50: flower['x'] = -50
                if flower['y'] < -50: flower['y'] = self.height + 50
                if flower['y'] > self.height + 50: flower['y'] = -50
                
                self.draw_flower(int(flower['x']), int(flower['y']), 
                               flower['size'], flower['color'], flower['type'])
            
            # Update and draw modaks
            for modak in self.modaks:
                modak['x'] += math.cos(modak['angle']) * modak['speed']
                modak['y'] += math.sin(modak['angle']) * modak['speed']
                modak['angle'] += 0.01
                
                # Bounce off walls
                if modak['x'] < modak['size'] or modak['x'] > self.width - modak['size']:
                    modak['angle'] = math.pi - modak['angle']
                if modak['y'] < modak['size'] or modak['y'] > self.height - modak['size']:
                    modak['angle'] = -modak['angle']
                
                self.draw_modak(int(modak['x']), int(modak['y']), modak['size'])
            
            # Draw main Ganesha in center
            self.draw_traditional_ganesha(self.width // 2, self.height // 2 + 50, 200)
            
            # Draw traditional Andhra decorations
            # Rangoli pattern at bottom
            rangoli_colors = [self.colors['red'], self.colors['saffron'], 
                            self.colors['yellow'], self.colors['green']]
            for i in range(8):
                angle = time * 0.02 + i * math.pi / 4
                radius = 100 + 20 * math.sin(time * 0.05 + i)
                x_r = self.width // 2 + radius * math.cos(angle)
                y_r = self.height - 50 + radius * math.sin(angle)
                color = rangoli_colors[i % len(rangoli_colors)]
                pygame.draw.circle(self.screen, color, (int(x_r), int(y_r)), 15)
            
            # Draw Telugu text blessings
            self.draw_telugu_text("వినాయక చవితి శుభాకాంక్షలు!", 
                                self.width // 2, 100, 60, self.colors['red'])
            
            self.draw_telugu_text("శ్రీ గణేశాయ నమః", 
                                self.width // 2, 160, 40, self.colors['gold'])
            
            blessings = [
                "విఘ్నేశ్వరాయ వరదాయ సురప్రియాయ",
                "లంబోదరాయ శూర్పకర్ణాయ రక్తాంగాయ",
                "మోదక ప్రియాయ వినాయకాయ నమో నమః"
            ]
            
            for i, blessing in enumerate(blessings):
                self.draw_telugu_text(blessing, self.width // 2, 
                                    220 + i * 40, 30, self.colors['saffron'])
            
            # Draw traditional diyas
            for i in range(5):
                x_diya = 200 + i * 200
                # Diya base
                pygame.draw.ellipse(self.screen, (184, 134, 11), 
                                  (x_diya, self.height - 100, 40, 20))
                # Flame with animation
                flame_height = 30 + 10 * math.sin(time * 0.1 + i)
                flame_points = [
                    (x_diya + 20, self.height - 100),
                    (x_diya + 15, self.height - 100 - flame_height),
                    (x_diya + 25, self.height - 100 - flame_height),
                    (x_diya + 20, self.height - 100)
                ]
                pygame.draw.polygon(self.screen, (255, 69, 0), flame_points)
            
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

# Run the Andhra style celebration
if __name__ == "__main__":
    celebration = AndhraVinayakaChavithi()
    celebration.run()