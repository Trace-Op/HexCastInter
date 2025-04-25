import math
import core

class Sine(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="SIN",
            signature="Num -> Num",
            name="Sine",
            game_name="Sine Purification",
            parameters=[core.Number],
            output=[core.Number],
        )
    
    def execute(self, frame):
        if len(frame.stack) == 0:
            frame.stack.append(core.Garbage())
            return
        
        a = frame.stack.pop()

        if (not isinstance(a, core.Number) or isinstance(a, bool)):
            frame.stack.append(core.Garbage())
            return

        frame.stack.append(math.sin(a))
    
    tests = [
        ("Sine operation", "PI 4 DIV 1 ADD SIN", [math.sin((math.pi / 4.0)+1)]),
        ("Insuficient parameters 0 of 1", "SIN", [core.Garbage()]),
        ("Invalid type", "LIST SIN", [core.Garbage()]),
        ("Invalid type (bool)", "TRUE SIN", [core.Garbage()]),
    ]


class Cosine(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="COS",
            signature="Num -> Num",
            name="Cosine",
            game_name="Cosine Purification",
            parameters=[core.Number],
            output=[core.Number],
        )
    
    def execute(self, frame):
        if len(frame.stack) == 0:
            frame.stack.append(core.Garbage())
            return
        
        a = frame.stack.pop()

        if (not isinstance(a, core.Number) or isinstance(a, bool)):
            frame.stack.append(core.Garbage())
            return

        frame.stack.append(math.cos(a))
    
    tests = [
        ("Cosine operation", "PI 4 DIV 1 ADD COS", [math.cos((math.pi / 4.0)+1)]),
        ("Insuficient parameters 0 of 1", "COS", [core.Garbage()]),
        ("Invalid type", "LIST COS", [core.Garbage()]),
        ("Invalid type (bool)", "TRUE COS", [core.Garbage()]),
    ]


class Tangent(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="TAN",
            signature="Num -> Num",
            name="Tangent",
            game_name="Tangent Purification",
            parameters=[core.Number],
            output=[core.Number],
        )
    
    def execute(self, frame):
        if len(frame.stack) == 0:
            frame.stack.append(core.Garbage())
            return
        
        a = frame.stack.pop()

        if (not isinstance(a, core.Number) or isinstance(a, bool)):
            frame.stack.append(core.Garbage())
            return

        frame.stack.append(math.tan(a))
    
    tests = [
        ("Tangent operation", "PI 4 DIV 1 ADD TAN", [math.tan((math.pi / 4.0)+1)]),
        ("Insuficient parameters 0 of 1", "TAN", [core.Garbage()]),
        ("Invalid type", "LIST TAN", [core.Garbage()]),
        ("Invalid type (bool)", "TRUE TAN", [core.Garbage()]),
    ]


class Arcsine(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="ASIN",
            signature="Num -> Num",
            name="Arc sine",
            game_name="Inverse Sine Prfn.",
            parameters=[core.Number],
            output=[core.Number],
        )
    
    def execute(self, frame):
        if len(frame.stack) == 0:
            frame.stack.append(core.Garbage())
            return
        
        a = frame.stack.pop()

        if (not isinstance(a, core.Number) or isinstance(a, bool)):
            frame.stack.append(core.Garbage())
            return

        if (a > 1 or a < -1):
            frame.stack.append(core.Garbage())
            return

        frame.stack.append(math.asin(a))
    
    tests = [
        ("Arc sine operation", "1 ASIN", [math.asin(1)]),
        ("Arc sine Out of domain (>1)", "2 ASIN", [core.Garbage()]),
        ("Arc sine Out of domain (<-1)", "-2 ASIN", [core.Garbage()]),
        ("Insuficient parameters 0 of 1", "ASIN", [core.Garbage()]),
        ("Invalid type", "LIST ASIN", [core.Garbage()]),
        ("Invalid type (bool)", "TRUE ASIN", [core.Garbage()]),
    ]


class Arccosine(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="ACOS",
            signature="Num -> Num",
            name="Arc cosine",
            game_name="Inverse Cosine Prfn.",
            parameters=[core.Number],
            output=[core.Number],
        )
    
    def execute(self, frame):
        if len(frame.stack) == 0:
            frame.stack.append(core.Garbage())
            return
        
        a = frame.stack.pop()

        if (not isinstance(a, core.Number) or isinstance(a, bool)):
            frame.stack.append(core.Garbage())
            return

        if (a > 1 or a < -1):
            frame.stack.append(core.Garbage())
            return

        frame.stack.append(math.acos(a))
    
    tests = [
        ("Arc cosine operation", "1 ACOS", [math.acos(1)]),
        ("Arc cosine Out of domain (>1)", "2 ACOS", [core.Garbage()]),
        ("Arc cosine Out of domain (<-1)", "-2 ACOS", [core.Garbage()]),
        ("Insuficient parameters 0 of 1", "ACOS", [core.Garbage()]),
        ("Invalid type", "LIST ACOS", [core.Garbage()]),
        ("Invalid type (bool)", "TRUE ACOS", [core.Garbage()]),
    ]


class Arctangent(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="ATAN",
            signature="Num -> Num",
            name="Arc tangent",
            game_name="Inverse Tangent Prfn.",
            parameters=[core.Number],
            output=[core.Number],
        )
    
    def execute(self, frame):
        if len(frame.stack) == 0:
            frame.stack.append(core.Garbage())
            return
        
        a = frame.stack.pop()

        if (not isinstance(a, core.Number) or isinstance(a, bool)):
            frame.stack.append(core.Garbage())
            return

        frame.stack.append(math.atan(a))
    
    tests = [
        ("Arc tangent operation", "1 ATAN", [math.atan(1)]),
        ("Insuficient parameters 0 of 1", "ATAN", [core.Garbage()]),
        ("Invalid type", "LIST ATAN", [core.Garbage()]),
        ("Invalid type (bool)", "TRUE ATAN", [core.Garbage()]),
    ]


class Arctangent2(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="ATAN2",
            signature="Num, Num -> Num",
            name="Arc tangent 2",
            game_name="Inverse Tan. Prfn. II",
            parameters=[core.Number],
            output=[core.Number],
        )
    
    def execute(self, frame):
        if len(frame.stack) == 0:
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return

        if len(frame.stack) == 1:
            frame.stack.append(core.Garbage())
            return
        
        y = frame.stack.pop()
        x = frame.stack.pop()

        if ((not isinstance(x, core.Number) or isinstance(x, bool)) or 
            (not isinstance(y, core.Number) or isinstance(y, bool))):
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return

        frame.stack.append(math.atan2(x, y))
    
    tests = [
        ("Arc tangent (x,y) operation", "2 5 ATAN2", [math.atan2(2, 5)]),
        ("Insuficient parameters 0 of 2", "ATAN2", [core.Garbage(), core.Garbage()]),
        ("Insufficient parameters 1 of 2", "5 ATAN2", [5, core.Garbage()]),
        ("Invalid type", "LIST LIST ATAN2", [core.Garbage(), core.Garbage()]),
        ("Invalid type (bool)", "TRUE TRUE ATAN2", [core.Garbage(), core.Garbage()]),
    ]


class logarithm(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="LOG",
            signature="Num, Num -> Num",
            name="Logarithm",
            game_name="Logarithmic Distillation",
            parameters=[core.Number],
            output=[core.Number],
        )
    
    def execute(self, frame):
        if len(frame.stack) == 0:
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return

        if len(frame.stack) == 1:
            frame.stack.append(core.Garbage())
            return
        
        base = frame.stack.pop()
        x = frame.stack.pop()

        if ((not isinstance(x, core.Number) or isinstance(x, bool)) or 
            (not isinstance(base, core.Number) or isinstance(base, bool))):
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return

        frame.stack.append(math.log(x, base))
    
    tests = [
        ("Logarithm operation", "2 5 LOG", [math.log(2, 5)]),
        ("Insuficient parameters 0 of 2", "LOG", [core.Garbage(), core.Garbage()]),
        ("Insufficient parameters 1 of 2", "5 LOG", [5, core.Garbage()]),
        ("Invalid type", "LIST LIST LOG", [core.Garbage(), core.Garbage()]),
        ("Invalid type (bool)", "TRUE TRUE LOG", [core.Garbage(), core.Garbage()]),
    ]
