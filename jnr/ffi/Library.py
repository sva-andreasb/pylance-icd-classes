def getRuntime():
    '''public static Runtime getRuntime(final Object library)
    '''
def loadLibrary():
    '''public static <T> T loadLibrary(final String libraryName, final Class<T> interfaceClass)
    public static <T> T loadLibrary(final Class<T> interfaceClass, final String... libraryNames)
    public static <T> T loadLibrary(final String libraryName, final Class<T> interfaceClass, final Map<LibraryOption, ?> libraryOptions)
    public static <T> T loadLibrary(final Class<T> interfaceClass, final Map<LibraryOption, ?> libraryOptions, final String... libraryNames)
    '''
def addLibraryPath():
    '''public static synchronized void addLibraryPath(final String libraryName, final File path)
    '''
def getLibraryPath():
    '''public static List<String> getLibraryPath(final String libraryName)
    '''
def getInstance():
    '''public static Library getInstance(final String libraryName)
    '''
def getName():
    '''public String getName()
    '''
