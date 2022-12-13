EXTENSION_SEPARATOR = "char  '.'"
def normalize():
    '''public static String normalize(final String filename)
    public static String normalize(final String filename, final boolean unixSeparator)
    '''
def normalizeNoEndSeparator():
    '''public static String normalizeNoEndSeparator(final String filename)
    public static String normalizeNoEndSeparator(final String filename, final boolean unixSeparator)
    '''
def concat():
    '''public static String concat(final String basePath, final String fullFilenameToAdd)
    '''
def directoryContains():
    '''public static boolean directoryContains(final String canonicalParent, final String canonicalChild)
    '''
def separatorsToUnix():
    '''public static String separatorsToUnix(final String path)
    '''
def separatorsToWindows():
    '''public static String separatorsToWindows(final String path)
    '''
def separatorsToSystem():
    '''public static String separatorsToSystem(final String path)
    '''
def getPrefixLength():
    '''public static int getPrefixLength(final String filename)
    '''
def indexOfLastSeparator():
    '''public static int indexOfLastSeparator(final String filename)
    '''
def indexOfExtension():
    '''public static int indexOfExtension(final String filename)
    '''
def getPrefix():
    '''public static String getPrefix(final String filename)
    '''
def getPath():
    '''public static String getPath(final String filename)
    '''
def getPathNoEndSeparator():
    '''public static String getPathNoEndSeparator(final String filename)
    '''
def getFullPath():
    '''public static String getFullPath(final String filename)
    '''
def getFullPathNoEndSeparator():
    '''public static String getFullPathNoEndSeparator(final String filename)
    '''
def getName():
    '''public static String getName(final String filename)
    '''
def getBaseName():
    '''public static String getBaseName(final String filename)
    '''
def getExtension():
    '''public static String getExtension(final String filename)
    '''
def removeExtension():
    '''public static String removeExtension(final String filename)
    '''
def equals():
    '''public static boolean equals(final String filename1, final String filename2)
    public static boolean equals(String filename1, String filename2, final boolean normalized, IOCase caseSensitivity)
    '''
def equalsOnSystem():
    '''public static boolean equalsOnSystem(final String filename1, final String filename2)
    '''
def equalsNormalized():
    '''public static boolean equalsNormalized(final String filename1, final String filename2)
    '''
def equalsNormalizedOnSystem():
    '''public static boolean equalsNormalizedOnSystem(final String filename1, final String filename2)
    '''
def isExtension():
    '''public static boolean isExtension(final String filename, final String extension)
    public static boolean isExtension(final String filename, final String[] extensions)
    public static boolean isExtension(final String filename, final Collection<String> extensions)
    '''
def wildcardMatch():
    '''public static boolean wildcardMatch(final String filename, final String wildcardMatcher)
    public static boolean wildcardMatch(final String filename, final String wildcardMatcher, IOCase caseSensitivity)
    '''
def wildcardMatchOnSystem():
    '''public static boolean wildcardMatchOnSystem(final String filename, final String wildcardMatcher)
    '''
