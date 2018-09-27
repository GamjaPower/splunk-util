from setuptools import setup, find_packages
from sputil.base import VERSION

setup(name='sputil',
      version=VERSION,
      url='https://github.com/GamjaPower/splunk-util',
      license='MIT',
      author='Jason Shim',
      author_email='sst9696@gmail.com',
      description='Splunk Utility',
      packages=find_packages(exclude=['']),
      long_description=open('README.md').read(),
      zip_safe=False,
      install_requires=['requests>=2.0.0',
                        'splunk-sdk>=1.6.0',
                        'pyutil>=3.0.0'],
      setup_requires=['nose>=1.3.0'],
      test_suite='nose.collector',
      scripts=['bin/sputil'],
      classifiers=[
          "Programming Language :: Python :: 2",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],)
