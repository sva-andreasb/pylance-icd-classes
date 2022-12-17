PATH_DELIMITER = "String  \";\""
def ():
    '''returns FileManager\n\n
    ()\n
    (final FileManager filemanager)\n
    (final LocationMapper _mapper)\n
    '''
def setMapper():
    '''returns None\n\n
    setMapper(final LocationMapper _mapper)\n
    '''
def setLocationMapper():
    '''returns None\n\n
    setLocationMapper(final LocationMapper _mapper)\n
    '''
def getLocationMapper():
    '''returns LocationMapper\n\n
    getLocationMapper()\n
    '''
def locators():
    '''returns Iterator<Locator>\n\n
    locators()\n
    '''
def addLocator():
    '''returns None\n\n
    addLocator(final Locator loc)\n
    '''
def addLocatorFile():
    '''returns None\n\n
    addLocatorFile()\n
    addLocatorFile(final String dir)\n
    '''
def addLocatorClassLoader():
    '''returns None\n\n
    addLocatorClassLoader(final ClassLoader cLoad)\n
    '''
def addLocatorURL():
    '''returns None\n\n
    addLocatorURL()\n
    '''
def addLocatorZip():
    '''returns None\n\n
    addLocatorZip(final String zfn)\n
    '''
def remove():
    '''returns None\n\n
    remove(final Locator loc)\n
    '''
def resetCache():
    '''returns None\n\n
    resetCache()\n
    '''
def setModelCaching():
    '''returns None\n\n
    setModelCaching(final boolean state)\n
    '''
def getCachingModels():
    '''returns boolean\n\n
    getCachingModels()\n
    '''
def getFromCache():
    '''returns Model\n\n
    getFromCache(final String filenameOrURI)\n
    '''
def hasCachedModel():
    '''returns boolean\n\n
    hasCachedModel(final String filenameOrURI)\n
    '''
def addCacheModel():
    '''returns None\n\n
    addCacheModel(final String uri, final Model m)\n
    '''
def removeCacheModel():
    '''returns None\n\n
    removeCacheModel(final String uri)\n
    '''
def loadModel():
    '''returns Model\n\n
    loadModel(final String filenameOrURI)\n
    loadModel(final String filenameOrURI, final String rdfSyntax)\n
    loadModel(final String filenameOrURI, final String baseURI, final String rdfSyntax)\n
    '''
def readModel():
    '''returns Model\n\n
    readModel(final Model model, final String filenameOrURI)\n
    readModel(final Model model, final String filenameOrURI, final String rdfSyntax)\n
    readModel(final Model model, final String filenameOrURI, final String baseURI, final String syntax)\n
    '''
def open():
    '''returns InputStream\n\n
    open(final String filenameOrURI)\n
    '''
def remap():
    '''returns String\n\n
    remap(final String filenameOrURI)\n
    '''
def mapURI():
    '''returns String\n\n
    mapURI(final String filenameOrURI)\n
    '''
def readWholeFileAsUTF8():
    '''returns String\n\n
    readWholeFileAsUTF8(final InputStream in)\n
    readWholeFileAsUTF8(final String filename)\n
    '''
def openNoMap():
    '''returns InputStream\n\n
    openNoMap(final String filenameOrURI)\n
    '''
def openNoMapOrNull():
    '''returns TypedStream\n\n
    openNoMapOrNull(final String filenameOrURI)\n
    '''
