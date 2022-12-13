INDENT_DEFAULT = "int  4"
EXPORT_DEFAULT = "boolean  false"
AUTOFILL_DEFAULT = "boolean  false"
def getConnection():
    '''    public OalApiConnection getConnection()
    '''
def getSession():
    '''    public ApiSession getSession()
    '''
def release():
    '''    public void release()
    '''
def close():
    '''    public void close()
    '''
def getSessionId():
    '''    public String getSessionId()
    '''
def find():
    '''    public ModelObject[] find(final String query, final int depth, final Guid mss, final String[] permissions)
    public ModelObject find(final Guid guid, final int depth, final String[] permissions)
    '''
def findXML():
    '''    public String findXML(final String query, final int depth, final int indent, final Guid mss, final String[] permissions)
    public void findXML(final String query, final int depth, final int indent, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions, final String suppressList, final OutputStream out)
    public String findXML(final String query, final int depth, final int indent, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions, final String suppressList, final String outFile, final long maxFileSize)
    public String findXML(final Guid guid, final int depth, final int indent, final String[] permissions)
    '''
def findJDO():
    '''    public ModelObject[] findJDO(final String root, final String jdoQuery, final String jdoVarDecl, final int depth, final Guid mss, final String[] permissions)
    '''
def join():
    '''    public ModelObject[] join(final String query, final int depth, final Guid mss, final String[] permissions)
    '''
def executeQuery():
    '''    public DataResultSet executeQuery(final String query, final Guid mss, final String[] permissions)
    '''
def getMetaData():
    '''    public ObjectClass getMetaData(final String className)
    public ObjectClass getMetaData(final String className, final Locale locale)
    public ObjectClass getMetaData(final String className, final boolean flatten)
    public ObjectClass getMetaData(final String className, final boolean flatten, final Locale locale)
    '''
def getAllMetaData():
    '''    public ObjectClass[] getAllMetaData()
    public ObjectClass[] getAllMetaData(final Locale locale)
    public ObjectClass[] getAllMetaData(final boolean flatten)
    public ObjectClass[] getAllMetaData(final boolean flatten, final Locale locale)
    '''
def getClassNames():
    '''    public String[] getClassNames()
    '''
def update():
    '''    public Guid update(final ModelObject obj, final Guid mss)
    public Guid[] update(final ModelObject[] objs, final Guid mss)
    public Guid update(final ModelObject obj, final Guid mss, final String bidiFormat, final int bidiFlag)
    public Guid[] update(final ModelObject[] objs, final Guid mss, final BidiProfile[] profile, final int[] bidiFlag)
    public Guid[] update(final ModelObject[] objs, final Guid mss, final String[] bidiFormat, final int[] bidiFlag)
    public Guid update(final ModelObject obj, final Guid mss, final BidiProfile profile, final int bidiFlag)
    '''
def updateMerge():
    '''    public LinkedHashMap updateMerge(final ModelObject[] objs, final Guid mss)
    '''
def updateXML():
    '''    public Guid[] updateXML(final String xml, final Guid mss)
    '''
def add():
    '''    public Guid[] add(final ModelObject[] objs, final Guid mss)
    '''
def delete():
    '''    public int delete(final Guid[] guids, final Guid mss)
    public int delete(final ModelObject[] objs, final Guid mss)
    '''
def findChanges():
    '''    public ModelObject[] findChanges(final String query, final int depth, final long start, final long end, final int changeType)
    '''
def findChangesInXml():
    '''    public String findChangesInXml(final String query, final int depth, final long start, final long end, final int changeType)
    '''
def getChangeHistory():
    '''    public ChangeHistory[] getChangeHistory(final Guid[] Guids, final long start, final long end)
    public ChangeHistory[] getChangeHistory(final Guid[] Guids, final long start, final long end, final int offset, final int nextBatch)
    public ChangeHistory[] getChangeHistory(final Guid Guid, final long start, final long end)
    public ChangeHistory[] getChangeHistory(final Guid[] Guids, final long start, final long end, final int filterType)
    '''
def getNumberOfChanges():
    '''    public int getNumberOfChanges(final Guid[] Guids, final long start, final long end)
    '''
def getChangeHistoryFlat():
    '''    public ChangeHistory[] getChangeHistoryFlat(final Guid[] Guids, final long start, final long end)
    public ChangeHistory[] getChangeHistoryFlat(final Guid Guid, final long start, final long end)
    public ChangeHistory[] getChangeHistoryFlat(final Guid[] Guids, final long start, final long end, final int filterType)
    '''
def getPropagatedChanges():
    '''    public ChangeHistory[] getPropagatedChanges(final long primaryKey)
    '''
def getChangeHistoryInXML():
    '''    public String getChangeHistoryInXML(final Guid[] Guids, final long start, final long end)
    public String getChangeHistoryInXML(final Guid Guid, final long start, final long end)
    public String getChangeHistoryInXML(final Guid[] Guids, final long start, final long end, final int filterType)
    '''
def getChangeHistoryFlatInXML():
    '''    public String getChangeHistoryFlatInXML(final Guid[] Guids, final long start, final long end)
    public String getChangeHistoryFlatInXML(final Guid Guid, final long start, final long end)
    public String getChangeHistoryFlatInXML(final Guid[] Guids, final long start, final long end, final int filterType)
    '''
def getPropagatedChangesInXML():
    '''    public String getPropagatedChangesInXML(final long primaryKey)
    '''
def toString():
    '''    public String toString()
    '''
def addArrayElements():
    '''    public void addArrayElements(final Guid object, final String attrName, final Guid[] elements, final Guid mss)
    '''
def removeArrayElements():
    '''    public void removeArrayElements(final Guid object, final String attrName, final Guid[] elements, final Guid mss)
    '''
def importData():
    '''    public void importData(final URI source, final boolean rebuildTopo, final Guid mss)
    '''
def exportData():
    '''    public void exportData(final File directoryToWriteTo, final long maxFileSize, final Guid mss)
    '''
def beginTransaction():
    '''    public void beginTransaction(final int timeout)
    public void beginTransaction()
    '''
def commitTransaction():
    '''    public void commitTransaction()
    '''
def rollback():
    '''    public void rollback()
    '''
def defineExtendedAttributeMeta():
    '''    public void defineExtendedAttributeMeta(final UserDataMeta udm)
    '''
def getExtendedAttributeMeta():
    '''    public UserDataMeta[] getExtendedAttributeMeta(final String classname)
    '''
def setExtendedAttributes():
    '''    public void setExtendedAttributes(final Guid objGuid, final AttrNameValue[] attrNameVal)
    '''
def getExtendedAttributes():
    '''    public AttrNameValue[] getExtendedAttributes(final Guid objGuid)
    '''
def removeExtendedAttributeMeta():
    '''    public void removeExtendedAttributeMeta(final String classname, final Guid acct)
    '''
def getDomain():
    '''    public CMDBDomain getDomain(final Guid guid)
    '''
def isECMDB():
    '''    public boolean isECMDB()
    '''
def getResultMetaData():
    '''    public ResultMetaData getResultMetaData(final String className, final String[] attribs)
    '''
def getEDM():
    '''    public EDMInterface getEDM()
    '''
def getChangedClasses():
    '''    public String[] getChangedClasses(final long start, final long end, final int changeType)
    '''
def getInventorySummary():
    '''    public String getInventorySummary(final boolean cached, final String fileName)
    '''
def getAttributesWithReplacementValues():
    '''    public String[] getAttributesWithReplacementValues(final String fqModelObjectClass)
    '''
def getReplacementValues():
    '''    public String[] getReplacementValues(final String fqModelObjectClass, final String attribute)
    '''
def generateExplicitRelationships():
    '''    public void generateExplicitRelationships()
    '''
def getAttrPrioClassMeta():
    '''    public String getAttrPrioClassMeta()
    '''
def getDataSources():
    '''    public ArrayList getDataSources()
    '''
def setDataSources():
    '''    public Guid[] setDataSources(final ArrayList dataSources)
    '''
def removeDataSources():
    '''    public void removeDataSources(final ArrayList dataSources)
    '''
def getPriorityRules():
    '''    public ArrayList getPriorityRules()
    '''
def setPriorityRules():
    '''    public Guid[] setPriorityRules(final ArrayList priorityRules)
    '''
def removePriorityRules():
    '''    public void removePriorityRules(final ArrayList priorityRules)
    '''
def mergeObjects():
    '''    public int mergeObjects(final Guid durableGuid, final Guid transientGuid, final int mergeType)
    '''
def assignMssToDataSource():
    '''    public boolean assignMssToDataSource(final Guid mssGuid, final AttributePrioDataSources apds)
    '''
def validateBidiFormat():
    '''    public boolean validateBidiFormat(final String bFormat)
    '''
def createBidiProfile():
    '''    public BidiProfile createBidiProfile(final String name, final String desc, final String format)
    '''
