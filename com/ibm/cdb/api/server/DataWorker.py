def DataWorker():
    '''public DataWorker(final TopologyManagerFactory topologyManagerFactory, final ApiProps props)
    '''
def findXML():
    '''public String findXML(final ApiServerBean apiServer, final String sessionId, final Guid object_id, final int depth, final int indent, final Guid mss, final String[] permissions)
    public String findXML(final ApiServerBean apiServer, final String sessionId, final Guid[] objectIds, final int depth, final int indent, final Guid mss, final String[] permissions)
    '''
def findInitXML():
    '''public void findInitXML(final ApiServerBean apiServer, final String sessionId, final String query, final Guid[] guids, final int depth, final int fetch_size, final int indent, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions, final String suppressList)
    '''
def nextXML():
    '''public String nextXML(final String sessionId)
    '''
def findInitCursor():
    '''public String findInitCursor(final ApiServerBean apiServer, final String sessionId, final String query, final Guid mss, final String[] permissions)
    '''
def findInitData():
    '''public void findInitData(final ApiServerBean apiServer, final String sessionId, final String query, final Guid[] guids, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions)
    '''
def extractClassNameFromQuery():
    '''public static String extractClassNameFromQuery(String query)
    '''
def nextDataCursor():
    '''public ModelObject[] nextDataCursor(final String sessionId, final String cursorId, final int start, final int size, final int depth)
    '''
def cursorSize():
    '''public int cursorSize(final String sessionId, final String cursorId)
    '''
def closeCursor():
    '''public void closeCursor(final String sessionId, final String cursorId)
    '''
def nextDataResult():
    '''public ModelObject[] nextDataResult(final String sessionId, final int start, final int size, final int depth)
    '''
def insert():
    '''public Guid[] insert(final ApiServerBean bean, final String sessionId, final String xml, final boolean isImport, final Guid mss, final BulkloadInterface bulkloadInterface)
    '''
def add():
    '''public Guid[] add(final ApiServerBean bean, final String sessionId, final ModelObject[] objs, final Guid mss, final BulkloadInterface bulkloadInterface)
    '''
def update():
    '''public Guid[] update(final ApiServerBean bean, final String sessionId, final ModelObject[] objs, final Guid mss, final BulkloadInterface bulkloadInterface)
    '''
def deleteById():
    '''public int deleteById(final ApiServerBean apiServer, final String sessionId, final Guid objectId, final Guid mss, final BulkloadInterface bulkloadInterface)
    '''
def deleteMssObjLink():
    '''public void deleteMssObjLink(final ApiServerBean apiServer, final String sessionId, final Guid objGuid, final Guid mssGuid)
    '''
def getAttributesWithReplacementValues():
    '''public String[] getAttributesWithReplacementValues(final ApiServerBean apiServer, final String session_id, final String fqModelObjectClass)
    '''
def getReplacementValues():
    '''public String[] getReplacementValues(final ApiServerBean bean, final String session_id, final String fqModelObjectClass, final String attribute)
    '''
def find():
    '''public ModelObject[] find(final ApiServerBean apiServer, final String sessionId, final Guid[] guids, final String query, final int depth, final String jdoQuery, final String jdoVardecl, final Guid mss, final String[] permissions)
    '''
def evaluateGuids():
    '''public List evaluateGuids(final String sessionId, final ModelObject mo)
    '''
def getGuidAliases():
    '''public List getGuidAliases(final ApiServerBean apiServer, final String sessionId, final Guid guid)
    '''
def updateMerge():
    '''public LinkedHashMap updateMerge(final ApiServerBean bean, final String sessionId, final ModelObject[] objs, final Guid mss, final BulkloadInterface bulkloadInterface)
    '''
def getAttrPrioClassMeta():
    '''public String getAttrPrioClassMeta()
    '''
def getShortName():
    '''public String getShortName(final String className)
    '''
def getDataSources():
    '''public ArrayList getDataSources(final ApiServerBean bean, final String sessionId)
    '''
def setDataSources():
    '''public Guid[] setDataSources(final ApiServerBean bean, final String sessionId, final ArrayList dataSources)
    '''
def removeDataSources():
    '''public void removeDataSources(final ApiServerBean bean, final String sessionId, final ArrayList dataSources)
    '''
def getPriorityRules():
    '''public ArrayList getPriorityRules(final ApiServerBean bean, final String sessionId)
    '''
def setPriorityRules():
    '''public Guid[] setPriorityRules(final ApiServerBean bean, final String sessionId, final ArrayList priorityRules)
    '''
def removePriorityRules():
    '''public void removePriorityRules(final ApiServerBean bean, final String sessionId, final ArrayList priorityRules)
    '''
def mergeObjects():
    '''public int mergeObjects(final ApiServerBean bean, final String sessionId, final Guid durableGuid, final Guid transientGuid, final int mergeType)
    '''
def assignMssToDataSource():
    '''public boolean assignMssToDataSource(final ApiServerBean bean, final String sessionId, final Guid mssGuid, final AttributePrioDataSources apds)
    '''
