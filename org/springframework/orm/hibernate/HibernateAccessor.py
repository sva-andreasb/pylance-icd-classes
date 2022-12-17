FLUSH_NEVER = "int  0"
FLUSH_AUTO = "int  1"
FLUSH_EAGER = "int  2"
FLUSH_COMMIT = "int  3"
def ():
    '''returns HibernateAccessor\n\n
    ()\n
    '''
def setSessionFactory():
    '''returns None\n\n
    setSessionFactory(final SessionFactory sessionFactory)\n
    '''
def getSessionFactory():
    '''returns SessionFactory\n\n
    getSessionFactory()\n
    '''
def setEntityInterceptorBeanName():
    '''returns None\n\n
    setEntityInterceptorBeanName(final String entityInterceptorBeanName)\n
    '''
def setEntityInterceptor():
    '''returns None\n\n
    setEntityInterceptor(final Interceptor entityInterceptor)\n
    '''
def getEntityInterceptor():
    '''returns Interceptor\n\n
    getEntityInterceptor()\n
    '''
def setJdbcExceptionTranslator():
    '''returns None\n\n
    setJdbcExceptionTranslator(final SQLExceptionTranslator jdbcExceptionTranslator)\n
    '''
def getJdbcExceptionTranslator():
    '''returns SQLExceptionTranslator\n\n
    getJdbcExceptionTranslator()\n
    '''
def setFlushModeName():
    '''returns None\n\n
    setFlushModeName(final String constantName)\n
    '''
def setFlushMode():
    '''returns None\n\n
    setFlushMode(final int flushMode)\n
    '''
def getFlushMode():
    '''returns int\n\n
    getFlushMode()\n
    '''
def setBeanFactory():
    '''returns None\n\n
    setBeanFactory(final BeanFactory beanFactory)\n
    '''
def afterPropertiesSet():
    '''returns None\n\n
    afterPropertiesSet()\n
    '''
def convertHibernateAccessException():
    '''returns DataAccessException\n\n
    convertHibernateAccessException(final HibernateException ex)\n
    '''
