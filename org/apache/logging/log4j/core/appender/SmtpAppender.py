def newBuilder():
'''public static Builder newBuilder()
'''
pass
def createAppender():
'''public static SmtpAppender createAppender(@PluginConfiguration final Configuration config, @PluginAttribute("name") @Required final String name, @PluginAttribute("to") final String to, @PluginAttribute("cc") final String cc, @PluginAttribute("bcc") final String bcc, @PluginAttribute("from") final String from, @PluginAttribute("replyTo") final String replyTo, @PluginAttribute("subject") final String subject, @PluginAttribute("smtpProtocol") final String smtpProtocol, @PluginAttribute("smtpHost") final String smtpHost, @PluginAttribute(value = "smtpPort", defaultString = "0") @ValidPort final String smtpPortStr, @PluginAttribute("smtpUsername") final String smtpUsername, @PluginAttribute(value = "smtpPassword", sensitive = true) final String smtpPassword, @PluginAttribute("smtpDebug") final String smtpDebug, @PluginAttribute("bufferSize") final String bufferSizeStr, @PluginElement("Layout") Layout<? extends Serializable> layout, @PluginElement("Filter") Filter filter, @PluginAttribute("ignoreExceptions") final String ignore)
'''
pass
def isFiltered():
'''public boolean isFiltered(final LogEvent event)
'''
pass
def append():
'''public void append(final LogEvent event)
'''
pass
def Builder():
'''public Builder()
'''
pass
def setTo():
'''public Builder setTo(final String to)
'''
pass
def setCc():
'''public Builder setCc(final String cc)
'''
pass
def setBcc():
'''public Builder setBcc(final String bcc)
'''
pass
def setFrom():
'''public Builder setFrom(final String from)
'''
pass
def setReplyTo():
'''public Builder setReplyTo(final String replyTo)
'''
pass
def setSubject():
'''public Builder setSubject(final String subject)
'''
pass
def setSmtpProtocol():
'''public Builder setSmtpProtocol(final String smtpProtocol)
'''
pass
def setSmtpHost():
'''public Builder setSmtpHost(final String smtpHost)
'''
pass
def setSmtpPort():
'''public Builder setSmtpPort(final int smtpPort)
'''
pass
def setSmtpUsername():
'''public Builder setSmtpUsername(final String smtpUsername)
'''
pass
def setSmtpPassword():
'''public Builder setSmtpPassword(final String smtpPassword)
'''
pass
def setSmtpDebug():
'''public Builder setSmtpDebug(final boolean smtpDebug)
'''
pass
def setBufferSize():
'''public Builder setBufferSize(final int bufferSize)
'''
pass
def setSslConfiguration():
'''public Builder setSslConfiguration(final SslConfiguration sslConfiguration)
'''
pass
def setLayout():
'''public Builder setLayout(final Layout<? extends Serializable> layout)
'''
pass
def setFilter():
'''public Builder setFilter(final Filter filter)
'''
pass
def build():
'''public SmtpAppender build()
'''
pass
