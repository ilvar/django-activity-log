from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='django-activity-log',
      version=version,
      description="Generic Django activity logging app!",

      classifiers=[
        'Development Status :: 1 - Initial',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
      ],
      keywords='django activity models',
      author='Arcady Chumachenko',
      author_email='arcady.chumachenko@gmail.com',
      url='http://github.com/ilvar/django-activity-log',
      license='BSD',
      packages = find_packages('.'),
      package_dir = {'': '.'},
      include_package_data=True,
      install_requires=[
          'setuptools',
      ],
      zip_safe=False,
)
