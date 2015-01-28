import glob
import os

for fileName in glob.glob('*.png'):
	newName = fileName[:-4] + ".jpg"
	os.rename(fileName, newName)