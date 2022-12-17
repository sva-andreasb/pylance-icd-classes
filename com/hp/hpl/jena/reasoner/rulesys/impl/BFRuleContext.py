def ():
    '''returns BFRuleContext\n\n
    (final ForwardRuleInfGraphI graph)\n
    '''
def getEnv():
    '''returns BindingEnvironment\n\n
    getEnv()\n
    '''
def getEnvStack():
    '''returns BindingStack\n\n
    getEnvStack()\n
    '''
def getGraph():
    '''returns InfGraph\n\n
    getGraph()\n
    '''
def getRule():
    '''returns Rule\n\n
    getRule()\n
    '''
def setRule():
    '''returns None\n\n
    setRule(final Rule rule)\n
    '''
def addTriple():
    '''returns None\n\n
    addTriple(final Triple t)\n
    '''
def add():
    '''returns None\n\n
    add(final Triple t)\n
    '''
def flushPending():
    '''returns None\n\n
    flushPending()\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final Triple t)\n
    contains(final Node s, final Node p, final Node o)\n
    '''
def find():
    '''returns ClosableIterator<Triple>\n\n
    find(final Node s, final Node p, final Node o)\n
    '''
def getNextTriple():
    '''returns Triple\n\n
    getNextTriple()\n
    '''
def resetEnv():
    '''returns None\n\n
    resetEnv(final int newSize)\n
    '''
def silentAdd():
    '''returns None\n\n
    silentAdd(final Triple t)\n
    '''
def remove():
    '''returns None\n\n
    remove(final Triple t)\n
    '''
