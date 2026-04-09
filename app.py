from flask import Flask, render_template

app = Flask(__name__)

shaharlar = ["Toshkent", "Samarqand", "Buxoro", "Namangan", "Andijon"]

@app.route('/shaharlar/<int:i>/info')
def shahar_info(i):
    if 0 <= i < len(shaharlar):
        shahar = shaharlar[i]
        uzunlik = len(shahar)
        bosh_harf = shahar[0].isupper()

        return render_template(
            'shahar_info.html',
            shahar=shahar,
            uzunlik=uzunlik,
            bosh_harf=bosh_harf
        )
    else:
        return "Noto'g'ri indeks ❌"

if __name__ == "__main__":
    app.run(debug=True)
