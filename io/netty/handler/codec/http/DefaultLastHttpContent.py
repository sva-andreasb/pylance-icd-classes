def DefaultLastHttpContent():
    '''public DefaultLastHttpContent()
    public DefaultLastHttpContent(final ByteBuf content)
    public DefaultLastHttpContent(final ByteBuf content, final boolean validateHeaders)
    '''
def copy():
    '''public LastHttpContent copy()
    '''
def duplicate():
    '''public LastHttpContent duplicate()
    '''
def retainedDuplicate():
    '''public LastHttpContent retainedDuplicate()
    '''
def replace():
    '''public LastHttpContent replace(final ByteBuf content)
    '''
def retain():
    '''public LastHttpContent retain(final int increment)
    public LastHttpContent retain()
    '''
def touch():
    '''public LastHttpContent touch()
    public LastHttpContent touch(final Object hint)
    '''
def trailingHeaders():
    '''public HttpHeaders trailingHeaders()
    '''
def toString():
    '''public String toString()
    '''
def validateName():
    '''public void validateName(final CharSequence name)
    '''
