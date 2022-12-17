def ():
    '''returns State\n\n
    (final Component component)\n
    (final Graphics graphics, final Dimension size)\n
    ()\n
    (final Graphics2D g)\n
    '''
def gsave():
    '''returns None\n\n
    gsave()\n
    '''
def grestore():
    '''returns None\n\n
    grestore()\n
    '''
def grestoreall():
    '''returns None\n\n
    grestoreall()\n
    '''
def initgraphics():
    '''returns None\n\n
    initgraphics()\n
    '''
def newpath():
    '''returns None\n\n
    newpath()\n
    '''
def moveto():
    '''returns None\n\n
    moveto(final double x, final double y)\n
    moveto(final Point2D p)\n
    '''
def rmoveto():
    '''returns None\n\n
    rmoveto(final double dx, final double dy)\n
    '''
def lineto():
    '''returns None\n\n
    lineto(final double x, final double y)\n
    lineto(final Point2D p)\n
    '''
def rlineto():
    '''returns None\n\n
    rlineto(final double dx, final double dy)\n
    '''
def arc():
    '''returns None\n\n
    arc(final double cx, final double cy, final double r, final double ang1, final double ang2)\n
    '''
def arcn():
    '''returns None\n\n
    arcn(final double cx, final double cy, final double r, final double ang1, final double ang2)\n
    '''
def curveto():
    '''returns None\n\n
    curveto(final double x1, final double y1, final double x2, final double y2, final double x3, final double y3)\n
    '''
def rcurveto():
    '''returns None\n\n
    rcurveto(final double dx1, final double dy1, final double dx2, final double dy2, final double dx3, final double dy3)\n
    '''
def closepath():
    '''returns None\n\n
    closepath()\n
    '''
def clippath():
    '''returns None\n\n
    clippath()\n
    '''
def erasepage():
    '''returns None\n\n
    erasepage()\n
    '''
def charpath():
    '''returns None\n\n
    charpath(final String aString, final boolean adjustForStroking)\n
    '''
def showpage():
    '''returns None\n\n
    showpage()\n
    '''
def show():
    '''returns None\n\n
    show(final String string)\n
    '''
def fill():
    '''returns None\n\n
    fill()\n
    '''
def eofill():
    '''returns None\n\n
    eofill()\n
    '''
def stroke():
    '''returns None\n\n
    stroke()\n
    '''
def rectfill():
    '''returns None\n\n
    rectfill(final double x, final double y, final double width, final double height)\n
    rectfill(final Rectangle2D rect)\n
    '''
def rectstroke():
    '''returns None\n\n
    rectstroke(final double x, final double y, final double width, final double height)\n
    rectstroke(final Rectangle2D rect)\n
    '''
def rectpath():
    '''returns None\n\n
    rectpath(final double x, final double y, final double width, final double height)\n
    '''
def findFont():
    '''returns Font\n\n
    findFont(String fontname)\n
    '''
def recordState():
    '''returns None\n\n
    recordState(final Graphics2D g)\n
    '''
def stampState():
    '''returns None\n\n
    stampState(final Graphics2D g, final Dimension size)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
