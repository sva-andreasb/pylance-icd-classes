def ():
    '''returns RETERuleContext\n\n
    (final ForwardRuleInfGraphI graph, final RETEEngine engine)\n
    '''
def getEnv():
    '''returns BindingEnvironment\n\n
    getEnv()\n
    '''
def getGraph():
    '''returns InfGraph\n\n
    getGraph()\n
    '''
def getEngine():
    '''returns RETEEngine\n\n
    getEngine()\n
    '''
def getRule():
    '''returns Rule\n\n
    getRule()\n
    '''
def setRule():
    '''returns None\n\n
    setRule(final Rule rule)\n
    '''
def setEnv():
    '''returns None\n\n
    setEnv(final BindingEnvironment env)\n
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
def silentAdd():
    '''returns None\n\n
    silentAdd(final Triple t)\n
    '''
def remove():
    '''returns None\n\n
    remove(final Triple t)\n
    '''
def add():
    '''returns None\n\n
    add(final Triple t)\n
    '''
def shouldFire():
    '''returns boolean\n\n
    shouldFire(final boolean allowUnsafe)\n
    '''
def shouldStillFire():
    '''returns boolean\n\n
    shouldStillFire()\n
    '''
