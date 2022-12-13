def DefaultBHttpServerConnection():
'''public DefaultBHttpServerConnection(final int buffersize, final int fragmentSizeHint, final CharsetDecoder chardecoder, final CharsetEncoder charencoder, final MessageConstraints constraints, final ContentLengthStrategy incomingContentStrategy, final ContentLengthStrategy outgoingContentStrategy, final HttpMessageParserFactory<HttpRequest> requestParserFactory, final HttpMessageWriterFactory<HttpResponse> responseWriterFactory)
public DefaultBHttpServerConnection(final int buffersize, final CharsetDecoder chardecoder, final CharsetEncoder charencoder, final MessageConstraints constraints)
public DefaultBHttpServerConnection(final int buffersize)
'''
pass
def bind():
'''public void bind(final Socket socket)
'''
pass
def receiveRequestHeader():
'''public HttpRequest receiveRequestHeader()
'''
pass
def receiveRequestEntity():
'''public void receiveRequestEntity(final HttpEntityEnclosingRequest request)
'''
pass
def sendResponseHeader():
'''public void sendResponseHeader(final HttpResponse response)
'''
pass
def sendResponseEntity():
'''public void sendResponseEntity(final HttpResponse response)
'''
pass
def flush():
'''public void flush()
'''
pass
