import pytest


"""
    Запускает тесты в pytest нужно лишь прописать
    python test_start.py
    все тесты в папке tests там их и меняем
"""


def start():
    assert True == True


if __name__ == '__main__':
    pytest.main()
