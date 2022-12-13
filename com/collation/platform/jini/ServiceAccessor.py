def ServiceAccessor():
    '''    public ServiceAccessor(final ServiceAccessListener listener, final Class[] interfaces, final String name, final String reggieHost, final int reggiePort)
    public ServiceAccessor(final ServiceAccessListener listener, final Class[] interfaces, final String name)
    public ServiceAccessor(final ServiceAccessListener listener, final Class[] interfaces)
    public ServiceAccessor(final Class intf)
    public ServiceAccessor(final Class intf, final String host, final int port)
    public ServiceAccessor(final Class intf, final String name)
    '''
def run():
    '''    public void run()
    public void run()
    public void run()
    public void run()
    '''
def putLocalServiceImpl():
    '''    public static synchronized void putLocalServiceImpl(final Class interface_, final Object service)
    '''
def isLocalServiceImpl():
    '''    public boolean isLocalServiceImpl()
    '''
def setDebugEnabled():
    '''    public static void setDebugEnabled(final boolean enable)
    '''
def setDefaultUnicastHost():
    '''    public static synchronized void setDefaultUnicastHost(final String host)
    '''
def setDefaultUnicastPort():
    '''    public static synchronized void setDefaultUnicastPort(final int port)
    '''
def addListener():
    '''    public void addListener(final ServiceAccessListener l)
    '''
def getService():
    '''    public synchronized Object getService()
    public synchronized Object getService(final int timeout)
    public synchronized Object getService(final boolean useLocal, final int timeout)
    public synchronized Object getService(final boolean useLocal)
    '''
def disconnectFromRegistrar():
    '''    public void disconnectFromRegistrar()
    '''
def serviceChanged():
    '''    public synchronized void serviceChanged(final ServiceDiscoveryEvent e)
    '''
def serviceRemoved():
    '''    public synchronized void serviceRemoved(final ServiceDiscoveryEvent e)
    '''
def serviceAdded():
    '''    public synchronized void serviceAdded(final ServiceDiscoveryEvent e)
    '''
def terminate():
    '''    public void terminate()
    '''
