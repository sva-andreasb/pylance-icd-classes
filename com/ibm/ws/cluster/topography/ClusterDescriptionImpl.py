def ClusterDescriptionImpl():
'''public ClusterDescriptionImpl(final DescriptionKey key)
'''
pass
def getDefinitionKey():
'''public String getDefinitionKey()
'''
pass
def setStructuralEpoch():
'''public synchronized void setStructuralEpoch(final long epoch)
'''
pass
def setClusterScopedData():
'''public void setClusterScopedData(final DescriptionKey dataKey, final byte[] data)
'''
pass
def setClusterWeightTable():
'''public void setClusterWeightTable(final Map weightTable)
'''
pass
def setClusterWeightTableEntry():
'''public void setClusterWeightTableEntry(final DescriptionKey memberKey, final Integer weight)
'''
pass
def setClusterIdentityForWeightTable():
'''public void setClusterIdentityForWeightTable(final Identity parentClusterIdentity)
'''
pass
def removeClusterScopedData():
'''public void removeClusterScopedData(final DescriptionKey dataKey)
'''
pass
def setInfluentialEpoch():
'''public synchronized void setInfluentialEpoch(final long epoch)
'''
pass
def addMember():
'''public void addMember(final ClusterMemberDescription member)
public void addMember(final ClusterMemberDescription member, final int delay)
'''
pass
def removeMember():
'''public void removeMember(final ClusterMemberDescription member)
public void removeMember(final ClusterMemberDescription member, final int delay)
'''
pass
def setSelectionDescription():
'''public synchronized void setSelectionDescription(final SelectionDescription selection)
'''
pass
def setBackupCluster():
'''public synchronized void setBackupCluster(final ClusterDescription backupCluster)
'''
pass
def exportToStream():
'''public synchronized void exportToStream(final DataOutput out, final Format format)
'''
pass
def handleNotification():
'''public void handleNotification(final DescriptionKey key, final String type, final Object data, final Object handback)
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def setMemento():
'''public void setMemento(final Description.Memento memento)
'''
pass
def setQuiesce():
'''public void setQuiesce(final Identity member)
'''
pass
def unsetQuiesce():
'''public void unsetQuiesce(final Identity member)
'''
pass
def getWeightTableKey():
'''public static DescriptionKey getWeightTableKey(final DescriptionKey cluster)
'''
pass
def getStructuralEpoch():
'''public long getStructuralEpoch()
'''
pass
def getClusterMembers():
'''public Iterator getClusterMembers()
'''
pass
def getMembers():
'''public Map getMembers()
'''
pass
def getMemberEntrySet():
'''public Set getMemberEntrySet()
'''
pass
def getWeightTable():
'''public Map getWeightTable()
'''
pass
def getWeightTableEntry():
'''public int getWeightTableEntry(final DescriptionKey memberKey)
'''
pass
def getBackupCluster():
'''public ClusterDescription getBackupCluster()
'''
pass
def getSelectionDescription():
'''public SelectionDescription getSelectionDescription()
'''
pass
def getInfluentialEpoch():
'''public long getInfluentialEpoch()
'''
pass
def getClusterScopedData():
'''public byte[] getClusterScopedData(final DescriptionKey dataKey)
public Set getClusterScopedData()
'''
pass
def isQuiesced():
'''public boolean isQuiesced(final Identity member)
'''
pass
def getQuiesceState():
'''public Map getQuiesceState()
'''
pass
def getState():
'''public byte getState()
'''
pass
def isLeaf():
'''public boolean isLeaf()
'''
pass
