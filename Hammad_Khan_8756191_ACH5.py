import re

source = "hammad khan 8756191 Lorem ipsum doflor szit ametß, consqecytetu$r adipibsching elit, sed do eiusmod tewmporα incid6kgidunt ut labq8ore et café dolore_ magna aliqua. Purus! sit{|}~ \t\n\r\x0b\x0c amet volutpat cons&jequat mau7ris. Penaxtibus et"

findAllH = re.findall("h", source)
print("Found", len(findAllH), "matches of the letter h")

findAllDigits = re.findall("\d", source)
print("Found", len(findAllDigits), "matches of digits")

findAllAlphanumeric = re.findall("\w", source)
print("Found", len(findAllAlphanumeric), "matches of alphanumeric")

findAllNonAlphanumeric = re.findall("\W", source)
print("Found", len(findAllNonAlphanumeric), "matches of nonalphanumeric")

findAllSpaces = re.findall("\s", source)
print("Found", len(findAllSpaces), "matches of spaces") 