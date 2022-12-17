def ():
    '''returns IloOplExecutionController\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloOplExecutionControllerBaseI impl)\n
    '''
def setOwn():
    '''returns None\n\n
    setOwn(final boolean cMemoryOwn)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def getOut():
    '''returns ostream\n\n
    getOut()\n
    '''
def enableAbort():
    '''returns None\n\n
    enableAbort()\n
    '''
def disableAbort():
    '''returns None\n\n
    disableAbort()\n
    '''
def abort():
    '''returns None\n\n
    abort()\n
    '''
def notifyNew():
    '''returns None\n\n
    notifyNew(final IloOplModel opl)\n
    notifyNew(final IloCplex algorithm)\n
    notifyNew(final IloCP algorithm)\n
    '''
def notifyEnd():
    '''returns None\n\n
    notifyEnd(final IloOplModel opl)\n
    notifyEnd(final IloCplex algorithm)\n
    notifyEnd(final IloCP algorithm)\n
    '''
def notifyCall():
    '''returns None\n\n
    notifyCall(final IloOplModel opl)\n
    notifyCall(final IloCplex algorithm)\n
    notifyCall(final IloCP algorithm)\n
    '''
def notifyReturn():
    '''returns None\n\n
    notifyReturn(final IloOplModel opl, final boolean status)\n
    notifyReturn(final IloCplex algorithm, final boolean status)\n
    notifyReturn(final IloCP algorithm, final boolean status)\n
    '''
def setImpl():
    '''returns None\n\n
    setImpl(final IloOplExecutionControllerBaseI impl)\n
    '''
