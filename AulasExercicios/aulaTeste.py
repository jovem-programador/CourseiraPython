def fatorial(n):
    i = fat = 1
    if not n < 0:
        while i <= n:
            fat = fat * i
            i += 1
    else:
        return 0
    return fat

def test_fatorial0():
    assert fatorial(0) == 1

def test_fatorial1():
    assert fatorial(1) == 1

def test_fatorial2():
    assert fatorial(4) == 24

def test_fatorial3():
    assert fatorial(5) == 120

def test_fatorial4():
    assert fatorial(-10) == 0