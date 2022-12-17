def getSize():
    '''returns long\n\n
    getSize(final Object[] objects, final Class<?> type, final Type genericType, final Annotation[] annotations, final MediaType mediaType)\n
    '''
def isWriteable():
    '''returns boolean\n\n
    isWriteable(final Class<?> type, final Type genericType, final Annotation[] annotations, final MediaType mediaType)\n
    '''
def writeTo():
    '''returns None\n\n
    writeTo(final Object[] objects, final Class<?> type, final Type genericType, final Annotation[] annotations, final MediaType mediaType, final MultivaluedMap<String, Object> map, final OutputStream outputStream)\n
    '''
def isReadable():
    '''returns boolean\n\n
    isReadable(final Class<?> type, final Type genericType, final Annotation[] annotations, final MediaType mediaType)\n
    '''
def readFrom():
    '''returns Object[]\n\n
    readFrom(final Class<Object[]> type, final Type genericType, final Annotation[] annotations, final MediaType mediaType, final MultivaluedMap<String, String> map, final InputStream inputStream)\n
    '''
