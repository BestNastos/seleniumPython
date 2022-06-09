# from selenium import webdriver
# driver = webdriver.Firefox()
# driver.get("https://www.google.com/")
# driver.find_element_by_name("q").send_keys("software testing")

import unittest


class TestUnitTest(unittest.TestCase):  # class should start with "Test"

    def setUp(self):
        print("setUp and tearDown with (self) is called before and after every method")

    @classmethod
    def setUpClass(cls):
        print("setUpClass and tearDownClass with (cls) is called before and after class once")

    def test_upper(self):  # test should start with "test"
        print("test_upper")
        result = "foo"
        expected = "FOO"
        self.assertEqual(result, expected)

    def test_lower(self):
        print("test_lower")
        result = "foo"
        expected = "foo"
        self.assertEqual(result, expected)


# if __name__ == "__main__":
#     unittest.main(argv=[""], exit = False)

# output test_upper:
# Ran 1 test in 0.004s
# FAILED (failures=1)
# FOO != foo
# Expected :foo
# Actual   :FOO

# output test_lower:
# Ran 1 test in 0.002s
# OK

def runsuit():
    suite = unittest.TestSuite()
    suite.addTest(TestUnitTest('test_lower'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(runsuit()) # doesn/t work. it just runs everything . comment it out - nothing changes