from setuptools import setup
from occpollution import __version__ as current_version

setup(
  name='occpollution',
  version=current_version,
  description='Visualization of Ozone pollution in Occitanie',
  url='https://github.com/MegDie/occpollution',
  author='Mégane Diéval, Gueladio Niasse, Jean-Baptiste Elucson',
  author_email='megane.dieval@etu.umontpellier.fr',
  license='MIT',
  packages=['occpollution', 'occpollution.map',
   'occpollution.ani', 'occpollution.preprocess', 'occpollution.io', 'occpollution.map'],
  zip_safe=False
)