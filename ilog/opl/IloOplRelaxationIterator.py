def ():
    '''returns IloOplRelaxationIterator\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloOplModel model)\n
    '''
def setOwn():
    '''returns None\n\n
    setOwn(final boolean cMemoryOwn)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def printRelaxation():
    '''returns int\n\n
    printRelaxation(final OutputStream outs)\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def getLB():
    '''returns double\n\n
    getLB()\n
    '''
def getUB():
    '''returns double\n\n
    getUB()\n
    '''
def getRelaxedLB():
    '''returns double\n\n
    getRelaxedLB()\n
    '''
def getRelaxedUB():
    '''returns double\n\n
    getRelaxedUB()\n
    '''
def getConstraint():
    '''returns IloConstraint\n\n
    getConstraint()\n
    '''
def attach():
    '''returns None\n\n
    attach(final IloConstraintMap cts, final IloNumMap prefs)\n
    attach(final IloConstraint ct, final double pref)\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns None\n\n
    next()\n
    '''
def first():
    '''returns None\n\n
    first()\n
    '''
