def ():
    '''returns OslcPresentataionGenerator\n\n
    (final byte[] presentataion)\n
    '''
def generatePresentataion():
    '''returns String\n\n
    generatePresentataion(final MboRemote oslcInteraction)\n
    '''
def getAppXML():
    '''returns Document\n\n
    getAppXML(final String app, final UserInfo userInfo)\n
    '''
def getOslcTabGroup():
    '''returns Element\n\n
    getOslcTabGroup(final Element parent, final String appName, final String tabName)\n
    '''
def generateNewMenu():
    '''returns None\n\n
    generateNewMenu(final String intGroupName, final String menuId, final String newMenuId, final String sigOptionName, final String menuLabel)\n
    '''
def modifyMenuItem():
    '''returns None\n\n
    modifyMenuItem(final Element in)\n
    '''
def getMenu():
    '''returns Element\n\n
    getMenu(final String name, final boolean remove)\n
    '''
def getAppplicationsTab():
    '''returns Element\n\n
    getAppplicationsTab(final String tabName, final String appName)\n
    '''
def getOslcLinkTab():
    '''returns Element\n\n
    getOslcLinkTab(final Element parent, final String oslcTabName)\n
    '''
def addButton():
    '''returns String\n\n
    addButton(final Element btngroup, final String oslcTabName, final String interaction, final String providerName, final String mapOption, final String buttonLabel)\n
    '''
def removePresentataion():
    '''returns String\n\n
    removePresentataion(final MboRemote oslcInteraction, final boolean hasLink)\n
    '''
def findButton():
    '''returns boolean\n\n
    findButton(final Element in, final String inid, final boolean remove)\n
    '''
def findById():
    '''returns Element\n\n
    findById(final Element in, final String inid)\n
    '''
def findByName():
    '''returns Element\n\n
    findByName(final Element in, final String inName)\n
    '''
def modifyAttributeMenu():
    '''returns None\n\n
    modifyAttributeMenu(Element in, final Map<String, String> modifyMenuMap)\n
    '''
def generateUniqueID():
    '''returns String\n\n
    generateUniqueID()\n
    '''
def getPresentataionDocument():
    '''returns Document\n\n
    getPresentataionDocument()\n
    '''
def hasLicenseAccess():
    '''returns boolean\n\n
    hasLicenseAccess(final String licensevalue)\n
    '''
