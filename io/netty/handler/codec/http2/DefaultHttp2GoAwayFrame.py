def ():
    '''returns DefaultHttp2GoAwayFrame\n\n
    (final Http2Error error)\n
    (final long errorCode)\n
    (final Http2Error error, final ByteBuf content)\n
    (final long errorCode, final ByteBuf content)\n
    '''
def name():
    '''returns String\n\n
    name()\n
    '''
def errorCode():
    '''returns long\n\n
    errorCode()\n
    '''
def extraStreamIds():
    '''returns int\n\n
    extraStreamIds()\n
    '''
def setExtraStreamIds():
    '''returns Http2GoAwayFrame\n\n
    setExtraStreamIds(final int extraStreamIds)\n
    '''
def lastStreamId():
    '''returns int\n\n
    lastStreamId()\n
    '''
def copy():
    '''returns Http2GoAwayFrame\n\n
    copy()\n
    '''
def duplicate():
    '''returns Http2GoAwayFrame\n\n
    duplicate()\n
    '''
def retainedDuplicate():
    '''returns Http2GoAwayFrame\n\n
    retainedDuplicate()\n
    '''
def replace():
    '''returns Http2GoAwayFrame\n\n
    replace(final ByteBuf content)\n
    '''
def retain():
    '''returns Http2GoAwayFrame\n\n
    retain()\n
    retain(final int increment)\n
    '''
def touch():
    '''returns Http2GoAwayFrame\n\n
    touch()\n
    touch(final Object hint)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
