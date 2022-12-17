ANT_CORE_URI = "String  \"antlib:org.apache.tools.ant\""
ANT_CURRENT_URI = "String  \"ant:current\""
ANTLIB_URI = "String  \"antlib:\""
ANT_TYPE = "String  \"ant-type\""
HELPER_PROPERTY = "String  \"org.apache.tools.ant.ProjectHelper\""
SERVICE_ID = "String  \"META-INF/services/org.apache.tools.ant.ProjectHelper\""
PROJECTHELPER_REFERENCE = "String  \"ant.projectHelper\""
def ():
    '''returns ProjectHelper\n\n
    ()\n
    '''
def getImportStack():
    '''returns Vector\n\n
    getImportStack()\n
    '''
def getExtensionStack():
    '''returns List\n\n
    getExtensionStack()\n
    '''
def parse():
    '''returns None\n\n
    parse(final Project project, final Object source)\n
    '''
def canParseAntlibDescriptor():
    '''returns boolean\n\n
    canParseAntlibDescriptor(final Resource r)\n
    '''
def parseAntlibDescriptor():
    '''returns UnknownElement\n\n
    parseAntlibDescriptor(final Project containingProject, final Resource source)\n
    '''
def canParseBuildFile():
    '''returns boolean\n\n
    canParseBuildFile(final Resource buildFile)\n
    '''
def getDefaultBuildFile():
    '''returns String\n\n
    getDefaultBuildFile()\n
    '''
