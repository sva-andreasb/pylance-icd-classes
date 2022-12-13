def ClusterDescriptionImpl():
    '''public ClusterDescriptionImpl(final DescriptionKey key)
    '''
def getDefinitionKey():
    '''public String getDefinitionKey()
    '''
def setStructuralEpoch():
    '''public synchronized void setStructuralEpoch(final long epoch)
    '''
def setClusterScopedData():
    '''public void setClusterScopedData(final DescriptionKey dataKey, final byte[] data)
    '''
def setClusterWeightTable():
    '''public void setClusterWeightTable(final Map weightTable)
    '''
def setClusterWeightTableEntry():
    '''public void setClusterWeightTableEntry(final DescriptionKey memberKey, final Integer weight)
    '''
def setClusterIdentityForWeightTable():
    '''public void setClusterIdentityForWeightTable(final Identity parentClusterIdentity)
    '''
def removeClusterScopedData():
    '''public void removeClusterScopedData(final DescriptionKey dataKey)
    '''
def setInfluentialEpoch():
    '''public synchronized void setInfluentialEpoch(final long epoch)
    '''
def addMember():
    '''public void addMember(final ClusterMemberDescription member)
    public void addMember(final ClusterMemberDescription member, final int delay)
    '''
def removeMember():
    '''public void removeMember(final ClusterMemberDescription member)
    public void removeMember(final ClusterMemberDescription member, final int delay)
    '''
def setSelectionDescription():
    '''public synchronized void setSelectionDescription(final SelectionDescription selection)
    '''
def setBackupCluster():
    '''public synchronized void setBackupCluster(final ClusterDescription backupCluster)
    '''
def exportToStream():
    '''public synchronized void exportToStream(final DataOutput out, final Format format)
    '''
def handleNotification():
    '''public void handleNotification(final DescriptionKey key, final String type, final Object data, final Object handback)
    '''
def toString():
    '''public String toString()
    public String toString()
    '''
def setMemento():
    '''public void setMemento(final Description.Memento memento)
    '''
def setQuiesce():
    '''public void setQuiesce(final Identity member)
    '''
def unsetQuiesce():
    '''public void unsetQuiesce(final Identity member)
    '''
def getWeightTableKey():
    '''public static DescriptionKey getWeightTableKey(final DescriptionKey cluster)
    '''
def getStructuralEpoch():
    '''public long getStructuralEpoch()
    '''
def getClusterMembers():
    '''public Iterator getClusterMembers()
    '''
def getMembers():
    '''public Map getMembers()
    '''
def getMemberEntrySet():
    '''public Set getMemberEntrySet()
    '''
def getWeightTable():
    '''public Map getWeightTable()
    '''
def getWeightTableEntry():
    '''public int getWeightTableEntry(final DescriptionKey memberKey)
    '''
def getBackupCluster():
    '''public ClusterDescription getBackupCluster()
    '''
def getSelectionDescription():
    '''public SelectionDescription getSelectionDescription()
    '''
def getInfluentialEpoch():
    '''public long getInfluentialEpoch()
    '''
def getClusterScopedData():
    '''public byte[] getClusterScopedData(final DescriptionKey dataKey)
    public Set getClusterScopedData()
    '''
def isQuiesced():
    '''public boolean isQuiesced(final Identity member)
    '''
def getQuiesceState():
    '''public Map getQuiesceState()
    '''
def getState():
    '''public byte getState()
    '''
def isLeaf():
    '''public boolean isLeaf()
    '''
