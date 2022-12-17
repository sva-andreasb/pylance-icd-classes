DEFAULT_NSTOPKG_FILE = "String  \"NStoPkg.properties\""
def ():
    '''returns Emitter\n\n
    ()\n
    '''
def setServerSide():
    '''returns None\n\n
    setServerSide(final boolean value)\n
    '''
def isServerSide():
    '''returns boolean\n\n
    isServerSide()\n
    '''
def setSkeletonWanted():
    '''returns None\n\n
    setSkeletonWanted(final boolean value)\n
    '''
def isSkeletonWanted():
    '''returns boolean\n\n
    isSkeletonWanted()\n
    '''
def setHelperWanted():
    '''returns None\n\n
    setHelperWanted(final boolean value)\n
    '''
def isHelperWanted():
    '''returns boolean\n\n
    isHelperWanted()\n
    '''
def setTestCaseWanted():
    '''returns None\n\n
    setTestCaseWanted(final boolean value)\n
    '''
def isTestCaseWanted():
    '''returns boolean\n\n
    isTestCaseWanted()\n
    '''
def isBuildFileWanted():
    '''returns boolean\n\n
    isBuildFileWanted()\n
    '''
def setBuildFileWanted():
    '''returns None\n\n
    setBuildFileWanted(final boolean value)\n
    '''
def setAllWanted():
    '''returns None\n\n
    setAllWanted(final boolean all)\n
    '''
def isAllWanted():
    '''returns boolean\n\n
    isAllWanted()\n
    '''
def getNamespaces():
    '''returns Namespaces\n\n
    getNamespaces()\n
    '''
def setOutputDir():
    '''returns None\n\n
    setOutputDir(final String outputDir)\n
    '''
def getOutputDir():
    '''returns String\n\n
    getOutputDir()\n
    '''
def getPackageName():
    '''returns String\n\n
    getPackageName()\n
    '''
def setPackageName():
    '''returns None\n\n
    setPackageName(final String packageName)\n
    '''
def setScope():
    '''returns None\n\n
    setScope(final Scope scope)\n
    '''
def getScope():
    '''returns Scope\n\n
    getScope()\n
    '''
def setNStoPkg():
    '''returns None\n\n
    setNStoPkg(final String NStoPkgFilename)\n
    '''
def setNamespaceMap():
    '''returns None\n\n
    setNamespaceMap(final HashMap map)\n
    '''
def getNamespaceMap():
    '''returns HashMap\n\n
    getNamespaceMap()\n
    '''
def setNamespaceIncludes():
    '''returns None\n\n
    setNamespaceIncludes(final List nsIncludes)\n
    '''
def getNamespaceIncludes():
    '''returns List\n\n
    getNamespaceIncludes()\n
    '''
def setNamespaceExcludes():
    '''returns None\n\n
    setNamespaceExcludes(final List nsExcludes)\n
    '''
def getNamespaceExcludes():
    '''returns List\n\n
    getNamespaceExcludes()\n
    '''
def setProperties():
    '''returns None\n\n
    setProperties(final List properties)\n
    '''
def getProperties():
    '''returns List\n\n
    getProperties()\n
    '''
def getDefaultTypeMapping():
    '''returns TypeMapping\n\n
    getDefaultTypeMapping()\n
    '''
def setDefaultTypeMapping():
    '''returns None\n\n
    setDefaultTypeMapping(final TypeMapping defaultTM)\n
    '''
def setFactory():
    '''returns None\n\n
    setFactory(final String factory)\n
    '''
def getGeneratedFileInfo():
    '''returns GeneratedFileInfo\n\n
    getGeneratedFileInfo()\n
    '''
def getGeneratedClassNames():
    '''returns List\n\n
    getGeneratedClassNames()\n
    '''
def getGeneratedFileNames():
    '''returns List\n\n
    getGeneratedFileNames()\n
    '''
def getPackage():
    '''returns String\n\n
    getPackage(final String namespace)\n
    getPackage(final QName qName)\n
    '''
def getJavaName():
    '''returns String\n\n
    getJavaName(final QName qName)\n
    '''
def getJavaVariableName():
    '''returns String\n\n
    getJavaVariableName(final QName typeQName, final QName xmlName, final boolean isElement)\n
    '''
def run():
    '''returns None\n\n
    run(final String wsdlURL)\n
    run(final String context, final Document doc)\n
    '''
def getTypeMappingVersion():
    '''returns String\n\n
    getTypeMappingVersion()\n
    '''
def setTypeMappingVersion():
    '''returns None\n\n
    setTypeMappingVersion(final String typeMappingVersion)\n
    '''
def getBaseName():
    '''returns String\n\n
    getBaseName(final QName qNameIn)\n
    '''
def getWriterFactory():
    '''returns GeneratorFactory\n\n
    getWriterFactory()\n
    '''
def emit():
    '''returns None\n\n
    emit(final String uri)\n
    emit(final String context, final Document doc)\n
    '''
def generateServerSide():
    '''returns None\n\n
    generateServerSide(final boolean value)\n
    '''
def getGenerateServerSide():
    '''returns boolean\n\n
    getGenerateServerSide()\n
    '''
def deploySkeleton():
    '''returns None\n\n
    deploySkeleton(final boolean value)\n
    '''
def getDeploySkeleton():
    '''returns boolean\n\n
    getDeploySkeleton()\n
    '''
def setHelperGeneration():
    '''returns None\n\n
    setHelperGeneration(final boolean value)\n
    '''
def getHelperGeneration():
    '''returns boolean\n\n
    getHelperGeneration()\n
    '''
def generateImports():
    '''returns None\n\n
    generateImports(final boolean generateImports)\n
    '''
def debug():
    '''returns None\n\n
    debug(final boolean value)\n
    '''
def getDebug():
    '''returns boolean\n\n
    getDebug()\n
    '''
def verbose():
    '''returns None\n\n
    verbose(final boolean value)\n
    '''
def getVerbose():
    '''returns boolean\n\n
    getVerbose()\n
    '''
def generateTestCase():
    '''returns None\n\n
    generateTestCase(final boolean value)\n
    '''
def generateAll():
    '''returns None\n\n
    generateAll(final boolean all)\n
    '''
def isTypeCollisionProtection():
    '''returns boolean\n\n
    isTypeCollisionProtection()\n
    '''
def setTypeCollisionProtection():
    '''returns None\n\n
    setTypeCollisionProtection(final boolean value)\n
    '''
def getImplementationClassName():
    '''returns String\n\n
    getImplementationClassName()\n
    '''
def setImplementationClassName():
    '''returns None\n\n
    setImplementationClassName(final String implementationClassName)\n
    '''
def isAllowInvalidURL():
    '''returns boolean\n\n
    isAllowInvalidURL()\n
    '''
def setAllowInvalidURL():
    '''returns None\n\n
    setAllowInvalidURL(final boolean allowInvalidURL)\n
    '''
def setQName2ClassMap():
    '''returns None\n\n
    setQName2ClassMap(final HashMap map)\n
    '''
def getQName2ClassMap():
    '''returns HashMap\n\n
    getQName2ClassMap()\n
    '''
def getServiceDesc():
    '''returns ServiceDesc\n\n
    getServiceDesc()\n
    '''
def setServiceDesc():
    '''returns None\n\n
    setServiceDesc(final ServiceDesc serviceDesc)\n
    '''
def isDeploy():
    '''returns boolean\n\n
    isDeploy()\n
    '''
def setDeploy():
    '''returns None\n\n
    setDeploy(final boolean isDeploy)\n
    '''
def setWrapArrays():
    '''returns None\n\n
    setWrapArrays(final boolean wrapArrays)\n
    '''
