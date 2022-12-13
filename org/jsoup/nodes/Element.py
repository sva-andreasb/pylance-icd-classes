def Element():
    '''    public Element(final String tag)
    public Element(final Tag tag, final String baseUri, final Attributes attributes)
    public Element(final Tag tag, final String baseUri)
    '''
def attributes():
    '''    public Attributes attributes()
    '''
def baseUri():
    '''    public String baseUri()
    '''
def childNodeSize():
    '''    public int childNodeSize()
    '''
def nodeName():
    '''    public String nodeName()
    '''
def tagName():
    '''    public String tagName()
    public Element tagName(final String tagName)
    '''
def normalName():
    '''    public String normalName()
    '''
def tag():
    '''    public Tag tag()
    '''
def isBlock():
    '''    public boolean isBlock()
    '''
def id():
    '''    public String id()
    '''
def attr():
    '''    public Element attr(final String attributeKey, final String attributeValue)
    public Element attr(final String attributeKey, final boolean attributeValue)
    '''
def dataset():
    '''    public Map<String, String> dataset()
    '''
def parent():
    '''    public final Element parent()
    '''
def parents():
    '''    public Elements parents()
    '''
def child():
    '''    public Element child(final int index)
    '''
def children():
    '''    public Elements children()
    '''
def textNodes():
    '''    public List<TextNode> textNodes()
    '''
def dataNodes():
    '''    public List<DataNode> dataNodes()
    '''
def select():
    '''    public Elements select(final String cssQuery)
    '''
def selectFirst():
    '''    public Element selectFirst(final String cssQuery)
    '''
def is():
    '''    public boolean is(final String cssQuery)
    public boolean is(final Evaluator evaluator)
    '''
def appendChild():
    '''    public Element appendChild(final Node child)
    '''
def appendTo():
    '''    public Element appendTo(final Element parent)
    '''
def prependChild():
    '''    public Element prependChild(final Node child)
    '''
def insertChildren():
    '''    public Element insertChildren(int index, final Collection<? extends Node> children)
    public Element insertChildren(int index, final Node... children)
    '''
def appendElement():
    '''    public Element appendElement(final String tagName)
    '''
def prependElement():
    '''    public Element prependElement(final String tagName)
    '''
def appendText():
    '''    public Element appendText(final String text)
    '''
def prependText():
    '''    public Element prependText(final String text)
    '''
def append():
    '''    public Element append(final String html)
    '''
def prepend():
    '''    public Element prepend(final String html)
    '''
def before():
    '''    public Element before(final String html)
    public Element before(final Node node)
    '''
def after():
    '''    public Element after(final String html)
    public Element after(final Node node)
    '''
def empty():
    '''    public Element empty()
    '''
def wrap():
    '''    public Element wrap(final String html)
    '''
def cssSelector():
    '''    public String cssSelector()
    '''
def siblingElements():
    '''    public Elements siblingElements()
    '''
def nextElementSibling():
    '''    public Element nextElementSibling()
    '''
def nextElementSiblings():
    '''    public Elements nextElementSiblings()
    '''
def previousElementSibling():
    '''    public Element previousElementSibling()
    '''
def previousElementSiblings():
    '''    public Elements previousElementSiblings()
    '''
def firstElementSibling():
    '''    public Element firstElementSibling()
    '''
def elementSiblingIndex():
    '''    public int elementSiblingIndex()
    '''
def lastElementSibling():
    '''    public Element lastElementSibling()
    '''
def getElementsByTag():
    '''    public Elements getElementsByTag(String tagName)
    '''
def getElementById():
    '''    public Element getElementById(final String id)
    '''
def getElementsByClass():
    '''    public Elements getElementsByClass(final String className)
    '''
def getElementsByAttribute():
    '''    public Elements getElementsByAttribute(String key)
    '''
def getElementsByAttributeStarting():
    '''    public Elements getElementsByAttributeStarting(String keyPrefix)
    '''
def getElementsByAttributeValue():
    '''    public Elements getElementsByAttributeValue(final String key, final String value)
    '''
def getElementsByAttributeValueNot():
    '''    public Elements getElementsByAttributeValueNot(final String key, final String value)
    '''
def getElementsByAttributeValueStarting():
    '''    public Elements getElementsByAttributeValueStarting(final String key, final String valuePrefix)
    '''
def getElementsByAttributeValueEnding():
    '''    public Elements getElementsByAttributeValueEnding(final String key, final String valueSuffix)
    '''
def getElementsByAttributeValueContaining():
    '''    public Elements getElementsByAttributeValueContaining(final String key, final String match)
    '''
def getElementsByAttributeValueMatching():
    '''    public Elements getElementsByAttributeValueMatching(final String key, final Pattern pattern)
    public Elements getElementsByAttributeValueMatching(final String key, final String regex)
    '''
def getElementsByIndexLessThan():
    '''    public Elements getElementsByIndexLessThan(final int index)
    '''
def getElementsByIndexGreaterThan():
    '''    public Elements getElementsByIndexGreaterThan(final int index)
    '''
def getElementsByIndexEquals():
    '''    public Elements getElementsByIndexEquals(final int index)
    '''
def getElementsContainingText():
    '''    public Elements getElementsContainingText(final String searchText)
    '''
def getElementsContainingOwnText():
    '''    public Elements getElementsContainingOwnText(final String searchText)
    '''
def getElementsMatchingText():
    '''    public Elements getElementsMatchingText(final Pattern pattern)
    public Elements getElementsMatchingText(final String regex)
    '''
def getElementsMatchingOwnText():
    '''    public Elements getElementsMatchingOwnText(final Pattern pattern)
    public Elements getElementsMatchingOwnText(final String regex)
    '''
def getAllElements():
    '''    public Elements getAllElements()
    '''
def text():
    '''    public String text()
    public Element text(final String text)
    '''
def head():
    '''    public void head(final Node node, final int depth)
    public void head(final Node node, final int depth)
    '''
def tail():
    '''    public void tail(final Node node, final int depth)
    public void tail(final Node node, final int depth)
    '''
def wholeText():
    '''    public String wholeText()
    '''
def ownText():
    '''    public String ownText()
    '''
def hasText():
    '''    public boolean hasText()
    '''
def data():
    '''    public String data()
    '''
def className():
    '''    public String className()
    '''
def classNames():
    '''    public Set<String> classNames()
    public Element classNames(final Set<String> classNames)
    '''
def hasClass():
    '''    public boolean hasClass(final String className)
    '''
def addClass():
    '''    public Element addClass(final String className)
    '''
def removeClass():
    '''    public Element removeClass(final String className)
    '''
def toggleClass():
    '''    public Element toggleClass(final String className)
    '''
def val():
    '''    public String val()
    public Element val(final String value)
    '''
def html():
    '''    public String html()
    public <T extends Appendable> T html(final T appendable)
    public Element html(final String html)
    '''
def clone():
    '''    public Element clone()
    '''
def shallowClone():
    '''    public Element shallowClone()
    '''
def onContentsChanged():
    '''    public void onContentsChanged()
    '''
