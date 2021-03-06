from setuptools import setup, find_packages

setup(name="OpenOPC",
      version='1.3.2',
      download_url='https://github.com/iterativ/OpenOPC/tarball/master',
      description="This is a clone of http://openopc.sourceforge.net modified to be used with distutils",
      keywords='python, opc, openopc',
      url='http://openopc.sourceforge.net',
      license='GPLv2',
      packages=['OpenOPC'],
      zip_safe=False,
      )
