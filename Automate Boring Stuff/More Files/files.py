import shutil, os

# getting current directory for easier access
currDir = os.getcwd()


print "=Copying Files="

# args: source, destination
# if destination is a filename, it will be used as the new name of the copied folder
shutil.copy(currDir + '/copyFile', currDir + '/testFolder')

# Python doesn't like to create folders that already exist
if os.path.exists(currDir + '/testFolderBackup') is not True:
    # to copy whole folders we can use copytree()
    shutil.copytree(currDir + '/testFolder', currDir + '/testFolderBackup')

print "> Complete"

print "=Moving and Renaming Files and Folders="

# this could be better treated but that's not the point of these exercises
if os.path.exists(currDir + '/moveFile'):
    # like copy but just moves file into directory, does not leave a copy behind
    shutil.move(currDir + '/moveFile', currDir + '/testFolder')

if os.path.exists(currDir + '/moveFileOrgName'):
    # moving a file to a destination that ends in a filename will rename the file
    shutil.move(currDir + '/moveFileOrgName', currDir + '/testFolder/moveFileRenamed')

# if destination folder does not exist then Python assumes destination is a filename and renames the file
# if destination contains an inner folder that does not exist, it will bring up an exception

print "> Completed"

print "=Deleting Files="

if os.path.exists(currDir + '/deleteFile'):
    # delete file
    os.unlink(currDir + '/deleteFile')

if os.path.exists(currDir + '/emptyFolder'):
    # delete empty folder
    os.rmdir(currDir + '/emptyFolder')

if os.path.exists(currDir + '/fileFolder'):
    # delete file and everything in it
    shutil.rmtree(currDir + '/fileFolder')

# Possible alternative is installing send2trsh since these fucntions delete files and folders PERMANENTLY
# to install run: 'pip install send2trash' from a terminal window
# this will send something to the recycle bin rather than straight up delete it

print "> Completed"

print "=Walking a Directory Tree="

# os.walk() returns string for current Folder, list of strings of subfolders and list of strings of filenames
for foldername, subfolders, filenames in os.walk('..'):
    print foldername
    for subfolder in subfolders:
        print "\t", subfolder
    for filename in filenames:
        print "\t\t", filename

# I WILL BE SKIPPING ZIPFILES FOR NOW
