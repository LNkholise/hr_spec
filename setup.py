from setuptools import setup, find_packages

setup(
    name='hr_spec',
    version='0.1.0',
    description='A simple, efficient astrophysics package to help classify stars and predict their evolutionary stages based on fundamental stellar parameters, without the need to reference complex HR diagrams every time.',
    author_email='leonkholise@gmail.com',
    author='Lekoro Nkholise',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'astropy'
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'hr_spec=hr_spec.cli:main',
        ],
    },
    classifiers=[],

)
