from setuptools import setup

setup(name='aih_generate',
      version='0.1',
      description='Generate graphql code',
      url='',
      author='aih',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['aih_generate'],
      install_requires=[
          'JinJa2',
          'six',
          'PyYAML'
      ],
      scripts=['bin/aih_generate'],
      include_package_data=True,
      zip_safe=False)