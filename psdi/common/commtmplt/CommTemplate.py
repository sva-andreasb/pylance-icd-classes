def CommTemplate():
'''public CommTemplate(final MboSet ms)
'''
pass
def add():
'''public void add()
'''
pass
def duplicate():
'''public MboRemote duplicate()
'''
pass
def delete():
'''public void delete(final long accessModifier)
'''
pass
def canDelete():
'''public void canDelete()
'''
pass
def canDeactivate():
'''public void canDeactivate()
'''
pass
def addPersonRecipients():
'''public void addPersonRecipients(final MboSetRemote personSet)
'''
pass
def addGroupRecipients():
'''public void addGroupRecipients(final MboSetRemote groupSet)
'''
pass
def addRoleRecipients():
'''public void addRoleRecipients(final MboSetRemote roleSet)
'''
pass
def updateRecipientList():
'''public String updateRecipientList(final String listName)
'''
pass
def sendMessage():
'''public void sendMessage()
public void sendMessage(final MboRemote targetMbo, final MboRemote originatingMbo)
public void sendMessage(final MboRemote targetMbo)
'''
pass
def convertSendTo():
'''public String convertSendTo(final String relationship, final MboRemote owner)
public String convertSendTo(final String relationship, final MboRemote owner, final String messagetype)
'''
pass
def convertSendToMap():
'''public HashSet<String> convertSendToMap(final String relationship, final MboRemote owner, final String messagetype)
'''
pass
def changeStatus():
'''public void changeStatus(final String status, Date asOfDate)
'''
pass
def setTreeAttrs():
'''public void setTreeAttrs(final MboRemote tree)
'''
pass
def checkDeleteRole():
'''public static void checkDeleteRole(final Mbo role)
'''
pass
def exists():
'''public boolean exists(final MboRemote currRecipient, final String type, final String id)
'''
pass
def getRefAppsRels():
'''public Hashtable getRefAppsRels()
'''
pass
def getDocLinksFromSelectedFolder():
'''public void getDocLinksFromSelectedFolder(final MboRemote mbo, final MboSetRemote relatedDocLinkSet)
'''
pass
def needRefresh():
'''public void needRefresh(final boolean flag)
'''
pass
def isSubstituted():
'''public boolean isSubstituted()
'''
pass
def setSubstituted():
'''public void setSubstituted(final boolean substituted)
'''
pass
