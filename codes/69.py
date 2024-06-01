def mySqrt(x: int) -> int:
    if x == 0 or x == 1:
        return x

    l = 2
    r = x
    while True:
        m = int((l + r) / 2)
        m_sq = m * m
        lower_bound_check = (m - 1) * (m - 1)
        upper_bound_check = (m + 1) * (m + 1)
        if lower_bound_check < x and upper_bound_check > x:
            return m if x >= (m * m) else m - 1
        elif m_sq < x:
            l = m
        else:
            r = m
        
print(mySqrt(100))