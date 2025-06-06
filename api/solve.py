from flask import Flask, request, jsonify
from src.solver import solve

app = Flask(__name__)



@app.route("/api/solve", methods=["POST"])
def solve_words():
    """
    Summary:
        This code sets up a Flask web server that
        listens for POST requests on the '/solver' endpoint.

    Returns:
        JSON: List of valid words based on the centre letter
        and outer letters provided in the request.
    """
    data = request.get_json()
    centre_letter = data.get("centre_letter", "")
    outer_letters = data.get("outer_letters", [])
    print(f"Received centre: {centre_letter}, outer: {outer_letters}") # for debugging
    words = solve(centre_letter, outer_letters)
    return jsonify({"words": words})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
