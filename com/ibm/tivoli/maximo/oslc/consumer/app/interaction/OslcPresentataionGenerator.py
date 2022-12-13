def OslcPresentataionGenerator():
'''public OslcPresentataionGenerator(final byte[] presentataion)
'''
pass
def generatePresentataion():
'''public String generatePresentataion(final MboRemote oslcInteraction)
'''
pass
def getAppXML():
'''public Document getAppXML(final String app, final UserInfo userInfo)
'''
pass
def getOslcTabGroup():
'''public Element getOslcTabGroup(final Element parent, final String appName, final String tabName)
'''
pass
def getAppplicationsTabs():
'''public Map<String, String> getAppplicationsTabs(final String appName)
'''
pass
def getAppplicationsMenus():
'''public Map<String, List<InteractionGroupAppMenuInfo>> getAppplicationsMenus(Element top, final Map<String, List<InteractionGroupAppMenuInfo>> allMenus)
'''
pass
def generateNewMenu():
'''public void generateNewMenu(final String intGroupName, final String menuId, final String newMenuId, final String sigOptionName, final String menuLabel)
'''
pass
def modifyMenuItem():
'''public void modifyMenuItem(final Element in)
'''
pass
def getMenu():
'''public Element getMenu(final String name, final boolean remove)
'''
pass
def getAppplicationsTab():
'''public Element getAppplicationsTab(final String tabName, final String appName)
'''
pass
def getOslcLinkTab():
'''public Element getOslcLinkTab(final Element parent, final String oslcTabName)
'''
pass
def addButton():
'''public String addButton(final Element btngroup, final String oslcTabName, final String interaction, final String providerName, final String mapOption, final String buttonLabel)
'''
pass
def removePresentataion():
'''public String removePresentataion(final MboRemote oslcInteraction, final boolean hasLink)
'''
pass
def findButton():
'''public boolean findButton(final Element in, final String inid, final boolean remove)
'''
pass
def findById():
'''public Element findById(final Element in, final String inid)
'''
pass
def findByName():
'''public Element findByName(final Element in, final String inName)
'''
pass
def modifyAttributeMenu():
'''public void modifyAttributeMenu(Element in, final Map<String, String> modifyMenuMap)
'''
pass
def generateUniqueID():
'''public String generateUniqueID()
'''
pass
def getPresentataionDocument():
'''public Document getPresentataionDocument()
'''
pass
def hasLicenseAccess():
'''public boolean hasLicenseAccess(final String licensevalue)
'''
pass
def getFileName():
'''public static String getFileName(final String inter, final String name)
'''
pass
