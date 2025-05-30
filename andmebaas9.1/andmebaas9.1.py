import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

CREATE_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS languages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS genres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    ); 

    CREATE TABLE IF NOT EXISTS directors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        director_id INTEGER,
        release_year INTEGER,
        genre_id INTEGER,
        duration INTEGER,
        rating REAL,
        language_id INTEGER,
        country_id INTEGER,
        description TEXT,
        FOREIGN KEY (director_id) REFERENCES directors(id),
        FOREIGN KEY (genre_id) REFERENCES genres(id),
        FOREIGN KEY (language_id) REFERENCES languages(id),
        FOREIGN KEY (country_id) REFERENCES countries(id)
    );
"""

def create_table():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.executescript(CREATE_TABLE_QUERY)
    conn.commit()
    conn.close()

def insert_initial_data():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    data = {
        'languages': [('English',), ('Estonian',), ('French',), ('German',)],
        'countries': [('USA',), ('UK',), ('France',), ('Germany',)],
        'genres': [('Drama',), ('Sci-Fi',), ('Crime',), ('Comedy',), ('Adventure',), ('Action',), ('Thriller',)],
        'directors': [('Francis Ford Coppola',), ('Christopher Nolan',), 
                      ('Quentin Tarantino',), ('Steven Spielberg',), ('Martin Scorsese',)]
    }
    for table, values in data.items():
        cursor.executemany(f"INSERT OR IGNORE INTO {table} (name) VALUES (?)", values)
    conn.commit()
    cursor.execute("SELECT id FROM directors WHERE name = ?", ("Francis Ford Coppola",))
    director_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM genres WHERE name = ?", ("Drama",))
    genre_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM languages WHERE name = ?", ("English",))
    language_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM countries WHERE name = ?", ("USA",))
    country_id = cursor.fetchone()[0]
    cursor.execute("""
        INSERT INTO movies 
        (title, director_id, release_year, genre_id, duration, rating, language_id, country_id, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        ("The From In With.", director_id, 1994, genre_id, 142, 9.3, language_id, country_id, "Kirjandus....")
    )
    conn.commit()
    conn.close()

def load_data_from_db(tree, search_query=""):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    if search_query:
        cursor.execute("""
            SELECT movies.id, movies.title, directors.name, movies.release_year, genres.name,
                   movies.duration, movies.rating, languages.name, countries.name, movies.description
            FROM movies
            JOIN directors ON movies.director_id = directors.id
            JOIN genres ON movies.genre_id = genres.id
            JOIN languages ON movies.language_id = languages.id
            JOIN countries ON movies.country_id = countries.id
            WHERE directors.name LIKE ?
        """, ('%' + search_query + '%',))
    else:
        cursor.execute("""
            SELECT movies.id, movies.title, directors.name, movies.release_year, genres.name,
                   movies.duration, movies.rating, languages.name, countries.name, movies.description
            FROM movies
            JOIN directors ON movies.director_id = directors.id
            JOIN genres ON movies.genre_id = genres.id
            JOIN languages ON movies.language_id = languages.id
            JOIN countries ON movies.country_id = countries.id
        """)
    rows = cursor.fetchall()
    conn.close()
    for item in tree.get_children():
        tree.delete(item)
    for row in rows:
        tree.insert("", "end", values=row[1:], iid=row[0])

def lisa_aken():
    aken = tk.Toplevel()
    aken.title("Lisa uus film")
    labels = ["Pealkiri", "Aasta", "Kestus", "Reiting", "Kirjeldus"]
    entries = {}
    for i, label in enumerate(labels):
        tk.Label(aken, text=label).grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(aken)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[label] = entry
    director_combo = ttk.Combobox(aken)
    genre_combo = ttk.Combobox(aken)
    language_combo = ttk.Combobox(aken)
    country_combo = ttk.Combobox(aken)
    tk.Label(aken, text="Režissöör").grid(row=5, column=0, padx=10, pady=5)
    director_combo.grid(row=5, column=1, padx=10, pady=5)
    tk.Button(aken, text="Lisa režissöör", command=lambda: lisa_uus("directors")).grid(row=5, column=2, padx=5)
    tk.Label(aken, text="Žanr").grid(row=6, column=0, padx=10, pady=5)
    genre_combo.grid(row=6, column=1, padx=10, pady=5)
    tk.Button(aken, text="Lisa žanr", command=lambda: lisa_uus("genres")).grid(row=6, column=2, padx=5)
    tk.Label(aken, text="Keel").grid(row=7, column=0, padx=10, pady=5)
    language_combo.grid(row=7, column=1, padx=10, pady=5)
    tk.Button(aken, text="Lisa keel", command=lambda: lisa_uus("languages")).grid(row=7, column=2, padx=5)
    tk.Label(aken, text="Riik").grid(row=8, column=0, padx=10, pady=5)
    country_combo.grid(row=8, column=1, padx=10, pady=5)
    tk.Button(aken, text="Lisa riik", command=lambda: lisa_uus("countries")).grid(row=8, column=2, padx=5)

    def fill_combos():
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM directors")
        director_combo['values'] = [f"{row[0]}: {row[1]}" for row in cursor.fetchall()]
        cursor.execute("SELECT id, name FROM genres")
        genre_combo['values'] = [f"{row[0]}: {row[1]}" for row in cursor.fetchall()]
        cursor.execute("SELECT id, name FROM languages")
        language_combo['values'] = [f"{row[0]}: {row[1]}" for row in cursor.fetchall()]
        cursor.execute("SELECT id, name FROM countries")
        country_combo['values'] = [f"{row[0]}: {row[1]}" for row in cursor.fetchall()]
        conn.close()
    fill_combos()
    def salvesta():
        try:
            title = entries["Pealkiri"].get()
            release_year = int(entries["Aasta"].get())
            duration = int(entries["Kestus"].get())
            rating = float(entries["Reiting"].get())
            description = entries["Kirjeldus"].get()
            director_id = int(director_combo.get().split(":")[0])
            genre_id = int(genre_combo.get().split(":")[0])
            language_id = int(language_combo.get().split(":")[0])
            country_id = int(country_combo.get().split(":")[0])
            conn = sqlite3.connect('movies.db')
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO movies 
                (title, director_id, release_year, genre_id, duration, rating, language_id, country_id, description)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (title, director_id, release_year, genre_id, duration, rating, language_id, country_id, description))
            conn.commit()
            conn.close()
            load_data_from_db(tree)
            messagebox.showinfo("Edu", "Film lisati edukalt!")
            aken.destroy()
        except Exception as e:
            messagebox.showerror("Viga", f"Filmi lisamine ebaõnnestus: {e}")
    tk.Button(aken, text="Salvesta", command=salvesta).grid(row=9, column=0, columnspan=3, pady=10)

def open_update_window(record_id):
    print(f"Avan akna filmile ID-ga: {record_id}")
    update_window = tk.Toplevel(root)
    update_window.title("Muuda filmi andmeid")

    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT title, release_year, duration, rating, description,
               director_id, genre_id, language_id, country_id
        FROM movies
        WHERE id=?
    """, (record_id,))
    movie = cursor.fetchone()

    cursor.execute("SELECT id, name FROM directors")
    directors = cursor.fetchall()
    cursor.execute("SELECT id, name FROM genres")
    genres = cursor.fetchall()
    cursor.execute("SELECT id, name FROM languages")
    languages = cursor.fetchall()
    cursor.execute("SELECT id, name FROM countries")
    countries = cursor.fetchall()
    conn.close()

    labels = ["Pealkiri", "Aasta", "Kestus", "Reiting", "Kirjeldus"]
    entries = {}
    for i, label in enumerate(labels):
        tk.Label(update_window, text=label).grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(update_window)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[label] = entry

    entries["Pealkiri"].insert(0, movie[0])
    entries["Aasta"].insert(0, movie[1])
    entries["Kestus"].insert(0, movie[2])
    entries["Reiting"].insert(0, movie[3])
    entries["Kirjeldus"].insert(0, movie[4])

    tk.Label(update_window, text="Režissöör").grid(row=5, column=0)
    director_combo = ttk.Combobox(update_window)
    director_combo.grid(row=5, column=1)
    director_combo['values'] = [f"{id}: {name}" for id, name in directors]
    director_combo.set(f"{movie[5]}: {next(name for id, name in directors if id == movie[5])}")

    tk.Label(update_window, text="Žanr").grid(row=6, column=0)
    genre_combo = ttk.Combobox(update_window)
    genre_combo.grid(row=6, column=1)
    genre_combo['values'] = [f"{id}: {name}" for id, name in genres]
    genre_combo.set(f"{movie[6]}: {next(name for id, name in genres if id == movie[6])}")

    tk.Label(update_window, text="Keel").grid(row=7, column=0)
    language_combo = ttk.Combobox(update_window)
    language_combo.grid(row=7, column=1)
    language_combo['values'] = [f"{id}: {name}" for id, name in languages]
    language_combo.set(f"{movie[7]}: {next(name for id, name in languages if id == movie[7])}")

    tk.Label(update_window, text="Riik").grid(row=8, column=0)
    country_combo = ttk.Combobox(update_window)
    country_combo.grid(row=8, column=1)
    country_combo['values'] = [f"{id}: {name}" for id, name in countries]
    country_combo.set(f"{movie[8]}: {next(name for id, name in countries if id == movie[8])}")

def lisa_uus(table_name):
    aken = tk.Toplevel()
    aken.title(f"Lisa uus {table_name[:-1]}")
    tk.Label(aken, text=f"{table_name[:-1]} nimi:").pack(pady=5)
    entry = tk.Entry(aken)
    entry.pack(pady=5)
    def salvesta():
        nimi = entry.get()
        if nimi:
            conn = sqlite3.connect('movies.db')
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO {table_name} (name) VALUES (?)", (nimi,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Edu", f"{table_name[:-1]} lisati edukalt!")
            aken.destroy()
    tk.Button(aken, text="Salvesta", command=salvesta).pack(pady=10)

def onSearch():
    global search
    search = search_entry.get().strip()
    load_data_from_db(tree, search)

def on_update():
    selected_item = tree.selection()
    if selected_item:
        record_id = int(selected_item[0])
        print(f"Muudame filmi ID-ga: {record_id}")
        open_update_window(record_id)
    else:
        messagebox.showwarning("Valik puudub", "Palun vali kõigepealt rida!")

def on_delete():
    selected_item = tree.selection()
    if selected_item:
        record_id = selected_item[0]
        print(f"Kustutame filmi ID-ga: {record_id}")
        confirm = messagebox.askyesno("Kinnita kustutamine", "Kas oled kindel, et soovid selle rea kustutada?")
        if confirm:
            conn = sqlite3.connect('movies.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM movies WHERE id=?", (record_id,))
            conn.commit()
            conn.close()
            load_data_from_db(tree)
            messagebox.showinfo("Edukalt kustutatud", "Rida on edukalt kustutatud!")
    else:
        messagebox.showwarning("Valik puudub", "Palun vali kõigepealt rida!")

root = tk.Tk()
root.title("Filmide andmebaas")
root.geometry("1000x600")

create_table()

insert_initial_data()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Lisa film", command=lisa_aken).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Muuda filmi", command=on_update).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Kustuta film", command=on_delete).pack(side=tk.LEFT, padx=5)

search_frame = tk.Frame(root)
search_frame.pack(pady=10)
tk.Label(search_frame, text="Otsi:").pack(side=tk.LEFT)

search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=5)
tk.Button(search_frame, text="Otsi", command=onSearch).pack(side=tk.LEFT)

frame = tk.Frame(root)
frame.pack(pady=20, fill=tk.BOTH, expand=True, padx=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree = ttk.Treeview(frame, yscrollcommand=scrollbar.set, 
                   columns=("title", "director", "year", "genre", "duration", "rating", "language", "country", "description"), 
                   show="headings")
tree.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=tree.yview)

tree.heading("title", text="Pealkiri")
tree.heading("director", text="Režissöör")
tree.heading("year", text="Aasta")
tree.heading("genre", text="Žanr")
tree.heading("duration", text="Kestus")
tree.heading("rating", text="Reiting")
tree.heading("language", text="Keel")
tree.heading("country", text="Riik")
tree.heading("description", text="Kirjeldus")

tree.column("title", width=150)
tree.column("director", width=100)
tree.column("year", width=60)
tree.column("genre", width=100)
tree.column("duration", width=60)
tree.column("rating", width=60)
tree.column("language", width=80)
tree.column("country", width=80)
tree.column("description", width=200)

load_data_from_db(tree)
root.mainloop()
