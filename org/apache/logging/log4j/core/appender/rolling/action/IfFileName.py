def getSyntaxAndPattern():
    '''public String getSyntaxAndPattern()
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
def createNameCondition():
    '''public static IfFileName createNameCondition(@PluginAttribute("glob") final String glob, @PluginAttribute("regex") final String regex, @PluginElement("PathConditions") final PathCondition... nestedConditions)
    '''
def toString():
    '''public String toString()
    '''
