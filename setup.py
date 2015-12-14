from setuptools import setup
#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.

setup(name='Bibtex_File_Comparison_and_Update',
      version='1.2',
      description='This application aims to compare two bibtex files and help the user in keeping bibtex records in sync on both the files',
      url='https://github.com/mziauddin/Bibtex-File-Comparison-and-Update',
      download_url = 'https://pypi.python.org/pypi?:action=display&name=Bibtex_File_Comparison_and_Update&version=1.1',
      author='Mohammed Ziauddin',
      author_email='mdziauddin@ku.edu',
      # license='MIT',
      packages=['Bibtex-File-Comparison-and-Update'],
      install_requires=[
          'bibtexparser','gitpython','pymongo'
      ],      
      test_suite='nose.collector',
      tests_require=['nose'],
      scripts=['script'],
      classifiers = [
              'Programming Language :: Python',
              'Natural Language :: English',
              'Intended Audience :: Developers',
              'License :: OSI Approved :: Apache Software License',
              'Operating System :: OS Independent',
              'Topic :: Software Development :: Libraries :: Python Modules',
              'Topic :: Software Development :: Libraries :: Application Frameworks',
              ],
      zip_safe=False)