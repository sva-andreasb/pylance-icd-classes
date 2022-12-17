COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloDomServiceEntryImpl\n\n
    (final String scope, final Object source)\n
    '''
def getScope():
    '''returns String\n\n
    getScope()\n
    '''
def getSource():
    '''returns Object\n\n
    getSource()\n
    '''
def getActiveClients():
    '''returns Set<IloDomServiceClient>\n\n
    getActiveClients()\n
    '''
def getPassiveClients():
    '''returns Set<IloDomServiceClient>\n\n
    getPassiveClients()\n
    '''
def getLastUpdateTimestamp():
    '''returns Date\n\n
    getLastUpdateTimestamp()\n
    '''
def open():
    '''returns boolean\n\n
    open(final IloDomModelManager<?> modelManager)\n
    '''
def activate():
    '''returns boolean\n\n
    activate(final IloDomServiceClient client)\n
    '''
def passivate():
    '''returns boolean\n\n
    passivate(final IloDomServiceClient client)\n
    '''
def dispose():
    '''returns boolean\n\n
    dispose(final IloDomServiceClient client)\n
    '''
def close():
    '''returns boolean\n\n
    close()\n
    '''
def getState():
    '''returns EntryState\n\n
    getState()\n
    '''
