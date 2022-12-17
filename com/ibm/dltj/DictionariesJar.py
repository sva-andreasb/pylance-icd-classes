CACHE_NONE = "int  0"
CACHE_WEAK = "int  1"
CACHE_SOFT = "int  2"
CACHE_HARD = "int  3"
LANGUAGEWARE_PREFIX = "String  \"LanguageWare-\""
LANGUAGEWARE_DICTIONARY_PREFIX = "String  \"LanguageWare-Dictionary-\""
STANDARD = "String  \"Std\""
def ():
    '''returns DictionariesJar\n\n
    (final File file)\n
    (final File file, final boolean b, final int n)\n
    (final File file, final boolean verify, final int dictionaryCacheType, final int loadFlags)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def clearCache():
    '''returns None\n\n
    clearCache()\n
    '''
def getGenericTypes():
    '''returns String[]\n\n
    getGenericTypes()\n
    '''
def getGenericTypeEntryNames():
    '''returns String[]\n\n
    getGenericTypeEntryNames(final String s)\n
    '''
def getGenericTypeEntryInputStreams():
    '''returns InputStream[]\n\n
    getGenericTypeEntryInputStreams(final String s, final String s2)\n
    '''
def getProperties():
    '''returns Properties\n\n
    getProperties(final String s)\n
    '''
def getPropertiesTypes():
    '''returns String[]\n\n
    getPropertiesTypes()\n
    '''
def getDictionaryTypes():
    '''returns String[]\n\n
    getDictionaryTypes()\n
    '''
def getDictionaryNames():
    '''returns String[]\n\n
    getDictionaryNames(final String s)\n
    '''
def getDictionaries():
    '''returns Dictionary[]\n\n
    getDictionaries(final String s)\n
    '''
def getDictionary():
    '''returns Dictionary\n\n
    getDictionary(final String name)\n
    '''
def compare():
    '''returns int\n\n
    compare(final Object o, final Object o2)\n
    '''
