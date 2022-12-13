def CloseWebSocketFrame():
'''public CloseWebSocketFrame()
public CloseWebSocketFrame(final WebSocketCloseStatus status)
public CloseWebSocketFrame(final WebSocketCloseStatus status, final String reasonText)
public CloseWebSocketFrame(final int statusCode, final String reasonText)
public CloseWebSocketFrame(final boolean finalFragment, final int rsv)
public CloseWebSocketFrame(final boolean finalFragment, final int rsv, final int statusCode, final String reasonText)
public CloseWebSocketFrame(final boolean finalFragment, final int rsv, final ByteBuf binaryData)
'''
pass
def statusCode():
'''public int statusCode()
'''
pass
def reasonText():
'''public String reasonText()
'''
pass
def copy():
'''public CloseWebSocketFrame copy()
'''
pass
def duplicate():
'''public CloseWebSocketFrame duplicate()
'''
pass
def retainedDuplicate():
'''public CloseWebSocketFrame retainedDuplicate()
'''
pass
def replace():
'''public CloseWebSocketFrame replace(final ByteBuf content)
'''
pass
def retain():
'''public CloseWebSocketFrame retain()
public CloseWebSocketFrame retain(final int increment)
'''
pass
def touch():
'''public CloseWebSocketFrame touch()
public CloseWebSocketFrame touch(final Object hint)
'''
pass
