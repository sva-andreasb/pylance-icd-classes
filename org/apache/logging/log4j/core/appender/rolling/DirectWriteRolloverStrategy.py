def newBuilder():
    '''public static Builder newBuilder()
    '''
def createStrategy():
    '''public static DirectWriteRolloverStrategy createStrategy(@PluginAttribute("maxFiles") final String maxFiles, @PluginAttribute("compressionLevel") final String compressionLevelStr, @PluginElement("Actions") final Action[] customActions, @PluginAttribute(value = "stopCustomActionsOnError", defaultBoolean = true) final boolean stopCustomActionsOnError, @PluginConfiguration final Configuration config)
    '''
def getCompressionLevel():
    '''public int getCompressionLevel()
    '''
def getCustomActions():
    '''public List<Action> getCustomActions()
    public Action[] getCustomActions()
    '''
def getMaxFiles():
    '''public int getMaxFiles()
    public String getMaxFiles()
    '''
def isStopCustomActionsOnError():
    '''public boolean isStopCustomActionsOnError()
    public boolean isStopCustomActionsOnError()
    '''
def getTempCompressedFilePattern():
    '''public PatternProcessor getTempCompressedFilePattern()
    public String getTempCompressedFilePattern()
    '''
def getCurrentFileName():
    '''public String getCurrentFileName(final RollingFileManager manager)
    '''
def clearCurrentFileName():
    '''public void clearCurrentFileName()
    '''
def rollover():
    '''public RolloverDescription rollover(final RollingFileManager manager)
    '''
def toString():
    '''public String toString()
    '''
def Builder():
    '''public Builder()
    '''
def build():
    '''public DirectWriteRolloverStrategy build()
    '''
def withMaxFiles():
    '''public Builder withMaxFiles(final String maxFiles)
    '''
def getCompressionLevelStr():
    '''public String getCompressionLevelStr()
    '''
def withCompressionLevelStr():
    '''public Builder withCompressionLevelStr(final String compressionLevelStr)
    '''
def withCustomActions():
    '''public Builder withCustomActions(final Action[] customActions)
    '''
def withStopCustomActionsOnError():
    '''public Builder withStopCustomActionsOnError(final boolean stopCustomActionsOnError)
    '''
def withTempCompressedFilePattern():
    '''public Builder withTempCompressedFilePattern(final String tempCompressedFilePattern)
    '''
def getConfig():
    '''public Configuration getConfig()
    '''
def withConfig():
    '''public Builder withConfig(final Configuration config)
    '''
