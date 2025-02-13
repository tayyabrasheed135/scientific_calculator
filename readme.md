# Scientific Calculator

A Python-based scientific calculator that implements various mathematical operations using Object-Oriented Programming principles. This calculator supports basic arithmetic, scientific operations, and trigonometric calculations while maintaining a history of all operations.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Scientific operations (square root, power, natural logarithm)
- Trigonometric functions (sine, cosine, tangent)
- Calculation history logging
- Input validation
- Exception handling
- User-friendly command-line interface

## Project Structure

```
scientific-calculator/
├── src/
├── __init__.py
├── calculator.py
├── helper.py
├── main.py
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

## Demo
[![Scientific Calculator Demo](https://github.com/tayyabrasheed135/scientific_calculator/blob/main/R%26D%20progress%2014-feb-2025.mp4)](<video controls src="https://github.com/tayyabrasheed135/scientific_calculator/blob/main/R%26D%20progress%2014-feb-2025.mp4" title="./R&D%20progress%2014-feb-2025.mp4"></video>)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/scientific-calculator.git
cd scientific-calculator
```

2. (Optional) Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the calculator from the command line:

```bash
python src/main.py
```

Follow the on-screen menu to perform calculations:
1. Choose an operation from the menu (1-12)
2. Enter the required numbers when prompted
3. View the result
4. Check calculation history using option 11
5. Exit using option 12

## Testing

Run the tests using pytest:

```bash
pytest tests/
```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request


## Acknowledgments

- Python `math` module for mathematical operations
- Built with Python 3.x