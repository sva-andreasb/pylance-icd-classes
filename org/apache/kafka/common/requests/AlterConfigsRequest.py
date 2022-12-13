def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def AlterConfigsRequest():
    '''public AlterConfigsRequest(final short version, final Map<Resource, Config> configs, final boolean validateOnly)
    public AlterConfigsRequest(final Struct struct, final short version)
    '''
def configs():
    '''public Map<Resource, Config> configs()
    '''
def validateOnly():
    '''public boolean validateOnly()
    '''
def getErrorResponse():
    '''public AbstractResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def parse():
    '''public static AlterConfigsRequest parse(final ByteBuffer buffer, final short version)
    '''
def Config():
    '''public Config(final Collection<ConfigEntry> entries)
    '''
def entries():
    '''public Collection<ConfigEntry> entries()
    '''
def ConfigEntry():
    '''public ConfigEntry(final String name, final String value)
    '''
def name():
    '''public String name()
    '''
def value():
    '''public String value()
    '''
def Builder():
    '''public Builder(final Map<Resource, Config> configs, final boolean validateOnly)
    '''
def build():
    '''public AlterConfigsRequest build(final short version)
    '''
