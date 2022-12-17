def ():
    '''returns CloseSuppressingInvocationHandler\n\n
    ()\n
    (final SessionFactory sessionFactory)\n
    (final SessionFactory sessionFactory, final boolean allowCreate)\n
    (final Session target)\n
    '''
def setAllowCreate():
    '''returns None\n\n
    setAllowCreate(final boolean allowCreate)\n
    '''
def isAllowCreate():
    '''returns boolean\n\n
    isAllowCreate()\n
    '''
def setAlwaysUseNewSession():
    '''returns None\n\n
    setAlwaysUseNewSession(final boolean alwaysUseNewSession)\n
    '''
def isAlwaysUseNewSession():
    '''returns boolean\n\n
    isAlwaysUseNewSession()\n
    '''
def setExposeNativeSession():
    '''returns None\n\n
    setExposeNativeSession(final boolean exposeNativeSession)\n
    '''
def isExposeNativeSession():
    '''returns boolean\n\n
    isExposeNativeSession()\n
    '''
def setCheckWriteOperations():
    '''returns None\n\n
    setCheckWriteOperations(final boolean checkWriteOperations)\n
    '''
def isCheckWriteOperations():
    '''returns boolean\n\n
    isCheckWriteOperations()\n
    '''
def setCacheQueries():
    '''returns None\n\n
    setCacheQueries(final boolean cacheQueries)\n
    '''
def isCacheQueries():
    '''returns boolean\n\n
    isCacheQueries()\n
    '''
def setQueryCacheRegion():
    '''returns None\n\n
    setQueryCacheRegion(final String queryCacheRegion)\n
    '''
def getQueryCacheRegion():
    '''returns String\n\n
    getQueryCacheRegion()\n
    '''
def execute():
    '''returns Object\n\n
    execute(final HibernateCallback action)\n
    execute(final HibernateCallback action, final boolean exposeNativeSession)\n
    '''
def executeFind():
    '''returns List\n\n
    executeFind(final HibernateCallback action)\n
    '''
def get():
    '''returns Object\n\n
    get(final Class entityClass, final Serializable id)\n
    get(final Class entityClass, final Serializable id, final LockMode lockMode)\n
    '''
def doInHibernate():
    '''returns Object\n\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    doInHibernate(final Session session)\n
    '''
def load():
    '''returns None\n\n
    load(final Class entityClass, final Serializable id)\n
    load(final Class entityClass, final Serializable id, final LockMode lockMode)\n
    load(final Object entity, final Serializable id)\n
    '''
def loadAll():
    '''returns List\n\n
    loadAll(final Class entityClass)\n
    '''
def refresh():
    '''returns None\n\n
    refresh(final Object entity)\n
    refresh(final Object entity, final LockMode lockMode)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final Object entity)\n
    '''
def evict():
    '''returns None\n\n
    evict(final Object entity)\n
    '''
def initialize():
    '''returns None\n\n
    initialize(final Object proxy)\n
    '''
def lock():
    '''returns None\n\n
    lock(final Object entity, final LockMode lockMode)\n
    '''
def save():
    '''returns None\n\n
    save(final Object entity)\n
    save(final Object entity, final Serializable id)\n
    '''
def update():
    '''returns None\n\n
    update(final Object entity)\n
    update(final Object entity, final LockMode lockMode)\n
    '''
def saveOrUpdate():
    '''returns None\n\n
    saveOrUpdate(final Object entity)\n
    '''
def saveOrUpdateAll():
    '''returns None\n\n
    saveOrUpdateAll(final Collection entities)\n
    '''
def saveOrUpdateCopy():
    '''returns Object\n\n
    saveOrUpdateCopy(final Object entity)\n
    '''
def delete():
    '''returns int\n\n
    delete(final Object entity)\n
    delete(final Object entity, final LockMode lockMode)\n
    delete(final String queryString)\n
    delete(final String queryString, final Object value, final Type type)\n
    delete(final String queryString, final Object[] values, final Type[] types)\n
    '''
def deleteAll():
    '''returns None\n\n
    deleteAll(final Collection entities)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def find():
    '''returns List\n\n
    find(final String queryString)\n
    find(final String queryString, final Object value)\n
    find(final String queryString, final Object value, final Type type)\n
    find(final String queryString, final Object[] values)\n
    find(final String queryString, final Object[] values, final Type[] types)\n
    '''
def findByNamedParam():
    '''returns List\n\n
    findByNamedParam(final String queryString, final String paramName, final Object value)\n
    findByNamedParam(final String queryString, final String paramName, final Object value, final Type type)\n
    findByNamedParam(final String queryString, final String[] paramNames, final Object[] values)\n
    findByNamedParam(final String queryString, final String[] paramNames, final Object[] values, final Type[] types)\n
    '''
def findByValueBean():
    '''returns List\n\n
    findByValueBean(final String queryString, final Object valueBean)\n
    '''
def findByNamedQuery():
    '''returns List\n\n
    findByNamedQuery(final String queryName)\n
    findByNamedQuery(final String queryName, final Object value)\n
    findByNamedQuery(final String queryName, final Object value, final Type type)\n
    findByNamedQuery(final String queryName, final Object[] values)\n
    findByNamedQuery(final String queryName, final Object[] values, final Type[] types)\n
    '''
def findByNamedQueryAndNamedParam():
    '''returns List\n\n
    findByNamedQueryAndNamedParam(final String queryName, final String paramName, final Object value)\n
    findByNamedQueryAndNamedParam(final String queryName, final String paramName, final Object value, final Type type)\n
    findByNamedQueryAndNamedParam(final String queryName, final String[] paramNames, final Object[] values)\n
    findByNamedQueryAndNamedParam(final String queryName, final String[] paramNames, final Object[] values, final Type[] types)\n
    '''
def findByNamedQueryAndValueBean():
    '''returns List\n\n
    findByNamedQueryAndValueBean(final String queryName, final Object valueBean)\n
    '''
def iterate():
    '''returns Iterator\n\n
    iterate(final String queryString)\n
    iterate(final String queryString, final Object value)\n
    iterate(final String queryString, final Object value, final Type type)\n
    iterate(final String queryString, final Object[] values)\n
    iterate(final String queryString, final Object[] values, final Type[] types)\n
    '''
def closeIterator():
    '''returns None\n\n
    closeIterator(final Iterator it)\n
    '''
def invoke():
    '''returns Object\n\n
    invoke(final Object proxy, final Method method, final Object[] args)\n
    '''
