from flask import Flask, render_template_string
import threading
import webbrowser

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Happy Vinayaka Chavithi 2023</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            font-family: 'Arial', sans-serif;
            overflow: hidden;
        }
        
        .container {
            position: relative;
            width: 100vw;
            height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        
        .ganesha {
            font-size: 120px;
            animation: float 3s ease-in-out infinite;
            text-shadow: 0 0 20px gold;
        }
        
        .title {
            color: white;
            font-size: 3em;
            text-align: center;
            margin: 20px 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        
        .subtitle {
            color: gold;
            font-size: 1.5em;
            text-align: center;
            margin: 10px 0;
        }
        
        .blessings {
            color: white;
            font-size: 1.2em;
            text-align: center;
            margin: 20px 0;
        }
        
        .modak {
            position: absolute;
            font-size: 30px;
            animation: fall linear infinite;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
        }
        
        @keyframes fall {
            to { transform: translateY(100vh) rotate(360deg); }
        }
        
        .firework {
            position: absolute;
            width: 5px;
            height: 5px;
            background: gold;
            border-radius: 50%;
            animation: explode 1s ease-out infinite;
        }
        
        @keyframes explode {
            0% { transform: scale(1); opacity: 1; }
            100% { transform: scale(20); opacity: 0; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="ganesha">🐘</div>
        <h1 class="title">Happy Vinayaka Chavithi 2023</h1>
        <div class="subtitle">May Lord Ganesha Bless You With</div>
        <div class="blessings" id="blessing">Wisdom & Prosperity</div>
    </div>

    <script>
        // Create falling modaks
        function createModak() {
            const modak = document.createElement('div');
            modak.className = 'modak';
            modak.innerHTML = '🪔';
            modak.style.left = Math.random() * 100 + 'vw';
            modak.style.animationDuration = (Math.random() * 3 + 2) + 's';
            document.body.appendChild(modak);
            
            setTimeout(() => {
                modak.remove();
            }, 5000);
        }
        
        // Create fireworks
        function createFirework() {
            const firework = document.createElement('div');
            firework.className = 'firework';
            firework.style.left = Math.random() * 100 + 'vw';
            firework.style.top = Math.random() * 100 + 'vh';
            firework.style.background = `hsl(${Math.random() * 360}, 100%, 50%)`;
            document.body.appendChild(firework);
            
            setTimeout(() => {
                firework.remove();
            }, 1000);
        }
        
        // Rotate blessings
        const blessings = [
            "Wisdom & Prosperity",
            "Success & Happiness", 
            "Peace & Harmony",
            "Health & Wealth",
            "Love & Joy"
        ];
        
        let blessingIndex = 0;
        const blessingElement = document.getElementById('blessing');
        
        setInterval(() => {
            blessingIndex = (blessingIndex + 1) % blessings.length;
            blessingElement.style.opacity = 0;
            setTimeout(() => {
                blessingElement.textContent = blessings[blessingIndex];
                blessingElement.style.opacity = 1;
            }, 500);
        }, 3000);
        
        // Start animations
        setInterval(createModak, 500);
        setInterval(createFirework, 1000);
        
        // Initial creations
        for(let i = 0; i < 20; i++) {
            setTimeout(createModak, i * 100);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    threading.Timer(1.5, open_browser).start()
    app.run(debug=True)