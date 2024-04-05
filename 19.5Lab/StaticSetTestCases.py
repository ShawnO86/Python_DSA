from StaticSet import StaticSet

class StaticSetTestCase:
    def compare_sets(self,
                     test_feedback,
                     actual,
                     expected,
                     title,
                     points):
        passed = True

        # Compare actual vs. expected set's size
        if actual.get_size() != expected.get_size():
            passed = False
        else:
            # Expected and actual have equal sizes, so compare contents
            for element in expected.elements:
                if not actual.contains(element):
                    passed = False

        # Print the pass or fail message with expected and actual sets
        print(f"""{'PASS' if passed else 'FAIL'}: {title}
  Expected: {expected}
  Actual:   {actual}""",
              file=test_feedback)

        return points if passed else 0.0

    def execute(self, test_feedback):
        pass

# BinaryOpsTestCase represents an executable test case for the StaticSet's
# union(), intersection(), and difference() methods
class BinaryOpsTestCase(StaticSetTestCase):
    def __init__(self,
                 A_elements,
                 B_elements,
                 expected_union_elements,
                 expected_intersection_elements,
                 expected_A_minus_B_elements,
                 expected_B_minus_A_elements):
        self.set_A = StaticSet(A_elements)
        self.set_B = StaticSet(B_elements)
        self.expected_union = StaticSet(expected_union_elements)
        self.expected_intersection = StaticSet(expected_intersection_elements)
        self.expected_A_minus_B = StaticSet(expected_A_minus_B_elements)
        self.expected_B_minus_A = StaticSet(expected_B_minus_A_elements)

    def execute(self, test_feedback):
        # Print sets A and B first
        print(f"""A = {self.set_A}""", file=test_feedback)
        print(f"""B = {self.set_B}""", file=test_feedback)

        # Create the two StaticSet objects from the StaticSet objects
        static_set_A = StaticSet(self.set_A.elements)
        static_set_B = StaticSet(self.set_B.elements)

        # Create the union, intersection, and differences
        actual_union = static_set_A.union(static_set_B)
        actual_intersection = static_set_A.intersection(static_set_B)
        actual_A_minus_B = static_set_A.difference(static_set_B)
        actual_B_minus_A = static_set_B.difference(static_set_A)

        # Verify that performing operations didn't change either StaticSet's size
        size_checks = ((static_set_A, self.set_A, "A"),
                       (static_set_B, self.set_B, "B")
                       )

        for size_check in size_checks:
            set1, set2, set_name = size_check
            if set1.get_size() != set2.get_size():
                print(f"""FAIL: creating the union/intersection/difference of static_sets A and B
changed set {set_name}'s size from {set1.get_size()} to {set2.get_size()}""",
                      file=test_feedback)
                return 0.0

        # Compare actual vs. expected sets
        total_points = 0.0
        total_points += self.compare_sets(
            test_feedback,
            actual_union,
            self.expected_union,
            "Union operation",
            1.0
        )
        total_points += self.compare_sets(
            test_feedback,
            actual_intersection,
            self.expected_intersection,
            "Intersection operation",
            1.0
        )
        total_points += self.compare_sets(
            test_feedback,
            actual_A_minus_B,
            self.expected_A_minus_B,
            "A \ B operation",
            0.5
        )
        total_points += self.compare_sets(
            test_feedback,
            actual_B_minus_A,
            self.expected_B_minus_A,
            "B \ A operation",
            0.5)

        return  total_points

# UnaryOpsTestCase represents an executable test case for the StaticSet's
# filter() and map() methods
class UnaryOpsTestCase(StaticSetTestCase):
    def __init__(self,
                 source_set,
                 filter_predicate,
                 map_function,
                 expected_filtered,
                 expected_mapped
                 ):
        self.source_set = StaticSet(source_set)
        self.filter_predicate = filter_predicate
        self.map_function = map_function
        self.expected_filtered = StaticSet(expected_filtered)
        self.expected_mapped = StaticSet(expected_mapped)

    def execute(self, test_feedback):
        # Print the source set first
        print(f"""Set = {self.source_set}""", file=test_feedback)

        # Create the StaticSet object from the set source
        static_set = StaticSet(self.source_set.elements)

        # Create the filtered and mapped sets
        actual_filtered = static_set.filter(self.filter_predicate)
        actual_mapped = static_set.map(self.map_function)

        # Verify that performing operations didn't change static_set's size
        if static_set.get_size() != self.source_set.get_size():
            print(f"""FAIL: filtering and/or mapping static_set S changed S's size \
from {self.source_set.get_size()} to {static_set.get_size()}""",
                  file=test_feedback)
            return 0.0

        # Compare actual vs. expected sets
        total_points = 0.0
        total_points += self.compare_sets(
            test_feedback,
            actual_filtered,
            self.expected_filtered,
            "Filter operation",
            1.0
        )
        total_points += self.compare_sets(
            test_feedback,
            actual_mapped,
            self.expected_mapped,
            "Map operation",
            1.0
        )

        return total_points
