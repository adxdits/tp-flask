from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

jeux_videos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/saisie.html', methods=['GET', 'POST'])
def saisie():
    if request.method == 'POST':
        nom = request.form['nom']
        plateforme = request.form['plateforme']
        prix = request.form['prix']
        description = request.form['description']
        jeu = {'nom': nom, 'plateforme': plateforme, 'prix': prix, 'description': description}
        jeux_videos.append(jeu)
        return redirect(url_for('liste'))
    return render_template('saisie.html')


@app.route('/liste.html')
def liste():
    return render_template('liste.html', jeux_videos=jeux_videos)

if __name__ == '__main__':
    app.run(debug=True)
