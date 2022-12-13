def StructuredDataMessage():
    '''public StructuredDataMessage(final String id, final String msg, final String type)
    public StructuredDataMessage(final String id, final String msg, final String type, final int maxLength)
    public StructuredDataMessage(final String id, final String msg, final String type, final Map<String, String> data)
    public StructuredDataMessage(final String id, final String msg, final String type, final Map<String, String> data, final int maxLength)
    public StructuredDataMessage(final StructuredDataId id, final String msg, final String type)
    public StructuredDataMessage(final StructuredDataId id, final String msg, final String type, final int maxLength)
    public StructuredDataMessage(final StructuredDataId id, final String msg, final String type, final Map<String, String> data)
    public StructuredDataMessage(final StructuredDataId id, final String msg, final String type, final Map<String, String> data, final int maxLength)
    '''
def getFormats():
    '''public String[] getFormats()
    '''
def getId():
    '''public StructuredDataId getId()
    '''
def getType():
    '''public String getType()
    '''
def formatTo():
    '''public void formatTo(final StringBuilder buffer)
    public void formatTo(final String[] formats, final StringBuilder buffer)
    '''
def getFormat():
    '''public String getFormat()
    '''
def asString():
    '''public String asString()
    public String asString(final String format)
    public final String asString(final Format format, final StructuredDataId structuredDataId)
    public final void asString(final Format format, final StructuredDataId structuredDataId, final StringBuilder sb)
    '''
def getFormattedMessage():
    '''public String getFormattedMessage()
    public String getFormattedMessage(final String[] formats)
    '''
def toString():
    '''public String toString()
    '''
def newInstance():
    '''public StructuredDataMessage newInstance(final Map<String, String> map)
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
def hashCode():
    '''public int hashCode()
    '''
