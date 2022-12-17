def ():
    '''returns IloOplExecutionControllerWrapper\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final IloOplExecutionController deleg)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def notifyNew():
    '''returns None\n\n
    notifyNew(final IloOplModel opl)\n
    notifyNew(final IloCplex cplex)\n
    notifyNew(final IloCP cp)\n
    '''
def notifyEnd():
    '''returns None\n\n
    notifyEnd(final IloOplModel opl)\n
    notifyEnd(final IloCplex cplex)\n
    notifyEnd(final IloCP cp)\n
    '''
def notifyCall():
    '''returns None\n\n
    notifyCall(final IloOplModel opl)\n
    notifyCall(final IloCplex cplex)\n
    notifyCall(final IloCP cp)\n
    '''
def notifyReturn():
    '''returns None\n\n
    notifyReturn(final IloOplModel opl, final boolean status)\n
    notifyReturn(final IloCplex cplex, final boolean status)\n
    notifyReturn(final IloCP cp, final boolean status)\n
    '''
