def ():
    '''returns Builder\n\n
    (final short version)\n
    (final ApiKeys apiKey)\n
    (final ApiKeys apiKey, final short allowedVersion)\n
    (final ApiKeys apiKey, final short oldestAllowedVersion, final short latestAllowedVersion)\n
    '''
def version():
    '''returns short\n\n
    version()\n
    '''
def toSend():
    '''returns Send\n\n
    toSend(final String destination, final RequestHeader header)\n
    '''
def serialize():
    '''returns ByteBuffer\n\n
    serialize(final RequestHeader header)\n
    '''
def toString():
    '''returns String\n\n
    toString(final boolean verbose)\n
    '''
def getErrorResponse():
    '''returns AbstractResponse\n\n
    getErrorResponse(final Throwable e)\n
    '''
def apiKey():
    '''returns ApiKeys\n\n
    apiKey()\n
    '''
def oldestAllowedVersion():
    '''returns short\n\n
    oldestAllowedVersion()\n
    '''
def latestAllowedVersion():
    '''returns short\n\n
    latestAllowedVersion()\n
    '''
def build():
    '''returns T\n\n
    build()\n
    '''
