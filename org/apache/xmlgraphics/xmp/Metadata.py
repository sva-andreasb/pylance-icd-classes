def ():
    '''returns Metadata\n\n
    ()\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final XMPProperty prop)\n
    '''
def getProperty():
    '''returns XMPProperty\n\n
    getProperty(final String uri, final String localName)\n
    getProperty(final QName name)\n
    '''
def removeProperty():
    '''returns XMPProperty\n\n
    removeProperty(final QName name)\n
    '''
def getValueProperty():
    '''returns XMPProperty\n\n
    getValueProperty()\n
    '''
def getPropertyCount():
    '''returns int\n\n
    getPropertyCount()\n
    '''
def iterator():
    '''returns Iterator\n\n
    iterator()\n
    '''
def mergeInto():
    '''returns None\n\n
    mergeInto(final Metadata target, final List<Class> exclude)\n
    '''
def toSAX():
    '''returns None\n\n
    toSAX(final ContentHandler handler)\n
    '''
