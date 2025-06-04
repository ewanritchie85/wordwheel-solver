# Wordwheel Solver

A Python tool to solve wordwheel puzzles by finding all valid words from a set of letters input by the user.

## Features

- Finds all possible words from a given set of 8 outer letters and one central letter
- Uses the EWOL word list, but can be adapted to use others
- Command-line interface

## Installation

```bash
git clone https://github.com/yourusername/wordwheel-solver.git
cd wordwheel-solver
make requirements
```

## Usage

```bash
python solver.py --letters abcdefg --center a
```

- `--letters`: All available letters
- `--center`: The required center letter

## Example

```bash
python solver.py --letters rstlnea --center e
```

## License

MIT License

## Contributing

Pull requests are welcome! For major changes, please open an issue first.
