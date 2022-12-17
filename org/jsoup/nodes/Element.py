def ():
    '''returns Element\n\n
    (final String tag)\n
    (final Tag tag, final String baseUri, final Attributes attributes)\n
    (final Tag tag, final String baseUri)\n
    '''
def attributes():
    '''returns Attributes\n\n
    attributes()\n
    '''
def baseUri():
    '''returns String\n\n
    baseUri()\n
    '''
def childNodeSize():
    '''returns int\n\n
    childNodeSize()\n
    '''
def nodeName():
    '''returns String\n\n
    nodeName()\n
    '''
def tagName():
    '''returns Element\n\n
    tagName()\n
    tagName(final String tagName)\n
    '''
def normalName():
    '''returns String\n\n
    normalName()\n
    '''
def tag():
    '''returns Tag\n\n
    tag()\n
    '''
def isBlock():
    '''returns boolean\n\n
    isBlock()\n
    '''
def id():
    '''returns String\n\n
    id()\n
    '''
def attr():
    '''returns Element\n\n
    attr(final String attributeKey, final String attributeValue)\n
    attr(final String attributeKey, final boolean attributeValue)\n
    '''
def parents():
    '''returns Elements\n\n
    parents()\n
    '''
def child():
    '''returns Element\n\n
    child(final int index)\n
    '''
def children():
    '''returns Elements\n\n
    children()\n
    '''
def textNodes():
    '''returns List<TextNode>\n\n
    textNodes()\n
    '''
def dataNodes():
    '''returns List<DataNode>\n\n
    dataNodes()\n
    '''
def select():
    '''returns Elements\n\n
    select(final String cssQuery)\n
    '''
def selectFirst():
    '''returns Element\n\n
    selectFirst(final String cssQuery)\n
    '''
def is():
    '''returns boolean\n\n
    is(final String cssQuery)\n
    is(final Evaluator evaluator)\n
    '''
def appendChild():
    '''returns Element\n\n
    appendChild(final Node child)\n
    '''
def appendTo():
    '''returns Element\n\n
    appendTo(final Element parent)\n
    '''
def prependChild():
    '''returns Element\n\n
    prependChild(final Node child)\n
    '''
def insertChildren():
    '''returns Element\n\n
    insertChildren(int index, final Collection<? extends Node> children)\n
    insertChildren(int index, final Node... children)\n
    '''
def appendElement():
    '''returns Element\n\n
    appendElement(final String tagName)\n
    '''
def prependElement():
    '''returns Element\n\n
    prependElement(final String tagName)\n
    '''
def appendText():
    '''returns Element\n\n
    appendText(final String text)\n
    '''
def prependText():
    '''returns Element\n\n
    prependText(final String text)\n
    '''
def append():
    '''returns Element\n\n
    append(final String html)\n
    '''
def prepend():
    '''returns Element\n\n
    prepend(final String html)\n
    '''
def before():
    '''returns Element\n\n
    before(final String html)\n
    before(final Node node)\n
    '''
def after():
    '''returns Element\n\n
    after(final String html)\n
    after(final Node node)\n
    '''
def empty():
    '''returns Element\n\n
    empty()\n
    '''
def wrap():
    '''returns Element\n\n
    wrap(final String html)\n
    '''
def cssSelector():
    '''returns String\n\n
    cssSelector()\n
    '''
def siblingElements():
    '''returns Elements\n\n
    siblingElements()\n
    '''
def nextElementSibling():
    '''returns Element\n\n
    nextElementSibling()\n
    '''
def nextElementSiblings():
    '''returns Elements\n\n
    nextElementSiblings()\n
    '''
def previousElementSibling():
    '''returns Element\n\n
    previousElementSibling()\n
    '''
def previousElementSiblings():
    '''returns Elements\n\n
    previousElementSiblings()\n
    '''
def firstElementSibling():
    '''returns Element\n\n
    firstElementSibling()\n
    '''
def elementSiblingIndex():
    '''returns int\n\n
    elementSiblingIndex()\n
    '''
def lastElementSibling():
    '''returns Element\n\n
    lastElementSibling()\n
    '''
def getElementsByTag():
    '''returns Elements\n\n
    getElementsByTag(String tagName)\n
    '''
def getElementById():
    '''returns Element\n\n
    getElementById(final String id)\n
    '''
def getElementsByClass():
    '''returns Elements\n\n
    getElementsByClass(final String className)\n
    '''
def getElementsByAttribute():
    '''returns Elements\n\n
    getElementsByAttribute(String key)\n
    '''
def getElementsByAttributeStarting():
    '''returns Elements\n\n
    getElementsByAttributeStarting(String keyPrefix)\n
    '''
def getElementsByAttributeValue():
    '''returns Elements\n\n
    getElementsByAttributeValue(final String key, final String value)\n
    '''
def getElementsByAttributeValueNot():
    '''returns Elements\n\n
    getElementsByAttributeValueNot(final String key, final String value)\n
    '''
def getElementsByAttributeValueStarting():
    '''returns Elements\n\n
    getElementsByAttributeValueStarting(final String key, final String valuePrefix)\n
    '''
def getElementsByAttributeValueEnding():
    '''returns Elements\n\n
    getElementsByAttributeValueEnding(final String key, final String valueSuffix)\n
    '''
def getElementsByAttributeValueContaining():
    '''returns Elements\n\n
    getElementsByAttributeValueContaining(final String key, final String match)\n
    '''
def getElementsByAttributeValueMatching():
    '''returns Elements\n\n
    getElementsByAttributeValueMatching(final String key, final Pattern pattern)\n
    getElementsByAttributeValueMatching(final String key, final String regex)\n
    '''
def getElementsByIndexLessThan():
    '''returns Elements\n\n
    getElementsByIndexLessThan(final int index)\n
    '''
def getElementsByIndexGreaterThan():
    '''returns Elements\n\n
    getElementsByIndexGreaterThan(final int index)\n
    '''
def getElementsByIndexEquals():
    '''returns Elements\n\n
    getElementsByIndexEquals(final int index)\n
    '''
def getElementsContainingText():
    '''returns Elements\n\n
    getElementsContainingText(final String searchText)\n
    '''
def getElementsContainingOwnText():
    '''returns Elements\n\n
    getElementsContainingOwnText(final String searchText)\n
    '''
def getElementsMatchingText():
    '''returns Elements\n\n
    getElementsMatchingText(final Pattern pattern)\n
    getElementsMatchingText(final String regex)\n
    '''
def getElementsMatchingOwnText():
    '''returns Elements\n\n
    getElementsMatchingOwnText(final Pattern pattern)\n
    getElementsMatchingOwnText(final String regex)\n
    '''
def getAllElements():
    '''returns Elements\n\n
    getAllElements()\n
    '''
def text():
    '''returns Element\n\n
    text()\n
    text(final String text)\n
    '''
def head():
    '''returns None\n\n
    head(final Node node, final int depth)\n
    head(final Node node, final int depth)\n
    '''
def tail():
    '''returns None\n\n
    tail(final Node node, final int depth)\n
    tail(final Node node, final int depth)\n
    '''
def wholeText():
    '''returns String\n\n
    wholeText()\n
    '''
def ownText():
    '''returns String\n\n
    ownText()\n
    '''
def hasText():
    '''returns boolean\n\n
    hasText()\n
    '''
def data():
    '''returns String\n\n
    data()\n
    '''
def className():
    '''returns String\n\n
    className()\n
    '''
def classNames():
    '''returns Element\n\n
    classNames()\n
    classNames(final Set<String> classNames)\n
    '''
def hasClass():
    '''returns boolean\n\n
    hasClass(final String className)\n
    '''
def addClass():
    '''returns Element\n\n
    addClass(final String className)\n
    '''
def removeClass():
    '''returns Element\n\n
    removeClass(final String className)\n
    '''
def toggleClass():
    '''returns Element\n\n
    toggleClass(final String className)\n
    '''
def val():
    '''returns Element\n\n
    val()\n
    val(final String value)\n
    '''
def html():
    '''returns Element\n\n
    html()\n
    html(final String html)\n
    '''
def clone():
    '''returns Element\n\n
    clone()\n
    '''
def shallowClone():
    '''returns Element\n\n
    shallowClone()\n
    '''
def onContentsChanged():
    '''returns None\n\n
    onContentsChanged()\n
    '''
