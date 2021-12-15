import pytest
from utils import age_percentiles


def test_percentel():
    dates = ['17.11.2000', '23.07.1976', '05.05.1981', '11.09.2001']
    response = age_percentiles(dates)
    print(response)
    assert response == {'50': '10.02.1991', '75': '24.02.1980', '99': '14.09.1976'}


if __name__ == '__main__':
    pytest.main()
