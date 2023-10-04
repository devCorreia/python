# Listas
album_1 = ["Luz", "Djavan", 1982, 10]
print(album_1)

album_list = ["Extra", "A tabua de Esmeralda", "Ideologia",
              "Back to Black", "Currents"]
print(album_list)

# 1 - Buscar os dois primeiros itens da lista
print(album_list[:2])

# 2 - Buscar o último item da lista
print(album_list[-1])

# 3 - Buscar álbuns de uma posição em diante
print(album_list[1:4])

# 4 - Tamanho da lista
print(len(album_list))

# 5 - Recuperar um item da lista pelo indice
print(album_list.index("Back to Black"))

# 6 - Adicionar item ao final da lista
album_list.append("Cidade do Pecado")
print(album_list)

# 7 - Ordenar uma lista
album_list.sort()
print(album_list)

# 8 - Copiar os itens de uma lista para a outra
album_heard = album_list.copy()
album_heard.remove("Currents")
print(album_heard)

# 9 - Remover todos os itens da Lista
album_list.clear()
print(album_list)


# Tuplas
album_tuple = ("Extra", "A tabua de Esmeralda", "Ideologia",
              "Back to Black", "Currents")
print(album_tuple)
print(type(album_tuple))

# 1 - Buscar os dois primeiros itens da tupla
print(album_tuple[:2])

# 2 - Buscar o último item
print(album_tuple[-1])

# 3 - Buscar albúns até uma determinada posição
print(album_tuple[:4])

# 4 - Buscar albúns de uma posição em diante
print(album_tuple[2:5])

# 5 - Recuperar um item da tupla pelo índice 
print(album_tuple.index("A tabua de Esmeralda"))

# Set
music_set = {"Meu País, Tim Maia", "Magnólia, Jorge Ben Jor", "Coleção, Cassiano", "Pelas Sombras, Arthur Verocai"}
print(music_set)

# 1 - Buscar o tamanho do set
print(len(music_set))

# 2 - True e 1 são considerados o mesmo valor
example_set = {"Fifa 24", True, 1, 90.50}
print(example_set)

# 3 - Adicionar item de outro set
music_set.update(example_set)
print(music_set)

# 4 - Remover um item no set
music_set.remove(True)
music_set.remove(90.50)
print(music_set)

# Não possibilita recuperar valores via slice


# Dicionarios
music = {
  "name": "O Show tem que continuar",
  "artist": "Arlindo Cruz",
  "yearLaunch": "2009",
  "genre": ["Samba", "Pagode"] 
  }
print(music)
print(len(music))
print(type(music))

# 1 - Recuperar um elemento do dicionário
print(music["genre"])
print(music.get("yearLaunch"))

# 2 - Buscar apenas as chaves do dicionário
print(music.keys())

# 3 - Buscar apenas os valores do dicionário
print(music.values())

# 4 - Buscar itens do dicionário com chave e valor
print(music.items())

# 5 - Adicionar itens no dicionário
music["duration"] = 3.34
print(music)

# 6 - Atualizar itens no dicionário 
music.update({"reproductions": 23.061,})
print(music)

# 7 - Remover item no dicionário 
music.pop("duration")
print(music)



# Dicionario aninhado 
import pprint

musicDict ={
  "crime pays":{
    "year launch": 2019,
    "album": ["bandana"],
    "genre":["RAP"]  
  },
  "all caps":{
    "year launch": 2004,
    "album":["madvillainy"],
    "genre":["RAP"]
  },
  "réu confesso":{
    "year launch": 1973,
    "album":["tim maia 1973"],
    "genre":["MPB"]
  }
}
pp = pprint.PrettyPrinter(depth=5)
pp.pprint(musicDict)

# Buscar uma informação dentro de um dicionario aninhado
print(musicDict["crime pays"]["genre"]) 

# Adicionar um novo item
musicDict["all caps"]["singer"] = "mf doom"
print(musicDict["all caps"])

# Excluir um dicionario
del musicDict["réu confesso"]
pp.pprint(musicDict)
