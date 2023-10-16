from setuptools import find_packages, setup
import pathlib

with open(str(pathlib.Path(__file__).parent.absolute()) + \
        "/flitton_fib_py/version.py", "r") as fh:
    version = fh.read().split("=")[1].replace("'", "")

setup(
    name="python-rust-fib",
    version=version,
    author="Eduardo G. A. de Oliveira",
    author_email="eduardo.g.amaral1997@gmail.com",
    description="Calculates a Fibonacci number",
    install_requires=[
            "PyYAML>=4.1.2",
            "dill>=0.2.8",
    ],
    extras_require={
        "server": [
            "Flask>=1.0.0",
        ],
    },
    packages=find_packages(exclude=("tests", "begin")),
    python_requires='>=3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fib-number = fib_py.cmd.fib_numb:fib_numb',
        ],
    },
)

