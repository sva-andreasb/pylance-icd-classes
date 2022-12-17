def ():
    '''returns IloOplScriptDebuggerBaseI\n\n
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
def getOut():
    '''returns ostream\n\n
    getOut()\n
    '''
def setOut():
    '''returns None\n\n
    setOut(final ostream outs)\n
    '''
def handleInterruption():
    '''returns None\n\n
    handleInterruption()\n
    '''
def handleScriptResult():
    '''returns None\n\n
    handleScriptResult(final String value)\n
    '''
def getCurrentBreakpointId():
    '''returns int\n\n
    getCurrentBreakpointId()\n
    '''
def registerPause():
    '''returns None\n\n
    registerPause()\n
    '''
def unregisterPause():
    '''returns None\n\n
    unregisterPause()\n
    '''
def registerBreakpoint():
    '''returns None\n\n
    registerBreakpoint(final int id, final IloOplLocation loc)\n
    '''
def unregisterBreakpoint():
    '''returns None\n\n
    unregisterBreakpoint(final int id, final IloOplLocation loc)\n
    '''
def registerStepOver():
    '''returns None\n\n
    registerStepOver()\n
    '''
def registerStepIn():
    '''returns None\n\n
    registerStepIn()\n
    '''
def registerStepOut():
    '''returns None\n\n
    registerStepOut()\n
    '''
def registerStepToCursor():
    '''returns None\n\n
    registerStepToCursor(final IloOplLocation loc)\n
    '''
def registerScript():
    '''returns None\n\n
    registerScript(final String code)\n
    '''
def keepAlive():
    '''returns None\n\n
    keepAlive()\n
    '''
def evalScript():
    '''returns String\n\n
    evalScript(final String code)\n
    '''
