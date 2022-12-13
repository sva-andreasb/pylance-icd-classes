def getInstanceFor():
    '''public static MamManager getInstanceFor(final XMPPConnection connection)
    public static MamManager getInstanceFor(final MultiUserChat multiUserChat)
    public static synchronized MamManager getInstanceFor(final XMPPConnection connection, final Jid archiveAddress)
    '''
def getArchiveAddress():
    '''public Jid getArchiveAddress()
    '''
def queryArchive():
    '''public MamQueryResult queryArchive(final Integer max)
    public MamQueryResult queryArchive(final Jid withJid)
    public MamQueryResult queryArchive(final Date start, final Date end)
    public MamQueryResult queryArchive(final List<FormField> additionalFields)
    public MamQueryResult queryArchive(final Integer max, final Date start, final Date end, final Jid withJid, final List<FormField> additionalFields)
    public MamQueryResult queryArchive(final String node, final Integer max, final Date start, final Date end, final Jid withJid, final List<FormField> additionalFields)
    public MamQuery queryArchive(final MamQueryArgs mamQueryArgs)
    '''
def queryArchiveWithStartDate():
    '''public MamQueryResult queryArchiveWithStartDate(final Date start)
    '''
def queryArchiveWithEndDate():
    '''public MamQueryResult queryArchiveWithEndDate(final Date end)
    '''
def page():
    '''public MamQueryResult page(final DataForm dataForm, final RSMSet rsmSet)
    public MamQueryResult page(final String node, final DataForm dataForm, final RSMSet rsmSet)
    '''
def pageNext():
    '''public MamQueryResult pageNext(final MamQueryResult mamQueryResult, final int count)
    public List<Message> pageNext(final int count)
    '''
def pagePrevious():
    '''public MamQueryResult pagePrevious(final MamQueryResult mamQueryResult, final int count)
    public List<Message> pagePrevious(final int count)
    '''
def pageBefore():
    '''public MamQueryResult pageBefore(final Jid chatJid, final String messageUid, final int max)
    '''
def pageAfter():
    '''public MamQueryResult pageAfter(final Jid chatJid, final String messageUid, final int max)
    '''
def mostRecentPage():
    '''public MamQueryResult mostRecentPage(final Jid chatJid, final int max)
    '''
def queryMostRecentPage():
    '''public MamQuery queryMostRecentPage(final Jid jid, final int max)
    '''
def retrieveFormFields():
    '''public List<FormField> retrieveFormFields()
    public List<FormField> retrieveFormFields(final String node)
    '''
def isSupported():
    '''public boolean isSupported()
    '''
def getMessageUidOfLatestMessage():
    '''public String getMessageUidOfLatestMessage()
    '''
def retrieveArchivingPreferences():
    '''public MamPrefsResult retrieveArchivingPreferences()
    '''
def updateArchivingPreferences():
    '''public MamPrefsResult updateArchivingPreferences(final List<Jid> alwaysJids, final List<Jid> neverJids, final MamPrefsIQ.DefaultBehavior defaultBehavior)
    public MamPrefsResult updateArchivingPreferences(final MamPrefs mamPrefs)
    '''
def enableMamForAllMessages():
    '''public MamPrefsResult enableMamForAllMessages()
    '''
def enableMamForRosterMessages():
    '''public MamPrefsResult enableMamForRosterMessages()
    '''
def setDefaultBehavior():
    '''public MamPrefsResult setDefaultBehavior(final MamPrefsIQ.DefaultBehavior desiredDefaultBehavior)
    public void setDefaultBehavior(final MamPrefsIQ.DefaultBehavior defaultBehavior)
    '''
def connectionCreated():
    '''public void connectionCreated(final XMPPConnection connection)
    '''
def builder():
    '''public static Builder builder()
    '''
def Builder():
    '''public Builder()
    '''
def queryNode():
    '''public Builder queryNode(final String node)
    '''
def limitResultsToJid():
    '''public Builder limitResultsToJid(final Jid withJid)
    '''
def limitResultsSince():
    '''public Builder limitResultsSince(final Date start)
    '''
def limitResultsBefore():
    '''public Builder limitResultsBefore(final Date end)
    '''
def setResultPageSize():
    '''public Builder setResultPageSize(final Integer max)
    '''
def setResultPageSizeTo():
    '''public Builder setResultPageSizeTo(final int max)
    '''
def onlyReturnMessageCount():
    '''public Builder onlyReturnMessageCount()
    '''
def withAdditionalFormField():
    '''public Builder withAdditionalFormField(final FormField formField)
    '''
def withAdditionalFormFields():
    '''public Builder withAdditionalFormFields(final List<FormField> additionalFields)
    '''
def afterUid():
    '''public Builder afterUid(final String afterUid)
    '''
def beforeUid():
    '''public Builder beforeUid(final String beforeUid)
    '''
def queryLastPage():
    '''public Builder queryLastPage()
    '''
def build():
    '''public MamQueryArgs build()
    '''
def isComplete():
    '''public boolean isComplete()
    '''
def getMessages():
    '''public List<Message> getMessages()
    public List<Message> getMessages()
    '''
def getMessageCount():
    '''public int getMessageCount()
    '''
def getPage():
    '''public MamQueryPage getPage()
    '''
def getForwarded():
    '''public List<Forwarded> getForwarded()
    '''
def getMamResultCarrierMessages():
    '''public List<Message> getMamResultCarrierMessages()
    '''
def getMamFinIq():
    '''public MamFinIQ getMamFinIq()
    '''
def asMamPrefs():
    '''public MamPrefs asMamPrefs()
    '''
def getAlwaysJids():
    '''public List<Jid> getAlwaysJids()
    '''
def getNeverJids():
    '''public List<Jid> getNeverJids()
    '''
