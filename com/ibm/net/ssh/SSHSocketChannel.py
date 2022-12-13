def open():
'''public static SocketChannel open()
'''
pass
def connect():
'''public boolean connect(final SocketAddress remote)
public boolean connect(final SocketAddress remote, final int timeout)
'''
pass
def finishConnect():
'''public boolean finishConnect()
'''
pass
def isConnected():
'''public boolean isConnected()
'''
pass
def isConnectionPending():
'''public boolean isConnectionPending()
'''
pass
def socket():
'''public Socket socket()
'''
pass
def read():
'''public long read(final ByteBuffer[] dsts, final int offset, final int length)
public int read(final ByteBuffer dst)
'''
pass
def write():
'''public long write(final ByteBuffer[] srcs, final int offset, final int length)
public int write(final ByteBuffer src)
'''
pass
def implCloseSelectableChannel():
'''public void implCloseSelectableChannel()
'''
pass
def implConfigureBlocking():
'''public void implConfigureBlocking(final boolean block)
'''
pass
