from setuptools import setup

setup(name='cxflow-scikit',
      version='0.1',
      description='Scientific plugin for cxflow',
      long_description='Plugin providing various statistical hooks and visualizations.',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Operating System :: Unix',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
      ],
      keywords='tensorflow wrapper',
      url='https://github.com/Cognexa/cxflow-scikit',
      author='Petr Belohlavek',
      author_email='me@petrbel.cz',
      license='MIT',
      packages=[
          'cxflow_scikit',
      ],
      include_package_data=True,
      zip_safe=False,
      test_suite='cxflow_scikit.tests',
      install_requires=[line for line in open('requirements.txt', 'r').readlines() if not line.startswith('#')],
     )
