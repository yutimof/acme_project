import sqlite3

# Подключение к базе данных SQLite
con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

# Выполнение запроса на удаление записей из таблицы django_migrations
cur.execute('DROP TABLE auth_permission;')

# Подтверждение изменений
con.commit()

# Закрытие соединения
con.close()
