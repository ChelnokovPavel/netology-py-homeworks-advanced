import io

import pytest

from homework_4.app import secretary_program_start


@pytest.mark.parametrize('commands', [
    (['p', '10006', 'q']),
    (['ap', 'q']),
    (['l', 'q']),
    (['s', '10006', 'q']),
    (['a', '666', 'necronomicon', 'warlock', '3', 'q']),
    (['d', '10006', 'q']),
    (['m', '10006', '3', 'q']),
    (['as', '4', 'q']),
    (['help', 'q']),
    (['q'])
])
def test_secretary_program_start(monkeypatch, commands):
    mock_stdout = io.StringIO()
    monkeypatch.setattr('sys.stdout', mock_stdout)
    commands = iter(commands)
    monkeypatch.setattr('builtins.input', lambda _: next(commands))
    secretary_program_start()
    mock_stdout.getvalue()
    assert isinstance(mock_stdout.getvalue(), str)
