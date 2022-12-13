def doConfigure():
    '''    public void doConfigure(final String filename, final LoggerRepository repository)
    public void doConfigure(final URL url, final LoggerRepository repository)
    public void doConfigure(final InputStream inputStream, final LoggerRepository repository)
    public void doConfigure(final Reader reader, final LoggerRepository repository)
    public void doConfigure(final Element element, final LoggerRepository repository)
    '''
def configure():
    '''    public static void configure(final Element element)
    public static void configure(final String filename)
    public static void configure(final URL url)
    '''
def configureAndWatch():
    '''    public static void configureAndWatch(final String configFilename)
    public static void configureAndWatch(final String configFilename, final long delay)
    '''
def subst():
    '''    public static String subst(final String value, final Properties props)
    '''
def setParameter():
    '''    public static void setParameter(final Element elem, final PropertySetter propSetter, final Properties props)
    '''
def parseElement():
    '''    public static Object parseElement(final Element element, final Properties props, final Class expectedClass)
    '''
