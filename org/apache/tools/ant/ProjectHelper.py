ANT_CORE_URI = "String  \"antlib:org.apache.tools.ant\""
ANT_CURRENT_URI = "String  \"ant:current\""
ANTLIB_URI = "String  \"antlib:\""
ANT_TYPE = "String  \"ant-type\""
HELPER_PROPERTY = "String  \"org.apache.tools.ant.ProjectHelper\""
SERVICE_ID = "String  \"META-INF/services/org.apache.tools.ant.ProjectHelper\""
PROJECTHELPER_REFERENCE = "String  \"ant.projectHelper\""
def configureProject():
    '''public static void configureProject(final Project project, final File buildFile)
    '''
def ProjectHelper():
    '''public ProjectHelper()
    '''
def getImportStack():
    '''public Vector getImportStack()
    '''
def getExtensionStack():
    '''public List getExtensionStack()
    '''
def getCurrentTargetPrefix():
    '''public static String getCurrentTargetPrefix()
    '''
def setCurrentTargetPrefix():
    '''public static void setCurrentTargetPrefix(final String prefix)
    '''
def getCurrentPrefixSeparator():
    '''public static String getCurrentPrefixSeparator()
    '''
def setCurrentPrefixSeparator():
    '''public static void setCurrentPrefixSeparator(final String sep)
    '''
def isInIncludeMode():
    '''public static boolean isInIncludeMode()
    '''
def setInIncludeMode():
    '''public static void setInIncludeMode(final boolean includeMode)
    '''
def parse():
    '''public void parse(final Project project, final Object source)
    '''
def getProjectHelper():
    '''public static ProjectHelper getProjectHelper()
    '''
def getContextClassLoader():
    '''public static ClassLoader getContextClassLoader()
    '''
def configure():
    '''public static void configure(Object target, final AttributeList attrs, final Project project)
    '''
def addText():
    '''public static void addText(final Project project, final Object target, final char[] buf, final int start, final int count)
    public static void addText(final Project project, Object target, final String text)
    '''
def storeChild():
    '''public static void storeChild(final Project project, final Object parent, final Object child, final String tag)
    '''
def replaceProperties():
    '''public static String replaceProperties(final Project project, final String value)
    public static String replaceProperties(final Project project, final String value, final Hashtable keys)
    '''
def parsePropertyString():
    '''public static void parsePropertyString(final String value, final Vector fragments, final Vector propertyRefs)
    '''
def genComponentName():
    '''public static String genComponentName(final String uri, final String name)
    '''
def extractUriFromComponentName():
    '''public static String extractUriFromComponentName(final String componentName)
    '''
def extractNameFromComponentName():
    '''public static String extractNameFromComponentName(final String componentName)
    '''
def addLocationToBuildException():
    '''public static BuildException addLocationToBuildException(final BuildException ex, final Location newLocation)
    '''
def canParseAntlibDescriptor():
    '''public boolean canParseAntlibDescriptor(final Resource r)
    '''
def parseAntlibDescriptor():
    '''public UnknownElement parseAntlibDescriptor(final Project containingProject, final Resource source)
    '''
def canParseBuildFile():
    '''public boolean canParseBuildFile(final Resource buildFile)
    '''
def getDefaultBuildFile():
    '''public String getDefaultBuildFile()
    '''
