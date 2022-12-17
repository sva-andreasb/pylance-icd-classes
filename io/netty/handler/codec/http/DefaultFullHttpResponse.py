def ():
    '''returns DefaultFullHttpResponse\n\n
    (final HttpVersion version, final HttpResponseStatus status)\n
    (final HttpVersion version, final HttpResponseStatus status, final ByteBuf content)\n
    (final HttpVersion version, final HttpResponseStatus status, final boolean validateHeaders)\n
    (final HttpVersion version, final HttpResponseStatus status, final boolean validateHeaders, final boolean singleFieldHeaders)\n
    (final HttpVersion version, final HttpResponseStatus status, final ByteBuf content, final boolean validateHeaders)\n
    (final HttpVersion version, final HttpResponseStatus status, final ByteBuf content, final boolean validateHeaders, final boolean singleFieldHeaders)\n
    (final HttpVersion version, final HttpResponseStatus status, final ByteBuf content, final HttpHeaders headers, final HttpHeaders trailingHeaders)\n
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
    '''returns FullHttpResponse\n\n
    retain()\n
    retain(final int increment)\n
    '''
def touch():
    '''returns FullHttpResponse\n\n
    touch()\n
    touch(final Object hint)\n
    '''
def release():
    '''returns boolean\n\n
    release()\n
    release(final int decrement)\n
    '''
def setProtocolVersion():
    '''returns FullHttpResponse\n\n
    setProtocolVersion(final HttpVersion version)\n
    '''
def setStatus():
    '''returns FullHttpResponse\n\n
    setStatus(final HttpResponseStatus status)\n
    '''
def copy():
    '''returns FullHttpResponse\n\n
    copy()\n
    '''
def duplicate():
    '''returns FullHttpResponse\n\n
    duplicate()\n
    '''
def retainedDuplicate():
    '''returns FullHttpResponse\n\n
    retainedDuplicate()\n
    '''
def replace():
    '''returns FullHttpResponse\n\n
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
