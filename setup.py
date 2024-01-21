from setuptools import setup, find_packages

setup(
    name='car_project',  # Replace with your package name
    version='0.1',  # Your package's initial version
    author='Fariz',  # Your name
    author_email='farrza111@gmail.com',  # Your email
    description='A Python project to model various types of cars',  # A short description
    # long_description=open('README.md').read(),  # Long description read from the README file
    long_description_content_type='text/markdown',  # Type of the long description
    # url='https://github.com/yourusername/car_project',  # Link to your project's repository
    packages=find_packages(exclude='tests*'),  # Automatically find all packages in your project
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Choose the appropriate license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum version requirement of Python
    extras_require={
        'dev': [ 'pytest'
            # Development dependencies
            # e.g., 'pytest', 'sphinx'
        ],
    },
)
