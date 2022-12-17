def ():
    '''returns Builder\n\n
    (final Struct struct, final short versionId)\n
    (final ByteBuffer hmac, final long renewTimePeriod)\n
    '''
def getErrorResponse():
    '''returns AbstractResponse\n\n
    getErrorResponse(final int throttleTimeMs, final Throwable e)\n
    '''
def hmac():
    '''returns ByteBuffer\n\n
    hmac()\n
    '''
def renewTimePeriod():
    '''returns long\n\n
    renewTimePeriod()\n
    '''
def build():
    '''returns RenewDelegationTokenRequest\n\n
    build(final short version)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
