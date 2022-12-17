def ():
    '''returns IloOplDataElements\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env)\n
    (final IloOplModelDefinition def, final IloOplDataSource source, final boolean enableScriptExpressions)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def getElementIterator():
    '''returns Iterator\n\n
    getElementIterator()\n
    '''
def makeElement():
    '''returns IloOplElement\n\n
    makeElement(final String name, final IloTuple value)\n
    makeElement(final String name, final int value)\n
    makeElement(final String name, final double value)\n
    makeElement(final String name, final String value)\n
    '''
def cpp_MakeElement():
    '''returns IloOplElement\n\n
    cpp_MakeElement(final String name, final ilog.opl_core.cppimpl.IloTuple value)\n
    '''
def addElement():
    '''returns None\n\n
    addElement(final IloOplElement element)\n
    '''
def addElementAs():
    '''returns None\n\n
    addElementAs(final String name, final IloOplElement element)\n
    '''
def setElement():
    '''returns None\n\n
    setElement(final IloOplElement element)\n
    '''
def getElement():
    '''returns IloOplElement\n\n
    getElement(final String name)\n
    '''
def makeScriptExpression():
    '''returns IloOplScriptExpression\n\n
    makeScriptExpression(final String name, final IloStringArray paramNames, final String code)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
