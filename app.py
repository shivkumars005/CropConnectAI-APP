from flask import Flask, render_template, jsonify, request, send_file
import random
from gtts import gTTS
import io
import os

app = Flask(__name__)

# In-memory storage for OTPs and registered users
otp_storage = {}
registered_users = set()

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/prices')
def login():
    return render_template('prices.html')

@app.route('/about')
def terms():
    return render_template('about.html')

@app.route('/rotation')
def rotation():
    return render_template('rotate.html')

@app.route('/fertilizers')
def fertilizers():
    return render_template('fertilizers.html')

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/bot')
def bot():
    return render_template('bot.html')

# OTP routes
@app.route('/send_otp_register', methods=['POST'])
def send_otp_register():
    data = request.get_json()
    mobile = data['mobile']
    otp = random.randint(100000, 999999)
    otp_storage[mobile] = otp
    return jsonify({'success': True, 'otp': otp})

@app.route('/verify_otp_register', methods=['POST'])
def verify_otp_register():
    data = request.get_json()
    mobile = data['mobile']
    entered_otp = data['otp']
    if otp_storage.get(mobile) == int(entered_otp):
        registered_users.add(mobile)
        del otp_storage[mobile]
        return jsonify({'success': True, 'message': 'Registration completed'})
    return jsonify({'success': False, 'message': 'Invalid OTP'})

@app.route('/send_otp_login', methods=['POST'])
def send_otp_login():
    data = request.get_json()
    mobile = data['mobile']
    if mobile not in registered_users:
        return jsonify({'success': False, 'message': 'No account found, Register now'})
    otp = random.randint(100000, 999999)
    otp_storage[mobile] = otp
    return jsonify({'success': True, 'otp': otp})

@app.route('/verify_otp_login', methods=['POST'])
def verify_otp_login():
    data = request.get_json()
    mobile = data['mobile']
    entered_otp = data['otp']
    if otp_storage.get(mobile) == int(entered_otp):
        del otp_storage[mobile]
        return jsonify({'success': True, 'message': 'Login successful'})
    return jsonify({'success': False, 'message': 'Invalid OTP'})

# TTS API
@app.route('/tts', methods=['POST'])
def tts():
    data = request.get_json()
    text = data['text']
    lang = data['lang'].split('-')[0]
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        audio = io.BytesIO()
        tts.write_to_fp(audio)
        audio.seek(0)
        return send_file(audio, mimetype='audio/mp3')
    except Exception as e:
        print(f"TTS error: {e}")
        return jsonify({'success': False, 'message': 'TTS failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)
