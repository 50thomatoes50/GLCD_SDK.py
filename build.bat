@echo off
d:\Python27_32\python setup.py sdist --formats=gztar,zip
d:\Python27_32\python setup.py bdist_wininst
pause