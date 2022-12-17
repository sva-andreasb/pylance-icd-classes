ELEMENT_NAME = "String  \"workgroup\""
NAMESPACE = "String  \"http://jabber.org/protocol/workgroup\""
def ():
    '''returns WorkgroupInformation\n\n
    (final EntityBareJid workgroupJID)\n
    '''
def getWorkgroupJID():
    '''returns EntityBareJid\n\n
    getWorkgroupJID()\n
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
    '''returns String\n\n
    toXML(final String enclosingNamespace)\n
    '''
def parse():
    '''returns WorkgroupInformation\n\n
    parse(final XmlPullParser parser, final int initialDepth)\n
    '''
