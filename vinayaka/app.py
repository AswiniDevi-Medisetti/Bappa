from flask import Flask, render_template, jsonify
import random
from datetime import datetime

app = Flask(__name__)

# English blessings data
blessings_data = {
    "blessings": [
        "May Lord Ganesha remove all obstacles from your path",
        "Wishing you wisdom, prosperity and success in all endeavors",
        "May His blessings bring peace and harmony to your life",
        "Let the divine energy of Ganesha guide you always",
        "Blessed with happiness, health and spiritual growth",
        "May every beginning be auspicious and every ending successful",
        "May you achieve all your goals with Ganesha's grace",
        "Divine protection and guidance in your journey"
    ],
    "quotes": [
        "The remover of obstacles, the lord of beginnings",
        "Where there is faith, there is Ganesha",
        "Wisdom and prosperity follow his blessings",
        "Every ending is a new beginning with Ganesha"
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_blessing')
def get_blessing():
    blessing = random.choice(blessings_data["blessings"])
    quote = random.choice(blessings_data["quotes"])
    return jsonify({
        'blessing': blessing,
        'quote': quote,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route('/get_all_blessings')
def get_all_blessings():
    return jsonify(blessings_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)