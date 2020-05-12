import pytest
from src.exercise import main

def test_exercise(capsys):
    main()
    out, err = capsys.readouterr()
    assert out == "Matthew's account, balance: 900\nMy account, balance: 100\n"
