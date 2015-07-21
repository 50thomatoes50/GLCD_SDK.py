from distutils.core import setup
setup(name='GLCD_SDK',
      version='0.0.1',
      description='Python Wrapper for Logitech LCD SDK',
      install_requires=['python=2.7'],
      author='Thomas Portassau',
      author_email='50thomatoes50@gmail.com',
      url='https://github.com/50thomatoes50/GLCD_SDK.py',
      py_modules=['GLCD_SDK'],
      package_dir={'GLCD_SDK': 'GLCD_SDK'},
      data_files=[('bitmaps', ['Screenshot/1.png', 'Screenshot/2.png'])],
      platforms=['Windows'],
      license="Mozilla Public License 2.0"
)