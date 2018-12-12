from setuptools import setup

setup(name='gsym',
      version='0.1',
      description='A package to parse DWARF and generate gsym data from it.',
      url="TBD",
      packages=['gsym'],
      entry_points={
        'console_scripts': ['gsym=gsym.command_line:main'],
        },
      python_requires='>=2.7',
      install_requires=[]
      )
