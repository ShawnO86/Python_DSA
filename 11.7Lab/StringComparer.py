class StringComparer:
    def compare(self, string1, string2):
        if string1 < string2:
            return -1
        elif string1 > string2:
            return 1
        else:
            return 0