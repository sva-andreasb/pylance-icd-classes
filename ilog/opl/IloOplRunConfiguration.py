def ():
    '''returns IloOplRunConfiguration\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final String modPath)\n
    (final IloEnv env, final String modPath, final String datPath)\n
    (final IloEnv env, final String modPath, final IloStringArray datPaths)\n
    (final IloOplModelDefinition def)\n
    (final IloOplModelDefinition def, final IloOplDataElements dataElements)\n
    '''
def setOwn():
    '''returns None\n\n
    setOwn(final boolean cMemoryOwn)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def setCplex():
    '''returns None\n\n
    setCplex(final IloCplex cplex)\n
    '''
def setCP():
    '''returns None\n\n
    setCP(final IloCP cp)\n
    '''
def getCplex():
    '''returns IloCplex\n\n
    getCplex()\n
    '''
def getCP():
    '''returns IloCP\n\n
    getCP()\n
    '''
def getOplModel():
    '''returns IloOplModel\n\n
    getOplModel()\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def addDatPath():
    '''returns None\n\n
    addDatPath(final String datPath)\n
    '''
def isCompiledModel():
    '''returns boolean\n\n
    isCompiledModel()\n
    '''
def setErrorHandler():
    '''returns None\n\n
    setErrorHandler(final IloOplErrorHandler handler)\n
    '''
def setSettings():
    '''returns None\n\n
    setSettings(final IloOplSettings settings)\n
    '''
def setOwnCplex():
    '''returns None\n\n
    setOwnCplex(final boolean own)\n
    '''
def getErrorHandler():
    '''returns IloOplErrorHandler\n\n
    getErrorHandler()\n
    '''
def getSettings():
    '''returns IloOplSettings\n\n
    getSettings()\n
    '''
def setOwnCP():
    '''returns None\n\n
    setOwnCP(final boolean own)\n
    '''
