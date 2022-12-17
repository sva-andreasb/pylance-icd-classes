CLASS = "int  1"
INTERFACE = "int  2"
ASPECT = "int  3"
INNER = "int  4"
ANONYMOUS = "int  5"
ENUM = "int  6"
ANNOTATION = "int  7"
def ():
    '''returns TypeCategoryTypePattern\n\n
    (final int category)\n
    '''
def getTypeCategory():
    '''returns int\n\n
    getTypeCategory()\n
    '''
def matchesInstanceof():
    '''returns FuzzyBoolean\n\n
    matchesInstanceof(final ResolvedType type)\n
    '''
def parameterizeWith():
    '''returns TypePattern\n\n
    parameterizeWith(final Map typeVariableMap, final World w)\n
    '''
def accept():
    '''returns Object\n\n
    accept(final PatternNodeVisitor visitor, final Object data)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream s)\n
    '''
