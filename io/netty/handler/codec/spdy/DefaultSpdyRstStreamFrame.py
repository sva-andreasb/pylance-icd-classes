def ():
    '''returns DefaultSpdyRstStreamFrame\n\n
    (final int streamId, final int statusCode)\n
    (final int streamId, final SpdyStreamStatus status)\n
    '''
def setStreamId():
    '''returns SpdyRstStreamFrame\n\n
    setStreamId(final int streamId)\n
    '''
def setLast():
    '''returns SpdyRstStreamFrame\n\n
    setLast(final boolean last)\n
    '''
def status():
    '''returns SpdyStreamStatus\n\n
    status()\n
    '''
def setStatus():
    '''returns SpdyRstStreamFrame\n\n
    setStatus(final SpdyStreamStatus status)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
