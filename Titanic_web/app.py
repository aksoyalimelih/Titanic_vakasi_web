from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Verileri al
        bilet_sinifi = int(request.json.get('bilet_sinifi', 1))
        yas = int(request.json.get('yas', 0))
        cocuk_sayisi = int(request.json.get('cocuk_sayisi', 0))
        yanindaki_kisi_sayisi = int(request.json.get('yanindaki_kisi_sayisi', 0))
        yetiskin_mi = int(request.json.get('yetiskin_mi', 1))
        limanlar = {
            'C': request.json.get('liman_C', 'off') == 'on',
            'Q': request.json.get('liman_Q', 'off') == 'on',
            'S': request.json.get('liman_S', 'off') == 'on'
        }
        memleketler = {
            'Cherbourg': request.json.get('memleket_Cherbourg', 'off') == 'on',
            'Queenstown': request.json.get('memleket_Queenstown', 'off') == 'on',
            'Southampton': request.json.get('memleket_Southampton', 'off') == 'on'
        }
        
        # Burada modelinizi kullanarak tahmin yapabilirsiniz.
        # Örnek olarak sabit bir tahmin döndürülmüştür.
        prediction = 1 if bilet_sinifi == 1 else 0
        
        return jsonify({'prediction': prediction})

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)