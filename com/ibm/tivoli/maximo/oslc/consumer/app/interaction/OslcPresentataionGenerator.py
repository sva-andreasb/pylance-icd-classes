def OslcPresentataionGenerator():
    '''    public OslcPresentataionGenerator(final byte[] presentataion)
    '''
def generatePresentataion():
    '''    public String generatePresentataion(final MboRemote oslcInteraction)
    '''
def getAppXML():
    '''    public Document getAppXML(final String app, final UserInfo userInfo)
    '''
def getOslcTabGroup():
    '''    public Element getOslcTabGroup(final Element parent, final String appName, final String tabName)
    '''
def getAppplicationsTabs():
    '''    public Map<String, String> getAppplicationsTabs(final String appName)
    '''
def getAppplicationsMenus():
    '''    public Map<String, List<InteractionGroupAppMenuInfo>> getAppplicationsMenus(Element top, final Map<String, List<InteractionGroupAppMenuInfo>> allMenus)
    '''
def generateNewMenu():
    '''    public void generateNewMenu(final String intGroupName, final String menuId, final String newMenuId, final String sigOptionName, final String menuLabel)
    '''
def modifyMenuItem():
    '''    public void modifyMenuItem(final Element in)
    '''
def getMenu():
    '''    public Element getMenu(final String name, final boolean remove)
    '''
def getAppplicationsTab():
    '''    public Element getAppplicationsTab(final String tabName, final String appName)
    '''
def getOslcLinkTab():
    '''    public Element getOslcLinkTab(final Element parent, final String oslcTabName)
    '''
def addButton():
    '''    public String addButton(final Element btngroup, final String oslcTabName, final String interaction, final String providerName, final String mapOption, final String buttonLabel)
    '''
def removePresentataion():
    '''    public String removePresentataion(final MboRemote oslcInteraction, final boolean hasLink)
    '''
def findButton():
    '''    public boolean findButton(final Element in, final String inid, final boolean remove)
    '''
def findById():
    '''    public Element findById(final Element in, final String inid)
    '''
def findByName():
    '''    public Element findByName(final Element in, final String inName)
    '''
def modifyAttributeMenu():
    '''    public void modifyAttributeMenu(Element in, final Map<String, String> modifyMenuMap)
    '''
def generateUniqueID():
    '''    public String generateUniqueID()
    '''
def getPresentataionDocument():
    '''    public Document getPresentataionDocument()
    '''
def hasLicenseAccess():
    '''    public boolean hasLicenseAccess(final String licensevalue)
    '''
def getFileName():
    '''    public static String getFileName(final String inter, final String name)
    '''
