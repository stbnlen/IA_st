import math
import numpy as np
import pandas as pd


def get_number_of_bins(x: pd.Series, bin_size: float = 1.0) -> int:
    """Calculate the number of bins for a given pandas Series and bin size.

    Args:
        x: A pandas Series.
        bin_size: The size of each bin.

    Returns:
        The number of bins.
    """
    x = pd.Series(x)
    bin_size = float(bin_size)

    range_x = np.ptp(x)
    return int(math.ceil(range_x / bin_size))
