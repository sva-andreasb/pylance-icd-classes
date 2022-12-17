def ():
    '''returns IloOplOutlineListenerBaseI\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    '''
def setOwn():
    '''returns None\n\n
    setOwn(final boolean cMemoryOwn)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def notifyElementDefinition():
    '''returns None\n\n
    notifyElementDefinition(final IloOplElementDefinition def)\n
    '''
def notifyClosePreProcessing():
    '''returns None\n\n
    notifyClosePreProcessing()\n
    '''
def notifyPushConstraint():
    '''returns None\n\n
    notifyPushConstraint(final String name, final IloOplLocation location)\n
    '''
def notifyPopConstraint():
    '''returns None\n\n
    notifyPopConstraint()\n
    '''
def notifyExecute():
    '''returns None\n\n
    notifyExecute(final String name, final IloOplLocation location)\n
    '''
def notifyAssert():
    '''returns None\n\n
    notifyAssert(final String name, final IloOplLocation location)\n
    '''
def notifyObjective():
    '''returns None\n\n
    notifyObjective(final boolean simple, final boolean minimize, final IloOplLocation location)\n
    '''
