def createAppender():
'''public static JeroMqAppender createAppender(@Required(message = "No name provided for JeroMqAppender") @PluginAttribute("name") final String name, @PluginElement("Layout") Layout<?> layout, @PluginElement("Filter") final Filter filter, @PluginElement("Properties") final Property[] properties, @PluginAttribute("ignoreExceptions") final boolean ignoreExceptions, @PluginAttribute(value = "affinity", defaultLong = 0L) final long affinity, @PluginAttribute(value = "backlog", defaultLong = 100L) final long backlog, @PluginAttribute("delayAttachOnConnect") final boolean delayAttachOnConnect, @PluginAttribute("identity") final byte[] identity, @PluginAttribute(value = "ipv4Only", defaultBoolean = true) final boolean ipv4Only, @PluginAttribute(value = "linger", defaultLong = -1L) final long linger, @PluginAttribute(value = "maxMsgSize", defaultLong = -1L) final long maxMsgSize, @PluginAttribute(value = "rcvHwm", defaultLong = 1000L) final long rcvHwm, @PluginAttribute(value = "receiveBufferSize", defaultLong = 0L) final long receiveBufferSize, @PluginAttribute(value = "receiveTimeOut", defaultLong = -1L) final int receiveTimeOut, @PluginAttribute(value = "reconnectIVL", defaultLong = 100L) final long reconnectIVL, @PluginAttribute(value = "reconnectIVLMax", defaultLong = 0L) final long reconnectIVLMax, @PluginAttribute(value = "sendBufferSize", defaultLong = 0L) final long sendBufferSize, @PluginAttribute(value = "sendTimeOut", defaultLong = -1L) final int sendTimeOut, @PluginAttribute(value = "sndHwm", defaultLong = 1000L) final long sndHwm, @PluginAttribute(value = "tcpKeepAlive", defaultInt = -1) final int tcpKeepAlive, @PluginAttribute(value = "tcpKeepAliveCount", defaultLong = -1L) final long tcpKeepAliveCount, @PluginAttribute(value = "tcpKeepAliveIdle", defaultLong = -1L) final long tcpKeepAliveIdle, @PluginAttribute(value = "tcpKeepAliveInterval", defaultLong = -1L) final long tcpKeepAliveInterval, @PluginAttribute("xpubVerbose") final boolean xpubVerbose)
'''
pass
def append():
'''public synchronized void append(final LogEvent event)
'''
pass
def stop():
'''public boolean stop(final long timeout, final TimeUnit timeUnit)
'''
pass
def toString():
'''public String toString()
'''
pass
