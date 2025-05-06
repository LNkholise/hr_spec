## HR-Spec: Stellar Evolution Predictor

HR-Spec is a Python package for basic stellar evolution prediction and classification. It provides simple utilities to predict stellar parameters and classify stars based on their temperature and luminosity.

### Freatures
This package allows you to :
 - Predict stellar evolution parameters (luminosity, radius, temperature, lifetime)
 - Classify stars by spectral type and luminosity class
 -Integrate Astropy units for physical calculations

### Installation
You can install HR-spec using 
```bash
    pip install hr-spec
```
Alternatively, you can install from source (which is the viable option for now):
```bash
    git clone https://github.com/LNkholise/hr-spec.git
    cd hr-spec
    pip install -e .
```
or 
```bash 
    pip install .
```

### Dependencies
See `requirements.txt` for extensive list.

### Usage 
#### Python API
```python
    from hr_spec import stellar

    # Predict evolution of a Sun-like star
    result = stellar.predict_evolution(mass=1.0, metallicity=0.02, age=5)
    print(f"Evolutionary parameters: {result}")

    # Classify a star
    classification = stellar.classify(temperature=5778, luminosity=1.0)
    print(f"Spectral classification: {classification}")
```
#### Command Line Interface
```bash
    # Predict stellar evolution
    hr_spec predict --mass  1.0 --metallicity 0.02 --age 5

    # Classify a star
    hr_spec classify --temperature 5778 --luminosity 1.0
```
#### Contributing
If you find any bugs or would like to contribute to the development of `HR Spec`, feel free to open an issue or create a pull request.
- Fork repo.
- Create a new branch `git checkout -b feature-branch`.
- Make changes.
- Commit your changes `git push feature-branch`.
- Open a pull request.