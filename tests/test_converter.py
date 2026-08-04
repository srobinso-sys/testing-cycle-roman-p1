# test suite
from roman.converter import * 
import pytest

def test_one():
    assert to_roman(1) == "I"


def test_two():
    assert to_roman(2) == "II"


def test_three():
    assert to_roman(3) == "III"


def test_five():
    assert to_roman(5) == "V"


def test_ten():
    assert to_roman(10) == "X"


def test_fifty():
    assert to_roman(50) == "L"


def test_hundred():
    assert to_roman(100) == "C"


def test_five_hundred():
    assert to_roman(500) == "D"


def test_thousand():
    assert to_roman(1000) == "M"


def test_from_one():
    assert from_roman("I") == 1


def test_from_five():
    assert from_roman("V") == 5


def test_from_two():
    assert from_roman("II") == 2


def test_roundtrip_small():
    assert from_roman(to_roman(7)) == 7


def test_roundtrip_medium():
    assert from_roman(to_roman(58)) == 58


def test_lowercase_input():
    assert from_roman("xi") == 11


def test_three_thousand_ninety_nine():
    assert to_roman(3999) == "MMMCMXCIX"

def test_from_roman_one_hundred():
    assert from_roman("C") == 100


def test_from_roman_five_hundred():
    assert from_roman("D") == 500


def test_from_roman_one_thousand():
    assert from_roman("M") == 1000

def test_from_roman_four():
    assert from_roman("IV") == 4


def test_from_roman_nine():
    assert from_roman("IX") == 9


def test_from_roman_forty():
    assert from_roman("XL") == 40


def test_from_roman_ninety():
    assert from_roman("XC") == 90


def test_from_roman_four_hundred():
    assert from_roman("CD") == 400


def test_from_roman_nine_hundred():
    assert from_roman("CM") == 900

def test_from_roman_error_integer_input():
    with pytest.raises(RomanError, match="value must be a string"):
        from_roman(123)


def test_from_roman_error_none_input():
    with pytest.raises(RomanError, match="value must be a string"):
        from_roman(None)


def test_from_roman_error_empty_string():
    with pytest.raises(RomanError, match="empty string is not a roman numeral"):
        from_roman("")


def test_from_roman_error_invalid_char_z():
    with pytest.raises(RomanError, match="invalid roman character: Z"):
        from_roman("XZI")


def test_from_roman_error_invalid_char_digit():
    with pytest.raises(RomanError, match="invalid roman character: 1"):
        from_roman("X1V")


def test_from_roman_error_invalid_subtractive_il():
    with pytest.raises(RomanError, match="invalid subtractive pair: IL"):
        from_roman("IL")


def test_from_roman_error_invalid_subtractive_vx():
    with pytest.raises(RomanError, match="invalid subtractive pair: VX"):
        from_roman("VX")


def test_from_roman_error_above_maximum():
    with pytest.raises(RomanError, match="value out of range 1..3999"):
        from_roman("MMMM")
        

def test_is_valid_roman_valid_simple():
    assert is_valid_roman("X") is True


def test_is_valid_roman_valid_complex():
    assert is_valid_roman("MCMXCIV") is True


def test_is_valid_roman_valid_lowercase():
    assert is_valid_roman("iv") is True


def test_is_valid_roman_invalid_character():
    assert is_valid_roman("ABC") is False


def test_is_valid_roman_invalid_subtractive_pair():
    assert is_valid_roman("IL") is False


def test_is_valid_roman_empty_string():
    assert is_valid_roman("") is False


def test_is_valid_roman_invalid_type():
    assert is_valid_roman(123) is False

# Integration tests

def test_integration_add_roman_ii_and_ii():
    result = add_roman("II", "II")
    assert result == "IV"
    assert is_valid_roman(result) is True


def test_integration_add_roman_iv_and_vi():
    result = add_roman("IV", "VI")
    assert result == "X"
    assert is_valid_roman(result) is True


def test_integration_add_roman_mcmxciv_and_vi():
    result = add_roman("MCMXCIV", "VI")
    assert result == "MM"
    assert is_valid_roman(result) is True


def test_integration_subtract_roman_x_and_i():
    result = subtract_roman("X", "I")
    assert result == "IX"
    assert is_valid_roman(result) is True


def test_integration_to_roman_boundary_min_valid():
    assert to_roman(1) == "I"


def test_integration_to_roman_boundary_max_valid():
    assert to_roman(3999) == "MMMCMXCIX"


def test_integration_to_roman_boundary_below_min_zero():
    with pytest.raises(RomanError, match="value must be >= 1"):
        to_roman(0)


def test_integration_to_roman_boundary_above_max_four_thousand():
    with pytest.raises(RomanError, match="value must be <= 3999"):
        to_roman(4000)


def test_integration_to_roman_boundary_negative_number():
    with pytest.raises(RomanError, match="value must be >= 1"):
        to_roman(-1)


def test_integration_to_roman_type_boolean_true():
    with pytest.raises(RomanError, match="value must be an integer"):
        to_roman(True)


def test_integration_to_roman_type_boolean_false():
    with pytest.raises(RomanError, match="value must be an integer"):
        to_roman(False)


def test_integration_to_roman_type_float():
    with pytest.raises(RomanError, match="value must be an integer"):
        to_roman(10.0)


def test_integration_to_roman_type_string():
    with pytest.raises(RomanError, match="value must be an integer"):
        to_roman("10")


def test_integration_from_roman_type_none():
    with pytest.raises(RomanError, match="value must be a string"):
        from_roman(None)


def test_integration_from_roman_type_list():
    with pytest.raises(RomanError, match="value must be a string"):
        from_roman(["X"])


def test_integration_from_roman_syntax_invalid_subtractive_il():
    with pytest.raises(RomanError, match="invalid subtractive pair: IL"):
        from_roman("IL")


def test_integration_from_roman_syntax_invalid_subtractive_ic():
    with pytest.raises(RomanError, match="invalid subtractive pair: IC"):
        from_roman("IC")


def test_integration_from_roman_syntax_invalid_subtractive_vx():
    with pytest.raises(RomanError, match="invalid subtractive pair: VX"):
        from_roman("VX")


def test_integration_from_roman_syntax_invalid_subtractive_xd():
    with pytest.raises(RomanError, match="invalid subtractive pair: XD"):
        from_roman("XD")


def test_integration_from_roman_syntax_unsupported_characters():
    with pytest.raises(RomanError, match="invalid roman character"):
        from_roman("XIV!")


def test_integration_from_roman_syntax_whitespace_padding():
    assert from_roman(" XIV ") == 14


def test_integration_from_roman_syntax_empty_string():
    with pytest.raises(RomanError, match="empty string is not a roman numeral"):
        from_roman("")


def test_integration_subtract_roman_exact_zero_boundary():
    with pytest.raises(RomanError):
        subtract_roman("I", "I")


def test_integration_subtract_roman_negative_result():
    with pytest.raises(RomanError):
        subtract_roman("V", "X")


def test_integration_add_roman_exact_max_boundary():
    result = add_roman("MMMCMXCVIII", "I")
    assert result == "MMMCMXCIX"
    assert is_valid_roman(result) is True


def test_integration_add_roman_overflow_maximum():
    with pytest.raises(RomanError):
        add_roman("MMM", "M")
        
# Acceptance test

def test_from_roman_trims_leading_and_trailing_whitespace():
    """Given a valid roman string with leading or trailing whitespace,
    When from_roman is called,
    Then it should trim the ends and return the correct integer.
    """
    assert from_roman("  IV  ") == 4
    assert from_roman("X ") == 10
    assert from_roman("\tMCMXCIV\n") == 1994


def test_from_roman_rejects_internal_whitespace():
    """Given a string with internal whitespace between valid symbols,
    When from_roman is called,
    Then it must raise RomanError.
    """
    with pytest.raises(RomanError):
        from_roman("X I")

    with pytest.raises(RomanError):
        from_roman("I V")

@pytest.mark.parametrize(
    "invalid_canonical_input",
    [
        "IIII",  
        "VIIII", 
        "XXXX",   
        "VV",     
    ],
)
def test_from_roman_rejects_non_canonical_strings(invalid_canonical_input):
    """Given a string representing a non-canonical roman numeral,
    When from_roman is called,
    Then it must raise RomanError.
    """
    with pytest.raises(RomanError):
        from_roman(invalid_canonical_input)