def ():
    '''returns IloCustomOplScriptDebugger\n\n
    (final IloOplFactory oplEnv, final IloOplModel opl)\n
    '''
def registerBreakpoint():
    '''returns None\n\n
    registerBreakpoint(final int id, final IloOplLocation loc)\n
    '''
def unregisterBreakpoint():
    '''returns None\n\n
    unregisterBreakpoint(final int id, final IloOplLocation loc)\n
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
def registerScript():
    '''returns None\n\n
    registerScript(final String code)\n
    '''
def keepAlive():
    '''returns None\n\n
    keepAlive()\n
    '''
def registerStepIn():
    '''returns None\n\n
    registerStepIn()\n
    '''
def registerStepOut():
    '''returns None\n\n
    registerStepOut()\n
    '''
def registerStepOver():
    '''returns None\n\n
    registerStepOver()\n
    '''
def registerStepToCursor():
    '''returns None\n\n
    registerStepToCursor(final IloOplLocation loc)\n
    '''
def evalScript():
    '''returns String\n\n
    evalScript(final String code)\n
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
