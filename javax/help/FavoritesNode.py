HEADER = "String  \"<?xml version=\\"1.0\\" encoding=\\"UTF-8\\"?>\n<!DOCTYPE favorites\n PUBLIC \\"-//Sun Microsystems Inc.//DTD JavaHelp Favorites Version 2.0//EN\\"\n        \\"http://java.sun.com/products/javahelp/favorites_2_0.dtd\\">\n\n<favorites version=\\"2.0\\">\n\""
ELEMENT = "String  \"favoriteitem\""
FOOTER = "String  \"</favorites>\""
def ():
    '''returns FavoritesNode\n\n
    (final FavoritesItem favoritesItem)\n
    '''
def getAllowsChildren():
    '''returns boolean\n\n
    getAllowsChildren()\n
    '''
def add():
    '''returns None\n\n
    add(final DefaultMutableTreeNode newChild)\n
    '''
def remove():
    '''returns None\n\n
    remove(final DefaultMutableTreeNode aChild)\n
    '''
def getVisibleChildCount():
    '''returns int\n\n
    getVisibleChildCount()\n
    '''
def getOffset():
    '''returns String\n\n
    getOffset()\n
    '''
def export():
    '''returns None\n\n
    export(final OutputStream out)\n
    '''
def exportNode():
    '''returns None\n\n
    exportNode(final OutputStreamWriter outputStreamWriter)\n
    '''
def exportHeader():
    '''returns OutputStreamWriter\n\n
    exportHeader(final OutputStream out)\n
    '''
def getXMLHeader():
    '''returns String\n\n
    getXMLHeader()\n
    '''
def getXMLElement():
    '''returns String\n\n
    getXMLElement()\n
    '''
def getDeepCopy():
    '''returns FavoritesNode\n\n
    getDeepCopy()\n
    '''
def isVisible():
    '''returns boolean\n\n
    isVisible()\n
    '''
def setVisible():
    '''returns None\n\n
    setVisible(final boolean visible)\n
    '''
