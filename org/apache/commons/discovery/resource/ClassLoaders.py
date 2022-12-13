def ClassLoaders():
    '''public ClassLoaders()
    '''
def size():
    '''public int size()
    '''
def get():
    '''public ClassLoader get(final int idx)
    '''
def put():
    '''public void put(final ClassLoader classLoader)
    public void put(final ClassLoader classLoader, final boolean prune)
    '''
def isAncestor():
    '''public boolean isAncestor(final ClassLoader classLoader)
    '''
def getLibLoaders():
    '''public static ClassLoaders getLibLoaders(final Class spi, final Class factory, final boolean prune)
    '''
def getAppLoaders():
    '''public static ClassLoaders getAppLoaders(final Class spi, final Class factory, final boolean prune)
    '''
