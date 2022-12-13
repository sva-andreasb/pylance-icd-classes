def getDeleteFilters():
    '''public PathCondition[] getDeleteFilters()
    '''
def accept():
    '''public boolean accept(final Path baseDir, final Path relativePath, final BasicFileAttributes attrs)
    public static boolean accept(final PathCondition[] list, final Path baseDir, final Path relativePath, final BasicFileAttributes attrs)
    '''
def beforeFileTreeWalk():
    '''public void beforeFileTreeWalk()
    public static void beforeFileTreeWalk(final PathCondition[] nestedConditions)
    '''
def createAndCondition():
    '''public static IfAll createAndCondition(@PluginElement("PathConditions") final PathCondition... components)
    '''
def toString():
    '''public String toString()
    '''
