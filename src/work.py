import xml.etree.ElementTree as ET
names = []
ips = []
partNumbers = []
# Parse XML from a file
tree = ET.parse('assets.xml')
root = tree.getroot()


for asset in root.findall('asset'):
    names.append(asset.find('assetName').text)
    ips.append(asset.find('ipAddress').text)

print(names[0],ips[0])
