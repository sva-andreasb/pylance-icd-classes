def ():
    '''returns DefaultFullHttpRequest\n\n
    (final HttpVersion httpVersion, final HttpMethod method, final String uri)\n
    (final HttpVersion httpVersion, final HttpMethod method, final String uri, final ByteBuf content)\n
    (final HttpVersion httpVersion, final HttpMethod method, final String uri, final boolean validateHeaders)\n
    (final HttpVersion httpVersion, final HttpMethod method, final String uri, final ByteBuf content, final boolean validateHeaders)\n
    (final HttpVersion httpVersion, final HttpMethod method, final String uri, final ByteBuf content, final HttpHeaders headers, final HttpHeaders trailingHeader)\n
    '''
def trailingHeaders():
    '''returns HttpHeaders\n\n
    trailingHeaders()\n
    '''
def content():
    '''returns ByteBuf\n\n
    content()\n
    '''
def refCnt():
    '''returns int\n\n
    refCnt()\n
    '''
def retain():
    '''returns FullHttpRequest\n\n
    retain()\n
    retain(final int increment)\n
    '''
def touch():
    '''returns FullHttpRequest\n\n
    touch()\n
    touch(final Object hint)\n
    '''
def release():
    '''returns boolean\n\n
    release()\n
    release(final int decrement)\n
    '''
def setProtocolVersion():
    '''returns FullHttpRequest\n\n
    setProtocolVersion(final HttpVersion version)\n
    '''
def setMethod():
    '''returns FullHttpRequest\n\n
    setMethod(final HttpMethod method)\n
    '''
def setUri():
    '''returns FullHttpRequest\n\n
    setUri(final String uri)\n
    '''
def copy():
    '''returns FullHttpRequest\n\n
    copy()\n
    '''
def duplicate():
    '''returns FullHttpRequest\n\n
    duplicate()\n
    '''
def retainedDuplicate():
    '''returns FullHttpRequest\n\n
    retainedDuplicate()\n
    '''
def replace():
    '''returns FullHttpRequest\n\n
    replace(final ByteBuf content)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
