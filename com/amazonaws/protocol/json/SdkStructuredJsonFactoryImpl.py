def SdkStructuredJsonFactoryImpl():
'''public SdkStructuredJsonFactoryImpl(final String contentTypePrefix, final JsonFactory jsonFactory, final Map<Class<?>, Unmarshaller<?, JsonUnmarshallerContext>> unmarshallers)
'''
pass
def createWriter():
'''public StructuredJsonGenerator createWriter(final String protocolVersion)
'''
pass
def createResponseHandler():
'''public <T> JsonResponseHandler<T> createResponseHandler(final JsonOperationMetadata operationMetadata, final Unmarshaller<T, JsonUnmarshallerContext> responseUnmarshaller)
'''
pass
def createErrorResponseHandler():
'''public JsonErrorResponseHandler createErrorResponseHandler(final List<JsonErrorUnmarshaller> errorUnmarshallers, final String customErrorCodeFieldName)
'''
pass
