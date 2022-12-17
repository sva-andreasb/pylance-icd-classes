def ():
    '''returns IloOplErrorHandlerWrapper\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def ok():
    '''returns boolean\n\n
    ok()\n
    '''
def handleFatal():
    '''returns boolean\n\n
    handleFatal(final IloOplMessage message, final IloOplLocation location)\n
    '''
def handleError():
    '''returns boolean\n\n
    handleError(final IloOplMessage message, final IloOplLocation location)\n
    '''
def handleWarning():
    '''returns boolean\n\n
    handleWarning(final IloOplMessage message, final IloOplLocation location)\n
    '''
def handleAssertFail():
    '''returns boolean\n\n
    handleAssertFail(final String label, final IloStringArray names, final IloMapIndexArray values, final IloOplLocation location)\n
    '''
def superHandleAssertFail():
    '''returns boolean\n\n
    superHandleAssertFail(final String label, final IloStringArray names, final IloMapIndexArray values, final IloOplLocation location)\n
    '''
def superOk():
    '''returns boolean\n\n
    superOk()\n
    '''
