def PurchView():
    '''public PurchView(final MboSet ms)
    '''
def getStatusListName():
    '''public String getStatusListName()
    '''
def init():
    '''public void init()
    '''
def add():
    '''public void add()
    '''
def copyPOLinesToCurrentContract():
    '''public void copyPOLinesToCurrentContract(final MboSetRemote sourcePOLineSet)
    '''
def copyPRLinesToCurrentContract():
    '''public void copyPRLinesToCurrentContract(final MboSetRemote sourcePRLineSet)
    '''
def copyPRLineToContract():
    '''public MboRemote copyPRLineToContract(final MboRemote sourcePRLine, final MboSetRemote contractLineSetRemote)
    '''
def duplicate():
    '''public MboRemote duplicate()
    '''
def createRelease():
    '''public MboRemote createRelease(final MboSetRemote contractLineSetRemote)
    public MboRemote createRelease(final String ponum, final MboSetRemote contractLineSetRemote)
    public MboRemote createRelease(final String ponum, final MboSetRemote contractLineSetRemote, final String siteID)
    '''
def createReleaseHeaderAndLines():
    '''public MboRemote createReleaseHeaderAndLines(final MboSetRemote contractLineSetRemote)
    public MboRemote createReleaseHeaderAndLines(final MboSetRemote contractLineSetRemote, final String siteID)
    '''
def copySelectedLinesToRelease():
    '''public void copySelectedLinesToRelease(final MboRemote releasePOHeader, final Vector selectedMbos)
    '''
def canCreateRelease():
    '''public void canCreateRelease()
    '''
def canCreateRFQ():
    '''public void canCreateRFQ()
    '''
def createPOHeader():
    '''public MboRemote createPOHeader()
    public MboRemote createPOHeader(final String siteID)
    '''
def copyPurchContractValuesToPOHeader():
    '''public void copyPurchContractValuesToPOHeader(final MboRemote poHeaderRemote)
    public void copyPurchContractValuesToPOHeader(final MboRemote poHeaderRemote, final String siteID)
    '''
def applyPriceAdjustment():
    '''public void applyPriceAdjustment(final MboSetRemote contractLineSetRemote)
    '''
def createRFQ():
    '''public MboRemote createRFQ(final MboSetRemote contractLineSetRemote)
    '''
def nullVendor():
    '''public void nullVendor()
    '''
def canChangeLineStatus():
    '''public void canChangeLineStatus()
    '''
def modify():
    '''public void modify()
    '''
def initRelationship():
    '''public void initRelationship(final String relationName, final MboSetRemote mboSet)
    '''
def getUnCommittedReleases():
    '''public double getUnCommittedReleases()
    '''
def getCommittedReleases():
    '''public double getCommittedReleases()
    '''
def getUnCommitedCost():
    '''public double getUnCommitedCost()
    '''
def getAmountOnOrder():
    '''public double getAmountOnOrder()
    '''
def getInvoiceVariance():
    '''public double getInvoiceVariance()
    '''
def getAmountReceived():
    '''public double getAmountReceived()
    '''
def canViewRelCost():
    '''public void canViewRelCost()
    '''
def createSWLic():
    '''public void createSWLic()
    '''
def deleteSWLic():
    '''public void deleteSWLic()
    '''
def canCreateSWLic():
    '''public void canCreateSWLic()
    '''
def copyPersonsToNamedUsers():
    '''public void copyPersonsToNamedUsers(final MboSetRemote personSetRemote)
    '''
def save():
    '''public void save()
    '''
def removeContractReferencesFromPR():
    '''public void removeContractReferencesFromPR()
    '''
def removeContractReferencesFromRFQ():
    '''public void removeContractReferencesFromRFQ()
    '''
def applyPriceToLines():
    '''public void applyPriceToLines()
    '''
def getPOCurrency():
    '''public void getPOCurrency(final String[] statuses)
    '''
def getSqlLineOrLoadedCost():
    '''public void getSqlLineOrLoadedCost()
    '''
