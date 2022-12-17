def ():
    '''returns IloTupleSchema\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final String name)\n
    (final IloEnv env)\n
    (final SWIGTYPE_p_IloTupleSchemaI impl)\n
    '''
def setOwn():
    '''returns None\n\n
    setOwn(final boolean cMemoryOwn)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def hasKey():
    '''returns boolean\n\n
    hasKey()\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def getSize():
    '''returns int\n\n
    getSize()\n
    '''
def getColumn():
    '''returns SWIGTYPE_p_IloColumnDefinitionI\n\n
    getColumn(final int i)\n
    getColumn(final IloIntArray path)\n
    '''
def getColumnName():
    '''returns String\n\n
    getColumnName(final int idx)\n
    '''
def addIntColumn():
    '''returns None\n\n
    addIntColumn(final String name)\n
    '''
def addNumColumn():
    '''returns None\n\n
    addNumColumn(final String name)\n
    '''
def addSymbolColumn():
    '''returns None\n\n
    addSymbolColumn(final String name)\n
    '''
def addTupleColumn():
    '''returns None\n\n
    addTupleColumn(final IloTupleSchema ax, final String name)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getTotalColumnNumber():
    '''returns int\n\n
    getTotalColumnNumber()\n
    '''
def getSharedPathFromAbsolutePosition():
    '''returns IloIntArray\n\n
    getSharedPathFromAbsolutePosition(final int position)\n
    '''
def getColumnIndex():
    '''returns int\n\n
    getColumnIndex(final String name)\n
    getColumnIndex(final SWIGTYPE_p_IloSymbolI name)\n
    '''
def getTupleColumn():
    '''returns IloTupleSchema\n\n
    getTupleColumn(final int colIndex)\n
    '''
def isInt():
    '''returns boolean\n\n
    isInt(final int index)\n
    isInt(final IloIntArray path)\n
    '''
def isNum():
    '''returns boolean\n\n
    isNum(final int index)\n
    isNum(final IloIntArray path)\n
    '''
def isSymbol():
    '''returns boolean\n\n
    isSymbol(final int index)\n
    isSymbol(final IloIntArray path)\n
    '''
def isTuple():
    '''returns boolean\n\n
    isTuple(final int index)\n
    isTuple(final IloIntArray path)\n
    '''
def isIntCollection():
    '''returns boolean\n\n
    isIntCollection(final int index)\n
    isIntCollection(final IloIntArray path)\n
    '''
def isNumCollection():
    '''returns boolean\n\n
    isNumCollection(final int index)\n
    isNumCollection(final IloIntArray path)\n
    '''
def isAnyCollection():
    '''returns boolean\n\n
    isAnyCollection(final int index)\n
    isAnyCollection(final IloIntArray path)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getOrMakeSharedKeySchema():
    '''returns IloTupleSchema\n\n
    getOrMakeSharedKeySchema()\n
    '''
def getTotalIndexFromKey():
    '''returns int\n\n
    getTotalIndexFromKey(final int key)\n
    '''
def getOrMakeTotalKeyIndexes():
    '''returns IloIntArray\n\n
    getOrMakeTotalKeyIndexes()\n
    '''
