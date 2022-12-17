def ():
    '''returns IloOplDataSerializer\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final IloOplSettings settings, final ostream outs)\n
    (final IloEnv env, final IloOplSettings settings, final ostream outs, final boolean header)\n
    (final IloEnv env, final IloOplSettings settings, final ostream outs, final String title)\n
    (final IloEnv env, final ostream outs)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def printElement():
    '''returns None\n\n
    printElement(final IloOplElement v)\n
    '''
def printArray():
    '''returns None\n\n
    printArray(final IloNumMap v)\n
    printArray(final IloIntMap v)\n
    printArray(final IloSymbolMap v)\n
    printArray(final IloTupleMap v)\n
    printArray(final IloNumSetMap v)\n
    printArray(final IloIntSetMap v)\n
    printArray(final IloSymbolSetMap v)\n
    printArray(final IloTupleSetMap v)\n
    '''
def printSet():
    '''returns None\n\n
    printSet(final IloNumSet v)\n
    printSet(final IloIntSet v)\n
    printSet(final IloSymbolSet v)\n
    printSet(final IloTupleSet v)\n
    '''
def printTuple():
    '''returns None\n\n
    printTuple(final IloTuple v)\n
    '''
def printTupleKey():
    '''returns None\n\n
    printTupleKey(final IloTuple v)\n
    '''
def printObject():
    '''returns None\n\n
    printObject(final IloOplObject v)\n
    '''
def printTupleToString():
    '''returns String\n\n
    printTupleToString(final IloTuple v)\n
    '''
def printTupleKeyToString():
    '''returns String\n\n
    printTupleKeyToString(final IloTuple v)\n
    '''
def printObjectToString():
    '''returns String\n\n
    printObjectToString(final IloOplObject v)\n
    '''
def printElementToString():
    '''returns String\n\n
    printElementToString(final IloOplElement v)\n
    '''
def keepRefOnOutputStreamAdapter():
    '''returns None\n\n
    keepRefOnOutputStreamAdapter(final JavaToCppOutputStreamAdapter stream)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def setOutputLimit():
    '''returns None\n\n
    setOutputLimit(final int limit)\n
    '''
def setRawStrings():
    '''returns None\n\n
    setRawStrings(final boolean raw)\n
    '''
def cpp_printTupleKeyToString():
    '''returns String\n\n
    cpp_printTupleKeyToString(final ilog.opl_core.cppimpl.IloTuple elem)\n
    '''
def cpp_printTupleToString():
    '''returns String\n\n
    cpp_printTupleToString(final ilog.opl_core.cppimpl.IloTuple elem)\n
    '''
def cpp_printObjectToString():
    '''returns String\n\n
    cpp_printObjectToString(final IloOplObject elem)\n
    '''
def cpp_printElementToString():
    '''returns String\n\n
    cpp_printElementToString(final IloOplElement elem)\n
    '''
