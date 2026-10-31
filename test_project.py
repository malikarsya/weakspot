from project import has_sequential_number, is_common, calculate_entropy

def test_has_sequential_number():
    assert has_sequential_number("12") == False
    assert has_sequential_number("13") == False
    assert has_sequential_number("abc") == False
    assert has_sequential_number("") == False
    assert has_sequential_number("12abc123") == True
    assert has_sequential_number("123") == True
    assert has_sequential_number("x987y") == True
    assert has_sequential_number("9876") == True


def test_is_common():
    assert is_common("qwerty") == True
    assert is_common("1q2w3e4r5t") == True
    assert is_common("121212") == True
    assert is_common("football") == True
    assert is_common("michael") == True
    assert is_common("iloveyou") == True
    assert is_common("MisterMustache") == False
    assert is_common("MadamSarsaparilla") == False
    assert is_common("YouCantHackMeDummy123") == False
    assert is_common("PalPalePalPalePap") == False



def test_calculate_entropy_single_type():
    assert round(calculate_entropy("aaaa"), 2) == 18.80
    assert round(calculate_entropy("ABC"), 2) == 14.10
    assert round(calculate_entropy("1111"), 2) == 13.29
    assert round(calculate_entropy("::"), 2) == 10.00

def test_calculate_entropy_mixed_type():
    assert round(calculate_entropy("aA"), 2) == 11.40
    assert round(calculate_entropy("abc123"), 2) == 31.02
    assert round(calculate_entropy("aB3!"), 2) == 26.22
    

def test_calculate_entropy_empty():
    assert calculate_entropy("") == 0