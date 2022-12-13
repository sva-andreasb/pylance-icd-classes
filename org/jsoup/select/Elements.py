def Elements():
    '''    public Elements()
    public Elements(final int initialCapacity)
    public Elements(final Collection<Element> elements)
    public Elements(final List<Element> elements)
    public Elements(final Element... elements)
    '''
def clone():
    '''    public Elements clone()
    '''
def attr():
    '''    public String attr(final String attributeKey)
    public Elements attr(final String attributeKey, final String attributeValue)
    '''
def hasAttr():
    '''    public boolean hasAttr(final String attributeKey)
    '''
def eachAttr():
    '''    public List<String> eachAttr(final String attributeKey)
    '''
def removeAttr():
    '''    public Elements removeAttr(final String attributeKey)
    '''
def addClass():
    '''    public Elements addClass(final String className)
    '''
def removeClass():
    '''    public Elements removeClass(final String className)
    '''
def toggleClass():
    '''    public Elements toggleClass(final String className)
    '''
def hasClass():
    '''    public boolean hasClass(final String className)
    '''
def val():
    '''    public String val()
    public Elements val(final String value)
    '''
def text():
    '''    public String text()
    '''
def hasText():
    '''    public boolean hasText()
    '''
def eachText():
    '''    public List<String> eachText()
    '''
def html():
    '''    public String html()
    public Elements html(final String html)
    '''
def outerHtml():
    '''    public String outerHtml()
    '''
def toString():
    '''    public String toString()
    '''
def tagName():
    '''    public Elements tagName(final String tagName)
    '''
def prepend():
    '''    public Elements prepend(final String html)
    '''
def append():
    '''    public Elements append(final String html)
    '''
def before():
    '''    public Elements before(final String html)
    '''
def after():
    '''    public Elements after(final String html)
    '''
def wrap():
    '''    public Elements wrap(final String html)
    '''
def unwrap():
    '''    public Elements unwrap()
    '''
def empty():
    '''    public Elements empty()
    '''
def remove():
    '''    public Elements remove()
    '''
def select():
    '''    public Elements select(final String query)
    '''
def not():
    '''    public Elements not(final String query)
    '''
def eq():
    '''    public Elements eq(final int index)
    '''
def is():
    '''    public boolean is(final String query)
    '''
def next():
    '''    public Elements next()
    public Elements next(final String query)
    '''
def nextAll():
    '''    public Elements nextAll()
    public Elements nextAll(final String query)
    '''
def prev():
    '''    public Elements prev()
    public Elements prev(final String query)
    '''
def prevAll():
    '''    public Elements prevAll()
    public Elements prevAll(final String query)
    '''
def parents():
    '''    public Elements parents()
    '''
def first():
    '''    public Element first()
    '''
def last():
    '''    public Element last()
    '''
def traverse():
    '''    public Elements traverse(final NodeVisitor nodeVisitor)
    '''
def filter():
    '''    public Elements filter(final NodeFilter nodeFilter)
    '''
def forms():
    '''    public List<FormElement> forms()
    '''
