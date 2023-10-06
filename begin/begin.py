import os

name = os.getcwd().split("/")[-2]

with open("../setup.py", "w") as f:
    f.write("from setuptools import find_packages, setup\n\n")
    f.write("setup(\n")
    f.write(f"    name=\"{name}\",\n")
    f.write("    version=\"0.0.1\",\n")
    f.write("    author=\"Eduardo Gabriel Amaral de Oliveira\",\n")
    f.write("    author_email=\"eduardo.g.amaral1997@gmail.com\",\n")
    f.write("    description=\"\",\n")
    f.write("    install_requires=[],\n")
    f.write("    packages=find_packages(exclude=[]),\n")
    f.write("    python_requires=\">=3\",\n")
    f.write("    tests_require=[\"pytest\"],\n")
    f.write(")\n")

with open("./info.json", "w") as f:
    f.write("{\n")
    f.write(f"  \"name\": \"{name}\",\n")
    f.write("}\n")

