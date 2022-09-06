from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Anyone',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='PyCUI',
  version='0.0.1',
  description='A tool to make UI inside the CMD',
  long_description=open('README.txt').read() + '\n\n' + open('ChangeLog.txt').read(),
  url='',  
  author='Zbořil Filip',
  author_email='filip.zboril0@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='UI, CMD', 
  packages=find_packages(),
  install_requires=[''] 
)