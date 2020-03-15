import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np

while __name__ == "__main__":
    dataPointsById = {} 
    years = []
    def parseXML(xmlfile):
        # grab the XML file and bring it into python
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        # add the data to our dictionary
        for child in root:
            dataPointsById[child[0].text] = [child[4].text, child[5].text]

    parseXML("dataset.xml")

    # create a 10x8 plot
    plt.figure(figsize=(10,8))

    # create an empty list and store data in it
    dataToPlot = []
    for key, value in dataPointsById.items():
        dataToPlot.append(value[1])
    # create a numpy int array from our list
    dataToPlot = np.array(dataToPlot, dtype='int')
    # create our x and y values from the count of times each year occurs
    x, y = np.unique(dataToPlot, return_counts=True)
    # create and show the scatter plot
    plt.scatter(x, y)
    plt.show()