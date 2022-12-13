def PenaltyBox():
'''public PenaltyBox(final HashMap<ClientInfo, Database> hashMap_, final boolean[] clientInfoFieldsToIgnore_)
public PenaltyBox(final HashMap<ClientInfo, Database> hashMap_, final boolean[] clientInfoFieldsToIgnore_, final String[] substringExtractionPatternsForClientInfo_)
public PenaltyBox(final HashMap<ClientInfo, Database> hashMap_, final boolean[] clientInfoFieldsToIgnore_, final int[][] substringExtractionPositionsForClientInfo_)
'''
pass
def getPenaltyBox():
'''public Database getPenaltyBox(final ClientInfo clientInfo)
'''
pass
def getFlavor():
'''public Flavor getFlavor()
public Flavor getFlavor()
'''
pass
def getHashMap():
'''public HashMap<ClientInfo, Database> getHashMap()
public HashMap<ClientInfo, ClientInfo> getHashMap()
'''
pass
def getClientInfoFieldsToIgnore():
'''public boolean[] getClientInfoFieldsToIgnore()
'''
pass
def getSubstringExtractionPatternsForClientInfo():
'''public String[] getSubstringExtractionPatternsForClientInfo()
public String[] getSubstringExtractionPatternsForClientInfo()
'''
pass
def getSubstringExtractionPositionsForClientInfo():
'''public int[][] getSubstringExtractionPositionsForClientInfo()
public int[][] getSubstringExtractionPositionsForClientInfo()
'''
pass
def incrNumberOfTimesApplied():
'''public void incrNumberOfTimesApplied()
'''
pass
def getNumberOfTransactionsThatMatchPenaltyBoxCriteria():
'''public long getNumberOfTransactionsThatMatchPenaltyBoxCriteria()
'''
pass
def resetNumberOfTimesApplied():
'''public void resetNumberOfTimesApplied()
'''
pass
def Remapping():
'''public Remapping(final String[] substringExtractionPatternsForClientInfo_, final String[] finalClientInfoSubstitutionPatterns_, final int[] conditionsOfSubstitution_)
public Remapping(final int[][] substringExtractionPositionsForClientInfo_, final String[] finalClientInfoSubstitutionPatterns_)
public Remapping(final HashMap<ClientInfo, ClientInfo> hashMap_, final boolean[] clientInfoFieldsToIgnoreInKey_)
public Remapping(final HashMap<ClientInfo, ClientInfo> hashMap_, final boolean[] clientInfoFieldsToIgnoreInKey_, final String[] substringExtractionPatternsForClientInfo_)
public Remapping(final HashMap<ClientInfo, ClientInfo> hashMap_, final boolean[] clientInfoFieldsToIgnoreInKey_, final int[][] substringExtractionPositionsForClientInfo_)
public Remapping(final String[] finalClientInfoSubstitutionPatterns_, final boolean[] clientInfoFieldsToIgnoreInKey_)
'''
pass
def remapClientInfo():
'''public ClientInfo remapClientInfo(final ClientInfo clientInfo, final Object[] array)
'''
pass
def getFinalClientInfoSubstitutionPatterns():
'''public String[] getFinalClientInfoSubstitutionPatterns()
'''
pass
def getConditionsOfSubstitution():
'''public int[] getConditionsOfSubstitution()
'''
pass
def getClientInfoFieldsToIgnoreInKey():
'''public boolean[] getClientInfoFieldsToIgnoreInKey()
'''
pass
