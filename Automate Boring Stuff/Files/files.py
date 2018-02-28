import os

print "=Correct Path="
# since Windows has a different file system than Linux or OS X os.path.join()
#   is able to output the correct path for the current system
path = os.path.join('usr', 'bin', 'spam')
print path

print "\n=Displaying Curent Working Directory="

# getcwd() gets current directory
# chdir() changes current directory
print "Current directory: ", os.getcwd()
print "Changing..."
os.chdir("/home/user/Documents/Python/Automate Boring Stuff/")
print "Current directory: ", os.getcwd()
# reverting changes
os.chdir("/home/user/Documents/Python/Automate Boring Stuff/Files")

# to create a directory we can use os.makedirs(arg), where arg is the path of directories you wish to create

print "\n=Absolute and Relative Paths="

# changes between absolute paths
# . for current directory   .. for
print os.path.abspath('.')
print os.path.abspath('../../..')
print os.path.abspath('../../../Python')

# you can also check if a given path is absolute or not
print "Is '.' an absolute path? ", os.path.isabs('.')
print "Is '/home/kronos/Documents/' an absolute path?", os.path.isabs('/home/kronos/Documents/')

# to get relative path to a certain folder we can use relpath(path, start)
print os.path.relpath('/home/user', '/home/user/Documents/Python/Automate Boring Stuff/Files')

print "\n=Separating Paths="

path = os.getcwd() + '/files.py'
# basename returns everything after the last slash
print "Base Name: ", os.path.basename(path)
# dirname returns everything before the last slash
print "Dir Name: ", os.path.dirname(path)
# we can also split these up into a tuple with split()
print os.path.split(path)
# or we can separate all directories (note the different syntax)
print path.split(os.path.sep)

print "\n=File Information="

# size of file
print os.path.getsize(path)

# list of filenames
print os.listdir(os.getcwd())

print "\n=Path Validity="

# return if file or folder exists
print os.path.exists(path)

# return if argument is a file
print os.path.isfile(path)

# return if argument is a folder
print os.path.isdir(os.getcwd())

print "\n=Opening and Reading Files="

# by default, open already has a r flag
helloFile = open(os.getcwd() + '/hello')
# you can also use readlines() to get a list of the string values for each line
print helloFile.read()

helloFile.close()

print "=Writing in Files="

# to be able to write in the file, you need to set a w flag
# opening a file that does not exist, both w and a flags will create a new one as a blank file
baconFile = open('bacon', 'w')

#writing to a file will overwrite everything
baconFile.write('Bacon!\n')
baconFile.close()

baconFile = open('bacon')
print baconFile.read()
baconFile.close()

# appending will add text to the end of the file (with no overwrite of previous data)
baconFile = open('bacon', 'a')
baconFile.write('Bacon again!')
baconFile.close()

baconFile = open('bacon')
print baconFile.readlines()
baconFile.close()
