from setuptools import setup

# to publish use:
# > python setup.py sdist upload
# which depends on ~/.pypirc

setup(name='shap',
      version='0.4',
      description='Explains the output of any machine learning model using expectations and Shapley values.',
      url='http://github.com/slundberg/shap',
      author='Scott Lundberg',
      author_email='slund1@cs.washington.edu',
      license='MIT',
      packages=['shap'],
      install_requires=['numpy', 'scipy', 'iml', 'sklearn', 'matplotlib'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
