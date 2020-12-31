import setuptools

with open("README.md", "r") as fo:
    long_description = fo.read()

setuptools.setup(
    name="geometria",
    version="1.0.0",
    author="B. T. Milnes",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BenjaminTMilnes/GeometriaPython",
    packages=["geometria"]
)
