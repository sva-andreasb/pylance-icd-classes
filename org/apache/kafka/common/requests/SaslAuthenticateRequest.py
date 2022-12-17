def ():
    '''returns Builder\n\n
    (final ByteBuffer saslAuthBytes)\n
    (final ByteBuffer saslAuthBytes, final short version)\n
    (final Struct struct, final short version)\n
    (final ByteBuffer saslAuthBytes)\n
    '''
def saslAuthBytes():
    '''returns ByteBuffer\n\n
    saslAuthBytes()\n
    '''
def getErrorResponse():
    '''returns AbstractResponse\n\n
    getErrorResponse(final int throttleTimeMs, final Throwable e)\n
    '''
def build():
    '''returns SaslAuthenticateRequest\n\n
    build(final short version)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
