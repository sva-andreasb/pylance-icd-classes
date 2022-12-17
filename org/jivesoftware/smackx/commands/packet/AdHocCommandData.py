ELEMENT = "String  \"command\""
NAMESPACE = "String  \"http://jabber.org/protocol/commands\""
namespace = "String  \"http://jabber.org/protocol/commands\""
def ():
    '''returns SpecificError\n\n
    ()\n
    (final AdHocCommand.SpecificErrorCondition condition)\n
    '''
def getId():
    '''returns Jid\n\n
    getId()\n
    '''
def setId():
    '''returns None\n\n
    setId(final Jid id)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def getNode():
    '''returns String\n\n
    getNode()\n
    '''
def setNode():
    '''returns None\n\n
    setNode(final String node)\n
    '''
def getNotes():
    '''returns List<AdHocCommandNote>\n\n
    getNotes()\n
    '''
def addNote():
    '''returns None\n\n
    addNote(final AdHocCommandNote note)\n
    '''
def removeNote():
    '''returns None\n\n
    removeNote(final AdHocCommandNote note)\n
    '''
def getForm():
    '''returns DataForm\n\n
    getForm()\n
    '''
def setForm():
    '''returns None\n\n
    setForm(final DataForm form)\n
    '''
def setAction():
    '''returns None\n\n
    setAction(final AdHocCommand.Action action)\n
    '''
def setStatus():
    '''returns None\n\n
    setStatus(final AdHocCommand.Status status)\n
    '''
def addAction():
    '''returns None\n\n
    addAction(final AdHocCommand.Action action)\n
    '''
def setExecuteAction():
    '''returns None\n\n
    setExecuteAction(final AdHocCommand.Action executeAction)\n
    '''
def setSessionID():
    '''returns None\n\n
    setSessionID(final String sessionID)\n
    '''
def getSessionID():
    '''returns String\n\n
    getSessionID()\n
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
