s=input("Введите текст")#вводим текст
s=s.split()#разбиваем текст на слова
s1=""#создаем пустую строку для того,чтобы добавлять в нее первую букву каждого слова
for i in s:#перебираем каждое слово в строке s
    s1+=i[0]#складываем все первые буквы каждого слова
print (s1)#выводим полученную строку