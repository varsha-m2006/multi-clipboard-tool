#myclip.py - A simple command-line tool to copy preset text snippets to the clipboard.
#Usage: py myclip.py <keyphrase>

#importing needed modules
import sys
import pyperclip

#Text dictionary with pretext available to copy
Text = {"Agree": "Yes,I agree. That Sounds Fine to me","Busy":"Sorry, can we do this laterthis week or next week?", "upsell": "Would you consider making this a monthly donation"}

#Case 1: When Keyphrase isn't entered according to format
if(len(sys.argv)<2):
    print("Usage: py myclip.py <keyphrase> - copy phrase text")
    sys.exit() 

#Second item of sys.arv stores kephrase provided by user
keyphrase=sys.argv[1]

#Case 2: When KeyPhrase exists in Text Dictionary
if(keyphrase in Text):
    #Copying to clipboard
    pyperclip.copy(Text[keyphrase])
    print(keyphrase +" Has been copied to local clipboard. Thank you.")
else:
    print("Doesn't exist in dictionary, not copied to clipboard")
