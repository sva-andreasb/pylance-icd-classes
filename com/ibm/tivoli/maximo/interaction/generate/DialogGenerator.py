def ():
    '''returns DialogGenerator\n\n
    ()\n
    '''
def generateDialog():
    '''returns String\n\n
    generateDialog(final MboRemote intGenerator, final byte[] presentataion)\n
    '''
def getAppXML():
    '''returns Document\n\n
    getAppXML(final String app, final UserInfo userInfo)\n
    '''
def removeDialog():
    '''returns String\n\n
    removeDialog(final Document doc, final String dialogID)\n
    '''
def findDialog():
    '''returns boolean\n\n
    findDialog(final Document doc, final String appName, final String dialogID)\n
    '''
def findElementByID():
    '''returns boolean\n\n
    findElementByID(final Element in, final String inid)\n
    '''
def findAction():
    '''returns boolean\n\n
    findAction(final Document doc, final String appName, final String actionId)\n
    '''
def findChildren():
    '''returns List<MboRemote>\n\n
    findChildren(final MboSetRemote set, final String relation, final String hierarchyPath)\n
    '''
def setLookup():
    '''returns None\n\n
    setLookup(final Element data, final String type)\n
    '''
def generateUniqueID():
    '''returns String\n\n
    generateUniqueID()\n
    '''
def getFileName():
    '''returns String\n\n
    getFileName(final String inter, final String name)\n
    '''
