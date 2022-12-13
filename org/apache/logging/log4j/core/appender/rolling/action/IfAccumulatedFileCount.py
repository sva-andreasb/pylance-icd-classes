def getThresholdCount():
    '''public int getThresholdCount()
    '''
def getNestedConditions():
    '''public List<PathCondition> getNestedConditions()
    '''
def accept():
    '''public boolean accept(final Path basePath, final Path relativePath, final BasicFileAttributes attrs)
    '''
def beforeFileTreeWalk():
    '''public void beforeFileTreeWalk()
    '''
def createFileCountCondition():
    '''public static IfAccumulatedFileCount createFileCountCondition(@PluginAttribute(value = "exceeds", defaultInt = Integer.MAX_VALUE) final int threshold, @PluginElement("PathConditions") final PathCondition... nestedConditions)
    '''
def toString():
    '''public String toString()
    '''
