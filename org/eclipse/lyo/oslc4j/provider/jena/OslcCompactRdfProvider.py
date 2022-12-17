def getSize():
    '''returns long\n\n
    getSize(final Compact compact, final Class<?> type, final Type genericType, final Annotation[] annotation, final MediaType mediaType)\n
    '''
def isWriteable():
    '''returns boolean\n\n
    isWriteable(final Class<?> type, final Type genericType, final Annotation[] annotations, final MediaType mediaType)\n
    '''
def writeTo():
    '''returns None\n\n
    writeTo(final Compact compact, final Class<?> type, final Type genericType, final Annotation[] annotations, final MediaType mediaType, final MultivaluedMap<String, Object> map, final OutputStream outputStream)\n
    '''
def isReadable():
    '''returns boolean\n\n
    isReadable(final Class<?> type, final Type genericType, final Annotation[] annotations, final MediaType mediaType)\n
    '''
def readFrom():
    '''returns Compact\n\n
    readFrom(final Class<Compact> type, final Type genericType, final Annotation[] annotations, final MediaType mediaType, final MultivaluedMap<String, String> map, final InputStream inputStream)\n
    '''
