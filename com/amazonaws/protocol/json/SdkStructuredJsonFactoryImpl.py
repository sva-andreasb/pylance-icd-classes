def ():
    '''returns SdkStructuredJsonFactoryImpl\n\n
    (final String contentTypePrefix, final JsonFactory jsonFactory, final Map<Class<?>, Unmarshaller<?, JsonUnmarshallerContext>> unmarshallers)\n
    '''
def createWriter():
    '''returns StructuredJsonGenerator\n\n
    createWriter(final String protocolVersion)\n
    '''
def createErrorResponseHandler():
    '''returns JsonErrorResponseHandler\n\n
    createErrorResponseHandler(final List<JsonErrorUnmarshaller> errorUnmarshallers, final String customErrorCodeFieldName)\n
    '''
