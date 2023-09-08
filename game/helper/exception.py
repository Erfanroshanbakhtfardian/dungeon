class MoveError(Exception):
    pass

class DirectionNameError(MoveError):
    pass 

class DirectionLimitError(MoveError):
    pass
