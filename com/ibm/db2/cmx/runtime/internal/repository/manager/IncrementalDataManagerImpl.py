def ():
    '''returns IncrementalDataManagerImpl\n\n
    (final Connection c, final String schema)\n
    '''
def add():
    '''returns MDOutputStream\n\n
    add(final String s, final String s2)\n
    '''
def canWrite():
    '''returns MetadataException\n\n
    canWrite(final String str)\n
    '''
def delete():
    '''returns None\n\n
    delete(final int n, final int i)\n
    '''
def getContent():
    '''returns InputStream\n\n
    getContent(final int n)\n
    '''
def list():
    '''returns List<IncrementalSavedDataInfo>\n\n
    list()\n
    list(final String s)\n
    '''
def replace():
    '''returns MDOutputStream\n\n
    replace(final String s, final String s2, final int i)\n
    '''
def updateState():
    '''returns None\n\n
    updateState(final int n, final String s, final int i)\n
    '''
