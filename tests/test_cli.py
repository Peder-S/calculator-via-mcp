import subprocess
import sys

SCRIPT = [sys.executable, '-m', 'calculator.cli']

def run(args):
    proc = subprocess.run(SCRIPT + args, capture_output=True, text=True)
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()

def test_cli_expression_success():
    code, out, err = run(['2', '+', '2'])
    assert code == 0
    assert out == '4.0'

def test_cli_expression_error():
    code, out, err = run(['5', '/', '0'])
    assert code == 1
    assert 'Cannot divide by zero' in err

def test_cli_interactive(monkeypatch, capsys):
    inputs = iter(['3 * 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))
    from calculator.cli import main
    main()
    captured = capsys.readouterr()
    assert '9.0' in captured.out
