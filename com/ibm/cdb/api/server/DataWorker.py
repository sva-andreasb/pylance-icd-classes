def DataWorker():
'''public DataWorker(final TopologyManagerFactory topologyManagerFactory, final ApiProps props)
'''
pass
def findXML():
'''public String findXML(final ApiServerBean apiServer, final String sessionId, final Guid object_id, final int depth, final int indent, final Guid mss, final String[] permissions)
public String findXML(final ApiServerBean apiServer, final String sessionId, final Guid[] objectIds, final int depth, final int indent, final Guid mss, final String[] permissions)
'''
pass
def findInitXML():
'''public void findInitXML(final ApiServerBean apiServer, final String sessionId, final String query, final Guid[] guids, final int depth, final int fetch_size, final int indent, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions, final String suppressList)
'''
pass
def nextXML():
'''public String nextXML(final String sessionId)
'''
pass
def findInitCursor():
'''public String findInitCursor(final ApiServerBean apiServer, final String sessionId, final String query, final Guid mss, final String[] permissions)
'''
pass
def findInitData():
'''public void findInitData(final ApiServerBean apiServer, final String sessionId, final String query, final Guid[] guids, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions)
'''
pass
def extractClassNameFromQuery():
'''public static String extractClassNameFromQuery(String query)
'''
pass
def nextDataCursor():
'''public ModelObject[] nextDataCursor(final String sessionId, final String cursorId, final int start, final int size, final int depth)
'''
pass
def cursorSize():
'''public int cursorSize(final String sessionId, final String cursorId)
'''
pass
def closeCursor():
'''public void closeCursor(final String sessionId, final String cursorId)
'''
pass
def nextDataResult():
'''public ModelObject[] nextDataResult(final String sessionId, final int start, final int size, final int depth)
'''
pass
def insert():
'''public Guid[] insert(final ApiServerBean bean, final String sessionId, final String xml, final boolean isImport, final Guid mss, final BulkloadInterface bulkloadInterface)
'''
pass
def add():
'''public Guid[] add(final ApiServerBean bean, final String sessionId, final ModelObject[] objs, final Guid mss, final BulkloadInterface bulkloadInterface)
'''
pass
def update():
'''public Guid[] update(final ApiServerBean bean, final String sessionId, final ModelObject[] objs, final Guid mss, final BulkloadInterface bulkloadInterface)
'''
pass
def deleteById():
'''public int deleteById(final ApiServerBean apiServer, final String sessionId, final Guid objectId, final Guid mss, final BulkloadInterface bulkloadInterface)
'''
pass
def deleteMssObjLink():
'''public void deleteMssObjLink(final ApiServerBean apiServer, final String sessionId, final Guid objGuid, final Guid mssGuid)
'''
pass
def getAttributesWithReplacementValues():
'''public String[] getAttributesWithReplacementValues(final ApiServerBean apiServer, final String session_id, final String fqModelObjectClass)
'''
pass
def getReplacementValues():
'''public String[] getReplacementValues(final ApiServerBean bean, final String session_id, final String fqModelObjectClass, final String attribute)
'''
pass
def find():
'''public ModelObject[] find(final ApiServerBean apiServer, final String sessionId, final Guid[] guids, final String query, final int depth, final String jdoQuery, final String jdoVardecl, final Guid mss, final String[] permissions)
'''
pass
def evaluateGuids():
'''public List evaluateGuids(final String sessionId, final ModelObject mo)
'''
pass
def getGuidAliases():
'''public List getGuidAliases(final ApiServerBean apiServer, final String sessionId, final Guid guid)
'''
pass
def updateMerge():
'''public LinkedHashMap updateMerge(final ApiServerBean bean, final String sessionId, final ModelObject[] objs, final Guid mss, final BulkloadInterface bulkloadInterface)
'''
pass
def getAttrPrioClassMeta():
'''public String getAttrPrioClassMeta()
'''
pass
def getShortName():
'''public String getShortName(final String className)
'''
pass
def getDataSources():
'''public ArrayList getDataSources(final ApiServerBean bean, final String sessionId)
'''
pass
def setDataSources():
'''public Guid[] setDataSources(final ApiServerBean bean, final String sessionId, final ArrayList dataSources)
'''
pass
def removeDataSources():
'''public void removeDataSources(final ApiServerBean bean, final String sessionId, final ArrayList dataSources)
'''
pass
def getPriorityRules():
'''public ArrayList getPriorityRules(final ApiServerBean bean, final String sessionId)
'''
pass
def setPriorityRules():
'''public Guid[] setPriorityRules(final ApiServerBean bean, final String sessionId, final ArrayList priorityRules)
'''
pass
def removePriorityRules():
'''public void removePriorityRules(final ApiServerBean bean, final String sessionId, final ArrayList priorityRules)
'''
pass
def mergeObjects():
'''public int mergeObjects(final ApiServerBean bean, final String sessionId, final Guid durableGuid, final Guid transientGuid, final int mergeType)
'''
pass
def assignMssToDataSource():
'''public boolean assignMssToDataSource(final ApiServerBean bean, final String sessionId, final Guid mssGuid, final AttributePrioDataSources apds)
'''
pass
