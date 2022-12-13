def getInstanceFor():
'''public static MamManager getInstanceFor(final XMPPConnection connection)
public static MamManager getInstanceFor(final MultiUserChat multiUserChat)
public static synchronized MamManager getInstanceFor(final XMPPConnection connection, final Jid archiveAddress)
'''
pass
def getArchiveAddress():
'''public Jid getArchiveAddress()
'''
pass
def queryArchive():
'''public MamQueryResult queryArchive(final Integer max)
public MamQueryResult queryArchive(final Jid withJid)
public MamQueryResult queryArchive(final Date start, final Date end)
public MamQueryResult queryArchive(final List<FormField> additionalFields)
public MamQueryResult queryArchive(final Integer max, final Date start, final Date end, final Jid withJid, final List<FormField> additionalFields)
public MamQueryResult queryArchive(final String node, final Integer max, final Date start, final Date end, final Jid withJid, final List<FormField> additionalFields)
public MamQuery queryArchive(final MamQueryArgs mamQueryArgs)
'''
pass
def queryArchiveWithStartDate():
'''public MamQueryResult queryArchiveWithStartDate(final Date start)
'''
pass
def queryArchiveWithEndDate():
'''public MamQueryResult queryArchiveWithEndDate(final Date end)
'''
pass
def page():
'''public MamQueryResult page(final DataForm dataForm, final RSMSet rsmSet)
public MamQueryResult page(final String node, final DataForm dataForm, final RSMSet rsmSet)
'''
pass
def pageNext():
'''public MamQueryResult pageNext(final MamQueryResult mamQueryResult, final int count)
public List<Message> pageNext(final int count)
'''
pass
def pagePrevious():
'''public MamQueryResult pagePrevious(final MamQueryResult mamQueryResult, final int count)
public List<Message> pagePrevious(final int count)
'''
pass
def pageBefore():
'''public MamQueryResult pageBefore(final Jid chatJid, final String messageUid, final int max)
'''
pass
def pageAfter():
'''public MamQueryResult pageAfter(final Jid chatJid, final String messageUid, final int max)
'''
pass
def mostRecentPage():
'''public MamQueryResult mostRecentPage(final Jid chatJid, final int max)
'''
pass
def queryMostRecentPage():
'''public MamQuery queryMostRecentPage(final Jid jid, final int max)
'''
pass
def retrieveFormFields():
'''public List<FormField> retrieveFormFields()
public List<FormField> retrieveFormFields(final String node)
'''
pass
def isSupported():
'''public boolean isSupported()
'''
pass
def getMessageUidOfLatestMessage():
'''public String getMessageUidOfLatestMessage()
'''
pass
def retrieveArchivingPreferences():
'''public MamPrefsResult retrieveArchivingPreferences()
'''
pass
def updateArchivingPreferences():
'''public MamPrefsResult updateArchivingPreferences(final List<Jid> alwaysJids, final List<Jid> neverJids, final MamPrefsIQ.DefaultBehavior defaultBehavior)
public MamPrefsResult updateArchivingPreferences(final MamPrefs mamPrefs)
'''
pass
def enableMamForAllMessages():
'''public MamPrefsResult enableMamForAllMessages()
'''
pass
def enableMamForRosterMessages():
'''public MamPrefsResult enableMamForRosterMessages()
'''
pass
def setDefaultBehavior():
'''public MamPrefsResult setDefaultBehavior(final MamPrefsIQ.DefaultBehavior desiredDefaultBehavior)
public void setDefaultBehavior(final MamPrefsIQ.DefaultBehavior defaultBehavior)
'''
pass
def connectionCreated():
'''public void connectionCreated(final XMPPConnection connection)
'''
pass
def builder():
'''public static Builder builder()
'''
pass
def Builder():
'''public Builder()
'''
pass
def queryNode():
'''public Builder queryNode(final String node)
'''
pass
def limitResultsToJid():
'''public Builder limitResultsToJid(final Jid withJid)
'''
pass
def limitResultsSince():
'''public Builder limitResultsSince(final Date start)
'''
pass
def limitResultsBefore():
'''public Builder limitResultsBefore(final Date end)
'''
pass
def setResultPageSize():
'''public Builder setResultPageSize(final Integer max)
'''
pass
def setResultPageSizeTo():
'''public Builder setResultPageSizeTo(final int max)
'''
pass
def onlyReturnMessageCount():
'''public Builder onlyReturnMessageCount()
'''
pass
def withAdditionalFormField():
'''public Builder withAdditionalFormField(final FormField formField)
'''
pass
def withAdditionalFormFields():
'''public Builder withAdditionalFormFields(final List<FormField> additionalFields)
'''
pass
def afterUid():
'''public Builder afterUid(final String afterUid)
'''
pass
def beforeUid():
'''public Builder beforeUid(final String beforeUid)
'''
pass
def queryLastPage():
'''public Builder queryLastPage()
'''
pass
def build():
'''public MamQueryArgs build()
'''
pass
def isComplete():
'''public boolean isComplete()
'''
pass
def getMessages():
'''public List<Message> getMessages()
public List<Message> getMessages()
'''
pass
def getMessageCount():
'''public int getMessageCount()
'''
pass
def getPage():
'''public MamQueryPage getPage()
'''
pass
def getForwarded():
'''public List<Forwarded> getForwarded()
'''
pass
def getMamResultCarrierMessages():
'''public List<Message> getMamResultCarrierMessages()
'''
pass
def getMamFinIq():
'''public MamFinIQ getMamFinIq()
'''
pass
def asMamPrefs():
'''public MamPrefs asMamPrefs()
'''
pass
def getAlwaysJids():
'''public List<Jid> getAlwaysJids()
'''
pass
def getNeverJids():
'''public List<Jid> getNeverJids()
'''
pass
