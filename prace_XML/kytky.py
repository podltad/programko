import xml.etree.ElementTree as ET 


tree = ET.parse('C:/Users/tadys/OneDrive/Plocha/python/prace_XML/plants 1.xml')
root = tree.getroot()



for element in root.findall("PLANT"):
    price = element.find('PRICE').text
    price = price[1:]
    if float(price) < 3:
        print(element.find('COMMON').text, element.find('BOTANICAL').text, element.find('PRICE').text)