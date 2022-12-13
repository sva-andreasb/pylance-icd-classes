def ServiceAccessor():
'''public ServiceAccessor(final ServiceAccessListener listener, final Class[] interfaces, final String name, final String reggieHost, final int reggiePort)
public ServiceAccessor(final ServiceAccessListener listener, final Class[] interfaces, final String name)
public ServiceAccessor(final ServiceAccessListener listener, final Class[] interfaces)
public ServiceAccessor(final Class intf)
public ServiceAccessor(final Class intf, final String host, final int port)
public ServiceAccessor(final Class intf, final String name)
'''
pass
def run():
'''public void run()
public void run()
public void run()
public void run()
'''
pass
def putLocalServiceImpl():
'''public static synchronized void putLocalServiceImpl(final Class interface_, final Object service)
'''
pass
def isLocalServiceImpl():
'''public boolean isLocalServiceImpl()
'''
pass
def setDebugEnabled():
'''public static void setDebugEnabled(final boolean enable)
'''
pass
def setDefaultUnicastHost():
'''public static synchronized void setDefaultUnicastHost(final String host)
'''
pass
def setDefaultUnicastPort():
'''public static synchronized void setDefaultUnicastPort(final int port)
'''
pass
def addListener():
'''public void addListener(final ServiceAccessListener l)
'''
pass
def getService():
'''public synchronized Object getService()
public synchronized Object getService(final int timeout)
public synchronized Object getService(final boolean useLocal, final int timeout)
public synchronized Object getService(final boolean useLocal)
'''
pass
def disconnectFromRegistrar():
'''public void disconnectFromRegistrar()
'''
pass
def serviceChanged():
'''public synchronized void serviceChanged(final ServiceDiscoveryEvent e)
'''
pass
def serviceRemoved():
'''public synchronized void serviceRemoved(final ServiceDiscoveryEvent e)
'''
pass
def serviceAdded():
'''public synchronized void serviceAdded(final ServiceDiscoveryEvent e)
'''
pass
def terminate():
'''public void terminate()
'''
pass
