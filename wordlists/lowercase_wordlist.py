import sys
import os
import shutil

if len(sys.argv) == 2:
  wordlist = sys.argv[1]
  if not os.path.isfile(wordlist):
    sys.exit('\nThe wordlist does not exist.')
else:
  sys.exit('\nMissing parameter. Usage: python lowercase_wordlist.py {wordlist}')

print('\nLowercase ' + wordlist + ' successfully.')
wordlist_lowercase = wordlist + '.tmp'
lines = []
tmpfile = open(wordlist_lowercase, "w")
for line in open(wordlist, "r"):
  if line.strip() != '' and line.strip().lower() + '\n' not in lines:
    lines.append(line.strip().lower() + '\n')
tmpfile.writelines(lines)
tmpfile.close()
shutil.copy(wordlist_lowercase, wordlist)
os.remove(wordlist_lowercase)
