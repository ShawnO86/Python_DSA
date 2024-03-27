from abc import ABC, abstractmethod

class Gradebook:
    # get_score() returns the specified student's score for the specified
    # assignment. None is returned if either:
    # - the assignment does not exist in the gradebook, or
    # - the assignment exists but no score exists for the specified student.
    @abstractmethod
    def get_score(self, assignment_name, studentID):
        pass

    # set_score() adds or updates a score in the gradebook.
    @abstractmethod
    def set_score(self, assignment_name, studentID, score):
        pass

    # get_assignment_scores() returns a dict that maps a student ID to
    # the student's score for the specified assignment. An entry
    # exists in the returned dict only if a score has been entered with the
    # set_score() function.
    @abstractmethod
    def get_assignment_scores(self, assignment_name):
        pass

    # get_sorted_assignment_names() returns a list with all distinct assignment
    # names, sorted in ascending order.
    @abstractmethod
    def get_sorted_assignment_names(self):
        pass

    # get_sorted_student_iDs() returns a list with all distinct student IDs,
    # sorted in ascending order.
    @abstractmethod
    def get_sorted_student_iDs(self):
        pass

    # get_student_scores() gets all scores that exist in the gradebook for the
    # student whose ID matches the function parameter. get_student_scores()
    # returns a dict that maps an assignment name to the student's
    # score for that assignment.
    @abstractmethod
    def get_student_scores(self, studentID):
        pass
