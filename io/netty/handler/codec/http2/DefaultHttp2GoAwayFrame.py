def DefaultHttp2GoAwayFrame():
    '''public DefaultHttp2GoAwayFrame(final Http2Error error)
    public DefaultHttp2GoAwayFrame(final long errorCode)
    public DefaultHttp2GoAwayFrame(final Http2Error error, final ByteBuf content)
    public DefaultHttp2GoAwayFrame(final long errorCode, final ByteBuf content)
    '''
def name():
    '''public String name()
    '''
def errorCode():
    '''public long errorCode()
    '''
def extraStreamIds():
    '''public int extraStreamIds()
    '''
def setExtraStreamIds():
    '''public Http2GoAwayFrame setExtraStreamIds(final int extraStreamIds)
    '''
def lastStreamId():
    '''public int lastStreamId()
    '''
def copy():
    '''public Http2GoAwayFrame copy()
    '''
def duplicate():
    '''public Http2GoAwayFrame duplicate()
    '''
def retainedDuplicate():
    '''public Http2GoAwayFrame retainedDuplicate()
    '''
def replace():
    '''public Http2GoAwayFrame replace(final ByteBuf content)
    '''
def retain():
    '''public Http2GoAwayFrame retain()
    public Http2GoAwayFrame retain(final int increment)
    '''
def touch():
    '''public Http2GoAwayFrame touch()
    public Http2GoAwayFrame touch(final Object hint)
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
def hashCode():
    '''public int hashCode()
    '''
def toString():
    '''public String toString()
    '''
