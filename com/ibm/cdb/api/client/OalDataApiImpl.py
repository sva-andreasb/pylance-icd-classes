INDENT_DEFAULT = "int  4"
EXPORT_DEFAULT = "boolean  false"
AUTOFILL_DEFAULT = "boolean  false"
def getConnection():
'''public OalApiConnection getConnection()
'''
pass
def getSession():
'''public ApiSession getSession()
'''
pass
def release():
'''public void release()
'''
pass
def close():
'''public void close()
'''
pass
def getSessionId():
'''public String getSessionId()
'''
pass
def find():
'''public ModelObject[] find(final String query, final int depth, final Guid mss, final String[] permissions)
public ModelObject find(final Guid guid, final int depth, final String[] permissions)
'''
pass
def findXML():
'''public String findXML(final String query, final int depth, final int indent, final Guid mss, final String[] permissions)
public void findXML(final String query, final int depth, final int indent, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions, final String suppressList, final OutputStream out)
public String findXML(final String query, final int depth, final int indent, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions, final String suppressList, final String outFile, final long maxFileSize)
public String findXML(final Guid guid, final int depth, final int indent, final String[] permissions)
'''
pass
def findJDO():
'''public ModelObject[] findJDO(final String root, final String jdoQuery, final String jdoVarDecl, final int depth, final Guid mss, final String[] permissions)
'''
pass
def join():
'''public ModelObject[] join(final String query, final int depth, final Guid mss, final String[] permissions)
'''
pass
def executeQuery():
'''public DataResultSet executeQuery(final String query, final Guid mss, final String[] permissions)
'''
pass
def getMetaData():
'''public ObjectClass getMetaData(final String className)
public ObjectClass getMetaData(final String className, final Locale locale)
public ObjectClass getMetaData(final String className, final boolean flatten)
public ObjectClass getMetaData(final String className, final boolean flatten, final Locale locale)
'''
pass
def getAllMetaData():
'''public ObjectClass[] getAllMetaData()
public ObjectClass[] getAllMetaData(final Locale locale)
public ObjectClass[] getAllMetaData(final boolean flatten)
public ObjectClass[] getAllMetaData(final boolean flatten, final Locale locale)
'''
pass
def getClassNames():
'''public String[] getClassNames()
'''
pass
def update():
'''public Guid update(final ModelObject obj, final Guid mss)
public Guid[] update(final ModelObject[] objs, final Guid mss)
public Guid update(final ModelObject obj, final Guid mss, final String bidiFormat, final int bidiFlag)
public Guid[] update(final ModelObject[] objs, final Guid mss, final BidiProfile[] profile, final int[] bidiFlag)
public Guid[] update(final ModelObject[] objs, final Guid mss, final String[] bidiFormat, final int[] bidiFlag)
public Guid update(final ModelObject obj, final Guid mss, final BidiProfile profile, final int bidiFlag)
'''
pass
def updateMerge():
'''public LinkedHashMap updateMerge(final ModelObject[] objs, final Guid mss)
'''
pass
def updateXML():
'''public Guid[] updateXML(final String xml, final Guid mss)
'''
pass
def add():
'''public Guid[] add(final ModelObject[] objs, final Guid mss)
'''
pass
def delete():
'''public int delete(final Guid[] guids, final Guid mss)
public int delete(final ModelObject[] objs, final Guid mss)
'''
pass
def findChanges():
'''public ModelObject[] findChanges(final String query, final int depth, final long start, final long end, final int changeType)
'''
pass
def findChangesInXml():
'''public String findChangesInXml(final String query, final int depth, final long start, final long end, final int changeType)
'''
pass
def getChangeHistory():
'''public ChangeHistory[] getChangeHistory(final Guid[] Guids, final long start, final long end)
public ChangeHistory[] getChangeHistory(final Guid[] Guids, final long start, final long end, final int offset, final int nextBatch)
public ChangeHistory[] getChangeHistory(final Guid Guid, final long start, final long end)
public ChangeHistory[] getChangeHistory(final Guid[] Guids, final long start, final long end, final int filterType)
'''
pass
def getNumberOfChanges():
'''public int getNumberOfChanges(final Guid[] Guids, final long start, final long end)
'''
pass
def getChangeHistoryFlat():
'''public ChangeHistory[] getChangeHistoryFlat(final Guid[] Guids, final long start, final long end)
public ChangeHistory[] getChangeHistoryFlat(final Guid Guid, final long start, final long end)
public ChangeHistory[] getChangeHistoryFlat(final Guid[] Guids, final long start, final long end, final int filterType)
'''
pass
def getPropagatedChanges():
'''public ChangeHistory[] getPropagatedChanges(final long primaryKey)
'''
pass
def getChangeHistoryInXML():
'''public String getChangeHistoryInXML(final Guid[] Guids, final long start, final long end)
public String getChangeHistoryInXML(final Guid Guid, final long start, final long end)
public String getChangeHistoryInXML(final Guid[] Guids, final long start, final long end, final int filterType)
'''
pass
def getChangeHistoryFlatInXML():
'''public String getChangeHistoryFlatInXML(final Guid[] Guids, final long start, final long end)
public String getChangeHistoryFlatInXML(final Guid Guid, final long start, final long end)
public String getChangeHistoryFlatInXML(final Guid[] Guids, final long start, final long end, final int filterType)
'''
pass
def getPropagatedChangesInXML():
'''public String getPropagatedChangesInXML(final long primaryKey)
'''
pass
def toString():
'''public String toString()
'''
pass
def addArrayElements():
'''public void addArrayElements(final Guid object, final String attrName, final Guid[] elements, final Guid mss)
'''
pass
def removeArrayElements():
'''public void removeArrayElements(final Guid object, final String attrName, final Guid[] elements, final Guid mss)
'''
pass
def importData():
'''public void importData(final URI source, final boolean rebuildTopo, final Guid mss)
'''
pass
def exportData():
'''public void exportData(final File directoryToWriteTo, final long maxFileSize, final Guid mss)
'''
pass
def beginTransaction():
'''public void beginTransaction(final int timeout)
public void beginTransaction()
'''
pass
def commitTransaction():
'''public void commitTransaction()
'''
pass
def rollback():
'''public void rollback()
'''
pass
def defineExtendedAttributeMeta():
'''public void defineExtendedAttributeMeta(final UserDataMeta udm)
'''
pass
def getExtendedAttributeMeta():
'''public UserDataMeta[] getExtendedAttributeMeta(final String classname)
'''
pass
def setExtendedAttributes():
'''public void setExtendedAttributes(final Guid objGuid, final AttrNameValue[] attrNameVal)
'''
pass
def getExtendedAttributes():
'''public AttrNameValue[] getExtendedAttributes(final Guid objGuid)
'''
pass
def removeExtendedAttributeMeta():
'''public void removeExtendedAttributeMeta(final String classname, final Guid acct)
'''
pass
def getDomain():
'''public CMDBDomain getDomain(final Guid guid)
'''
pass
def isECMDB():
'''public boolean isECMDB()
'''
pass
def getResultMetaData():
'''public ResultMetaData getResultMetaData(final String className, final String[] attribs)
'''
pass
def getEDM():
'''public EDMInterface getEDM()
'''
pass
def getChangedClasses():
'''public String[] getChangedClasses(final long start, final long end, final int changeType)
'''
pass
def getInventorySummary():
'''public String getInventorySummary(final boolean cached, final String fileName)
'''
pass
def getAttributesWithReplacementValues():
'''public String[] getAttributesWithReplacementValues(final String fqModelObjectClass)
'''
pass
def getReplacementValues():
'''public String[] getReplacementValues(final String fqModelObjectClass, final String attribute)
'''
pass
def generateExplicitRelationships():
'''public void generateExplicitRelationships()
'''
pass
def getAttrPrioClassMeta():
'''public String getAttrPrioClassMeta()
'''
pass
def getDataSources():
'''public ArrayList getDataSources()
'''
pass
def setDataSources():
'''public Guid[] setDataSources(final ArrayList dataSources)
'''
pass
def removeDataSources():
'''public void removeDataSources(final ArrayList dataSources)
'''
pass
def getPriorityRules():
'''public ArrayList getPriorityRules()
'''
pass
def setPriorityRules():
'''public Guid[] setPriorityRules(final ArrayList priorityRules)
'''
pass
def removePriorityRules():
'''public void removePriorityRules(final ArrayList priorityRules)
'''
pass
def mergeObjects():
'''public int mergeObjects(final Guid durableGuid, final Guid transientGuid, final int mergeType)
'''
pass
def assignMssToDataSource():
'''public boolean assignMssToDataSource(final Guid mssGuid, final AttributePrioDataSources apds)
'''
pass
def validateBidiFormat():
'''public boolean validateBidiFormat(final String bFormat)
'''
pass
def createBidiProfile():
'''public BidiProfile createBidiProfile(final String name, final String desc, final String format)
'''
pass
