from shutil import copyfile
from platform import system as platform
from distutils.core import setup

setup(
    name='PySchema',
    version='0.1',
    packages=['PySchema'],
    requirements=[],
    url='https://github.com/mateusmoutinho/PySchema',
    license='MIT',
    author='Mateus Moutinho',
    author_email='mateusmoutinho01@gmial.com',
    keywords='schema validation',
          
    classifiers=[
        'Development Status :: 3 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'License :: OSI Approved :: MIT License',   # Again, pick a license


    ],
    description=''
)

