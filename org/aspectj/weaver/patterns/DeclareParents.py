def ():
    '''returns DeclareParents\n\n
    (final TypePattern child, final List parents, final boolean isExtends)\n
    '''
def match():
    '''returns boolean\n\n
    match(final ResolvedType typeX)\n
    '''
def accept():
    '''returns Object\n\n
    accept(final PatternNodeVisitor visitor, final Object data)\n
    '''
def parameterizeWith():
    '''returns Declare\n\n
    parameterizeWith(final Map typeVariableBindingMap, final World w)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
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
def parentsIncludeInterface():
    '''returns boolean\n\n
    parentsIncludeInterface(final World w)\n
    '''
def parentsIncludeClass():
    '''returns boolean\n\n
    parentsIncludeClass(final World w)\n
    '''
def resolve():
    '''returns None\n\n
    resolve(final IScope scope)\n
    '''
def getParents():
    '''returns TypePatternList\n\n
    getParents()\n
    '''
def getChild():
    '''returns TypePattern\n\n
    getChild()\n
    '''
def isExtends():
    '''returns boolean\n\n
    isExtends()\n
    '''
def isAdviceLike():
    '''returns boolean\n\n
    isAdviceLike()\n
    '''
def findMatchingNewParents():
    '''returns List<ResolvedType>\n\n
    findMatchingNewParents(ResolvedType onType, final boolean reportErrors)\n
    '''
def getNameSuffix():
    '''returns String\n\n
    getNameSuffix()\n
    '''
def isMixin():
    '''returns boolean\n\n
    isMixin()\n
    '''
