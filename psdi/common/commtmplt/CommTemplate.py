def CommTemplate():
    '''    public CommTemplate(final MboSet ms)
    '''
def add():
    '''    public void add()
    '''
def duplicate():
    '''    public MboRemote duplicate()
    '''
def delete():
    '''    public void delete(final long accessModifier)
    '''
def canDelete():
    '''    public void canDelete()
    '''
def canDeactivate():
    '''    public void canDeactivate()
    '''
def addPersonRecipients():
    '''    public void addPersonRecipients(final MboSetRemote personSet)
    '''
def addGroupRecipients():
    '''    public void addGroupRecipients(final MboSetRemote groupSet)
    '''
def addRoleRecipients():
    '''    public void addRoleRecipients(final MboSetRemote roleSet)
    '''
def updateRecipientList():
    '''    public String updateRecipientList(final String listName)
    '''
def sendMessage():
    '''    public void sendMessage()
    public void sendMessage(final MboRemote targetMbo, final MboRemote originatingMbo)
    public void sendMessage(final MboRemote targetMbo)
    '''
def convertSendTo():
    '''    public String convertSendTo(final String relationship, final MboRemote owner)
    public String convertSendTo(final String relationship, final MboRemote owner, final String messagetype)
    '''
def convertSendToMap():
    '''    public HashSet<String> convertSendToMap(final String relationship, final MboRemote owner, final String messagetype)
    '''
def changeStatus():
    '''    public void changeStatus(final String status, Date asOfDate)
    '''
def setTreeAttrs():
    '''    public void setTreeAttrs(final MboRemote tree)
    '''
def checkDeleteRole():
    '''    public static void checkDeleteRole(final Mbo role)
    '''
def exists():
    '''    public boolean exists(final MboRemote currRecipient, final String type, final String id)
    '''
def getRefAppsRels():
    '''    public Hashtable getRefAppsRels()
    '''
def getDocLinksFromSelectedFolder():
    '''    public void getDocLinksFromSelectedFolder(final MboRemote mbo, final MboSetRemote relatedDocLinkSet)
    '''
def needRefresh():
    '''    public void needRefresh(final boolean flag)
    '''
def isSubstituted():
    '''    public boolean isSubstituted()
    '''
def setSubstituted():
    '''    public void setSubstituted(final boolean substituted)
    '''
