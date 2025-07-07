# Calculator via MCP

A terminal-based calculator written in Python.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Peder-S/calculator-via-mcp.git
   cd calculator-via-mcp
   ```
2. (Optional) Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Interactive mode
```bash
python -m calculator.cli
```

### Direct expression
```bash
python -m calculator.cli 5 + 3
```

## Testing
Run the test suite with:
```bash
pytest
```
