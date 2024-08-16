from setuptools import setup, find_packages

setup(

name='personal_assist_manager',
version='0.1',
packages=find_packages(
    include=['project-team-06-personal-assistant', 'project-team-06-personal-assistant.*']),
install_requires=[
    'colorama==0.4.6',
    'fuzzywuzzy==0.18.0',
    'Levenshtein==0.25.1',
    'prompt-toolkit==3.0.47',
    'python-Levenshtein==0.25.1',
    'rapidfuzz==3.9.6',
    'wcwidth==0.2.13',
    'win32-setctime==1.1.0',
    'setuptools==57.00',
],
entry_points={
    'console_scripts': [
        "Add entry point command to start an app(bot)"
    ],
},
author='6-team',
author_email='doroshenkoaldm@gmail.com',
description='Personal assistant bot',
long_description=open('README.md').read(),
long_description_content_type='text/markdown',
url='https://github.com/MHryhoriev/project-team-06-personal-assistant',
classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
],
)