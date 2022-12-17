def ():
    '''returns FunctorDatatype\n\n
    (final String name, final List<Node> args)\n
    (final String name, final Node[] args)\n
    (final String name, final List<Node> args, final BuiltinRegistry registry)\n
    ()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getArgs():
    '''returns Node[]\n\n
    getArgs()\n
    '''
def getArgLength():
    '''returns int\n\n
    getArgLength()\n
    '''
def isGround():
    '''returns boolean\n\n
    isGround()\n
    isGround(final BindingEnvironment env)\n
    '''
def evalAsBodyClause():
    '''returns boolean\n\n
    evalAsBodyClause(final RuleContext context)\n
    '''
def safeEvalAsBodyClause():
    '''returns boolean\n\n
    safeEvalAsBodyClause(final RuleContext context)\n
    '''
def getBoundArgs():
    '''returns Node[]\n\n
    getBoundArgs(final BindingEnvironment env)\n
    '''
def getImplementor():
    '''returns Builtin\n\n
    getImplementor()\n
    '''
def setImplementor():
    '''returns None\n\n
    setImplementor(final Builtin implementor)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def sameAs():
    '''returns boolean\n\n
    sameAs(final Object o)\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final Triple t)\n
    '''
