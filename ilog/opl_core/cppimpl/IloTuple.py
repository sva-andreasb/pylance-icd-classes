def ():
    '''returns IloTuple\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    ()\n
    '''
def setOwn():
    '''returns None\n\n
    setOwn(final boolean cMemoryOwn)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def getIntSetValue():
    '''returns IloIntSet\n\n
    getIntSetValue(final int index)\n
    getIntSetValue(final String col)\n
    '''
def getNumSetValue():
    '''returns IloNumSet\n\n
    getNumSetValue(final int index)\n
    getNumSetValue(final String col)\n
    '''
def getSymbolSetValue():
    '''returns IloSymbolSet\n\n
    getSymbolSetValue(final int index)\n
    getSymbolSetValue(final String col)\n
    '''
def getIntCollectionValue():
    '''returns IloIntCollection\n\n
    getIntCollectionValue(final int index)\n
    getIntCollectionValue(final String col)\n
    '''
def getNumCollectionValue():
    '''returns IloNumCollection\n\n
    getNumCollectionValue(final int index)\n
    getNumCollectionValue(final String col)\n
    '''
def getAnyCollectionValue():
    '''returns IloAnyCollection\n\n
    getAnyCollectionValue(final int index)\n
    getAnyCollectionValue(final String col)\n
    '''
def getNumMapValue():
    '''returns IloNumMap\n\n
    getNumMapValue(final int index)\n
    getNumMapValue(final String col)\n
    '''
def getIntMapValue():
    '''returns IloIntMap\n\n
    getIntMapValue(final int index)\n
    getIntMapValue(final String col)\n
    '''
def getSchema():
    '''returns IloTupleSchema\n\n
    getSchema()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def makeTupleBuffer():
    '''returns IloTupleBuffer\n\n
    makeTupleBuffer()\n
    '''
def getIndex():
    '''returns int\n\n
    getIndex()\n
    '''
def getCollection():
    '''returns IloTupleCollection\n\n
    getCollection()\n
    '''
def setIndex():
    '''returns None\n\n
    setIndex(final int i)\n
    '''
def setCollection():
    '''returns None\n\n
    setCollection(final IloTupleCollection coll)\n
    '''
def getIntValue():
    '''returns int\n\n
    getIntValue(final int index)\n
    getIntValue(final IloIntArray path)\n
    getIntValue(final String col)\n
    '''
def getNumValue():
    '''returns double\n\n
    getNumValue(final int index)\n
    getNumValue(final IloIntArray path)\n
    getNumValue(final String col)\n
    '''
def getAnyValue():
    '''returns SWIGTYPE_p_void\n\n
    getAnyValue(final int index)\n
    getAnyValue(final IloIntArray path)\n
    getAnyValue(final String col)\n
    '''
def getSymbolValue():
    '''returns IloSymbol\n\n
    getSymbolValue(final int index)\n
    getSymbolValue(final IloIntArray path)\n
    getSymbolValue(final String col)\n
    '''
def getStringValue():
    '''returns String\n\n
    getStringValue(final int index)\n
    getStringValue(final IloIntArray path)\n
    getStringValue(final String col)\n
    '''
def makeTupleValue_cpp():
    '''returns IloTuple\n\n
    makeTupleValue_cpp(final int index)\n
    makeTupleValue_cpp(final IloIntArray path)\n
    makeTupleValue_cpp(final String col)\n
    '''
def getMapItem():
    '''returns IloOplObject\n\n
    getMapItem(final IloIntArray path)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
