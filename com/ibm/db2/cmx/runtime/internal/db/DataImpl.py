def ():
    '''returns DataImpl\n\n
    ()\n
    '''
def queryResults():
    '''returns ResultSet\n\n
    queryResults(final String s, final Object... array)\n
    queryResults(final int n, final int n2, final int n3, final String s, final Object... array)\n
    queryResults(final StatementDescriptor statementDescriptor, final HandlerContainer<?, ?, ?> handlerContainer, final Object... array)\n
    queryResults(final StatementDescriptor statementDescriptor, final Object... array)\n
    '''
def update():
    '''returns int\n\n
    update(final String s, final Object... array)\n
    update(final StatementDescriptor statementDescriptor, final HandlerContainer<?, ?, ?> handlerContainer, final Object... array)\n
    update(final StatementDescriptor statementDescriptor, final Object... array)\n
    '''
def call():
    '''returns StoredProcedureResult\n\n
    call(final String s, final Object... array)\n
    '''
def getData():
    '''returns Data\n\n
    getData()\n
    '''
def getStatementDescriptor():
    '''returns StatementDescriptor\n\n
    getStatementDescriptor(final String s)\n
    '''
def getLogger():
    '''returns Logger\n\n
    getLogger()\n
    '''
def setData():
    '''returns None\n\n
    setData(final Data data)\n
    '''
def updateMany():
    '''returns int[]\n\n
    updateMany(final String... array)\n
    '''
