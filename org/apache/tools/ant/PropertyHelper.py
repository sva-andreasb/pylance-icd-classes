def setProject():
    '''returns None\n\n
    setProject(final Project p)\n
    '''
def getProject():
    '''returns Project\n\n
    getProject()\n
    '''
def setNext():
    '''returns None\n\n
    setNext(final PropertyHelper next)\n
    '''
def getNext():
    '''returns PropertyHelper\n\n
    getNext()\n
    '''
def getExpanders():
    '''returns Collection\n\n
    getExpanders()\n
    '''
def setPropertyHook():
    '''returns boolean\n\n
    setPropertyHook(final String ns, final String name, final Object value, final boolean inherited, final boolean user, final boolean isNew)\n
    '''
def getPropertyHook():
    '''returns Object\n\n
    getPropertyHook(final String ns, String name, final boolean user)\n
    '''
def parsePropertyString():
    '''returns None\n\n
    parsePropertyString(final String value, final Vector fragments, final Vector propertyRefs)\n
    '''
def replaceProperties():
    '''returns String\n\n
    replaceProperties(final String ns, final String value, final Hashtable keys)\n
    replaceProperties(final String value)\n
    '''
def parseProperties():
    '''returns Object\n\n
    parseProperties(final String value)\n
    '''
def containsProperties():
    '''returns boolean\n\n
    containsProperties(final String value)\n
    '''
def setProperty():
    '''returns boolean\n\n
    setProperty(final String ns, final String name, final Object value, final boolean verbose)\n
    setProperty(final String name, final Object value, final boolean verbose)\n
    '''
def setNewProperty():
    '''returns None\n\n
    setNewProperty(final String ns, final String name, final Object value)\n
    setNewProperty(final String name, final Object value)\n
    '''
def setUserProperty():
    '''returns None\n\n
    setUserProperty(final String ns, final String name, final Object value)\n
    setUserProperty(final String name, final Object value)\n
    '''
def setInheritedProperty():
    '''returns None\n\n
    setInheritedProperty(final String ns, final String name, final Object value)\n
    setInheritedProperty(final String name, final Object value)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String ns, final String name)\n
    getProperty(final String name)\n
    '''
def getUserProperty():
    '''returns Object\n\n
    getUserProperty(final String ns, final String name)\n
    getUserProperty(final String name)\n
    '''
def getProperties():
    '''returns Hashtable\n\n
    getProperties()\n
    '''
def getUserProperties():
    '''returns Hashtable\n\n
    getUserProperties()\n
    '''
def getInheritedProperties():
    '''returns Hashtable\n\n
    getInheritedProperties()\n
    '''
def copyInheritedProperties():
    '''returns None\n\n
    copyInheritedProperties(final Project other)\n
    '''
def copyUserProperties():
    '''returns None\n\n
    copyUserProperties(final Project other)\n
    '''
def add():
    '''returns None\n\n
    add(final Delegate delegate)\n
    '''
def testIfCondition():
    '''returns boolean\n\n
    testIfCondition(final Object value)\n
    '''
def testUnlessCondition():
    '''returns boolean\n\n
    testUnlessCondition(final Object value)\n
    '''
def evaluate():
    '''returns Object\n\n
    evaluate(final String property, final PropertyHelper propertyHelper)\n
    evaluate(final String prop, final PropertyHelper helper)\n
    '''
def parsePropertyName():
    '''returns String\n\n
    parsePropertyName(final String s, final ParsePosition pos, final ParseNextProperty notUsed)\n
    parsePropertyName(final String s, final ParsePosition pos, final ParseNextProperty notUsed)\n
    '''
