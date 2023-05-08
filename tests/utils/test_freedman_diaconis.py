import pytest
import pandas as pd
from utils.freedman_diaconis import freedman_diaconis_bandwidth


def test_input_type():
    with pytest.raises(TypeError):
        freedman_diaconis_bandwidth([1, 2, 3])


def test_output_type():
    x = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert isinstance(freedman_diaconis_bandwidth(x), float)


def test_output_range():
    x = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
    bandwidth = freedman_diaconis_bandwidth(x)
    assert bandwidth > 0 and bandwidth < max(x) - min(x)
