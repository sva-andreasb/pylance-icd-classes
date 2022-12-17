WEAVING_ADAPTOR_VERBOSE = "String  \"aj.weaving.verbose\""
SHOW_WEAVE_INFO_PROPERTY = "String  \"org.aspectj.weaver.showWeaveInfo\""
TRACE_MESSAGES_PROPERTY = "String  \"org.aspectj.tracing.messages\""
def ():
    '''returns WeavingClassFileProvider\n\n
    (final WeavingClassLoader loader)\n
    (final GeneratedClassHandler handler, final URL[] classURLs, final URL[] aspectURLs)\n
    (final PrintWriter writer)\n
    (final PrintWriter writer)\n
    (final String name, final byte[] bytes)\n
    '''
def getMessageHolder():
    '''returns IMessageHolder\n\n
    getMessageHolder()\n
    '''
def addURL():
    '''returns None\n\n
    addURL(final URL url)\n
    '''
def weaveClass():
    '''returns byte[]\n\n
    weaveClass(final String name, final byte[] bytes)\n
    weaveClass(String name, byte[] bytes, final boolean mustWeave)\n
    '''
def getContextId():
    '''returns String\n\n
    getContextId()\n
    '''
def setActiveProtectionDomain():
    '''returns None\n\n
    setActiveProtectionDomain(final ProtectionDomain protectionDomain)\n
    '''
def flushMessages():
    '''returns None\n\n
    flushMessages()\n
    '''
def setDelegate():
    '''returns None\n\n
    setDelegate(final IMessageHandler messageHandler)\n
    '''
def handleMessage():
    '''returns boolean\n\n
    handleMessage(final IMessage message)\n
    handleMessage(final IMessage message)\n
    '''
def isIgnoring():
    '''returns boolean\n\n
    isIgnoring(final IMessage.Kind kind)\n
    isIgnoring(final IMessage.Kind kind)\n
    '''
def dontIgnore():
    '''returns None\n\n
    dontIgnore(final IMessage.Kind kind)\n
    dontIgnore(final IMessage.Kind kind)\n
    '''
def ignore():
    '''returns None\n\n
    ignore(final IMessage.Kind kind)\n
    ignore(final IMessage.Kind kind)\n
    '''
def getUnmodifiableListView():
    '''returns List<IMessage>\n\n
    getUnmodifiableListView()\n
    '''
def setApplyAtAspectJMungersOnly():
    '''returns None\n\n
    setApplyAtAspectJMungersOnly()\n
    '''
def isApplyAtAspectJMungersOnly():
    '''returns boolean\n\n
    isApplyAtAspectJMungersOnly()\n
    '''
def getBytes():
    '''returns byte[]\n\n
    getBytes()\n
    '''
def getClassFileIterator():
    '''returns Iterator<UnwovenClassFile>\n\n
    getClassFileIterator()\n
    '''
def getRequestor():
    '''returns IWeaveRequestor\n\n
    getRequestor()\n
    '''
def acceptResult():
    '''returns None\n\n
    acceptResult(final IUnwovenClassFile result)\n
    '''
def processingReweavableState():
    '''returns None\n\n
    processingReweavableState()\n
    '''
def addingTypeMungers():
    '''returns None\n\n
    addingTypeMungers()\n
    '''
def weavingAspects():
    '''returns None\n\n
    weavingAspects()\n
    '''
def weavingClasses():
    '''returns None\n\n
    weavingClasses()\n
    '''
def weaveCompleted():
    '''returns None\n\n
    weaveCompleted()\n
    '''
