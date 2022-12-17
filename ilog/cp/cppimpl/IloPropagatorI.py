def ():
    '''returns IloPropagatorI\n\n
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
def addVar():
    '''returns None\n\n
    addVar(final IloNumVar var)\n
    '''
def violate():
    '''returns None\n\n
    violate()\n
    '''
def setMax():
    '''returns None\n\n
    setMax(final IloNumVar var, final double max)\n
    '''
def setMin():
    '''returns None\n\n
    setMin(final IloNumVar var, final double min)\n
    '''
def setRange():
    '''returns None\n\n
    setRange(final IloNumVar var, final double min, final double max)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final IloNumVar var, final double value)\n
    '''
def removeValue():
    '''returns None\n\n
    removeValue(final IloIntVar var, final int value)\n
    '''
def getMin():
    '''returns double\n\n
    getMin(final IloNumVar var)\n
    '''
def getMax():
    '''returns double\n\n
    getMax(final IloNumVar var)\n
    '''
def getValue():
    '''returns double\n\n
    getValue(final IloNumVar var)\n
    '''
def getDomainSize():
    '''returns int\n\n
    getDomainSize(final IloNumVar var)\n
    '''
def isInDomain():
    '''returns boolean\n\n
    isInDomain(final IloNumVar var, final int value)\n
    '''
def isFixed():
    '''returns boolean\n\n
    isFixed(final IloNumVar var)\n
    '''
def execute():
    '''returns None\n\n
    execute()\n
    '''
def makeClone():
    '''returns IloPropagatorI\n\n
    makeClone(final IloEnv env)\n
    '''
def iterator_IntVarIterator():
    '''returns IloCP_IntVarIterator\n\n
    iterator_IntVarIterator(final IloNumVar var)\n
    '''
