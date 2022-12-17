def ():
    '''returns SystemContextInvokerImpl\n\n
    (final Object[] array, final String typeName)\n
    '''
def extractContext():
    '''returns boolean\n\n
    extractContext(final SystemContext systemContext, final Map invokeContext)\n
    '''
def insertRequestContext():
    '''returns boolean\n\n
    insertRequestContext(final SystemContext requestContext)\n
    '''
def establishContext():
    '''returns boolean\n\n
    establishContext(final Map invokeContext)\n
    '''
def insertResponseContext():
    '''returns boolean\n\n
    insertResponseContext(final SystemContext responseContext)\n
    '''
def peekContext():
    '''returns boolean\n\n
    peekContext(final Map invokeContext)\n
    '''
def removeEstablishedContext():
    '''returns None\n\n
    removeEstablishedContext()\n
    '''
def requestFailed():
    '''returns None\n\n
    requestFailed()\n
    '''
def requestSucceeded():
    '''returns None\n\n
    requestSucceeded()\n
    requestSucceeded(final SystemContext context)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
