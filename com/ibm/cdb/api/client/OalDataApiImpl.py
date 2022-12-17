INDENT_DEFAULT = "int  4"
EXPORT_DEFAULT = "boolean  false"
AUTOFILL_DEFAULT = "boolean  false"
def getConnection():
    '''returns OalApiConnection\n\n
    getConnection()\n
    '''
def getSession():
    '''returns ApiSession\n\n
    getSession()\n
    '''
def release():
    '''returns None\n\n
    release()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getSessionId():
    '''returns String\n\n
    getSessionId()\n
    '''
def find():
    '''returns ModelObject\n\n
    find(final String query, final int depth, final Guid mss, final String[] permissions)\n
    find(final Guid guid, final int depth, final String[] permissions)\n
    '''
def findXML():
    '''returns String\n\n
    findXML(final String query, final int depth, final int indent, final Guid mss, final String[] permissions)\n
    findXML(final String query, final int depth, final int indent, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions, final String suppressList, final OutputStream out)\n
    findXML(final String query, final int depth, final int indent, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions, final String suppressList, final String outFile, final long maxFileSize)\n
    findXML(final Guid guid, final int depth, final int indent, final String[] permissions)\n
    '''
def findJDO():
    '''returns ModelObject[]\n\n
    findJDO(final String root, final String jdoQuery, final String jdoVarDecl, final int depth, final Guid mss, final String[] permissions)\n
    '''
def join():
    '''returns ModelObject[]\n\n
    join(final String query, final int depth, final Guid mss, final String[] permissions)\n
    '''
def executeQuery():
    '''returns DataResultSet\n\n
    executeQuery(final String query, final Guid mss, final String[] permissions)\n
    '''
def getMetaData():
    '''returns ObjectClass\n\n
    getMetaData(final String className)\n
    getMetaData(final String className, final Locale locale)\n
    getMetaData(final String className, final boolean flatten)\n
    getMetaData(final String className, final boolean flatten, final Locale locale)\n
    '''
def getAllMetaData():
    '''returns ObjectClass[]\n\n
    getAllMetaData()\n
    getAllMetaData(final Locale locale)\n
    getAllMetaData(final boolean flatten)\n
    getAllMetaData(final boolean flatten, final Locale locale)\n
    '''
def getClassNames():
    '''returns String[]\n\n
    getClassNames()\n
    '''
def update():
    '''returns Guid\n\n
    update(final ModelObject obj, final Guid mss)\n
    update(final ModelObject[] objs, final Guid mss)\n
    update(final ModelObject obj, final Guid mss, final String bidiFormat, final int bidiFlag)\n
    update(final ModelObject[] objs, final Guid mss, final BidiProfile[] profile, final int[] bidiFlag)\n
    update(final ModelObject[] objs, final Guid mss, final String[] bidiFormat, final int[] bidiFlag)\n
    update(final ModelObject obj, final Guid mss, final BidiProfile profile, final int bidiFlag)\n
    '''
def updateMerge():
    '''returns LinkedHashMap\n\n
    updateMerge(final ModelObject[] objs, final Guid mss)\n
    '''
def updateXML():
    '''returns Guid[]\n\n
    updateXML(final String xml, final Guid mss)\n
    '''
def add():
    '''returns Guid[]\n\n
    add(final ModelObject[] objs, final Guid mss)\n
    '''
def delete():
    '''returns int\n\n
    delete(final Guid[] guids, final Guid mss)\n
    delete(final ModelObject[] objs, final Guid mss)\n
    '''
def findChanges():
    '''returns ModelObject[]\n\n
    findChanges(final String query, final int depth, final long start, final long end, final int changeType)\n
    '''
def findChangesInXml():
    '''returns String\n\n
    findChangesInXml(final String query, final int depth, final long start, final long end, final int changeType)\n
    '''
def getChangeHistory():
    '''returns ChangeHistory[]\n\n
    getChangeHistory(final Guid[] Guids, final long start, final long end)\n
    getChangeHistory(final Guid[] Guids, final long start, final long end, final int offset, final int nextBatch)\n
    getChangeHistory(final Guid Guid, final long start, final long end)\n
    getChangeHistory(final Guid[] Guids, final long start, final long end, final int filterType)\n
    '''
def getNumberOfChanges():
    '''returns int\n\n
    getNumberOfChanges(final Guid[] Guids, final long start, final long end)\n
    '''
def getChangeHistoryFlat():
    '''returns ChangeHistory[]\n\n
    getChangeHistoryFlat(final Guid[] Guids, final long start, final long end)\n
    getChangeHistoryFlat(final Guid Guid, final long start, final long end)\n
    getChangeHistoryFlat(final Guid[] Guids, final long start, final long end, final int filterType)\n
    '''
def getPropagatedChanges():
    '''returns ChangeHistory[]\n\n
    getPropagatedChanges(final long primaryKey)\n
    '''
def getChangeHistoryInXML():
    '''returns String\n\n
    getChangeHistoryInXML(final Guid[] Guids, final long start, final long end)\n
    getChangeHistoryInXML(final Guid Guid, final long start, final long end)\n
    getChangeHistoryInXML(final Guid[] Guids, final long start, final long end, final int filterType)\n
    '''
def getChangeHistoryFlatInXML():
    '''returns String\n\n
    getChangeHistoryFlatInXML(final Guid[] Guids, final long start, final long end)\n
    getChangeHistoryFlatInXML(final Guid Guid, final long start, final long end)\n
    getChangeHistoryFlatInXML(final Guid[] Guids, final long start, final long end, final int filterType)\n
    '''
def getPropagatedChangesInXML():
    '''returns String\n\n
    getPropagatedChangesInXML(final long primaryKey)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def addArrayElements():
    '''returns None\n\n
    addArrayElements(final Guid object, final String attrName, final Guid[] elements, final Guid mss)\n
    '''
def removeArrayElements():
    '''returns None\n\n
    removeArrayElements(final Guid object, final String attrName, final Guid[] elements, final Guid mss)\n
    '''
def importData():
    '''returns None\n\n
    importData(final URI source, final boolean rebuildTopo, final Guid mss)\n
    '''
def exportData():
    '''returns None\n\n
    exportData(final File directoryToWriteTo, final long maxFileSize, final Guid mss)\n
    '''
def beginTransaction():
    '''returns None\n\n
    beginTransaction(final int timeout)\n
    beginTransaction()\n
    '''
def commitTransaction():
    '''returns None\n\n
    commitTransaction()\n
    '''
def rollback():
    '''returns None\n\n
    rollback()\n
    '''
def defineExtendedAttributeMeta():
    '''returns None\n\n
    defineExtendedAttributeMeta(final UserDataMeta udm)\n
    '''
def getExtendedAttributeMeta():
    '''returns UserDataMeta[]\n\n
    getExtendedAttributeMeta(final String classname)\n
    '''
def setExtendedAttributes():
    '''returns None\n\n
    setExtendedAttributes(final Guid objGuid, final AttrNameValue[] attrNameVal)\n
    '''
def getExtendedAttributes():
    '''returns AttrNameValue[]\n\n
    getExtendedAttributes(final Guid objGuid)\n
    '''
def removeExtendedAttributeMeta():
    '''returns None\n\n
    removeExtendedAttributeMeta(final String classname, final Guid acct)\n
    '''
def getDomain():
    '''returns CMDBDomain\n\n
    getDomain(final Guid guid)\n
    '''
def isECMDB():
    '''returns boolean\n\n
    isECMDB()\n
    '''
def getResultMetaData():
    '''returns ResultMetaData\n\n
    getResultMetaData(final String className, final String[] attribs)\n
    '''
def getEDM():
    '''returns EDMInterface\n\n
    getEDM()\n
    '''
def getChangedClasses():
    '''returns String[]\n\n
    getChangedClasses(final long start, final long end, final int changeType)\n
    '''
def getInventorySummary():
    '''returns String\n\n
    getInventorySummary(final boolean cached, final String fileName)\n
    '''
def getAttributesWithReplacementValues():
    '''returns String[]\n\n
    getAttributesWithReplacementValues(final String fqModelObjectClass)\n
    '''
def getReplacementValues():
    '''returns String[]\n\n
    getReplacementValues(final String fqModelObjectClass, final String attribute)\n
    '''
def generateExplicitRelationships():
    '''returns None\n\n
    generateExplicitRelationships()\n
    '''
def getAttrPrioClassMeta():
    '''returns String\n\n
    getAttrPrioClassMeta()\n
    '''
def getDataSources():
    '''returns ArrayList\n\n
    getDataSources()\n
    '''
def setDataSources():
    '''returns Guid[]\n\n
    setDataSources(final ArrayList dataSources)\n
    '''
def removeDataSources():
    '''returns None\n\n
    removeDataSources(final ArrayList dataSources)\n
    '''
def getPriorityRules():
    '''returns ArrayList\n\n
    getPriorityRules()\n
    '''
def setPriorityRules():
    '''returns Guid[]\n\n
    setPriorityRules(final ArrayList priorityRules)\n
    '''
def removePriorityRules():
    '''returns None\n\n
    removePriorityRules(final ArrayList priorityRules)\n
    '''
def mergeObjects():
    '''returns int\n\n
    mergeObjects(final Guid durableGuid, final Guid transientGuid, final int mergeType)\n
    '''
def assignMssToDataSource():
    '''returns boolean\n\n
    assignMssToDataSource(final Guid mssGuid, final AttributePrioDataSources apds)\n
    '''
def validateBidiFormat():
    '''returns boolean\n\n
    validateBidiFormat(final String bFormat)\n
    '''
def createBidiProfile():
    '''returns BidiProfile\n\n
    createBidiProfile(final String name, final String desc, final String format)\n
    '''
