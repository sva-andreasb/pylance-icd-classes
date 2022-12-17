def ():
    '''returns DataWorker\n\n
    (final TopologyManagerFactory topologyManagerFactory, final ApiProps props)\n
    '''
def findXML():
    '''returns String\n\n
    findXML(final ApiServerBean apiServer, final String sessionId, final Guid object_id, final int depth, final int indent, final Guid mss, final String[] permissions)\n
    findXML(final ApiServerBean apiServer, final String sessionId, final Guid[] objectIds, final int depth, final int indent, final Guid mss, final String[] permissions)\n
    '''
def findInitXML():
    '''returns None\n\n
    findInitXML(final ApiServerBean apiServer, final String sessionId, final String query, final Guid[] guids, final int depth, final int fetch_size, final int indent, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions, final String suppressList)\n
    '''
def nextXML():
    '''returns String\n\n
    nextXML(final String sessionId)\n
    '''
def findInitCursor():
    '''returns String\n\n
    findInitCursor(final ApiServerBean apiServer, final String sessionId, final String query, final Guid mss, final String[] permissions)\n
    '''
def findInitData():
    '''returns None\n\n
    findInitData(final ApiServerBean apiServer, final String sessionId, final String query, final Guid[] guids, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions)\n
    '''
def nextDataCursor():
    '''returns ModelObject[]\n\n
    nextDataCursor(final String sessionId, final String cursorId, final int start, final int size, final int depth)\n
    '''
def cursorSize():
    '''returns int\n\n
    cursorSize(final String sessionId, final String cursorId)\n
    '''
def closeCursor():
    '''returns None\n\n
    closeCursor(final String sessionId, final String cursorId)\n
    '''
def nextDataResult():
    '''returns ModelObject[]\n\n
    nextDataResult(final String sessionId, final int start, final int size, final int depth)\n
    '''
def insert():
    '''returns Guid[]\n\n
    insert(final ApiServerBean bean, final String sessionId, final String xml, final boolean isImport, final Guid mss, final BulkloadInterface bulkloadInterface)\n
    '''
def add():
    '''returns Guid[]\n\n
    add(final ApiServerBean bean, final String sessionId, final ModelObject[] objs, final Guid mss, final BulkloadInterface bulkloadInterface)\n
    '''
def update():
    '''returns Guid[]\n\n
    update(final ApiServerBean bean, final String sessionId, final ModelObject[] objs, final Guid mss, final BulkloadInterface bulkloadInterface)\n
    '''
def deleteById():
    '''returns int\n\n
    deleteById(final ApiServerBean apiServer, final String sessionId, final Guid objectId, final Guid mss, final BulkloadInterface bulkloadInterface)\n
    '''
def deleteMssObjLink():
    '''returns None\n\n
    deleteMssObjLink(final ApiServerBean apiServer, final String sessionId, final Guid objGuid, final Guid mssGuid)\n
    '''
def getAttributesWithReplacementValues():
    '''returns String[]\n\n
    getAttributesWithReplacementValues(final ApiServerBean apiServer, final String session_id, final String fqModelObjectClass)\n
    '''
def getReplacementValues():
    '''returns String[]\n\n
    getReplacementValues(final ApiServerBean bean, final String session_id, final String fqModelObjectClass, final String attribute)\n
    '''
def find():
    '''returns ModelObject[]\n\n
    find(final ApiServerBean apiServer, final String sessionId, final Guid[] guids, final String query, final int depth, final String jdoQuery, final String jdoVardecl, final Guid mss, final String[] permissions)\n
    '''
def evaluateGuids():
    '''returns List\n\n
    evaluateGuids(final String sessionId, final ModelObject mo)\n
    '''
def getGuidAliases():
    '''returns List\n\n
    getGuidAliases(final ApiServerBean apiServer, final String sessionId, final Guid guid)\n
    '''
def updateMerge():
    '''returns LinkedHashMap\n\n
    updateMerge(final ApiServerBean bean, final String sessionId, final ModelObject[] objs, final Guid mss, final BulkloadInterface bulkloadInterface)\n
    '''
def getAttrPrioClassMeta():
    '''returns String\n\n
    getAttrPrioClassMeta()\n
    '''
def getShortName():
    '''returns String\n\n
    getShortName(final String className)\n
    '''
def getDataSources():
    '''returns ArrayList\n\n
    getDataSources(final ApiServerBean bean, final String sessionId)\n
    '''
def setDataSources():
    '''returns Guid[]\n\n
    setDataSources(final ApiServerBean bean, final String sessionId, final ArrayList dataSources)\n
    '''
def removeDataSources():
    '''returns None\n\n
    removeDataSources(final ApiServerBean bean, final String sessionId, final ArrayList dataSources)\n
    '''
def getPriorityRules():
    '''returns ArrayList\n\n
    getPriorityRules(final ApiServerBean bean, final String sessionId)\n
    '''
def setPriorityRules():
    '''returns Guid[]\n\n
    setPriorityRules(final ApiServerBean bean, final String sessionId, final ArrayList priorityRules)\n
    '''
def removePriorityRules():
    '''returns None\n\n
    removePriorityRules(final ApiServerBean bean, final String sessionId, final ArrayList priorityRules)\n
    '''
def mergeObjects():
    '''returns int\n\n
    mergeObjects(final ApiServerBean bean, final String sessionId, final Guid durableGuid, final Guid transientGuid, final int mergeType)\n
    '''
def assignMssToDataSource():
    '''returns boolean\n\n
    assignMssToDataSource(final ApiServerBean bean, final String sessionId, final Guid mssGuid, final AttributePrioDataSources apds)\n
    '''
