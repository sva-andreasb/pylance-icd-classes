CATEGORY = "String  \"Log4j Builder\""
def BuilderManager():
    '''public BuilderManager()
    '''
def parseAppender():
    '''public Appender parseAppender(final String className, final Element appenderElement, final XmlConfiguration config)
    public Appender parseAppender(final String name, final String className, final String prefix, final String layoutPrefix, final String filterPrefix, final Properties props, final PropertiesConfiguration config)
    '''
def parseFilter():
    '''public Filter parseFilter(final String className, final Element filterElement, final XmlConfiguration config)
    public Filter parseFilter(final String className, final String filterPrefix, final Properties props, final PropertiesConfiguration config)
    '''
def parseLayout():
    '''public Layout parseLayout(final String className, final Element layoutElement, final XmlConfiguration config)
    public Layout parseLayout(final String className, final String layoutPrefix, final Properties props, final PropertiesConfiguration config)
    '''
def parseRewritePolicy():
    '''public RewritePolicy parseRewritePolicy(final String className, final Element rewriteElement, final XmlConfiguration config)
    public RewritePolicy parseRewritePolicy(final String className, final String policyPrefix, final Properties props, final PropertiesConfiguration config)
    '''
