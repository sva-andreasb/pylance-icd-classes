CATEGORY = "String  \"Log4j Builder\""
def ():
    '''returns BuilderManager\n\n
    ()\n
    '''
def parseAppender():
    '''returns Appender\n\n
    parseAppender(final String className, final Element appenderElement, final XmlConfiguration config)\n
    parseAppender(final String name, final String className, final String prefix, final String layoutPrefix, final String filterPrefix, final Properties props, final PropertiesConfiguration config)\n
    '''
def parseFilter():
    '''returns Filter\n\n
    parseFilter(final String className, final Element filterElement, final XmlConfiguration config)\n
    parseFilter(final String className, final String filterPrefix, final Properties props, final PropertiesConfiguration config)\n
    '''
def parseLayout():
    '''returns Layout\n\n
    parseLayout(final String className, final Element layoutElement, final XmlConfiguration config)\n
    parseLayout(final String className, final String layoutPrefix, final Properties props, final PropertiesConfiguration config)\n
    '''
def parseRewritePolicy():
    '''returns RewritePolicy\n\n
    parseRewritePolicy(final String className, final Element rewriteElement, final XmlConfiguration config)\n
    parseRewritePolicy(final String className, final String policyPrefix, final Properties props, final PropertiesConfiguration config)\n
    '''
