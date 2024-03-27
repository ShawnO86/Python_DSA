from Gradebook import Gradebook

class CourseGradebook(Gradebook):
    def __init__(self):
        self.grades = {}
        # Type any code needed here - I didn't need any additional attributes.

    # Return a dict that maps students to scores
    # An entry exists for a student only if one had been assigned by set_score
    def get_assignment_scores(self, assignment_name):
        if assignment_name in self.grades:
            return self.grades[assignment_name]
        else:
            return {}

    def get_score(self, assignment_name, studentID):
        if assignment_name in self.grades and studentID in self.grades[assignment_name]:
            return self.grades[assignment_name][studentID]
        else:
            return None

    def get_sorted_assignment_names(self):
        return sorted(self.grades.keys())

    # get_sorted_student_ids() returns a list with all distinct student ID,
    # sorted in ascending order.
    def get_sorted_student_IDs(self):
        # using a set means I don't have to check for duplicates
        result = set()
        for key in self.grades:
            for id in self.grades[key].keys():
                    result.add(id)
                    # the test expects a sorted list so that is what I returned
        return sorted(list(result))
        

    # get_student_scores() gets all scores that exist in the gradebook for the
    # student whose ID matches the method argument, and returns a dict that maps
    # each assignment name to the student's score for that assignment.
    def get_student_scores(self, studentID):
        result = {}
        for key in self.grades:
            if studentID in self.grades[key]:
                result[key] = self.grades[key][studentID]
        return result

    def set_score(self, assignment_name, studentID, score):
        if assignment_name in self.grades:
            self.grades[assignment_name][studentID] = score
        else: 
            self.grades[assignment_name] = {studentID: score}
        return self.grades