COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloCompositeDecisionVariable\n\n
    (final String name, final Object explanation, final IloPropertiesDef def)\n
    '''
def registerDecisionVariable():
    '''returns None\n\n
    registerDecisionVariable(final IloDecisionVariable v, final boolean force)\n
    '''
def needEngineUpdate():
    '''returns boolean\n\n
    needEngineUpdate(final int propIndex)\n
    '''
def getDecisionVariable():
    '''returns IloDecisionVariable\n\n
    getDecisionVariable(final String name)\n
    getDecisionVariable(final IloCompositeId name)\n
    '''
def internalRemoveVar():
    '''returns None\n\n
    internalRemoveVar(final String name)\n
    '''
def internalPutVar():
    '''returns None\n\n
    internalPutVar(final IloDecisionVariable var)\n
    '''
