
def predict_evolution(mass, metallicity, age):
    """
    Predicts the stellar evolution of a star based on its mass, metallicity, and age.

    Parameters:
    mass (float): Mass of the star in solar masses.
    metallicity (float): Metallicity of the star.
    age (float): Age of the star in billions of years.

    Returns:
    dict: A dictionary containing predicted properties of the star.
    """
    # Main sequence lifetime estimate (Gyr)
    lifetime = (10/mass) * (1 + 0.1 * -metallicity) # in Gyr, metal-poor stars have longer lifetimes

    # Derived properties based on mass
    luminosity = mass ** 3.5 # in solar units
    radius = mass ** 0.5 # in solar radii
    temperature = 5778 * (mass ** 0.625) # in Kelvin, might adjust for metallicity in later iterations

    # Determine the evolutionary stage
    if age < lifetime:
        evolutionary_stage = "Main Sequence"
    elif age < lifetime * 1.5:
        evolutionary_stage = "Red Giant Branch"
    elif age < lifetime * 2:
        evolutionary_stage = "Horizontal Branch"
    else:
        evolutionary_stage = "Asymptotic Giant Branch"

    return {
        "luminosity": round(luminosity, 3),
        "radius": round(radius, 3),
        "temperature": round(temperature, 2),
        "lifetime": round(lifetime, 3),
        "evolutionary_stage": evolutionary_stage
    }

def classify(temperature: float, luminosity: float):
    """
    Classify a star based on its temperature and luminosity using spectral and luminosity classes.

    Parameters:
    temperature (float): The temperature of the star in Kelvin.
    luminosity (float): The luminosity of the star in solar units.

    Returns:
    str: The classification of the star, e.g., "G V" (sun-like main sequence star).
    """
    # Spectral class by temperature
    # Note: These thresholds are very approximate and can vary based on the specific star and its environment.
    # Since this is a utility package, we are using a simplified classification.
    if temperature < 3700:
        spectral_class = "M"
    elif 3700 <= temperature < 5200:
        spectral_class = "K"
    elif 5200 <= temperature < 6000:
        spectral_class = "G"
    elif 6000 <= temperature < 7500:
        spectral_class = "F"
    elif 7500 <= temperature < 10000:
        spectral_class = "A"
    elif 10000 <= temperature < 30000:
        spectral_class = "B"
    else:
        spectral_class = "O"

    # Luminosity class by luminosity
    # Note: These thresholds are very approximate and can vary based on the specific star and its environment.
    # Since this is a utility package, we are using a simplified classification.
    if luminosity < 0.01:
        # White Dwarf
        luminosity_class = "WD"
    elif 0.01 <= luminosity < 0.6:
        # Subdwarf
        luminosity_class = "VI"
    elif 0.6 <= luminosity < 10:
        # Main Sequence
        luminosity_class = "V"
    elif 10 <= luminosity < 1000:
        # Giant
        luminosity_class = "III"
    else:
        # Supergiant
        luminosity_class = "I"

    return {
            "spectral_class": spectral_class, 
            "luminosity_class": luminosity_class
    }