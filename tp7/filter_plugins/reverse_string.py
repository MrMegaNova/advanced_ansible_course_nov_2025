def reverse_string (strval):
    return strval[::-1]

class FilterModule(object):
    def filters(self):
        return {
                "reverse_string":reverse_string
                }
