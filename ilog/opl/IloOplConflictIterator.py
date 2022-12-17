def ():
    '''returns IloOplConflictIterator\n\n
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
def printConflict():
    '''returns None\n\n
    printConflict(final OutputStream outs)\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def excludeConflict():
    '''returns None\n\n
    excludeConflict()\n
    '''
def attach():
    '''returns None\n\n
    attach(final IloConstraintMap cts, final IloNumMap prefs)\n
    attach(final IloConstraint ct, final double pref)\n
    '''
def clearAttachements():
    '''returns None\n\n
    clearAttachements()\n
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
def getExtractable():
    '''returns IloExtractable\n\n
    getExtractable()\n
    '''
def getStatus():
    '''returns int\n\n
    getStatus()\n
    '''
