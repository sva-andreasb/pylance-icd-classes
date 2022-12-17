def ():
    '''returns IloOplCustomDataHandlerWrapper\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def handleConnection():
    '''returns None\n\n
    handleConnection(final String connId, final String subId, final String spec)\n
    '''
def handleReadElement():
    '''returns None\n\n
    handleReadElement(final String connId, final String name, final String spec)\n
    '''
def handlePublishElement():
    '''returns None\n\n
    handlePublishElement(final String connId, final String name, final String spec)\n
    '''
def handleInvoke():
    '''returns boolean\n\n
    handleInvoke(final String name, final String funcname)\n
    '''
def closeConnections():
    '''returns None\n\n
    closeConnections()\n
    '''
