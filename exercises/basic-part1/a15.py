#Write a Python program to list all files in a directory in Python.

from os import listdir
from os.path import  isfile,join

files_list = [f for f in listdir('/home/jammy/dotfiles') if isfile(join('/home/jammy/dotfiles',f) ) ] 

print(files_list)