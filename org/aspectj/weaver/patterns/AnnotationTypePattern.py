EXACT = "byte  1"
BINDING = "byte  2"
NOT = "byte  3"
OR = "byte  4"
AND = "byte  5"
ELLIPSIS_KEY = "byte  6"
ANY_KEY = "byte  7"
WILD = "byte  8"
EXACTFIELD = "byte  9"
BINDINGFIELD = "byte  10"
BINDINGFIELD2 = "byte  11"
def fastMatches():
    '''returns FuzzyBoolean\n\n
    fastMatches(final AnnotatedElement annotated)\n
    '''
def remapAdviceFormals():
    '''returns AnnotationTypePattern\n\n
    remapAdviceFormals(final IntMap bindings)\n
    '''
def isAny():
    '''returns boolean\n\n
    isAny()\n
    '''
def resolveBindings():
    '''returns AnnotationTypePattern\n\n
    resolveBindings(final IScope scope, final Bindings bindings, final boolean allowBinding)\n
    '''
def setForParameterAnnotationMatch():
    '''returns None\n\n
    setForParameterAnnotationMatch()\n
    '''
def isForParameterAnnotationMatch():
    '''returns boolean\n\n
    isForParameterAnnotationMatch()\n
    '''
