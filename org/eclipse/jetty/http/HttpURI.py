def ():
    '''returns HttpURI\n\n
    ()\n
    (final boolean parsePartialAuth)\n
    (final String raw)\n
    (final byte[] raw, final int offset, final int length)\n
    (final URI uri)\n
    '''
def parse():
    '''returns None\n\n
    parse(final String raw)\n
    parse(final byte[] raw, final int offset, final int length)\n
    '''
def parseConnect():
    '''returns None\n\n
    parseConnect(final byte[] raw, final int offset, final int length)\n
    '''
def getScheme():
    '''returns String\n\n
    getScheme()\n
    '''
def getAuthority():
    '''returns String\n\n
    getAuthority()\n
    '''
def getHost():
    '''returns String\n\n
    getHost()\n
    '''
def getPort():
    '''returns int\n\n
    getPort()\n
    '''
def getPath():
    '''returns String\n\n
    getPath()\n
    '''
def getDecodedPath():
    '''returns String\n\n
    getDecodedPath()\n
    '''
def getPathAndParam():
    '''returns String\n\n
    getPathAndParam()\n
    '''
def getCompletePath():
    '''returns String\n\n
    getCompletePath()\n
    '''
def getParam():
    '''returns String\n\n
    getParam()\n
    '''
def getQuery():
    '''returns String\n\n
    getQuery()\n
    getQuery(final String encoding)\n
    '''
def hasQuery():
    '''returns boolean\n\n
    hasQuery()\n
    '''
def getFragment():
    '''returns String\n\n
    getFragment()\n
    '''
def decodeQueryTo():
    '''returns None\n\n
    decodeQueryTo(final MultiMap parameters)\n
    decodeQueryTo(final MultiMap parameters, final String encoding)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def writeTo():
    '''returns None\n\n
    writeTo(final Utf8StringBuilder buf)\n
    '''
