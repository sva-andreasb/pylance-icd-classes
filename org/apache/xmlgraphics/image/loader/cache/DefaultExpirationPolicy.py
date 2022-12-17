EXPIRATION_IMMEDIATE = "int  0"
EXPIRATION_NEVER = "int  -1"
def ():
    '''returns DefaultExpirationPolicy\n\n
    ()\n
    (final int expirationAfter)\n
    '''
def isExpired():
    '''returns boolean\n\n
    isExpired(final TimeStampProvider provider, final long timestamp)\n
    '''
