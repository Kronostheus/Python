import re

# initial r' marks input as a raw string and avoids extra backslashes
# use of parentheses allows the segmentation of input into groups
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

# search returns Match object or None
mo = phoneNumRegex.search('My number is 415-555-4242')

print "\n=Using group()="

# returns the matched text from the Match object
print mo.group()

# since we devided the regex object we can have 2 groups
print mo.group(1)
print mo.group(2)

print "\n=Using groups()="

# groups() returns a list that we can feed into variables
areaCode, mainNumber = mo.groups()
print areaCode
print mainNumber
print mo.groups()

print "\n=Escaping parentheses="

# we now want to be able to read parentheses, therefore we escape them with \( and \)
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (415) 555-4242')

print mo.group(1)
print mo.group(2)
print mo.groups()

print "\n=Using pipe to match multiple groups="

# using | we are looking for either Superman or Batman
# using group() will return the First match
heroRegex = re.compile(r'Superman|Batman')

mo1 = heroRegex.search("Batman and Superman")
print mo1.group()

mo2 = heroRegex.search("Superman and Lois Lane")
print mo2.group()

print "\n=Optional patterns (?)="

# the use of ()? should make wo optional and allow both Superman and Superwoman to match
# ? only allows Zero or One
superRegex = re.compile(r'Super(wo)?man')

mo1 = superRegex.search("The adventures of Superman")
print mo1.group()

mo2 = superRegex.search("The adventures of Superwoman")
print mo2.group()

print "\n=Optional patterns (*)="

# to allow several optional matches we can use * instead of ?
# * allows Zero or More
aoeRegex = re.compile(r'wo(lo)*lo')

mo1 = aoeRegex.search("wolo")
print mo1.group()

mo2 = aoeRegex.search("wololololo")
print mo2.group()

print "\n=Optional patterns (+)="

# + allows One or More
aoeRegex = re.compile(r'wo(lo)+lo')

mo1 = aoeRegex.search("wololo")
print mo1.group()

mo2 = aoeRegex.search("wolololo")
print mo2.group()

print "\n=Repeating Patterns="

# {3} will allow HaHaHa (or 3 instances of Ha)
haRegex = re.compile(r'(Ha){3}')

mo = haRegex.search("HaHaHa")
print mo.group()

print "\n=Repeating Patterns (with range)="

# We can also define a range (this case: between 3 and 5 Ha)
# {3,} is 3 or more
# {,5} is 0 to 5 matches
hahaRegex = re.compile(r'(Ha){3,5}')

mo1 = hahaRegex.search("HaHaHa")
print mo1.group()

mo2 = hahaRegex.search("HaHaHaHa")
print mo2.group()

mo3 = hahaRegex.search("HaHaHaHaHa")
print mo3.group()

print "\n=Repeating Patterns (with range) greedy vs. nongreedy="

# by default Python chooses the greedy (i.e longest) match
greedyRegex = re.compile(r'(Ha){3,5}')
# the use of ? after the curly braces picks the shortest matching (3)
nongreedyRegex = re.compile(r'(Ha){3,5}?')

mo1 = greedyRegex.search("HaHaHaHaHa")
print mo1.group()

mo2 = nongreedyRegex.search("HaHaHaHaHa")
print mo2.group()

print "\n=FindAll instead of search="

# findall will return a list of strings with all matches (list is as long as there are matches)

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print phoneNumRegex.findall("Cell: 415-555-9999 Work: 212-555-0000")

# if there are groups in the regular expression, findall will return a list of tuples with the matched groups
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print phoneNumRegex.findall("Cell: 415-555-9999 Work: 212-555-0000")


# Shorthand Character Classes
#
# \d            0-9
# \D            Anything NOT 0-9
# \w            letter, numeric digit, underscore
# \W            Anything NOT letter, numeric digit, underscore
# \s            space, tab, newline Character
# \S            Anything NOT space, tab or newline
#
# [0-5]         Matches numbers 0 to 5, which is shorter than writing (0|1|2|3|4|5)

print "\n=Shortand Character Classes="

# we're looking for strings matching: (1 or more) numeric digits [space] (1 or more) letters
mixRegex = re.compile(r'\d+\s\w+')
print mixRegex.findall("12 drummers, 11 pipers, 10 ladies, 9 lords, 8 maids, 7 swans")

print "\n=Custom Character Classes="

# we aim to find all vowels present (upper or lower case)
vowelRegex = re.compile(r'[aeiouAEIOU]')
print vowelRegex.findall("Robocop eats baby food. BABY FOOD!")

# [a-zA-Z0-9] should match all lowercase letters, uppercase letters and numbers

# ^ just after the opening bracket negates it's content. Ex: [^aeiouAEIOU] will look for consonants (both upper and lowercase)

print "\n=Caret and Dollar Sign Characters="

# ^ at the beginning of a regex looks for a match the start of the text
beginsWith = re.compile(r'^Hello')
print beginsWith.findall("Hello World!")

# $ will look for text ending with the given regex (this case, end with a number)
endsWith = re.compile(r'\d$')
print endsWith.findall("Your number is 42")

# combination of both to find text that begins and ends with a number
wholestringRegex = re.compile(r'^\d+$')
print wholestringRegex.findall("1234567890")
# this particular combination ensures that the text cannot have letters in between (since it has to have all numbers from start to finish and finish to start)
print "Should return empty list: ", wholestringRegex.findall("123xyz456")

print "\n=The WildCard Character="

# The .will match any character except for newline with
atRegex = re.compile(r'.at')
# Matches only one character thus "flat" will not match (will become lat)
print atRegex.findall("The cat in the hat sat on the flat mat")

# To match with an actual dot, escape it with a backslash: \..

print "\n=The Dot-Star (Everything)="

# (.*) basically means anything and everything except a newline
#   . means any character except newline
#   * means zero or more of the preceding character
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search("First Name: James Last Name: Bond")
print mo.group(1)
print mo.group(2)

print "\n=The Dot-Star Greedy vs. Non Greedy="

# dot-star is greedy and will try to match the longest string possible
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search("<To serve a man> for dinner>")
print "Greedy: ", mo.group()

# an ? after * will ensure a non greedy approach
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search("<To serve a man> for dinner>")
print "Non Greedy: ", mo.group()

print "\n=Including newline="

# re.DOTALL as a second argument will include \n with dot-star instead of only catching the first match before it
newlineRegex = re.compile(r'.*', re.DOTALL)
mo = newlineRegex.search("Hello\nWorld")
print mo.group()

print "\n=Case Insensitive="

# re.I makes the regex case insensitive (by default it is)
caseRegex = re.compile(r'robocop', re.I)
print caseRegex.findall("Robocop is a robocop that works with ROBOCOP")

print "\n=Substitute="

# we can use sub() to substitute matched text with a given word
namesRegex = re.compile(r'Agent \w+')
mod = namesRegex.sub('CENSORED', 'Agent Alice gave the documents to Agent Bob')
print mod

# seperate the first letter of the name in a group
namesRegex = re.compile(r'Agent (\w)\w*')
# we can use \1, \2, \3, etc. in the first argument to enter the text in the Nth group
mod = namesRegex.sub(r'\1****', 'Agent Alice gave the documents to Agent Bob')
print mod

# To better manage complex regex we can do this:

phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

# into (note the use of ''' for a multiline string and re.VERBOSE as second argument)

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    \d{3}                           # first 3 digits
    (\s|-|\.)                       # separator
    \d{4}                           # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
    )''', re.VERBOSE)

# To combine multiple 2nd arguments in compile(), one must use | as compile() technically only takes one variable as 2nd argument
someRegex = re.compile(r'foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
