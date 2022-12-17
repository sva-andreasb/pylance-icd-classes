def ():
    '''returns DefaultPrettyPrinter\n\n
    ()\n
    (final String rootSeparator)\n
    (final SerializableString rootSeparator)\n
    (final DefaultPrettyPrinter base)\n
    (final DefaultPrettyPrinter base, final SerializableString rootSeparator)\n
    '''
def withRootSeparator():
    '''returns DefaultPrettyPrinter\n\n
    withRootSeparator(final SerializableString rootSeparator)\n
    withRootSeparator(final String rootSeparator)\n
    '''
def indentArraysWith():
    '''returns None\n\n
    indentArraysWith(final Indenter i)\n
    '''
def indentObjectsWith():
    '''returns None\n\n
    indentObjectsWith(final Indenter i)\n
    '''
def withArrayIndenter():
    '''returns DefaultPrettyPrinter\n\n
    withArrayIndenter(Indenter i)\n
    '''
def withObjectIndenter():
    '''returns DefaultPrettyPrinter\n\n
    withObjectIndenter(Indenter i)\n
    '''
def withSpacesInObjectEntries():
    '''returns DefaultPrettyPrinter\n\n
    withSpacesInObjectEntries()\n
    '''
def withoutSpacesInObjectEntries():
    '''returns DefaultPrettyPrinter\n\n
    withoutSpacesInObjectEntries()\n
    '''
def withSeparators():
    '''returns DefaultPrettyPrinter\n\n
    withSeparators(final Separators separators)\n
    '''
def createInstance():
    '''returns DefaultPrettyPrinter\n\n
    createInstance()\n
    '''
def writeRootValueSeparator():
    '''returns None\n\n
    writeRootValueSeparator(final JsonGenerator g)\n
    '''
def writeStartObject():
    '''returns None\n\n
    writeStartObject(final JsonGenerator g)\n
    '''
def beforeObjectEntries():
    '''returns None\n\n
    beforeObjectEntries(final JsonGenerator g)\n
    '''
def writeObjectFieldValueSeparator():
    '''returns None\n\n
    writeObjectFieldValueSeparator(final JsonGenerator g)\n
    '''
def writeObjectEntrySeparator():
    '''returns None\n\n
    writeObjectEntrySeparator(final JsonGenerator g)\n
    '''
def writeEndObject():
    '''returns None\n\n
    writeEndObject(final JsonGenerator g, final int nrOfEntries)\n
    '''
def writeStartArray():
    '''returns None\n\n
    writeStartArray(final JsonGenerator g)\n
    '''
def beforeArrayValues():
    '''returns None\n\n
    beforeArrayValues(final JsonGenerator g)\n
    '''
def writeArrayValueSeparator():
    '''returns None\n\n
    writeArrayValueSeparator(final JsonGenerator g)\n
    '''
def writeEndArray():
    '''returns None\n\n
    writeEndArray(final JsonGenerator g, final int nrOfValues)\n
    '''
def writeIndentation():
    '''returns None\n\n
    writeIndentation(final JsonGenerator g, final int level)\n
    writeIndentation(final JsonGenerator g, final int level)\n
    '''
def isInline():
    '''returns boolean\n\n
    isInline()\n
    isInline()\n
    '''
