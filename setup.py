
from setuptools import setup, find_packages

# list dependencies from file
with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name="image_forgery_detection",
      version="0.1",
      description="Image forgery detector",
      author='La Pyae Phyo',
      packages=find_packages(),
      install_requires=requirements)
