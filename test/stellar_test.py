from hr_spec import stellar
import astropy.units as u
import numpy as np
from astropy.constants import L_sun, R_sun

def test_predict_evolution():
    T_sun = 5778 * u.K  # Solar temperature in Kelvin

    # Test case 1: Main Sequence Star
    result = stellar.predict_evolution(1.0, 0.02, 5)
    
    # Expected values in solar units:
    # Learn more about solar units at https://docs.astropy.org/en/stable/constants/
    expected_luminosity = 1.0  # 1.0 means 1 solar luminosity
    expected_radius = 1.0      # 1.0 means 1 solar radius
    expected_temperature = 5778.0
    expected_lifetime = 10.0   # 10 billion years for a Sun-like star
    
    # Using np.isclose() to compare floating-point values with some tolerance
    # I used a relative tolerance of 1e-5 for luminosity, radius, and temperature
    # and a relative tolerance of 1e-2 for lifetime
    # This is to account for the fact that lifetime can be more variable
    assert np.isclose(result['luminosity'], expected_luminosity, rtol=1e-5)
    assert np.isclose(result['radius'], expected_radius, rtol=1e-5)
    assert np.isclose(result['temperature'], expected_temperature, rtol=1e-5)
    assert np.isclose(result['lifetime'], expected_lifetime, rtol=1e-2)  # Slightly looser tolerance for lifetime
    assert result['evolutionary_stage'] == "Main Sequence"


def test_classify():
    # Test case 1: G V Star
    result = stellar.classify(5778, 1.0)
    assert result == {"spectral_class": "G", "luminosity_class": "V"}