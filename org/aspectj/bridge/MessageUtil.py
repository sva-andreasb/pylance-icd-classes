def abort():
    '''    public static boolean abort(final IMessageHandler handler, final String message)
    public static boolean abort(final IMessageHandler handler, final String message, final Throwable t)
    public static IMessage abort(final String message)
    public static IMessage abort(final String message, final Throwable thrown)
    '''
def fail():
    '''    public static boolean fail(final IMessageHandler handler, final String message)
    public static boolean fail(final IMessageHandler handler, final String message, final Throwable thrown)
    public static IMessage fail(final String message)
    public static IMessage fail(final String message, final Throwable thrown)
    '''
def error():
    '''    public static boolean error(final IMessageHandler handler, final String message)
    public static IMessage error(final String message, final ISourceLocation location)
    public static IMessage error(final String message)
    '''
def warn():
    '''    public static boolean warn(final IMessageHandler handler, final String message)
    public static IMessage warn(final String message, final ISourceLocation location)
    public static IMessage warn(final String message)
    '''
def debug():
    '''    public static boolean debug(final IMessageHandler handler, final String message)
    public static IMessage debug(final String message)
    '''
def info():
    '''    public static boolean info(final IMessageHandler handler, final String message)
    public static IMessage info(final String message)
    '''
def printMessageCounts():
    '''    public static void printMessageCounts(final PrintStream out, final IMessageHolder messageHolder)
    public static void printMessageCounts(final PrintStream out, final IMessageHolder holder, final String prefix)
    '''
def print():
    '''    public static void print(final PrintStream out, final IMessageHolder messageHolder)
    public static void print(final PrintStream out, final IMessageHolder holder, final String prefix)
    public static void print(final PrintStream out, final IMessageHolder holder, final String prefix, final IMessageRenderer renderer)
    public static void print(final PrintStream out, final IMessageHolder holder, final String prefix, final IMessageRenderer renderer, final IMessageHandler selector)
    public static void print(final PrintStream out, final IMessageHolder holder, final String prefix, IMessageRenderer renderer, IMessageHandler selector, final boolean printSummary)
    '''
def toShortString():
    '''    public static String toShortString(final IMessage message)
    '''
def numMessages():
    '''    public static int numMessages(final List<IMessage> messages, final IMessage.Kind kind, final boolean orGreater)
    '''
def getMessagesExcept():
    '''    public static IMessage[] getMessagesExcept(final IMessageHolder holder, final IMessage.Kind kind, final boolean orGreater)
    '''
def handleMessage():
    '''    public boolean handleMessage(final IMessage message)
    public boolean handleMessage(final IMessage message)
    '''
def isIgnoring():
    '''    public boolean isIgnoring(final IMessage.Kind kind)
    public boolean isIgnoring(final IMessage.Kind kind)
    '''
def dontIgnore():
    '''    public void dontIgnore(final IMessage.Kind kind)
    public void dontIgnore(final IMessage.Kind kind)
    '''
def ignore():
    '''    public void ignore(final IMessage.Kind kind)
    public void ignore(final IMessage.Kind kind)
    '''
def getMessages():
    '''    public static List<IMessage> getMessages(final IMessageHolder holder, final IMessage.Kind kind, final boolean orGreater, final String infix)
    public static List<IMessage> getMessages(final List<IMessage> messages, final IMessage.Kind kind)
    '''
def visitMessages():
    '''    public static IMessage[] visitMessages(final IMessageHolder holder, final IMessageHandler visitor, final boolean accumulate, final boolean abortOnFail)
    public static IMessage[] visitMessages(final IMessage[] messages, final IMessageHandler visitor, final boolean accumulate, final boolean abortOnFail)
    public static IMessage[] visitMessages(final Collection<IMessage> messages, final IMessageHandler visitor, final boolean accumulate, final boolean abortOnFail)
    '''
def makeSelector():
    '''    public static IMessageHandler makeSelector(final IMessage.Kind kind, final boolean orGreater, final String infix)
    '''
def renderMessage():
    '''    public static String renderMessage(final IMessage message)
    public static String renderMessage(final IMessage message, final boolean elide)
    '''
def addExtraSourceLocations():
    '''    public static String addExtraSourceLocations(final IMessage message, final String baseMessage)
    '''
def renderSourceLocation():
    '''    public static String renderSourceLocation(final ISourceLocation loc)
    '''
def renderMessageLine():
    '''    public static String renderMessageLine(final IMessage message, int textScale, int locScale, int max)
    '''
def renderCounts():
    '''    public static String renderCounts(final IMessageHolder holder)
    '''
def handlerPrintStream():
    '''    public static PrintStream handlerPrintStream(final IMessageHandler handler, final IMessage.Kind kind, final OutputStream overage, final String prefix)
    '''
def println():
    '''    public void println()
    public void println(final Object o)
    public void println(final String input)
    '''
def handleAll():
    '''    public static boolean handleAll(final IMessageHandler sink, final IMessageHolder source, final boolean fastFail)
    public static boolean handleAll(final IMessageHandler sink, final IMessageHolder source, final IMessage.Kind kind, final boolean orGreater, final boolean fastFail)
    public static boolean handleAll(final IMessageHandler sink, final IMessage[] sources, final boolean fastFail)
    '''
def handleAllExcept():
    '''    public static boolean handleAllExcept(final IMessageHandler sink, final IMessageHolder source, final IMessage.Kind kind, final boolean orGreater, final boolean fastFail)
    '''
def toString():
    '''    public String toString()
    public String toString()
    public String toString()
    public String toString()
    public String toString()
    public String toString()
    public String toString()
    public String toString()
    public String toString()
    public String toString()
    '''
def renderToString():
    '''    public String renderToString(final IMessage message)
    public String renderToString(final IMessage message)
    public String renderToString(final IMessage message)
    public String renderToString(final IMessage message)
    public String renderToString(final IMessage message)
    public String renderToString(final IMessage message)
    public String renderToString(final IMessage message)
    public String renderToString(final IMessage message)
    public String renderToString(final IMessage message)
    public String renderToString(final IMessage message)
    '''
