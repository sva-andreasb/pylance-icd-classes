def getDeleteFilters():
'''public PathCondition[] getDeleteFilters()
'''
pass
def accept():
'''public boolean accept(final Path baseDir, final Path relativePath, final BasicFileAttributes attrs)
public static boolean accept(final PathCondition[] list, final Path baseDir, final Path relativePath, final BasicFileAttributes attrs)
'''
pass
def beforeFileTreeWalk():
'''public void beforeFileTreeWalk()
public static void beforeFileTreeWalk(final PathCondition[] nestedConditions)
'''
pass
def createAndCondition():
'''public static IfAll createAndCondition(@PluginElement("PathConditions") final PathCondition... components)
'''
pass
def toString():
'''public String toString()
'''
pass
