def ():
    '''returns Status\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final String swigName, final int swigValue)\n
    '''
def setOwn():
    '''returns None\n\n
    setOwn(final boolean cMemoryOwn)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def getEnv():
    '''returns IloEnv\n\n
    getEnv()\n
    '''
def getModel():
    '''returns IloModel\n\n
    getModel()\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def out_stream():
    '''returns ostream\n\n
    out_stream()\n
    '''
def setOut():
    '''returns None\n\n
    setOut(final ostream arg0)\n
    '''
def warning():
    '''returns ostream\n\n
    warning()\n
    '''
def setWarning():
    '''returns None\n\n
    setWarning(final ostream arg0)\n
    '''
def error():
    '''returns ostream\n\n
    error()\n
    '''
def setError():
    '''returns None\n\n
    setError(final ostream arg0)\n
    '''
def extract():
    '''returns None\n\n
    extract(final IloModel arg0)\n
    '''
def solve():
    '''returns boolean\n\n
    solve()\n
    '''
def getStatus():
    '''returns Status\n\n
    getStatus()\n
    '''
def getObjValue():
    '''returns double\n\n
    getObjValue()\n
    '''
def getValue():
    '''returns double\n\n
    getValue(final IloNumVar var)\n
    getValue(final IloIntVar var)\n
    getValue(final IloObjective obj)\n
    getValue(final IloNumExprArg expr)\n
    '''
def getIntValue():
    '''returns int\n\n
    getIntValue(final IloIntVar var)\n
    '''
def getValues():
    '''returns None\n\n
    getValues(final IloNumVarArray var, final IloNumArray vals)\n
    getValues(final IloIntVarArray vars, final IloNumArray vals)\n
    '''
def isExtracted():
    '''returns boolean\n\n
    isExtracted(final IloExtractable extr)\n
    '''
def mySwigValue():
    '''returns int\n\n
    mySwigValue()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
