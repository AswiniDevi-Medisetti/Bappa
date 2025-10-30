import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as mcolors

def create_3d_ganesha_greeting():
    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create Ganesha-like shape using parametric equations
    theta = np.linspace(0, 2*np.pi, 100)
    phi = np.linspace(0, np.pi, 50)
    
    # Head (sphere)
    r_head = 1
    x_head = r_head * np.outer(np.cos(theta), np.sin(phi))
    y_head = r_head * np.outer(np.sin(theta), np.sin(phi))
    z_head = r_head * np.outer(np.ones(np.size(theta)), np.cos(phi)) + 2
    
    # Ears (ellipsoids)
    x_ear1 = 0.3 * np.outer(np.cos(theta), np.sin(phi)) + 0.8
    y_ear1 = 0.5 * np.outer(np.sin(theta), np.sin(phi)) + 0.2
    z_ear1 = 0.4 * np.outer(np.ones(np.size(theta)), np.cos(phi)) + 2.2
    
    x_ear2 = 0.3 * np.outer(np.cos(theta), np.sin(phi)) - 0.8
    y_ear2 = 0.5 * np.outer(np.sin(theta), np.sin(phi)) + 0.2
    z_ear2 = 0.4 * np.outer(np.ones(np.size(theta)), np.cos(phi)) + 2.2
    
    # Trunk (curved cylinder)
    t = np.linspace(0, 1, 50)
    x_trunk = 0.1 * np.sin(2*np.pi*t)
    y_trunk = -0.8 * t
    z_trunk = 1.5 + 0.3 * np.cos(2*np.pi*t)
    
    def animate(frame):
        ax.clear()
        
        # Add golden color effect with animation
        time_factor = 0.1 * frame
        
        # Plot head with animated color
        head_color = np.array([1.0, 0.84 + 0.1*np.sin(time_factor), 0.0])  # Gold color with animation
        ax.plot_surface(x_head, y_head, z_head, color=head_color, alpha=0.9)
        
        # Plot ears
        ax.plot_surface(x_ear1, y_ear1, z_ear1, color=head_color, alpha=0.8)
        ax.plot_surface(x_ear2, y_ear2, z_ear2, color=head_color, alpha=0.8)
        
        # Plot trunk with animation
        ax.plot(x_trunk, y_trunk + 0.1*np.sin(time_factor), z_trunk, 
                color='#8B4513', linewidth=8)
        
        # Add decorative elements
        # Crown
        crown_x = np.array([-0.5, 0, 0.5, 0, -0.5])
        crown_y = np.array([0.2, 0.5, 0.2, 0.4, 0.2])
        crown_z = np.array([2.8, 3.0, 2.8, 2.9, 2.8]) + 0.1*np.sin(time_factor)
        ax.plot(crown_x, crown_y, crown_z, 'r-', linewidth=3)
        
        # Set limits and viewing angle
        ax.set_xlim([-2, 2])
        ax.set_ylim([-2, 2])
        ax.set_zlim([0, 4])
        
        # Add floating modaks
        modak_angle = time_factor
        for i in range(5):
            angle = modak_angle + i * 2*np.pi/5
            modak_x = 1.5 * np.cos(angle)
            modak_y = 1.5 * np.sin(angle)
            modak_z = 1.0 + 0.2*np.sin(time_factor + i)
            
            # Create modak shape
            u = np.linspace(0, 2*np.pi, 20)
            v = np.linspace(0, np.pi, 20)
            mx = 0.2 * np.outer(np.cos(u), np.sin(v)) + modak_x
            my = 0.2 * np.outer(np.sin(u), np.sin(v)) + modak_y
            mz = 0.3 * np.outer(np.ones(np.size(u)), np.cos(v)) + modak_z
            
            ax.plot_surface(mx, my, mz, color='#FFD700', alpha=0.7)
        
        ax.set_title('🎉 Happy Vinayaka Chavithi 2023! 🎉\nMay Lord Ganesha bless you with wisdom and prosperity!', 
                    fontsize=16, fontweight='bold', color='#D4AF37', pad=20)
        
        ax.axis('off')
        ax.view_init(elev=20, azim=frame)
    
    anim = FuncAnimation(fig, animate, frames=360, interval=50, blit=False)
    plt.tight_layout()
    plt.show()

# Run the 3D animation
create_3d_ganesha_greeting()