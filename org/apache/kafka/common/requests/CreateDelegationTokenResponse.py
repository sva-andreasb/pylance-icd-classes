def ():
    '''returns CreateDelegationTokenResponse\n\n
    (final int throttleTimeMs, final Errors error, final KafkaPrincipal owner, final long issueTimestamp, final long expiryTimestamp, final long maxTimestamp, final String tokenId, final ByteBuffer hmac)\n
    (final int throttleTimeMs, final Errors error, final KafkaPrincipal owner)\n
    (final Struct struct)\n
    '''
def error():
    '''returns Errors\n\n
    error()\n
    '''
def owner():
    '''returns KafkaPrincipal\n\n
    owner()\n
    '''
def issueTimestamp():
    '''returns long\n\n
    issueTimestamp()\n
    '''
def expiryTimestamp():
    '''returns long\n\n
    expiryTimestamp()\n
    '''
def maxTimestamp():
    '''returns long\n\n
    maxTimestamp()\n
    '''
def tokenId():
    '''returns String\n\n
    tokenId()\n
    '''
def hmacBytes():
    '''returns byte[]\n\n
    hmacBytes()\n
    '''
def throttleTimeMs():
    '''returns int\n\n
    throttleTimeMs()\n
    '''
def hasError():
    '''returns boolean\n\n
    hasError()\n
    '''
