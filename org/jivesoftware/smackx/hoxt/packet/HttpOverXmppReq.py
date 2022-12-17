ELEMENT = "String  \"req\""
def getMethod():
    '''returns HttpMethod\n\n
    getMethod()\n
    '''
def getResource():
    '''returns String\n\n
    getResource()\n
    '''
def getMaxChunkSize():
    '''returns int\n\n
    getMaxChunkSize()\n
    '''
def isSipub():
    '''returns boolean\n\n
    isSipub()\n
    '''
def isIbb():
    '''returns boolean\n\n
    isIbb()\n
    '''
def isJingle():
    '''returns boolean\n\n
    isJingle()\n
    '''
def setMethod():
    '''returns Builder\n\n
    setMethod(final HttpMethod method)\n
    '''
def setResource():
    '''returns Builder\n\n
    setResource(final String resource)\n
    '''
def setJingle():
    '''returns Builder\n\n
    setJingle(final boolean jingle)\n
    '''
def setIbb():
    '''returns Builder\n\n
    setIbb(final boolean ibb)\n
    '''
def setSipub():
    '''returns Builder\n\n
    setSipub(final boolean sipub)\n
    '''
def setMaxChunkSize():
    '''returns Builder\n\n
    setMaxChunkSize(final int maxChunkSize)\n
    '''
def build():
    '''returns HttpOverXmppReq\n\n
    build()\n
    '''
