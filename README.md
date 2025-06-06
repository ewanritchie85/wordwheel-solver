# Wordwheel Solver

A Python tool to solve wordwheel puzzles by finding all valid words from a set of letters input by the user.

## Features

- Finds all valid words from 8 outer letters and 1 central letter
- Uses the EWOL word list (`./word_list.txt`) but can be adapted
- Includes a CLI and Flask API interface for flexibility

## Installation

```bash
git clone https://github.com/yourusername/wordwheel-solver.git
cd wordwheel-solver
make requirements
```

## Usage

### CLI mode
Run the app with:
```bash
python src/main.py
```
You will be prompted to enter a centre letter and 8 outer letters.

### Flask API mode
Start the server with:
```bash
export FLASK_APP=api/solve.py
export PYTHONPATH=$(pwd)
flask run
```

Send a POST request to the API:
```bash
curl -X POST http://127.0.0.1:5000/api/solve \
     -H "Content-Type: application/json" \
     -d '{"centre_letter": "e", "outer_letters": ["b", "c", "d", "f", "g", "h", "i", "j"]}'
```


## Example (CLI)

```bash
python src/main.py
```
Sample input:
```
Centre letter: e
Outer letters: bcdghij
```

## License

MIT License

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

## Development

To run unit tests and check coverage:
```bash
make run-checks
```
Ensure that `word_list.txt` is present in the root directory.