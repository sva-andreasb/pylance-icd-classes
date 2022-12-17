def ():
    '''returns Builder\n\n
    (final short version, final Map<Resource, Config> configs, final boolean validateOnly)\n
    (final Struct struct, final short version)\n
    (final Collection<ConfigEntry> entries)\n
    (final String name, final String value)\n
    (final Map<Resource, Config> configs, final boolean validateOnly)\n
    '''
def validateOnly():
    '''returns boolean\n\n
    validateOnly()\n
    '''
def getErrorResponse():
    '''returns AbstractResponse\n\n
    getErrorResponse(final int throttleTimeMs, final Throwable e)\n
    '''
def entries():
    '''returns Collection<ConfigEntry>\n\n
    entries()\n
    '''
def name():
    '''returns String\n\n
    name()\n
    '''
def value():
    '''returns String\n\n
    value()\n
    '''
def build():
    '''returns AlterConfigsRequest\n\n
    build(final short version)\n
    '''
