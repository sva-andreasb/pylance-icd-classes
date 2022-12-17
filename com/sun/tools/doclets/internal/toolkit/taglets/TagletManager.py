SIMPLE_TAGLET_OPT_SEPARATOR = "char  ':'"
ALT_SIMPLE_TAGLET_OPT_SEPARATOR = "String  \"-\""
def ():
    '''returns TagletManager\n\n
    (final boolean nosince, final boolean showversion, final boolean showauthor, final boolean javafx, final MessageRetriever message)\n
    '''
def addCustomTag():
    '''returns None\n\n
    addCustomTag(final Taglet value)\n
    addCustomTag(final String name, final JavaFileManager javaFileManager, final String s)\n
    '''
def getCustomTagNames():
    '''returns Set<String>\n\n
    getCustomTagNames()\n
    '''
def addNewSimpleCustomTag():
    '''returns None\n\n
    addNewSimpleCustomTag(final String key, final String s, String lowerCase)\n
    '''
def seenCustomTag():
    '''returns None\n\n
    seenCustomTag(final String s)\n
    '''
def checkTags():
    '''returns None\n\n
    checkTags(final Doc doc, final Tag[] array, final boolean b)\n
    '''
def getPackageCustomTaglets():
    '''returns Taglet[]\n\n
    getPackageCustomTaglets()\n
    '''
def getTypeCustomTaglets():
    '''returns Taglet[]\n\n
    getTypeCustomTaglets()\n
    '''
def getInlineCustomTaglets():
    '''returns Taglet[]\n\n
    getInlineCustomTaglets()\n
    '''
def getFieldCustomTaglets():
    '''returns Taglet[]\n\n
    getFieldCustomTaglets()\n
    '''
def getSerializedFormTaglets():
    '''returns Taglet[]\n\n
    getSerializedFormTaglets()\n
    '''
def getCustomTaglets():
    '''returns Taglet[]\n\n
    getCustomTaglets(final Doc doc)\n
    '''
def getConstructorCustomTaglets():
    '''returns Taglet[]\n\n
    getConstructorCustomTaglets()\n
    '''
def getMethodCustomTaglets():
    '''returns Taglet[]\n\n
    getMethodCustomTaglets()\n
    '''
def getOverviewCustomTaglets():
    '''returns Taglet[]\n\n
    getOverviewCustomTaglets()\n
    '''
def isKnownCustomTag():
    '''returns boolean\n\n
    isKnownCustomTag(final String key)\n
    '''
def printReport():
    '''returns None\n\n
    printReport()\n
    '''
def getTaglet():
    '''returns Taglet\n\n
    getTaglet(final String key)\n
    '''
