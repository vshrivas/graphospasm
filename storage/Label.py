import sys

# Storage
# Bytes 1-3: Label ID
# Bytes 4-103: Label
# Bytes 104-106: Next Label ID

class Label:
    LABEL_ID_OFFSET = 0
    LABEL_OFFSET = 3
    NEXT_LABEL_ID_OFFSET = 103
    MAX_LABEL_SIZE = 100

    storageSize = 106
    numLabels = 0

    def __init__(self, label, labelFile, labelID=None, nextLabelID=-1):
        if labelID is None:
            labelID = Label.numLabels
        self.labelID = labelID
        Label.numLabels += 1

        self.label = label

        self.labelFile = labelFile

        self.startOffset = self.labelID * Label.storageSize
        self.nextLabelID = nextLabelID

    def getLabelStr(self):
        return self.label
        
    def getLabelID(self):
        return self.labelID

    def setNextLabelID(self, nextLabelID):
        self.nextLabelID = nextLabelID

    def writeLabel(self, nextLabelID):
        # open label file
        storeFileName = self.labelFile.getFileName()
        storeFile = open(storeFileName, 'r+b')

        # seek to location for label and write label ID
        storeFile.seek(self.startOffset)
        storeFile.write(self.labelID.to_bytes(3, 
            byteorder = sys.byteorder, signed=True))

        # write label
        storeFile.seek(self.startOffset + Label.LABEL_OFFSET)
        # label is not of max size
        if(sys.getsizeof(self.label) != self.MAX_LABEL_SIZE):
            # pad key up to max size
            while len(self.label.encode('utf-8')) != self.MAX_LABEL_SIZE:
                self.label += ' '
        storeFile.write(bytearray(self.label, "utf8"))

        # write next label's ID
        storeFile.seek(self.startOffset + Label.NEXT_LABEL_ID_OFFSET)

        print("writing next label id: {0}".format(nextLabelID))
        storeFile.write(nextLabelID.to_bytes(3, 
            byteorder = sys.byteorder, signed=True))


        
