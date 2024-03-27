from Gradebook import Gradebook

class CourseGradebook(Gradebook):
    def __init__(self):
        self.grades = {}
        self.assignment_names = set()
        self.student_ids = set()

    # Return a dict that maps students to scores
    # An entry exists for a student only if one had been assigned by set_score
    def get_assignment_scores(self, assignment_name):
        assignment_scores = {}
        for student_id, assignments in self.grades.items():
            if assignment_name in assignments:
                assignment_scores[student_id] = assignments[assignment_name]
        return assignment_scores

    def get_score(self, assignment_name, student_id):
        if student_id in self.grades and assignment_name in self.grades[student_id]:
            return self.grades[student_id][assignment_name]
        else:
            return None

    def get_sorted_assignment_names(self):
        result = list(self.assignment_names)
        return sorted(result)

    # get_sorted_student_ids() returns a list with all distinct student ID,
    # sorted in ascending order.
    def get_sorted_student_IDs(self):
        result = list(self.student_ids)
        return sorted(result)

    # get_student_scores() gets all scores that exist in the gradebook for the
    # student whose ID matches the method argument, and returns a dict that maps
    # each assignment name to the student's score for that assignment.
    def get_student_scores(self, studentID):
        for key in self.grades:
            if key == studentID:
                return self.grades[key]
        return {}

    def set_score(self, assignment_name, studentID, score):
        if studentID in self.grades:
            self.grades[studentID].update({assignment_name: score})
        else:
            self.grades[studentID] = {assignment_name: score}
        self.assignment_names.add(assignment_name)
        self.student_ids.add(studentID)
        
            
