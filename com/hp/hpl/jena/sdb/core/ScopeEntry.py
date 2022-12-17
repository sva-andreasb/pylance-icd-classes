def ():
    '''returns ScopeEntry\n\n
    (final Var var, final SqlColumn column)\n
    '''
def reset():
    '''returns None\n\n
    reset(final Var var, final SqlColumn column, final ScopeStatus status)\n
    '''
def duplicate():
    '''returns ScopeEntry\n\n
    duplicate()\n
    '''
def getColumn():
    '''returns SqlColumn\n\n
    getColumn()\n
    '''
def getStatus():
    '''returns ScopeStatus\n\n
    getStatus()\n
    '''
def setStatus():
    '''returns None\n\n
    setStatus(final ScopeStatus newStatus)\n
    '''
def isOptional():
    '''returns boolean\n\n
    isOptional()\n
    '''
def isFixed():
    '''returns boolean\n\n
    isFixed()\n
    '''
def hasStatus():
    '''returns boolean\n\n
    hasStatus(final ScopeStatus testStatus2)\n
    '''
def getVar():
    '''returns Var\n\n
    getVar()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final ScopeEntry item)\n
    '''
def convert():
    '''returns Var\n\n
    convert(final ScopeEntry item)\n
    '''
def apply():
    '''returns None\n\n
    apply(final ScopeEntry item)\n
    '''
