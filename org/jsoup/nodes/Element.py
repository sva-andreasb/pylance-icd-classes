def Element():
'''public Element(final String tag)
public Element(final Tag tag, final String baseUri, final Attributes attributes)
public Element(final Tag tag, final String baseUri)
'''
pass
def attributes():
'''public Attributes attributes()
'''
pass
def baseUri():
'''public String baseUri()
'''
pass
def childNodeSize():
'''public int childNodeSize()
'''
pass
def nodeName():
'''public String nodeName()
'''
pass
def tagName():
'''public String tagName()
public Element tagName(final String tagName)
'''
pass
def normalName():
'''public String normalName()
'''
pass
def tag():
'''public Tag tag()
'''
pass
def isBlock():
'''public boolean isBlock()
'''
pass
def id():
'''public String id()
'''
pass
def attr():
'''public Element attr(final String attributeKey, final String attributeValue)
public Element attr(final String attributeKey, final boolean attributeValue)
'''
pass
def dataset():
'''public Map<String, String> dataset()
'''
pass
def parent():
'''public final Element parent()
'''
pass
def parents():
'''public Elements parents()
'''
pass
def child():
'''public Element child(final int index)
'''
pass
def children():
'''public Elements children()
'''
pass
def textNodes():
'''public List<TextNode> textNodes()
'''
pass
def dataNodes():
'''public List<DataNode> dataNodes()
'''
pass
def select():
'''public Elements select(final String cssQuery)
'''
pass
def selectFirst():
'''public Element selectFirst(final String cssQuery)
'''
pass
def is():
'''public boolean is(final String cssQuery)
public boolean is(final Evaluator evaluator)
'''
pass
def appendChild():
'''public Element appendChild(final Node child)
'''
pass
def appendTo():
'''public Element appendTo(final Element parent)
'''
pass
def prependChild():
'''public Element prependChild(final Node child)
'''
pass
def insertChildren():
'''public Element insertChildren(int index, final Collection<? extends Node> children)
public Element insertChildren(int index, final Node... children)
'''
pass
def appendElement():
'''public Element appendElement(final String tagName)
'''
pass
def prependElement():
'''public Element prependElement(final String tagName)
'''
pass
def appendText():
'''public Element appendText(final String text)
'''
pass
def prependText():
'''public Element prependText(final String text)
'''
pass
def append():
'''public Element append(final String html)
'''
pass
def prepend():
'''public Element prepend(final String html)
'''
pass
def before():
'''public Element before(final String html)
public Element before(final Node node)
'''
pass
def after():
'''public Element after(final String html)
public Element after(final Node node)
'''
pass
def empty():
'''public Element empty()
'''
pass
def wrap():
'''public Element wrap(final String html)
'''
pass
def cssSelector():
'''public String cssSelector()
'''
pass
def siblingElements():
'''public Elements siblingElements()
'''
pass
def nextElementSibling():
'''public Element nextElementSibling()
'''
pass
def nextElementSiblings():
'''public Elements nextElementSiblings()
'''
pass
def previousElementSibling():
'''public Element previousElementSibling()
'''
pass
def previousElementSiblings():
'''public Elements previousElementSiblings()
'''
pass
def firstElementSibling():
'''public Element firstElementSibling()
'''
pass
def elementSiblingIndex():
'''public int elementSiblingIndex()
'''
pass
def lastElementSibling():
'''public Element lastElementSibling()
'''
pass
def getElementsByTag():
'''public Elements getElementsByTag(String tagName)
'''
pass
def getElementById():
'''public Element getElementById(final String id)
'''
pass
def getElementsByClass():
'''public Elements getElementsByClass(final String className)
'''
pass
def getElementsByAttribute():
'''public Elements getElementsByAttribute(String key)
'''
pass
def getElementsByAttributeStarting():
'''public Elements getElementsByAttributeStarting(String keyPrefix)
'''
pass
def getElementsByAttributeValue():
'''public Elements getElementsByAttributeValue(final String key, final String value)
'''
pass
def getElementsByAttributeValueNot():
'''public Elements getElementsByAttributeValueNot(final String key, final String value)
'''
pass
def getElementsByAttributeValueStarting():
'''public Elements getElementsByAttributeValueStarting(final String key, final String valuePrefix)
'''
pass
def getElementsByAttributeValueEnding():
'''public Elements getElementsByAttributeValueEnding(final String key, final String valueSuffix)
'''
pass
def getElementsByAttributeValueContaining():
'''public Elements getElementsByAttributeValueContaining(final String key, final String match)
'''
pass
def getElementsByAttributeValueMatching():
'''public Elements getElementsByAttributeValueMatching(final String key, final Pattern pattern)
public Elements getElementsByAttributeValueMatching(final String key, final String regex)
'''
pass
def getElementsByIndexLessThan():
'''public Elements getElementsByIndexLessThan(final int index)
'''
pass
def getElementsByIndexGreaterThan():
'''public Elements getElementsByIndexGreaterThan(final int index)
'''
pass
def getElementsByIndexEquals():
'''public Elements getElementsByIndexEquals(final int index)
'''
pass
def getElementsContainingText():
'''public Elements getElementsContainingText(final String searchText)
'''
pass
def getElementsContainingOwnText():
'''public Elements getElementsContainingOwnText(final String searchText)
'''
pass
def getElementsMatchingText():
'''public Elements getElementsMatchingText(final Pattern pattern)
public Elements getElementsMatchingText(final String regex)
'''
pass
def getElementsMatchingOwnText():
'''public Elements getElementsMatchingOwnText(final Pattern pattern)
public Elements getElementsMatchingOwnText(final String regex)
'''
pass
def getAllElements():
'''public Elements getAllElements()
'''
pass
def text():
'''public String text()
public Element text(final String text)
'''
pass
def head():
'''public void head(final Node node, final int depth)
public void head(final Node node, final int depth)
'''
pass
def tail():
'''public void tail(final Node node, final int depth)
public void tail(final Node node, final int depth)
'''
pass
def wholeText():
'''public String wholeText()
'''
pass
def ownText():
'''public String ownText()
'''
pass
def hasText():
'''public boolean hasText()
'''
pass
def data():
'''public String data()
'''
pass
def className():
'''public String className()
'''
pass
def classNames():
'''public Set<String> classNames()
public Element classNames(final Set<String> classNames)
'''
pass
def hasClass():
'''public boolean hasClass(final String className)
'''
pass
def addClass():
'''public Element addClass(final String className)
'''
pass
def removeClass():
'''public Element removeClass(final String className)
'''
pass
def toggleClass():
'''public Element toggleClass(final String className)
'''
pass
def val():
'''public String val()
public Element val(final String value)
'''
pass
def html():
'''public String html()
public <T extends Appendable> T html(final T appendable)
public Element html(final String html)
'''
pass
def clone():
'''public Element clone()
'''
pass
def shallowClone():
'''public Element shallowClone()
'''
pass
def onContentsChanged():
'''public void onContentsChanged()
'''
pass
