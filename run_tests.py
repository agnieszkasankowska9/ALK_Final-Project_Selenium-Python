import HtmlTestRunner
import unittest

loader = unittest.TestLoader()
suite = loader.discover('tests')

runner = HtmlTestRunner.HTMLTestRunner(
    output='reports',
    report_name='Test Report'
)

runner.run(suite)