from datetime import timedelta, date

print('\nGenerating birthday wordlists. Please wait...\n')

wordlists = {
  'wordlist_birthday.txt' : [],
  'wordlist_birthday_extended.txt' : [],
  'wordlist_birthday_dmy.txt' : [],
  'wordlist_birthday_dmy_extended.txt' : [],
}

for i in range(0, 2):

  start_date = date.today()
  end_date = date(1930, 1, 1)

  while start_date >= end_date:
    if i == 0:
      wordlists.get('wordlist_birthday.txt').append(start_date.strftime('%y%m%d') + '\n')
      wordlists.get('wordlist_birthday_extended.txt').append(start_date.strftime('%y%m%d') + '\n')
      wordlists.get('wordlist_birthday_dmy.txt').append(start_date.strftime('%d%m%y') + '\n')
      wordlists.get('wordlist_birthday_dmy_extended.txt').append(start_date.strftime('%d%m%y') + '\n')
    else:
      wordlists.get('wordlist_birthday.txt').append(start_date.strftime('%Y%m%d') + '\n')
      wordlists.get('wordlist_birthday_extended.txt').append(start_date.strftime('%Y%m%d') + '\n')
      wordlists.get('wordlist_birthday_extended.txt').append(start_date.strftime('%Y/%m/%d') + '\n')
      wordlists.get('wordlist_birthday_extended.txt').append(start_date.strftime('%Y-%m-%d') + '\n')
      wordlists.get('wordlist_birthday_dmy.txt').append(start_date.strftime('%d%m%Y') + '\n')
      wordlists.get('wordlist_birthday_dmy_extended.txt').append(start_date.strftime('%d%m%Y') + '\n')
      wordlists.get('wordlist_birthday_dmy_extended.txt').append(start_date.strftime('%d/%m/%Y') + '\n')
      wordlists.get('wordlist_birthday_dmy_extended.txt').append(start_date.strftime('%d-%m-%Y') + '\n')

    start_date -= timedelta(days=1)

for wordlist in wordlists:
  wordlist_file = open(wordlist, "w")
  wordlist_file.writelines(wordlists.get(wordlist))
  wordlist_file.close()

message = 'The wordlists ' + ', '.join(list(wordlists.keys())) + ' were created successfully.'
print(message)
