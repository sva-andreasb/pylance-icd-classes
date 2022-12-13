STATIC_VARIABLES_KEY = "String  \"staticVariables\""
def newBuilder():
    '''public static <B extends Builder<B>> B newBuilder()
    '''
def start():
    '''public void start()
    '''
def stop():
    '''public boolean stop(final long timeout, final TimeUnit timeUnit)
    '''
def append():
    '''public void append(LogEvent event)
    '''
def getAppenders():
    '''public Map<String, AppenderControl> getAppenders()
    '''
def deleteAppender():
    '''public void deleteAppender(final String key)
    '''
def createAppender():
    '''public static RoutingAppender createAppender(final String name, final String ignore, final Routes routes, final Configuration config, final RewritePolicy rewritePolicy, final PurgePolicy purgePolicy, final Filter filter)
    '''
def getDefaultRoute():
    '''public Route getDefaultRoute()
    '''
def getDefaultRouteScript():
    '''public AbstractScript getDefaultRouteScript()
    public AbstractScript getDefaultRouteScript()
    '''
def getPurgePolicy():
    '''public PurgePolicy getPurgePolicy()
    public PurgePolicy getPurgePolicy()
    '''
def getRewritePolicy():
    '''public RewritePolicy getRewritePolicy()
    public RewritePolicy getRewritePolicy()
    '''
def getRoutes():
    '''public Routes getRoutes()
    public Routes getRoutes()
    '''
def getConfiguration():
    '''public Configuration getConfiguration()
    '''
def getScriptStaticVariables():
    '''public ConcurrentMap<Object, Object> getScriptStaticVariables()
    '''
def build():
    '''public RoutingAppender build()
    '''
def withRoutes():
    '''public B withRoutes(final Routes routes)
    '''
def withDefaultRouteScript():
    '''public B withDefaultRouteScript(final AbstractScript defaultRouteScript)
    '''
def withRewritePolicy():
    '''public B withRewritePolicy(final RewritePolicy rewritePolicy)
    '''
def withPurgePolicy():
    '''public void withPurgePolicy(final PurgePolicy purgePolicy)
    '''
