def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def AlterConfigsRequest():
'''public AlterConfigsRequest(final short version, final Map<Resource, Config> configs, final boolean validateOnly)
public AlterConfigsRequest(final Struct struct, final short version)
'''
pass
def configs():
'''public Map<Resource, Config> configs()
'''
pass
def validateOnly():
'''public boolean validateOnly()
'''
pass
def getErrorResponse():
'''public AbstractResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
'''
pass
def parse():
'''public static AlterConfigsRequest parse(final ByteBuffer buffer, final short version)
'''
pass
def Config():
'''public Config(final Collection<ConfigEntry> entries)
'''
pass
def entries():
'''public Collection<ConfigEntry> entries()
'''
pass
def ConfigEntry():
'''public ConfigEntry(final String name, final String value)
'''
pass
def name():
'''public String name()
'''
pass
def value():
'''public String value()
'''
pass
def Builder():
'''public Builder(final Map<Resource, Config> configs, final boolean validateOnly)
'''
pass
def build():
'''public AlterConfigsRequest build(final short version)
'''
pass
