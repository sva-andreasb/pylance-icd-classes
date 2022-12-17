def ():
    '''returns BBRuleContext\n\n
    (final BackwardRuleInfGraphI graph)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final Node s, final Node p, final Node o)\n
    contains(final Triple t)\n
    '''
def find():
    '''returns ClosableIterator<Triple>\n\n
    find(final Node s, final Node p, final Node o)\n
    '''
def getEnv():
    '''returns BindingEnvironment\n\n
    getEnv()\n
    '''
def setEnv():
    '''returns None\n\n
    setEnv(final BindingEnvironment env)\n
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
def silentAdd():
    '''returns None\n\n
    silentAdd(final Triple t)\n
    '''
def add():
    '''returns None\n\n
    add(final Triple t)\n
    '''
def remove():
    '''returns None\n\n
    remove(final Triple t)\n
    '''
def getTemp():
    '''returns Node\n\n
    getTemp(final Node instance, final Node prop, final Node pclass)\n
    '''
