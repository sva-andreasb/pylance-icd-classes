def ():
    '''returns BindingStack\n\n
    ()\n
    '''
def push():
    '''returns None\n\n
    push()\n
    '''
def unwind():
    '''returns None\n\n
    unwind()\n
    '''
def commit():
    '''returns None\n\n
    commit()\n
    '''
def reset():
    '''returns None\n\n
    reset(final int newSize)\n
    '''
def getEnvironment():
    '''returns Node[]\n\n
    getEnvironment()\n
    '''
def getBinding():
    '''returns Node\n\n
    getBinding(final Node node)\n
    '''
def getGroundVersion():
    '''returns Node\n\n
    getGroundVersion(final Node node)\n
    '''
def bind():
    '''returns boolean\n\n
    bind(final int i, final Node value)\n
    bind(final Node var, final Node value)\n
    '''
def bindNoCheck():
    '''returns None\n\n
    bindNoCheck(final Node_RuleVariable var, final Node value)\n
    '''
def instantiate():
    '''returns Triple\n\n
    instantiate(final TriplePattern pattern)\n
    '''
