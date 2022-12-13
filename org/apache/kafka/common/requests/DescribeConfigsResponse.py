def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def DescribeConfigsResponse():
'''public DescribeConfigsResponse(final int throttleTimeMs, final Map<Resource, Config> configs)
public DescribeConfigsResponse(final Struct struct)
'''
pass
def configs():
'''public Map<Resource, Config> configs()
'''
pass
def config():
'''public Config config(final Resource resource)
'''
pass
def throttleTimeMs():
'''public int throttleTimeMs()
'''
pass
def errorCounts():
'''public Map<Errors, Integer> errorCounts()
'''
pass
def parse():
'''public static DescribeConfigsResponse parse(final ByteBuffer buffer, final short version)
'''
pass
def Config():
'''public Config(final ApiError error, final Collection<ConfigEntry> entries)
'''
pass
def error():
'''public ApiError error()
'''
pass
def entries():
'''public Collection<ConfigEntry> entries()
'''
pass
def ConfigEntry():
'''public ConfigEntry(final String name, final String value, final ConfigSource source, final boolean isSensitive, final boolean readOnly, final Collection<ConfigSynonym> synonyms)
'''
pass
def name():
'''public String name()
public String name()
'''
pass
def value():
'''public String value()
public String value()
'''
pass
def isSensitive():
'''public boolean isSensitive()
'''
pass
def source():
'''public ConfigSource source()
public ConfigSource source()
'''
pass
def isReadOnly():
'''public boolean isReadOnly()
'''
pass
def synonyms():
'''public Collection<ConfigSynonym> synonyms()
'''
pass
def forId():
'''public static ConfigSource forId(final byte id)
'''
pass
def ConfigSynonym():
'''public ConfigSynonym(final String name, final String value, final ConfigSource source)
'''
pass
