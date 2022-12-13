def schemaVersions():
    '''    public static Schema[] schemaVersions()
    '''
def DescribeConfigsResponse():
    '''    public DescribeConfigsResponse(final int throttleTimeMs, final Map<Resource, Config> configs)
    public DescribeConfigsResponse(final Struct struct)
    '''
def configs():
    '''    public Map<Resource, Config> configs()
    '''
def config():
    '''    public Config config(final Resource resource)
    '''
def throttleTimeMs():
    '''    public int throttleTimeMs()
    '''
def errorCounts():
    '''    public Map<Errors, Integer> errorCounts()
    '''
def parse():
    '''    public static DescribeConfigsResponse parse(final ByteBuffer buffer, final short version)
    '''
def Config():
    '''    public Config(final ApiError error, final Collection<ConfigEntry> entries)
    '''
def error():
    '''    public ApiError error()
    '''
def entries():
    '''    public Collection<ConfigEntry> entries()
    '''
def ConfigEntry():
    '''    public ConfigEntry(final String name, final String value, final ConfigSource source, final boolean isSensitive, final boolean readOnly, final Collection<ConfigSynonym> synonyms)
    '''
def name():
    '''    public String name()
    public String name()
    '''
def value():
    '''    public String value()
    public String value()
    '''
def isSensitive():
    '''    public boolean isSensitive()
    '''
def source():
    '''    public ConfigSource source()
    public ConfigSource source()
    '''
def isReadOnly():
    '''    public boolean isReadOnly()
    '''
def synonyms():
    '''    public Collection<ConfigSynonym> synonyms()
    '''
def forId():
    '''    public static ConfigSource forId(final byte id)
    '''
def ConfigSynonym():
    '''    public ConfigSynonym(final String name, final String value, final ConfigSource source)
    '''
