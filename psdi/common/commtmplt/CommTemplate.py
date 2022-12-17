def ():
    '''returns CommTemplate\n\n
    (final MboSet ms)\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def canDeactivate():
    '''returns None\n\n
    canDeactivate()\n
    '''
def addPersonRecipients():
    '''returns None\n\n
    addPersonRecipients(final MboSetRemote personSet)\n
    '''
def addGroupRecipients():
    '''returns None\n\n
    addGroupRecipients(final MboSetRemote groupSet)\n
    '''
def addRoleRecipients():
    '''returns None\n\n
    addRoleRecipients(final MboSetRemote roleSet)\n
    '''
def updateRecipientList():
    '''returns String\n\n
    updateRecipientList(final String listName)\n
    '''
def sendMessage():
    '''returns None\n\n
    sendMessage()\n
    sendMessage(final MboRemote targetMbo, final MboRemote originatingMbo)\n
    sendMessage(final MboRemote targetMbo)\n
    '''
def convertSendTo():
    '''returns String\n\n
    convertSendTo(final String relationship, final MboRemote owner)\n
    convertSendTo(final String relationship, final MboRemote owner, final String messagetype)\n
    '''
def convertSendToMap():
    '''returns HashSet<String>\n\n
    convertSendToMap(final String relationship, final MboRemote owner, final String messagetype)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, Date asOfDate)\n
    '''
def setTreeAttrs():
    '''returns None\n\n
    setTreeAttrs(final MboRemote tree)\n
    '''
def exists():
    '''returns boolean\n\n
    exists(final MboRemote currRecipient, final String type, final String id)\n
    '''
def getRefAppsRels():
    '''returns Hashtable\n\n
    getRefAppsRels()\n
    '''
def getDocLinksFromSelectedFolder():
    '''returns None\n\n
    getDocLinksFromSelectedFolder(final MboRemote mbo, final MboSetRemote relatedDocLinkSet)\n
    '''
def needRefresh():
    '''returns None\n\n
    needRefresh(final boolean flag)\n
    '''
def isSubstituted():
    '''returns boolean\n\n
    isSubstituted()\n
    '''
def setSubstituted():
    '''returns None\n\n
    setSubstituted(final boolean substituted)\n
    '''
