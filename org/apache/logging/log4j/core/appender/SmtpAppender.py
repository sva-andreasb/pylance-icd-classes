def newBuilder():
    '''public static Builder newBuilder()
    '''
def createAppender():
    '''public static SmtpAppender createAppender(@PluginConfiguration final Configuration config, @PluginAttribute("name") @Required final String name, @PluginAttribute("to") final String to, @PluginAttribute("cc") final String cc, @PluginAttribute("bcc") final String bcc, @PluginAttribute("from") final String from, @PluginAttribute("replyTo") final String replyTo, @PluginAttribute("subject") final String subject, @PluginAttribute("smtpProtocol") final String smtpProtocol, @PluginAttribute("smtpHost") final String smtpHost, @PluginAttribute(value = "smtpPort", defaultString = "0") @ValidPort final String smtpPortStr, @PluginAttribute("smtpUsername") final String smtpUsername, @PluginAttribute(value = "smtpPassword", sensitive = true) final String smtpPassword, @PluginAttribute("smtpDebug") final String smtpDebug, @PluginAttribute("bufferSize") final String bufferSizeStr, @PluginElement("Layout") Layout<? extends Serializable> layout, @PluginElement("Filter") Filter filter, @PluginAttribute("ignoreExceptions") final String ignore)
    '''
def isFiltered():
    '''public boolean isFiltered(final LogEvent event)
    '''
def append():
    '''public void append(final LogEvent event)
    '''
def Builder():
    '''public Builder()
    '''
def setTo():
    '''public Builder setTo(final String to)
    '''
def setCc():
    '''public Builder setCc(final String cc)
    '''
def setBcc():
    '''public Builder setBcc(final String bcc)
    '''
def setFrom():
    '''public Builder setFrom(final String from)
    '''
def setReplyTo():
    '''public Builder setReplyTo(final String replyTo)
    '''
def setSubject():
    '''public Builder setSubject(final String subject)
    '''
def setSmtpProtocol():
    '''public Builder setSmtpProtocol(final String smtpProtocol)
    '''
def setSmtpHost():
    '''public Builder setSmtpHost(final String smtpHost)
    '''
def setSmtpPort():
    '''public Builder setSmtpPort(final int smtpPort)
    '''
def setSmtpUsername():
    '''public Builder setSmtpUsername(final String smtpUsername)
    '''
def setSmtpPassword():
    '''public Builder setSmtpPassword(final String smtpPassword)
    '''
def setSmtpDebug():
    '''public Builder setSmtpDebug(final boolean smtpDebug)
    '''
def setBufferSize():
    '''public Builder setBufferSize(final int bufferSize)
    '''
def setSslConfiguration():
    '''public Builder setSslConfiguration(final SslConfiguration sslConfiguration)
    '''
def setLayout():
    '''public Builder setLayout(final Layout<? extends Serializable> layout)
    '''
def setFilter():
    '''public Builder setFilter(final Filter filter)
    '''
def build():
    '''public SmtpAppender build()
    '''
