from jinja2 import Template
import sqlite3
import model

checked_genres = ()
checked_authors = (0,2)
checked_publishers = ()


conn = sqlite3.connect("library.sqlite")

df_author = model.get_author(conn)
df_publisher = model.get_publisher(conn)
df_genre = model.get_genre(conn)
df_card = model.cardQuerry(conn, checked_publishers, checked_genres, checked_authors)
conn.close()

f_template = open('template.html','r', encoding ='utf-8-sig')
html = f_template.read()
f_template.close()
# создаем объект-шаблон
template = Template(html)
# генерируем результат на основе шаблона
result_html = template.render(
    df_authors=df_author,
    df_publishers=df_publisher,
    df_genres=df_genre,
    card=df_card,
    checked_authors=checked_authors,
    checked_publishers=checked_publishers,
    checked_genres=checked_genres,
    len=len
)

f = open('result.html', 'w', encoding='utf-8-sig')
f.write(result_html)
f.close()
