def getArchiveAddress():
    '''returns Jid\n\n
    getArchiveAddress()\n
    '''
def queryArchive():
    '''returns MamQuery\n\n
    queryArchive(final Integer max)\n
    queryArchive(final Jid withJid)\n
    queryArchive(final Date start, final Date end)\n
    queryArchive(final List<FormField> additionalFields)\n
    queryArchive(final Integer max, final Date start, final Date end, final Jid withJid, final List<FormField> additionalFields)\n
    queryArchive(final String node, final Integer max, final Date start, final Date end, final Jid withJid, final List<FormField> additionalFields)\n
    queryArchive(final MamQueryArgs mamQueryArgs)\n
    '''
def queryArchiveWithStartDate():
    '''returns MamQueryResult\n\n
    queryArchiveWithStartDate(final Date start)\n
    '''
def queryArchiveWithEndDate():
    '''returns MamQueryResult\n\n
    queryArchiveWithEndDate(final Date end)\n
    '''
def page():
    '''returns MamQueryResult\n\n
    page(final DataForm dataForm, final RSMSet rsmSet)\n
    page(final String node, final DataForm dataForm, final RSMSet rsmSet)\n
    '''
def pageNext():
    '''returns List<Message>\n\n
    pageNext(final MamQueryResult mamQueryResult, final int count)\n
    pageNext(final int count)\n
    '''
def pagePrevious():
    '''returns List<Message>\n\n
    pagePrevious(final MamQueryResult mamQueryResult, final int count)\n
    pagePrevious(final int count)\n
    '''
def pageBefore():
    '''returns MamQueryResult\n\n
    pageBefore(final Jid chatJid, final String messageUid, final int max)\n
    '''
def pageAfter():
    '''returns MamQueryResult\n\n
    pageAfter(final Jid chatJid, final String messageUid, final int max)\n
    '''
def mostRecentPage():
    '''returns MamQueryResult\n\n
    mostRecentPage(final Jid chatJid, final int max)\n
    '''
def queryMostRecentPage():
    '''returns MamQuery\n\n
    queryMostRecentPage(final Jid jid, final int max)\n
    '''
def retrieveFormFields():
    '''returns List<FormField>\n\n
    retrieveFormFields()\n
    retrieveFormFields(final String node)\n
    '''
def isSupported():
    '''returns boolean\n\n
    isSupported()\n
    '''
def getMessageUidOfLatestMessage():
    '''returns String\n\n
    getMessageUidOfLatestMessage()\n
    '''
def retrieveArchivingPreferences():
    '''returns MamPrefsResult\n\n
    retrieveArchivingPreferences()\n
    '''
def updateArchivingPreferences():
    '''returns MamPrefsResult\n\n
    updateArchivingPreferences(final List<Jid> alwaysJids, final List<Jid> neverJids, final MamPrefsIQ.DefaultBehavior defaultBehavior)\n
    updateArchivingPreferences(final MamPrefs mamPrefs)\n
    '''
def enableMamForAllMessages():
    '''returns MamPrefsResult\n\n
    enableMamForAllMessages()\n
    '''
def enableMamForRosterMessages():
    '''returns MamPrefsResult\n\n
    enableMamForRosterMessages()\n
    '''
def setDefaultBehavior():
    '''returns None\n\n
    setDefaultBehavior(final MamPrefsIQ.DefaultBehavior desiredDefaultBehavior)\n
    setDefaultBehavior(final MamPrefsIQ.DefaultBehavior defaultBehavior)\n
    '''
def connectionCreated():
    '''returns None\n\n
    connectionCreated(final XMPPConnection connection)\n
    '''
def ():
    '''returns Builder\n\n
    ()\n
    '''
def queryNode():
    '''returns Builder\n\n
    queryNode(final String node)\n
    '''
def limitResultsToJid():
    '''returns Builder\n\n
    limitResultsToJid(final Jid withJid)\n
    '''
def limitResultsSince():
    '''returns Builder\n\n
    limitResultsSince(final Date start)\n
    '''
def limitResultsBefore():
    '''returns Builder\n\n
    limitResultsBefore(final Date end)\n
    '''
def setResultPageSize():
    '''returns Builder\n\n
    setResultPageSize(final Integer max)\n
    '''
def setResultPageSizeTo():
    '''returns Builder\n\n
    setResultPageSizeTo(final int max)\n
    '''
def onlyReturnMessageCount():
    '''returns Builder\n\n
    onlyReturnMessageCount()\n
    '''
def withAdditionalFormField():
    '''returns Builder\n\n
    withAdditionalFormField(final FormField formField)\n
    '''
def withAdditionalFormFields():
    '''returns Builder\n\n
    withAdditionalFormFields(final List<FormField> additionalFields)\n
    '''
def afterUid():
    '''returns Builder\n\n
    afterUid(final String afterUid)\n
    '''
def beforeUid():
    '''returns Builder\n\n
    beforeUid(final String beforeUid)\n
    '''
def queryLastPage():
    '''returns Builder\n\n
    queryLastPage()\n
    '''
def build():
    '''returns MamQueryArgs\n\n
    build()\n
    '''
def isComplete():
    '''returns boolean\n\n
    isComplete()\n
    '''
def getMessages():
    '''returns List<Message>\n\n
    getMessages()\n
    getMessages()\n
    '''
def getMessageCount():
    '''returns int\n\n
    getMessageCount()\n
    '''
def getPage():
    '''returns MamQueryPage\n\n
    getPage()\n
    '''
def getForwarded():
    '''returns List<Forwarded>\n\n
    getForwarded()\n
    '''
def getMamResultCarrierMessages():
    '''returns List<Message>\n\n
    getMamResultCarrierMessages()\n
    '''
def getMamFinIq():
    '''returns MamFinIQ\n\n
    getMamFinIq()\n
    '''
def asMamPrefs():
    '''returns MamPrefs\n\n
    asMamPrefs()\n
    '''
def getAlwaysJids():
    '''returns List<Jid>\n\n
    getAlwaysJids()\n
    '''
def getNeverJids():
    '''returns List<Jid>\n\n
    getNeverJids()\n
    '''
