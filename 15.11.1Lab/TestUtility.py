from CourseGradebook import CourseGradebook

# convenience function for print numbers with singular word for 1, plural otherwise
def count_string(collection, singular, plural):
    return (f"1 {singular}"
            if len(collection) == 1
            else f'{len(collection)} {plural}'
            )

rows = [
    ["student ID", "homework 1", "homework 2", "midterm", "homework 3", "homework 4", "course project", "final exam"],
    ["11111",  "92",     "89",     "91",   "100",     "100",    "100",    "95"],
    ["22222",  "",       "75",     "77.5", "80.5",    "81",     "60",     "54"],
    ["33333",  "100",    "100",    "88",   "100",     "100",    "90",     "77.5"],
    ["44444",  "60",     "50",     "40",   "30",      "",       "",       ""],
    ["55555",  "73.5",   "76.5",   "64.5", "71.5",    "77.5",   "87",     "63.5"],
    ["66666",  "82.5",   "84.5",   "91",   "92.5",    "86",     "0",      "97"],
    ["77777",  "77",     "76",     "75",   "74",      "73",     "72",     "71"],
    ["88888",  "64.5",   "74.5",   "88",   "84",      "84",     "85.5",   "81.5"],
    ["99999",  "100",    "100",    "88",   "100",     "100",    "80",     "79"],
    ["10000",  "88",     "90",     "92",   "87",      "88.5",   "77.5",   "90"],
    ["90000",  "80",     "85",     "90",   "95",      "100",    "85",     "94.5"],
]

 # Returns a sample gradebook to use for testing purposes.
def make_sample_gradebook():
    gradebook = CourseGradebook()
    populate_gradebook_from_rows(gradebook, rows)
    return gradebook

# Populates a CourseGradebook from a of rows. Each row is a of
# Row 0 must be the header row. Column 0 must be the student ID column.
def populate_gradebook_from_rows(gradebook, rows):
    # Iterate through non-header rows
    for row in rows[1:]:
        # Call set_score for each non-empty entry
        for assignment_name, score in zip(rows[0][1:], row[1:]):
            if len(score) > 0:             # 0 means score was "", indicating no score for assignment
                # Add to gradebook
                gradebook.set_score(assignment_name, int(row[0]), float(score))
