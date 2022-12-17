ELEMENT = "String  \"set\""
NAMESPACE = "String  \"http://jabber.org/protocol/rsm\""
def ():
    '''returns RSMSet\n\n
    (final int max)\n
    (final int max, final int index)\n
    (final String item, final PageDirection pageDirection)\n
    (final int max, final String item, final PageDirection pageDirection)\n
    (final String after, final String before, final int count, final int index, final String last, final int max, final String firstString, final int firstIndex)\n
    '''
def getAfter():
    '''returns String\n\n
    getAfter()\n
    '''
def getBefore():
    '''returns String\n\n
    getBefore()\n
    '''
def getCount():
    '''returns int\n\n
    getCount()\n
    '''
def getIndex():
    '''returns int\n\n
    getIndex()\n
    '''
def getLast():
    '''returns String\n\n
    getLast()\n
    '''
def getMax():
    '''returns int\n\n
    getMax()\n
    '''
def getFirst():
    '''returns String\n\n
    getFirst()\n
    '''
def getFirstIndex():
    '''returns int\n\n
    getFirstIndex()\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def toXML():
    '''returns XmlStringBuilder\n\n
    toXML(final String enclosingNamespace)\n
    '''
