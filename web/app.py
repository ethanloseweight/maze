from flask import Flask, render_template
from models.score_manager import ScoreManager

app = Flask(__name__)
score_manager = ScoreManager()
score_manager.load_from_json("../maze/scores.json")

""" To show HTML Default page """
@app.route('/')
def list_scores():
    data = score_manager.serialize()
    return render_template("list.html", scores=data["scores"])


if __name__ == '__main__':
    app.run(debug=True)

