from CommitEntities import *

from xml.etree.cElementTree import ElementTree, Element, SubElement, Comment, tostring, fromstring
from xml.dom import minidom

import untangle

class CommitQueryDataRequest:
    declaration = bytes('<?commitcrmxmlqueryrequest version="1.0" ?>', "ascii")
    
    def __init__(self, query, dataKind, name = "CommitAgent", maxRecordCnt = 255):
        self.query = query
        
        self.extAppName = name
        self.dataKind = dataKind
        self.maxRecordCnt = maxRecordCnt

        self.__createDomTree()
        
    def __createDomTree(self):
        self.tree = Element('CommitCRMQueryDataRequest')
        self.nameElement = SubElement(self.tree, 'ExternalApplicationName')
        self.nameElement.text = self.extAppName
        self.dataKindElement = SubElement(self.tree, 'Datakind')
        self.dataKindElement.text = self.dataKind
        self.recordCountElement = SubElement(self.tree, 'MaxRecordCount')
        self.recordCountElement.text = str(self.maxRecordCnt)

        self.queryElement = SubElement(self.tree, 'Query')
        self.whereElement = SubElement(self.queryElement, 'Where')

        #test
        self.queryContentElement = SubElement(self.whereElement, "FLDCRDFULLNAME", {"op" : "="})
        self.queryContentElement.text = "Bart De Hantsetters"

        self.orderElement = SubElement(self.queryElement, 'Order')

    def getDomTreeStr(self):
        return self.declaration + tostring(self.tree)

    def printDomTree(self):
        print(self.__prettify(self.getDomTreeStr()))

    def __prettify(self, dom_str):
        reparsed = minidom.parseString(dom_str)
        return reparsed.toprettyxml(indent="    ")

class CommitGetRecordDataRequest:
    def __init__(recId, fieldsList):
        pass

class CommitQueryDataResponse:
    def __init__(self, response):
        self.response_str = response
        self.doc = untangle.parse(self.response_str)

    def getRecIds(self):
        self.recIds = []
        for data in self.doc.CommitCRMQueryDataResponse.RecordData:
            self.recIds.append(data.get_elements()[0].cdata)

        return self.recIds
    
