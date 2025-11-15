# nom 1
users=['admin','operator']
new_user=input("Enter new user name")
users.append(new_user)
print(users)
# nom 2
users=['root','security']
new_user=input("Enter new user name")
users.insert(0,new_user)
print(users)
# nom 3
users=['alice','bob','charlie']
user=input("Enter user name")
users.remove(user)
print(users)
# nom 4
logs=['Access granted','Login failed','Connection lost']
log=logs.pop()
print(log)
print(logs)
# nom 5
a=['ok','error','ok','error','error']
b=a.count('error')
print(b)
# nom 6
a=['Access ok','Breach detected','System reboot','Breach detected']
index=a.index('Breach detected')
print(index)
# nom 7
a=[3,1,2,3,1,2]
a.sort()
print(a)
# nom 8
a=['2025-10-01','2025-10-02','2025-10-03']
a.reverse()
print(a)
nom 9
a=["alert","spam","login","error","spam","alert"]
a.remove("spam")
a.remove("spam")
a.append("END_LOG")
a.reverse()
b=a.count("alert")
print(b)
print(a)
# nom 10
whitelist = ['192.168.0.1', '192.168.0.2', '192.168.0.3', '192.168.0.4', '192.168.0.5']
remove_ip = input("Введите IP для удаления: ")
new_ip = input("Введите новый IP: ")
whitelist.remove(remove_ip)
whitelist.insert(2, new_ip)
whitelist.sort()
print("Обновлённый белый список:", whitelist)
print("Индекс нового IP:", whitelist.index(new_ip))
# nom 11
logins = ['ok', 'fail', 'fail', 'ok', 'fail']
fails = logins.count('fail')
for _ in range(fails):
    logins.remove('fail')
logins.append('audit_completed')
logins.reverse()
print("Количество неудачных входов:", fails)
print("Итоговый список:", logins)
print("Первый индекс 'ok':", logins.index('ok'))

# kontrolnie voprosi
1. Чем отличается append() от insert()?

append(x) — добавляет элемент в конец списка.

insert(i, x) — вставляет элемент в любое место, по указанному индексу i.

2. Что делает метод pop() без указания индекса?

pop() без индекса удаляет и возвращает последний элемент списка.

3. Можно ли удалить несколько одинаковых элементов методом remove()?

Нет, remove() удаляет только первое вхождение элемента.
Чтобы удалить все одинаковые элементы, нужно вызывать его в цикле или использовать генераторы/фильтрацию.

4. Как работает метод reverse()?

reverse() разворачивает список на месте, меняя порядок элементов на обратный.
Он ничего не возвращает (возвращает None), а меняет сам список.

5. В чём разница между count() и index()?

count(x) — считает, сколько раз элемент x встречается в списке.

index(x) — возвращает индекс первого вхождения элемента x.

6. Какие методы изменяют исходный список, а какие возвращают новое значение?
Изменяют список (in-place):

append()

insert()

pop()

remove()

reverse()

sort()

clear()

extend()

Возвращают новое значение (НЕ меняют исходный список):

count()

index()

sorted() — важное отличие от sort(): создаёт новый отсортированный список

операции срезов (например, my_list[::-1] — создание перевёрнутой копии)

7. Что произойдёт, если вызвать index() для отсутствующего элемента?

Будет ошибка:ValueError: <элемент> is not in list

8.Почему сортировка (sort()) может быть полезна при анализе событий безопасности?

Потому что сортировка помогает:

группировать похожие события (например, одинаковые типы ошибок рядом)

обнаруживать аномалии — редкие или выбивающиеся значения становятся заметнее

упорядочивать логи по времени или важности

быстрее искать повторяющиеся события