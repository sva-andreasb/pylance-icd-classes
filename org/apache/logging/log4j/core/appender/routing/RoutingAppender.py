STATIC_VARIABLES_KEY = "String  staticVariables""
def newBuilder():
'''public static <B extends Builder<B>> B newBuilder()
'''
pass
def start():
'''public void start()
'''
pass
def stop():
'''public boolean stop(final long timeout, final TimeUnit timeUnit)
'''
pass
def append():
'''public void append(LogEvent event)
'''
pass
def getAppenders():
'''public Map<String, AppenderControl> getAppenders()
'''
pass
def deleteAppender():
'''public void deleteAppender(final String key)
'''
pass
def createAppender():
'''public static RoutingAppender createAppender(final String name, final String ignore, final Routes routes, final Configuration config, final RewritePolicy rewritePolicy, final PurgePolicy purgePolicy, final Filter filter)
'''
pass
def getDefaultRoute():
'''public Route getDefaultRoute()
'''
pass
def getDefaultRouteScript():
'''public AbstractScript getDefaultRouteScript()
public AbstractScript getDefaultRouteScript()
'''
pass
def getPurgePolicy():
'''public PurgePolicy getPurgePolicy()
public PurgePolicy getPurgePolicy()
'''
pass
def getRewritePolicy():
'''public RewritePolicy getRewritePolicy()
public RewritePolicy getRewritePolicy()
'''
pass
def getRoutes():
'''public Routes getRoutes()
public Routes getRoutes()
'''
pass
def getConfiguration():
'''public Configuration getConfiguration()
'''
pass
def getScriptStaticVariables():
'''public ConcurrentMap<Object, Object> getScriptStaticVariables()
'''
pass
def build():
'''public RoutingAppender build()
'''
pass
def withRoutes():
'''public B withRoutes(final Routes routes)
'''
pass
def withDefaultRouteScript():
'''public B withDefaultRouteScript(final AbstractScript defaultRouteScript)
'''
pass
def withRewritePolicy():
'''public B withRewritePolicy(final RewritePolicy rewritePolicy)
'''
pass
def withPurgePolicy():
'''public void withPurgePolicy(final PurgePolicy purgePolicy)
'''
pass
