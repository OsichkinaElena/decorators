from z2 import make_logger

@make_logger("log.txt")
def diff(a, b):
    return a-b
diff(9,3)
