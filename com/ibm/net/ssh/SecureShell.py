DEFAULT_TERMINAL = "String  \"vt100\""
DEFAULT_ROWS = "int  24"
DEFAULT_COLUMNS = "int  80"
DEFAULT_WIDTH = "int  640"
DEFAULT_HEIGHT = "int  480"
DEFAULT_BREAK_LENGTH = "int  500"
def getOutputStream():
    '''returns OutputStream\n\n
    getOutputStream()\n
    '''
def getInputStream():
    '''returns InputStream\n\n
    getInputStream()\n
    '''
def getErrorStream():
    '''returns InputStream\n\n
    getErrorStream()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getTerminalRowSize():
    '''returns int\n\n
    getTerminalRowSize()\n
    '''
def getTerminalColumnSize():
    '''returns int\n\n
    getTerminalColumnSize()\n
    '''
def setTerminalSize():
    '''returns None\n\n
    setTerminalSize(final int rows, final int columns)\n
    '''
def doBreak():
    '''returns None\n\n
    doBreak()\n
    doBreak(final int breakLength)\n
    '''
