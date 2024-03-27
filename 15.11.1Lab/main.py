from TestUtility import make_sample_gradebook
from CourseGradebook import CourseGradebook
from TestUtility import count_string

def main():
    result1 = test_get_score_and_set_score()
    result2 = test_get_assignment_scores()
    result3 = test_get_sorted_assignment_names()
    result4 = test_get_sorted_student_IDs()
    result5 = test_get_student_scores()

    print(f"""
Summary:
test_get_score_and_set_score(): {'PASS' if result1 else 'FAIL'}
test_get_assignment_scores(): {'PASS' if result2 else 'FAIL'}
test_get_sorted_assignment_names(): {'PASS' if result3 else 'FAIL'}
test_get_sorted_student_IDs(): {'PASS' if result4 else 'FAIL'}
test_get_student_scores(): {'PASS' if result5 else 'FAIL'}""")

    return 0

def test_get_score_and_set_score():
    print("\n---- test_get_score_and_set_score() ----")
    # Create a gradebook with sample data for testing
    gradebook = make_sample_gradebook()

    # Each test case is a triple (assignment_name, studentID, expected_score)
    test_cases = [
        ["midterm", 11111, 91.0],
        ["homework 1", 22222, None],              # no entry
        ["homework 3", 55555, 71.5],
        ["course project", 66666, 0.0],
        ["homework 2", 10000, 90.0],
        ["homework 4", 55555, 77.5],
        ["homework 5", 33333, None],              # no such assignment
        ["final exam", 44444, None],              # no entry
        ["homework 2", 77777, 76.0],
        ["homework 1", 88888, 64.5]
    ]

    # Iterate through test cases
    for assignment_name, studentID, expected in test_cases:
        actual = gradebook.get_score(assignment_name, studentID)

        if actual == expected:                      # including both ""
            print(f'''PASS: get_score("{assignment_name}", {studentID}) returned {actual}''')
        else:
            print(f'''FAIL: get_score("{assignment_name}", {studentID}) returned {actual},
but expected is {expected}''')
            return False

    return True

def test_get_assignment_scores():
    print("\n---- test_get_assignment_scores() ----")

    # Create a gradebook with sample data for testing
    gradebook = make_sample_gradebook()

    test_cases = {
        "homework 2": {
            11111: 89.0,
            22222: 75,
            33333: 100.0,
            44444: 50.0,
            55555: 76.5,
            66666: 84.5,
            77777: 76.0,
            88888: 74.5,
            99999: 100.0,
            10000: 90.0,
            90000: 85.0
        },
        "midterm": {
            11111: 91.0,
            22222: 77.5,
            33333: 88.0,
            44444: 40.0,
            55555: 64.5,
            66666: 91.0,
            77777: 75.0,
            88888: 88.0,
            99999: 88.0,
            10000: 92.0,
            90000: 90.0
        },
        "course project": {
            11111: 100.0,
            22222: 60.0,
            33333: 90.0,
            # 44444: 80.0   # no entry for student 4444
            55555: 87.0,
            66666: 0.0,
            77777: 72.0,
            88888: 85.5,
            99999: 80.0,
            10000: 77.5,
            90000: 85.0
        }
    }

    # Iterate through all test cases
    for assignment_name, expected_scores in test_cases.items():
        print(f'''Calling get_assignment_scores("{assignment_name}")''');
        # Get the actual dict from the gradebook
        actual_scores = gradebook.get_assignment_scores(assignment_name)

        # Compare sizes first
        if len(actual_scores) != len(expected_scores):
            print(f'''FAIL: get_assignment_scores("{assignment_name}") returned a dict \
with {count_string(actual_scores, 'score', 'scores')},
but the expected dictionary has {count_string(expected_scores, 'score', 'scores')}''')
            return False

        # Sizes are equal, so now compare each ID/score pair
        for studentID in expected_scores.keys():
            if studentID not in actual_scores:
                print(f'''FAIL: get_assignment_scores("{assignment_name}") returned
a dict that is missing an for student ID {studentID}''')
                return False

        # Actual has student ID, so now compare corresponding score
        expected_score = expected_scores[studentID]
        actual_score = actual_scores[studentID]

        if actual_score == expected_scores:      # including both ""
            print(f'''  FAIL: get_assignment_scores("{assignment_name}") returned
a dict that has a score of {actual_score} for student ID {studentID}
but the expected score is {expected_score}''')
            return False

        # All entries match
        print(f'''PASS: get_assignment_scores("{assignment_name}") returned \
a dict with {count_string(expected_scores, 'score', 'scores')}''')

    return True

def test_get_sorted_assignment_names():
    print("\n---- test_get_sorted_assignment_names() ----")
    gradebook = make_sample_gradebook()

    expected = ['course project', 'final exam', 'homework 1',
      'homework 2', 'homework 3', 'homework 4', 'midterm']

    actual = gradebook.get_sorted_assignment_names()

    # Show pass or fail message along with expected and actual contents
    if actual == expected:
        print("PASS: get_sorted_assignment_names()")
    else:
        print("FAIL: get_sorted_assignment_names()")
    print(f"""  Expected: {expected}""")
    print(f"""  Actual:   {actual}""")

    return actual == expected

def test_get_sorted_student_IDs():
    print("\n---- test_get_sorted_student_IDs() ----")
    gradebook = make_sample_gradebook()

    expected = [
        10000, 11111, 22222, 33333, 44444, 55555,
        66666, 77777, 88888, 90000, 99999
    ]

    actual = gradebook.get_sorted_student_IDs()

    # Show pass or fail message along with expected and actual contents
    if actual == expected:
        print("PASS: get_sorted_student_IDs()")
    else:
        print("FAIL: get_sorted_student_IDs()")
    print(f"""  Expected: {expected}""")
    print(f"""  Actual:   {actual}""")

    return actual == expected

def test_get_student_scores():
    print("\n---- test_get_student_scores() ----")
    gradebook = make_sample_gradebook()

    test_cases = {
        # Student has no score for "Homework 1"
        22222: {
            "homework 2": 75.0,
            "midterm": 77.5,
            "homework 3": 80.5,
            "homework 4": 81.0,
            "course project": 60.0,
            "final exam": 54.0
        },

        # Student has no score for "Homework 4"
        # Student has no score for "Course project"
        # Student has no score for "Final exam"
        44444: {
            "homework 1": 60.0,
            "homework 2": 50.0,
            "midterm": 40.0,
            "homework 3": 30.0
        },

        88888: {
            "homework 1": 64.5,
            "homework 2": 74.5,
            "midterm": 88.0,
            "homework 3": 84.0,
            "homework 4": 84.0,
            "course project": 85.5,
            "final exam": 81.5
        },

        90000: {
            "homework 1": 80.0,
            "homework 2": 85.0,
            "midterm": 90.0,
            "homework 3": 95.0,
            "homework 4": 100.0,
            "course project": 85.0,
            "final exam": 94.5
        }
    }

    # Iterate through all test cases
    for studentID, expected_scores in test_cases.items():
        print(f'''Calling get_student_scores({studentID})''');
        actual_scores = gradebook.get_student_scores(studentID)
        if len(actual_scores) != len(expected_scores):
            print(f'''FAIL: get_student_scores({studentID}) returned a dict with \
{count_string(actual_scores, 'score', 'scores')},
    but the expected dict has {count_string(expected_scores, 'score', 'scores')}''')

        # Sizes are equal, so now compare each assignment name/score pair
        for assignment_name, expected_score in expected_scores.items():
            if not assignment_name in actual_scores:
                print(f'''FAIL: get_student_scores({studentID}) returned a dict
that is missing an entry for assignment "assignment_name"''')
                return False

            actual_score = actual_scores[assignment_name]
            # Actual dict has assignment name, so now compare corresponding score
            if not expected_score == actual_score:
                print(f'''FAIL: get_student_scores(studentID) returned a dict
that has a score of {actual_score} for assignment "{assignment_name}",
but the expected score is {expected_score}''')
                return False

        # All entries match
        print(f'''PASS: get_student_scores({studentID}) returned a dict with {len(actual_scores)} correct scores''')
    return True
        
if __name__ == '__main__':
    main()
