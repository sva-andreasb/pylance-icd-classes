def newBuilder():
'''public static Builder newBuilder()
'''
pass
def createStrategy():
'''public static DirectWriteRolloverStrategy createStrategy(@PluginAttribute("maxFiles") final String maxFiles, @PluginAttribute("compressionLevel") final String compressionLevelStr, @PluginElement("Actions") final Action[] customActions, @PluginAttribute(value = "stopCustomActionsOnError", defaultBoolean = true) final boolean stopCustomActionsOnError, @PluginConfiguration final Configuration config)
'''
pass
def getCompressionLevel():
'''public int getCompressionLevel()
'''
pass
def getCustomActions():
'''public List<Action> getCustomActions()
public Action[] getCustomActions()
'''
pass
def getMaxFiles():
'''public int getMaxFiles()
public String getMaxFiles()
'''
pass
def isStopCustomActionsOnError():
'''public boolean isStopCustomActionsOnError()
public boolean isStopCustomActionsOnError()
'''
pass
def getTempCompressedFilePattern():
'''public PatternProcessor getTempCompressedFilePattern()
public String getTempCompressedFilePattern()
'''
pass
def getCurrentFileName():
'''public String getCurrentFileName(final RollingFileManager manager)
'''
pass
def clearCurrentFileName():
'''public void clearCurrentFileName()
'''
pass
def rollover():
'''public RolloverDescription rollover(final RollingFileManager manager)
'''
pass
def toString():
'''public String toString()
'''
pass
def Builder():
'''public Builder()
'''
pass
def build():
'''public DirectWriteRolloverStrategy build()
'''
pass
def withMaxFiles():
'''public Builder withMaxFiles(final String maxFiles)
'''
pass
def getCompressionLevelStr():
'''public String getCompressionLevelStr()
'''
pass
def withCompressionLevelStr():
'''public Builder withCompressionLevelStr(final String compressionLevelStr)
'''
pass
def withCustomActions():
'''public Builder withCustomActions(final Action[] customActions)
'''
pass
def withStopCustomActionsOnError():
'''public Builder withStopCustomActionsOnError(final boolean stopCustomActionsOnError)
'''
pass
def withTempCompressedFilePattern():
'''public Builder withTempCompressedFilePattern(final String tempCompressedFilePattern)
'''
pass
def getConfig():
'''public Configuration getConfig()
'''
pass
def withConfig():
'''public Builder withConfig(final Configuration config)
'''
pass
