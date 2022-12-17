COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloReportHandlerBase\n\n
    ()\n
    '''
def getOplErrorHandler():
    '''returns IloOplErrorHandler\n\n
    getOplErrorHandler(final IloOplFactory oplF)\n
    '''
def customHandleError():
    '''returns boolean\n\n
    customHandleError(final IloOplMessage message, final IloOplLocation location)\n
    '''
def customHandleFatal():
    '''returns boolean\n\n
    customHandleFatal(final IloOplMessage message, final IloOplLocation location)\n
    '''
def customHandleWarning():
    '''returns boolean\n\n
    customHandleWarning(final IloOplMessage message, final IloOplLocation location)\n
    '''
def customOk():
    '''returns boolean\n\n
    customOk()\n
    '''
def customHandleAssertFail():
    '''returns boolean\n\n
    customHandleAssertFail(final String label, final IloStringArray names, final IloMapIndexArray values, final IloOplLocation location)\n
    '''
def clearIssuesOfOrigin():
    '''returns None\n\n
    clearIssuesOfOrigin(final int origin)\n
    '''
def setOriginContext():
    '''returns None\n\n
    setOriginContext(final int origin)\n
    '''
def getOriginContext():
    '''returns int\n\n
    getOriginContext()\n
    '''
