import re
text = "The rain in Spain falls mainly in the plain."

#search for a pattern
match = re.search("plain", text)
if match:
    print("Match found:", match.group())    
    print("Match starts at index:", match.start())
    print("Match ends at index:", match.end())

#find all occurrences of a pattern
matches = re.findall("in", text)
print("All matches found:", matches)

#replace occurrences of a pattern
new_text = re.sub("rain", "snow", text)
print("Text after replacement:", new_text)