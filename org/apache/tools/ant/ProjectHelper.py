ANT_CORE_URI = "String  antlib:org.apache.tools.ant""
ANT_CURRENT_URI = "String  ant:current""
ANTLIB_URI = "String  antlib:""
ANT_TYPE = "String  ant-type""
HELPER_PROPERTY = "String  org.apache.tools.ant.ProjectHelper""
SERVICE_ID = "String  META-INF/services/org.apache.tools.ant.ProjectHelper""
PROJECTHELPER_REFERENCE = "String  ant.projectHelper""
def configureProject():
'''public static void configureProject(final Project project, final File buildFile)
'''
pass
def ProjectHelper():
'''public ProjectHelper()
'''
pass
def getImportStack():
'''public Vector getImportStack()
'''
pass
def getExtensionStack():
'''public List getExtensionStack()
'''
pass
def getCurrentTargetPrefix():
'''public static String getCurrentTargetPrefix()
'''
pass
def setCurrentTargetPrefix():
'''public static void setCurrentTargetPrefix(final String prefix)
'''
pass
def getCurrentPrefixSeparator():
'''public static String getCurrentPrefixSeparator()
'''
pass
def setCurrentPrefixSeparator():
'''public static void setCurrentPrefixSeparator(final String sep)
'''
pass
def isInIncludeMode():
'''public static boolean isInIncludeMode()
'''
pass
def setInIncludeMode():
'''public static void setInIncludeMode(final boolean includeMode)
'''
pass
def parse():
'''public void parse(final Project project, final Object source)
'''
pass
def getProjectHelper():
'''public static ProjectHelper getProjectHelper()
'''
pass
def getContextClassLoader():
'''public static ClassLoader getContextClassLoader()
'''
pass
def configure():
'''public static void configure(Object target, final AttributeList attrs, final Project project)
'''
pass
def addText():
'''public static void addText(final Project project, final Object target, final char[] buf, final int start, final int count)
public static void addText(final Project project, Object target, final String text)
'''
pass
def storeChild():
'''public static void storeChild(final Project project, final Object parent, final Object child, final String tag)
'''
pass
def replaceProperties():
'''public static String replaceProperties(final Project project, final String value)
public static String replaceProperties(final Project project, final String value, final Hashtable keys)
'''
pass
def parsePropertyString():
'''public static void parsePropertyString(final String value, final Vector fragments, final Vector propertyRefs)
'''
pass
def genComponentName():
'''public static String genComponentName(final String uri, final String name)
'''
pass
def extractUriFromComponentName():
'''public static String extractUriFromComponentName(final String componentName)
'''
pass
def extractNameFromComponentName():
'''public static String extractNameFromComponentName(final String componentName)
'''
pass
def addLocationToBuildException():
'''public static BuildException addLocationToBuildException(final BuildException ex, final Location newLocation)
'''
pass
def canParseAntlibDescriptor():
'''public boolean canParseAntlibDescriptor(final Resource r)
'''
pass
def parseAntlibDescriptor():
'''public UnknownElement parseAntlibDescriptor(final Project containingProject, final Resource source)
'''
pass
def canParseBuildFile():
'''public boolean canParseBuildFile(final Resource buildFile)
'''
pass
def getDefaultBuildFile():
'''public String getDefaultBuildFile()
'''
pass
