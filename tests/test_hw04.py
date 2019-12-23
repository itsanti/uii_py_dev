from tasks import get_random_names, NAMES


def test_get_random_names_len():
    SIZE = 42
    assert len(get_random_names(NAMES, SIZE)) == SIZE


def test_get_random_names_set():
    SIZE = 42
    assert set(get_random_names(NAMES, SIZE)).issubset(NAMES), 'Generated set is not NAMES subset'
