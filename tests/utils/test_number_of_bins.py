import pandas as pd
from utils.number_of_bins import get_number_of_bins


def test_get_number_of_bins_with_default_bin_size():
    x = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    expected_result = 9
    assert get_number_of_bins(x) == expected_result


def test_get_number_of_bins_with_custom_bin_size():
    x = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    bin_size = 2
    expected_result = 5
    assert get_number_of_bins(x, bin_size) == expected_result


def test_get_number_of_bins_with_negative_values():
    x = pd.Series([-10, -5, 0, 5, 10])
    expected_result = 20
    assert get_number_of_bins(x) == expected_result
