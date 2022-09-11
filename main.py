from flask import Flask, render_template

from utils import load_candidates_from_json, get_candidate

app = Flask(__name__)


@app.route('/')
def main_page():
	candidates: List[dict] = load_candidates_from_json()
	return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:idx>")
def candidate_page(idx):
	candidate: dict = get_candidate(idx)
	if not candidate:
		return "Кандидат не найден"
	return render_template("card.html", candidate=candidate)


@app.route("/candidate/")
app.run()
