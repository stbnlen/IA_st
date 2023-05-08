import numpy as np
import pandas as pd


def freedman_diaconis_bandwidth(x: pd.Series) -> float:
    """
    Calculate the optimal bandwidth using the Freedman-Diaconis rule.

    Parameters:
    x (pandas.Series): The input data.

    Returns:
    float: The optimal bindwidth.

    Raises:
    TypeError: If the input is not a pandas Series object.
    """
    if not isinstance(x, pd.Series):
        raise TypeError("Input must be a pandas Series object.")
    IQR: float = np.subtract(*np.percentile(x, [75, 25]))
    N: int = len(x)
    k: float = 1 / 3
    return 2 * IQR / np.power(N, k)
