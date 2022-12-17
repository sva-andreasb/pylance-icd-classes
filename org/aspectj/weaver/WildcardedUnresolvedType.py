UNBOUND = "int  0"
EXTENDS = "int  1"
SUPER = "int  2"
def ():
    '''returns WildcardedUnresolvedType\n\n
    (final String signature, final UnresolvedType upperBound, final UnresolvedType lowerBound)\n
    '''
def getUpperBound():
    '''returns UnresolvedType\n\n
    getUpperBound()\n
    '''
def getLowerBound():
    '''returns UnresolvedType\n\n
    getLowerBound()\n
    '''
def isExtends():
    '''returns boolean\n\n
    isExtends()\n
    '''
def isSuper():
    '''returns boolean\n\n
    isSuper()\n
    '''
def isUnbound():
    '''returns boolean\n\n
    isUnbound()\n
    '''
