DEFAULT_TERMINAL = "String  \"vt100\""
DEFAULT_ROWS = "int  24"
DEFAULT_COLUMNS = "int  80"
DEFAULT_WIDTH = "int  640"
DEFAULT_HEIGHT = "int  480"
DEFAULT_BREAK_LENGTH = "int  500"
def getOutputStream():
    '''    public OutputStream getOutputStream()
    '''
def getInputStream():
    '''    public InputStream getInputStream()
    '''
def getErrorStream():
    '''    public InputStream getErrorStream()
    '''
def close():
    '''    public void close()
    '''
def getTerminalRowSize():
    '''    public int getTerminalRowSize()
    '''
def getTerminalColumnSize():
    '''    public int getTerminalColumnSize()
    '''
def setTerminalSize():
    '''    public void setTerminalSize(final int rows, final int columns)
    '''
def doBreak():
    '''    public void doBreak()
    public void doBreak(final int breakLength)
    '''
