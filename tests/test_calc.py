from calc import new_func_name


def test_plus_sum():

    assert new_func_name(1, 2) == 3
    assert new_func_name(-4, 2) == -2
