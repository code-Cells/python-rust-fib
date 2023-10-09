from setuptools import find_packages, setup

setup(
    name="python-rust-fib",
    version="0.0.1",
    author="Eduardo G. A. de Oliveira",
    author_email="eduardo.g.amaral1997@gmail.com",
    description="Calculates a Fibonacci number",
    install_requires=[],
    packages=find_packages(exclude=("tests", "begin")),
    python_requires='>=3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'fib-number = \
        flitton_fib_py.cmd.fib_numb:fib_numb',
        ],
    },
)

