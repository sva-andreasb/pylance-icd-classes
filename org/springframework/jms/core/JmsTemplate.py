DEFAULT_RECEIVE_TIMEOUT = "long  -1L"
def ():
    '''returns JmsTemplate\n\n
    ()\n
    (final ConnectionFactory connectionFactory)\n
    '''
def setPubSubDomain():
    '''returns None\n\n
    setPubSubDomain(final boolean pubSubDomain)\n
    '''
def isPubSubDomain():
    '''returns boolean\n\n
    isPubSubDomain()\n
    '''
def setDefaultDestination():
    '''returns None\n\n
    setDefaultDestination(final Destination destination)\n
    '''
def getDefaultDestination():
    '''returns Destination\n\n
    getDefaultDestination()\n
    '''
def setDefaultDestinationName():
    '''returns None\n\n
    setDefaultDestinationName(final String defaultDestinationName)\n
    '''
def getDefaultDestinationName():
    '''returns String\n\n
    getDefaultDestinationName()\n
    '''
def setDestinationResolver():
    '''returns None\n\n
    setDestinationResolver(final DestinationResolver destinationResolver)\n
    '''
def getDestinationResolver():
    '''returns DestinationResolver\n\n
    getDestinationResolver()\n
    '''
def setMessageConverter():
    '''returns None\n\n
    setMessageConverter(final MessageConverter messageConverter)\n
    '''
def getMessageConverter():
    '''returns MessageConverter\n\n
    getMessageConverter()\n
    '''
def setMessageIdEnabled():
    '''returns None\n\n
    setMessageIdEnabled(final boolean messageIdEnabled)\n
    '''
def isMessageIdEnabled():
    '''returns boolean\n\n
    isMessageIdEnabled()\n
    '''
def setMessageTimestampEnabled():
    '''returns None\n\n
    setMessageTimestampEnabled(final boolean messageTimestampEnabled)\n
    '''
def isMessageTimestampEnabled():
    '''returns boolean\n\n
    isMessageTimestampEnabled()\n
    '''
def setPubSubNoLocal():
    '''returns None\n\n
    setPubSubNoLocal(final boolean pubSubNoLocal)\n
    '''
def isPubSubNoLocal():
    '''returns boolean\n\n
    isPubSubNoLocal()\n
    '''
def setReceiveTimeout():
    '''returns None\n\n
    setReceiveTimeout(final long receiveTimeout)\n
    '''
def getReceiveTimeout():
    '''returns long\n\n
    getReceiveTimeout()\n
    '''
def setExplicitQosEnabled():
    '''returns None\n\n
    setExplicitQosEnabled(final boolean explicitQosEnabled)\n
    '''
def isExplicitQosEnabled():
    '''returns boolean\n\n
    isExplicitQosEnabled()\n
    '''
def setDeliveryMode():
    '''returns None\n\n
    setDeliveryMode(final int deliveryMode)\n
    '''
def getDeliveryMode():
    '''returns int\n\n
    getDeliveryMode()\n
    '''
def setPriority():
    '''returns None\n\n
    setPriority(final int priority)\n
    '''
def getPriority():
    '''returns int\n\n
    getPriority()\n
    '''
def setTimeToLive():
    '''returns None\n\n
    setTimeToLive(final long timeToLive)\n
    '''
def getTimeToLive():
    '''returns long\n\n
    getTimeToLive()\n
    '''
def execute():
    '''returns Object\n\n
    execute(final SessionCallback action, final boolean startConnection)\n
    execute(final SessionCallback action)\n
    execute(final ProducerCallback action)\n
    '''
def doInJms():
    '''returns Object\n\n
    doInJms(final Session session)\n
    doInJms(final Session session)\n
    doInJms(final Session session)\n
    doInJms(final Session session)\n
    doInJms(final Session session)\n
    doInJms(final Session session)\n
    doInJms(final Session session)\n
    '''
def send():
    '''returns None\n\n
    send(final MessageCreator messageCreator)\n
    send(final Destination destination, final MessageCreator messageCreator)\n
    send(final String destinationName, final MessageCreator messageCreator)\n
    '''
def convertAndSend():
    '''returns None\n\n
    convertAndSend(final Object message)\n
    convertAndSend(final Destination destination, final Object message)\n
    convertAndSend(final String destinationName, final Object message)\n
    convertAndSend(final Object message, final MessagePostProcessor postProcessor)\n
    convertAndSend(final Destination destination, final Object message, final MessagePostProcessor postProcessor)\n
    convertAndSend(final String destinationName, final Object message, final MessagePostProcessor postProcessor)\n
    '''
def createMessage():
    '''returns Message\n\n
    createMessage(final Session session)\n
    createMessage(final Session session)\n
    createMessage(final Session session)\n
    createMessage(final Session session)\n
    '''
def receive():
    '''returns Message\n\n
    receive()\n
    receive(final Destination destination)\n
    receive(final String destinationName)\n
    '''
def receiveSelected():
    '''returns Message\n\n
    receiveSelected(final String messageSelector)\n
    receiveSelected(final Destination destination, final String messageSelector)\n
    receiveSelected(final String destinationName, final String messageSelector)\n
    '''
def receiveAndConvert():
    '''returns Object\n\n
    receiveAndConvert()\n
    receiveAndConvert(final Destination destination)\n
    receiveAndConvert(final String destinationName)\n
    '''
def receiveSelectedAndConvert():
    '''returns Object\n\n
    receiveSelectedAndConvert(final String messageSelector)\n
    receiveSelectedAndConvert(final Destination destination, final String messageSelector)\n
    receiveSelectedAndConvert(final String destinationName, final String messageSelector)\n
    '''
