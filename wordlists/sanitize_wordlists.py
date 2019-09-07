import os
import shutil

path = '.'

wordlists = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
  for file in f:
    if file.endswith('.txt'):
      wordlists.append(os.path.join(r, file))

for wordlist in wordlists:
  print('Sanitizing ' + os.path.basename(wordlist))
  wordlist_sanitized = wordlist + '.tmp'
  lines = []
  tmpfile = open(wordlist_sanitized, "w")
  for line in open(wordlist, "r"):
    if line.strip() != '' and line.strip() not in lines:
      lines.append(line.strip() + '\n')
  if wordlist.endswith('_unordered.txt'):
    print('Unordered wordlist')
    tmpfile.writelines(lines)
  else:
    tmpfile.writelines(sorted(lines))
  tmpfile.close()
  shutil.copy(wordlist_sanitized, wordlist)
  os.remove(wordlist_sanitized)
