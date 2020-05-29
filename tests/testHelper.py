class formatter:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class TestHelper:
    def __init__(self):

        # Total number of tests run and the success rate
        self.test_counter = 0
        self.tests_passed = 0
        self.tests_failed = 0

        # color helper
        self.format_helper = formatter()

    # Call when a given test passes
    def __pass_test(self, testName):
        self.test_counter += 1
        self.tests_passed += 1
        print(self.format_helper.OKGREEN + "PASSED TEST #{} : {}".format(self.test_counter, testName) + self.format_helper.ENDC)

    # Call when a given test fails
    def __fail_test(self, testName):
        self.test_counter += 1
        self.tests_failed += 1
        print(self.format_helper.FAIL + "FAILED TEST #{} : {}".format(self.test_counter, testName) + self.format_helper.ENDC)

    # Call for test summaries
    def test_summary(self):
        print(self.format_helper.UNDERLINE + "Test Summary: " + self.format_helper.ENDC)
        print("\t Total tests run:    {}".format(self.test_counter))
        print("\t Total tests passed: {}".format(self.tests_passed))
        print("\t Total tests failed: {}".format(self.tests_failed))
        print("\t Success rate:       {:0.2f}".format(self.tests_passed / self.test_counter))

    # Tests if all provided arguments (after the test name) are equivalent
    def test_equal(self, testName, *args):
        n = len(args)

        if n <= 1:
            raise Error("Insufficient arguments to compare")

        for i in range(n-1):
            if args[i] != args[i+1]:
                self.__fail_test(testName)
                return

        self.__pass_test(testName)

    # Tests if all provided arguments (after the test name) are not equivalent
    def test_not_equal(self, testName, *args):
        n = len(args)

        if n <= 1:
            raise Error("Insufficient arguments to compare")

        for i in range(n-1):
            for j in range(i+1, n):
                if args[i] == args[j]:
                    self.__fail_test(testName)
                    return

        self.__pass_test(testName)



