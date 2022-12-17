def ():
    '''returns CloseWebSocketFrame\n\n
    ()\n
    (final WebSocketCloseStatus status)\n
    (final WebSocketCloseStatus status, final String reasonText)\n
    (final int statusCode, final String reasonText)\n
    (final boolean finalFragment, final int rsv)\n
    (final boolean finalFragment, final int rsv, final int statusCode, final String reasonText)\n
    (final boolean finalFragment, final int rsv, final ByteBuf binaryData)\n
    '''
def statusCode():
    '''returns int\n\n
    statusCode()\n
    '''
def reasonText():
    '''returns String\n\n
    reasonText()\n
    '''
def copy():
    '''returns CloseWebSocketFrame\n\n
    copy()\n
    '''
def duplicate():
    '''returns CloseWebSocketFrame\n\n
    duplicate()\n
    '''
def retainedDuplicate():
    '''returns CloseWebSocketFrame\n\n
    retainedDuplicate()\n
    '''
def replace():
    '''returns CloseWebSocketFrame\n\n
    replace(final ByteBuf content)\n
    '''
def retain():
    '''returns CloseWebSocketFrame\n\n
    retain()\n
    retain(final int increment)\n
    '''
def touch():
    '''returns CloseWebSocketFrame\n\n
    touch()\n
    touch(final Object hint)\n
    '''
