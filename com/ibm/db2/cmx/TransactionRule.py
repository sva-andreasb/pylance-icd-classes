def PenaltyBox():
    '''    public PenaltyBox(final HashMap<ClientInfo, Database> hashMap_, final boolean[] clientInfoFieldsToIgnore_)
    public PenaltyBox(final HashMap<ClientInfo, Database> hashMap_, final boolean[] clientInfoFieldsToIgnore_, final String[] substringExtractionPatternsForClientInfo_)
    public PenaltyBox(final HashMap<ClientInfo, Database> hashMap_, final boolean[] clientInfoFieldsToIgnore_, final int[][] substringExtractionPositionsForClientInfo_)
    '''
def getPenaltyBox():
    '''    public Database getPenaltyBox(final ClientInfo clientInfo)
    '''
def getFlavor():
    '''    public Flavor getFlavor()
    public Flavor getFlavor()
    '''
def getHashMap():
    '''    public HashMap<ClientInfo, Database> getHashMap()
    public HashMap<ClientInfo, ClientInfo> getHashMap()
    '''
def getClientInfoFieldsToIgnore():
    '''    public boolean[] getClientInfoFieldsToIgnore()
    '''
def getSubstringExtractionPatternsForClientInfo():
    '''    public String[] getSubstringExtractionPatternsForClientInfo()
    public String[] getSubstringExtractionPatternsForClientInfo()
    '''
def getSubstringExtractionPositionsForClientInfo():
    '''    public int[][] getSubstringExtractionPositionsForClientInfo()
    public int[][] getSubstringExtractionPositionsForClientInfo()
    '''
def incrNumberOfTimesApplied():
    '''    public void incrNumberOfTimesApplied()
    '''
def getNumberOfTransactionsThatMatchPenaltyBoxCriteria():
    '''    public long getNumberOfTransactionsThatMatchPenaltyBoxCriteria()
    '''
def resetNumberOfTimesApplied():
    '''    public void resetNumberOfTimesApplied()
    '''
def Remapping():
    '''    public Remapping(final String[] substringExtractionPatternsForClientInfo_, final String[] finalClientInfoSubstitutionPatterns_, final int[] conditionsOfSubstitution_)
    public Remapping(final int[][] substringExtractionPositionsForClientInfo_, final String[] finalClientInfoSubstitutionPatterns_)
    public Remapping(final HashMap<ClientInfo, ClientInfo> hashMap_, final boolean[] clientInfoFieldsToIgnoreInKey_)
    public Remapping(final HashMap<ClientInfo, ClientInfo> hashMap_, final boolean[] clientInfoFieldsToIgnoreInKey_, final String[] substringExtractionPatternsForClientInfo_)
    public Remapping(final HashMap<ClientInfo, ClientInfo> hashMap_, final boolean[] clientInfoFieldsToIgnoreInKey_, final int[][] substringExtractionPositionsForClientInfo_)
    public Remapping(final String[] finalClientInfoSubstitutionPatterns_, final boolean[] clientInfoFieldsToIgnoreInKey_)
    '''
def remapClientInfo():
    '''    public ClientInfo remapClientInfo(final ClientInfo clientInfo, final Object[] array)
    '''
def getFinalClientInfoSubstitutionPatterns():
    '''    public String[] getFinalClientInfoSubstitutionPatterns()
    '''
def getConditionsOfSubstitution():
    '''    public int[] getConditionsOfSubstitution()
    '''
def getClientInfoFieldsToIgnoreInKey():
    '''    public boolean[] getClientInfoFieldsToIgnoreInKey()
    '''
