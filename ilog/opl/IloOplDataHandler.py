def ():
    '''returns IloOplDataHandler\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final IloOplSettings settings, final ostream outs)\n
    (final IloEnv env, final ostream outs)\n
    '''
def setOwn():
    '''returns None\n\n
    setOwn(final boolean cMemoryOwn)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String name)\n
    '''
def restartElement():
    '''returns None\n\n
    restartElement(final String name)\n
    '''
def endElement():
    '''returns None\n\n
    endElement()\n
    '''
def setElement():
    '''returns None\n\n
    setElement(final IloOplElement element)\n
    '''
def invoke():
    '''returns None\n\n
    invoke(final String name, final String funcName)\n
    '''
def startArray():
    '''returns None\n\n
    startArray()\n
    '''
def endArray():
    '''returns None\n\n
    endArray()\n
    '''
def startIndexedArray():
    '''returns None\n\n
    startIndexedArray()\n
    '''
def endIndexedArray():
    '''returns None\n\n
    endIndexedArray()\n
    '''
def startTuple():
    '''returns None\n\n
    startTuple()\n
    '''
def endTuple():
    '''returns None\n\n
    endTuple()\n
    '''
def startNamedTuple():
    '''returns None\n\n
    startNamedTuple()\n
    '''
def endNamedTuple():
    '''returns None\n\n
    endNamedTuple()\n
    '''
def startSet():
    '''returns None\n\n
    startSet()\n
    '''
def endSet():
    '''returns None\n\n
    endSet()\n
    '''
def setItemIntIndex():
    '''returns None\n\n
    setItemIntIndex(final int value)\n
    '''
def setItemNumIndex():
    '''returns None\n\n
    setItemNumIndex(final double value)\n
    '''
def setItemStringIndex():
    '''returns None\n\n
    setItemStringIndex(final String value)\n
    '''
def startItemTupleIndex():
    '''returns None\n\n
    startItemTupleIndex()\n
    '''
def endItemTupleIndex():
    '''returns None\n\n
    endItemTupleIndex()\n
    '''
def setItemName():
    '''returns None\n\n
    setItemName(final String name)\n
    '''
def addIntItem():
    '''returns None\n\n
    addIntItem(final int value)\n
    '''
def addNumItem():
    '''returns None\n\n
    addNumItem(final double value)\n
    '''
def addStringItem():
    '''returns None\n\n
    addStringItem(final String value)\n
    '''
def getElement():
    '''returns IloOplElement\n\n
    getElement(final String name)\n
    '''
def executePrepare():
    '''returns None\n\n
    executePrepare(final String block)\n
    executePrepare(final IloOplScriptThunk prepare)\n
    '''
