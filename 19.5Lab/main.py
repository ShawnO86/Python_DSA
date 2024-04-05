import sys
from StaticSetTestCases import BinaryOpsTestCase, UnaryOpsTestCase

def main():
    # First test case tests binary operations: union, intersection, and
    # difference
    binary_ops_test_case = BinaryOpsTestCase(
        (42, 63, 99, 32, 18, 77, 64, 50, 12),
        (64, 16, 32, 8, 4, 1, 2),
        (1, 2, 4, 8, 12, 16, 18, 32, 42, 50, 63, 64, 77, 99),  # expected union
        (32, 64),                                              # expected intersection
        (42, 63, 99, 18, 77, 50, 12),                          # expected A minus B
        (1, 2, 4, 8, 16)                                       # expected B minus A
   )
    binary_test_case_points = binary_ops_test_case.execute(sys.stdout)

    # Next test case tests unary operations: filter and map
    print()
    unary_ops_test_case = UnaryOpsTestCase(
        ("zero", "one", "two", "three", "four", "five",
          "six", "seven", "eight", "nine", "ten"),
        # Filter each string with a length <= 4
        lambda str: len(str) <= 4,
        # Map from the string to the string's length
        lambda str: len(str),
        ("zero", "one", "two", "four", "five", "six", "nine", "ten"), # expected filtered
        (3, 4, 5)                                              # expected mapped
   )
    unary_test_case_points = unary_ops_test_case.execute(sys.stdout)

    print()
    print("Binary operations score:", binary_test_case_points, "out of 3")
    print("Unary operations score:", unary_test_case_points, "out of 2")

if __name__ == '__main__':
    main()
