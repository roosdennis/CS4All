from random import *

def count_doubles(N):
    """Tel aantal dubbele ogen bij N worpen
    """
    if N == 0:    # base case
        return 0  # 0 worpen, 0 dubbele ogen...

    d1 = choice([1,2,3,4,5,6])  # eerste dobbelsteen
    d2 = choice([1,2,3,4,5,6])  # tweede dobbelsteen

    if d1 != d2:
        return 0 + count_doubles(N - 1)  # niet gelijk
    else:
        return 1 + count_doubles(N - 1)  # gelijk! tel 1 op