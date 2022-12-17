def ():
    '''returns TextWebSocketFrame\n\n
    ()\n
    (final String text)\n
    (final ByteBuf binaryData)\n
    (final boolean finalFragment, final int rsv, final String text)\n
    (final boolean finalFragment, final int rsv, final ByteBuf binaryData)\n
    '''
def text():
    '''returns String\n\n
    text()\n
    '''
def copy():
    '''returns TextWebSocketFrame\n\n
    copy()\n
    '''
def duplicate():
    '''returns TextWebSocketFrame\n\n
    duplicate()\n
    '''
def retainedDuplicate():
    '''returns TextWebSocketFrame\n\n
    retainedDuplicate()\n
    '''
def replace():
    '''returns TextWebSocketFrame\n\n
    replace(final ByteBuf content)\n
    '''
def retain():
    '''returns TextWebSocketFrame\n\n
    retain()\n
    retain(final int increment)\n
    '''
def touch():
    '''returns TextWebSocketFrame\n\n
    touch()\n
    touch(final Object hint)\n
    '''
