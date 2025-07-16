import sqlite3
import os

DB_FILE = 'database.db'

if os.path.exists(DB_FILE):
    os.remove(DB_FILE)

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

create_table_sql = """
CREATE TABLE IF NOT EXISTS links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    url TEXT NOT NULL,
    clicks INTEGER DEFAULT 0,
    position INTEGER NOT NULL,
    thumbnail_url TEXT
);
"""
cursor.execute(create_table_sql)

links_iniciais = [
    ('Meu Portfólio de Projetos', 'https://github.com/wmarquesb', 0, 'https://www.google.com/s2/favicons?domain=github.com&sz=64'),
    ('Meu Perfil no LinkedIn', 'https://www.linkedin.com/in/williammarquesb/', 1, 'https://www.google.com/s2/favicons?domain=linkedin.com&sz=64'),
    ('Enviar um E-mail', 'mailto:williammarques.b@outlook.com', 2, 'https://img.icons8.com/material-outlined/50/new-post.png')
]

cursor.executemany("INSERT INTO links (title, url, position, thumbnail_url) VALUES (?, ?, ?, ?)", links_iniciais)

conn.commit()
conn.close()

print("Banco de dados e tabela 'links' recriados com sucesso!")
print("Dados iniciais inseridos.")