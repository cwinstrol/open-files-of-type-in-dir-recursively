import os
import glob
dir = '' #directory to be recursively searched
ext = 'txt' #file extension - pdf, psd, etc.
for file in glob.iglob(dir + '**/*.' + ext, recursive=True):
  os.startfile(file)
