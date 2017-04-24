# Storage
# Bytes 1-3: Label ID
# Bytes 4-7: Label
# Bytes 8-11: Next Label ID
class Label:
    LABEL_ID_OFFSET = 0
    LABEL_OFFSET = 3
    NEXT_LABEL_ID_OFFSET = 7

    storageSize = 11
    numLabels = 0

    def _init_(self, labelID=numLabels, label, labelFile):
        self.labelID = labelID

        self.label = label
        numLabels += 1

        self.labelFile = labelFile

        self.startOffset = self.labelID * Label.storageSize

    def writeLabel(self, nextLabelID):
        # open label file
		storeFileName = self.labelFile.getFileName()
		storeFile = open(storeFileName, 'a')

        # seek to location for label and write label ID
		storeFile.seek(self.startOffset)
        storeFile.write(self.labelID)

        # write label
        storeFile.seek(self.startOffset + Label.LABEL_OFFSET)
        storeFile.write(self.label)

        # write next label's ID
        storeFile.seek(self.startOffset + Label.NEXT_LABEL_ID_OFFSET)
        storeFile.write(self.nextLabelID)

        
