import pytest
import greenhouse


def test_convert_to_fahrenheit():
    assert greenhouse.convert_to_fahrenheit(0) == 32
    assert greenhouse.convert_to_fahrenheit(100) == 212
    assert greenhouse.convert_to_fahrenheit(-40) == -40
    assert greenhouse.convert_to_fahrenheit("37.0") == pytest.approx(98.6)
