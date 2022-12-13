LAZY = "int  1"
NOW = "int  2"
LOCAL = "int  4"
GLOBAL = "int  8"
def getDefault():
    '''    public static final Library getDefault()
    '''
def getCachedInstance():
    '''    public static final Library getCachedInstance(final String name, final int flags)
    '''
def openLibrary():
    '''    public static final Library openLibrary(final String name, int flags)
    '''
def getSymbolAddress():
    '''    public final long getSymbolAddress(final String name)
    '''
def getLastError():
    '''    public static final String getLastError()
    '''
