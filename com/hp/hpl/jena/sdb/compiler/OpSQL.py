def ():
    '''returns OpSQL\n\n
    (final SqlNode sqlNode, final Op original, final SDBRequest request)\n
    '''
def eval():
    '''returns QueryIterator\n\n
    eval(final QueryIterator input, final ExecutionContext execCxt)\n
    '''
def exec():
    '''returns QueryIterator\n\n
    exec(final ExecutionContext execCxt)\n
    exec(Binding parent, final ExecutionContext execCxt)\n
    '''
def getOriginal():
    '''returns Op\n\n
    getOriginal()\n
    '''
def effectiveOp():
    '''returns Op\n\n
    effectiveOp()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equalTo():
    '''returns boolean\n\n
    equalTo(final Op other, final NodeIsomorphismMap labelMap)\n
    '''
def getRequest():
    '''returns SDBRequest\n\n
    getRequest()\n
    '''
def output():
    '''returns None\n\n
    output(final IndentedWriter out)\n
    '''
def toSQL():
    '''returns String\n\n
    toSQL()\n
    '''
def getSqlNode():
    '''returns SqlNode\n\n
    getSqlNode()\n
    '''
def resetSqlNode():
    '''returns None\n\n
    resetSqlNode(final SqlNode sqlNode2)\n
    '''
def getBridge():
    '''returns SQLBridge\n\n
    getBridge()\n
    '''
def setBridge():
    '''returns None\n\n
    setBridge(final SQLBridge bridge)\n
    '''
def outputArgs():
    '''returns None\n\n
    outputArgs(final IndentedWriter out, final SerializationContext sCxt)\n
    '''
