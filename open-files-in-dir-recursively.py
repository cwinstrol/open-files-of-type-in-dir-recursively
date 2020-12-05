import os
import glob
dir = '' #edit this string to name the directory to be recursively searched (leaving this string empty may crash your system, depending)
ext = 'txt' #editable for other file extension types such as pdf, psd, etc.
for file in glob.iglob(dir + '**/*.' + ext, recursive=True):
  os.startfile(file)
