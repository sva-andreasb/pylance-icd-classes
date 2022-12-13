def JsonMappingException():
    '''public JsonMappingException(final String msg)
    public JsonMappingException(final String msg, final Throwable rootCause)
    public JsonMappingException(final String msg, final JsonLocation loc)
    public JsonMappingException(final String msg, final JsonLocation loc, final Throwable rootCause)
    public JsonMappingException(final Closeable processor, final String msg)
    public JsonMappingException(final Closeable processor, final String msg, final Throwable problem)
    public JsonMappingException(final Closeable processor, final String msg, final JsonLocation loc)
    '''
def from():
    '''public static JsonMappingException from(final JsonParser p, final String msg)
    public static JsonMappingException from(final JsonParser p, final String msg, final Throwable problem)
    public static JsonMappingException from(final JsonGenerator g, final String msg)
    public static JsonMappingException from(final JsonGenerator g, final String msg, final Throwable problem)
    public static JsonMappingException from(final DeserializationContext ctxt, final String msg)
    public static JsonMappingException from(final DeserializationContext ctxt, final String msg, final Throwable t)
    public static JsonMappingException from(final SerializerProvider ctxt, final String msg)
    public static JsonMappingException from(final SerializerProvider ctxt, final String msg, final Throwable problem)
    '''
def fromUnexpectedIOE():
    '''public static JsonMappingException fromUnexpectedIOE(final IOException src)
    '''
def wrapWithPath():
    '''public static JsonMappingException wrapWithPath(final Throwable src, final Object refFrom, final String refFieldName)
    public static JsonMappingException wrapWithPath(final Throwable src, final Object refFrom, final int index)
    public static JsonMappingException wrapWithPath(final Throwable src, final Reference ref)
    '''
def getPath():
    '''public List<Reference> getPath()
    '''
def getPathReference():
    '''public String getPathReference()
    public StringBuilder getPathReference(final StringBuilder sb)
    '''
def prependPath():
    '''public void prependPath(final Object referrer, final String fieldName)
    public void prependPath(final Object referrer, final int index)
    public void prependPath(final Reference r)
    '''
def getProcessor():
    '''public Object getProcessor()
    '''
def getLocalizedMessage():
    '''public String getLocalizedMessage()
    '''
def getMessage():
    '''public String getMessage()
    '''
def toString():
    '''public String toString()
    public String toString()
    '''
def Reference():
    '''public Reference(final Object from)
    public Reference(final Object from, final String fieldName)
    public Reference(final Object from, final int index)
    '''
def getFrom():
    '''public Object getFrom()
    '''
def getFieldName():
    '''public String getFieldName()
    '''
def getIndex():
    '''public int getIndex()
    '''
def getDescription():
    '''public String getDescription()
    '''
