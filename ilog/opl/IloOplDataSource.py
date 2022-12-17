def ():
    '''returns IloOplDataSource\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloOplDataSourceBaseI impl)\n
    (final IloEnv env, final String filename)\n
    (final IloEnv env, final istream ins, final String name)\n
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
def setDataHandler():
    '''returns None\n\n
    setDataHandler(final IloOplDataHandler handler)\n
    '''
def getDataHandler():
    '''returns IloOplDataHandler\n\n
    getDataHandler()\n
    '''
def setErrorHandler():
    '''returns None\n\n
    setErrorHandler(final IloOplErrorHandler handler)\n
    '''
def read():
    '''returns None\n\n
    read()\n
    '''
def getDataSourceName():
    '''returns String\n\n
    getDataSourceName()\n
    '''
def hasPrepare():
    '''returns boolean\n\n
    hasPrepare()\n
    '''
def getPrepare():
    '''returns IloOplScriptThunk\n\n
    getPrepare()\n
    '''
def setImpl():
    '''returns None\n\n
    setImpl(final IloOplDataSourceBaseI impl)\n
    '''
