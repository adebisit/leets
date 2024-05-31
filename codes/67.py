def addBinary(self, a: str, b: str) -> str:
    n = len(a)
    m = len(b)
    _n = n if n > m else m
    res = ""
    quot = 0
    
    for i in range(1, _n + 1):
        _a = a[-i] if i <= n else "0"
        _b = b[-i] if i <= m else "0"
        digit = int(_a) + int(_b) + quot
        quot = digit // 2
        rem = digit % 2
        res = str(rem) + res
    return ("1" if quot == 1 else "") + res