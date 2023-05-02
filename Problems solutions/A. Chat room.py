#Note: You need to learn about Regular Expressions

#Search for a sequence that starts with h
# The .e means seach for a character followed by e
# the ..e means for two characters followed by e
# The .*e means search for any character followed by e
import re
x=input()
ans=re.search("h.*e.*l.*l.*o",x)

if ans!= None:
    print("YES")
else:
    print("NO")   