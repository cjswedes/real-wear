from .base import *

DEBUG=True

# Test runner with no database creation
# TEST_RUNNER = 'ramsay.settings.discoverrunner.NoDbTestRunner'

INSTALLED_APPS += 'django_nose'
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
	'--with-coverage',
	'--cover-package=ledger, globe'
]