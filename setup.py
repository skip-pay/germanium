from setuptools import setup, find_packages

setup(
    name='skip-django-germanium',
    version='2.6.0',
    description='Helpful methods for Python Selenium and REST testing',
    author='Lukas Rychtecky, Lubos Matl',
    author_email='lukas.rychtecky@gmail.com, matllubos@gmail.com',
    url='https://github.com/skip-pay/germanium',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=[
        'django>=4.2',
        'PyVirtualDisplay>=0.1.2',
        'selenium>=2.37.2',
        'pynose>=1.5.4',
        'responses>=0.5.1',
    ],
    include_package_data=True,
    zip_safe=False,
)
