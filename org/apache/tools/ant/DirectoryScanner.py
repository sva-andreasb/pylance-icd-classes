MAX_LEVELS_OF_SYMLINKS = "int  5"
DOES_NOT_EXIST_POSTFIX = "String  \" does not exist.\""
def DirectoryScanner():
    '''public DirectoryScanner()
    '''
def match():
    '''public static boolean match(final String pattern, final String str)
    '''
def getDefaultExcludes():
    '''public static String[] getDefaultExcludes()
    '''
def addDefaultExclude():
    '''public static boolean addDefaultExclude(final String s)
    '''
def removeDefaultExclude():
    '''public static boolean removeDefaultExclude(final String s)
    '''
def resetDefaultExcludes():
    '''public static void resetDefaultExcludes()
    '''
def setBasedir():
    '''public void setBasedir(final String basedir)
    public synchronized void setBasedir(final File basedir)
    '''
def getBasedir():
    '''public synchronized File getBasedir()
    '''
def isCaseSensitive():
    '''public synchronized boolean isCaseSensitive()
    '''
def setCaseSensitive():
    '''public synchronized void setCaseSensitive(final boolean isCaseSensitive)
    '''
def setErrorOnMissingDir():
    '''public void setErrorOnMissingDir(final boolean errorOnMissingDir)
    '''
def isFollowSymlinks():
    '''public synchronized boolean isFollowSymlinks()
    '''
def setFollowSymlinks():
    '''public synchronized void setFollowSymlinks(final boolean followSymlinks)
    '''
def setMaxLevelsOfSymlinks():
    '''public void setMaxLevelsOfSymlinks(final int max)
    '''
def setIncludes():
    '''public synchronized void setIncludes(final String[] includes)
    '''
def setExcludes():
    '''public synchronized void setExcludes(final String[] excludes)
    '''
def addExcludes():
    '''public synchronized void addExcludes(final String[] excludes)
    '''
def setSelectors():
    '''public synchronized void setSelectors(final FileSelector[] selectors)
    '''
def isEverythingIncluded():
    '''public synchronized boolean isEverythingIncluded()
    '''
def scan():
    '''public void scan()
    '''
def getIncludedFiles():
    '''public String[] getIncludedFiles()
    '''
def getIncludedFilesCount():
    '''public synchronized int getIncludedFilesCount()
    '''
def getNotIncludedFiles():
    '''public synchronized String[] getNotIncludedFiles()
    '''
def getExcludedFiles():
    '''public synchronized String[] getExcludedFiles()
    '''
def getDeselectedFiles():
    '''public synchronized String[] getDeselectedFiles()
    '''
def getIncludedDirectories():
    '''public String[] getIncludedDirectories()
    '''
def getIncludedDirsCount():
    '''public synchronized int getIncludedDirsCount()
    '''
def getNotIncludedDirectories():
    '''public synchronized String[] getNotIncludedDirectories()
    '''
def getExcludedDirectories():
    '''public synchronized String[] getExcludedDirectories()
    '''
def getDeselectedDirectories():
    '''public synchronized String[] getDeselectedDirectories()
    '''
def getNotFollowedSymlinks():
    '''public synchronized String[] getNotFollowedSymlinks()
    '''
def addDefaultExcludes():
    '''public synchronized void addDefaultExcludes()
    '''
def getResource():
    '''public synchronized Resource getResource(final String name)
    '''
