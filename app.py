from flask import Flask, jsonify
from threading import Thread
import random

app = Flask(__name__)

# Nomes e sobrenomes brasileiros
nomes_br = [
    "João", "Lucas", "Mateus", "Rafael", "Pedro", "Bruno", "Gabriel", "Caio",
    "Tiago", "Luan", "André", "Vinícius", "Henrique", "Daniel", "Otávio", "Ítalo",
    "Yago", "Leandro", "Enzo", "Luiz", "Felipe", "Eduardo", "Heitor", "Cauã",
    "Diego", "Victor", "Samuel", "Jonathan", "Murilo", "Arthur", "Breno", "Guilherme",
    "José", "Fernando", "Alexandre", "Paulo", "Wesley", "Kelvin", "Thiago", "Alan",
    "Rodriguinho", "Renatinho", "Diguinho", "Juninho", "Paulinho", "Lulinha", "Tiquinho", "Marciel",
    "Dodô", "Zezinho", "Jadson", "Betinho", "Dieguinho", "Edilson", "Carlinhos", "Magrão",
    "Ricardinho", "Nenê", "Gegê", "Felipinho", "Kaká", "Serginho", "Rael", "Biel",
    "Pedrinho", "Léo", "Cleberson", "Thales", "Caio César", "Tales", "Jorginho", "Danrley",
    "Careca", "Binho", "Cafu", "Sávio", "Tita", "Muralha", "Mosquito", "Dodô"
]

sobrenomes_br = [
    "Silva", "Souza", "Oliveira", "Santos", "Lima", "Pereira", "Ferreira", "Almeida",
    "Costa", "Gomes", "Ribeiro", "Martins", "Carvalho", "Rocha", "Araújo", "Barbosa",
    "Nascimento", "Campos", "Teixeira", "Moreira", "Moura", "Dias", "Cardoso", "Monteiro",
    "Freitas", "Correia", "Machado", "Batista", "Pires", "Fonseca", "Rezende", "Vieira",
    "Farias", "Ramos", "Medeiros", "Neves", "Coelho", "Cavalcante", "Tavares", "Andrade",
    "Reis"
]

# Nomes e sobrenomes dos outros países sul-americanos
nomes_latam = [
    "Matías", "Santiago", "Agustín", "Facundo", "Tomás", "Brayan", "Julián", "Lucas",
    "Mauricio", "Cristian", "Ángel", "Gustavo", "Jonathan", "Maximiliano", "Sebastián", "Andrés",
    "Franco", "Emiliano", "Leonardo", "Nahuel", "Alan", "Damián", "Nicolás", "Juan", 
    "Rodrigo", "Diego", "Ezequiel", "Iván", "Esteban", "Enzo", "Luis", "Marcelo", 
    "Federico", "Pedro", "Kevin", "Miguel", "Jorge", "Eduardo", "Carlos", "Rafael"
]

sobrenomes_latam = [
    "Martínez", "Gómez", "Rodríguez", "Pérez", "Fernández", "López", "González", "Ramírez",
    "Díaz", "Torres", "Sánchez", "Castro", "Moreno", "Cabrera", "Rojas", "Silva",
    "Aguilar", "Ortiz", "Vega", "Navarro", "Herrera", "Vásquez", "Reyes", "Barrios",
    "Maldonado", "Escobar", "Salazar", "Meza", "Fuentes", "Moya", "Palacios", "Quintero",
    "Arias", "Alvarado", "Bravo", "Benítez", "Cardozo", "Figueroa", "Carvajal", "Paredes"
]

# Nacionalidades com pesos
nacionalidades = [
    ("🇧🇷 Brasil", 5), ("🇦🇷 Argentina", 3), ("🇺🇾 Uruguai", 2), ("🇨🇴 Colômbia", 2), ("🇨🇱 Chile", 2),
    ("🇪🇨 Equador", 1), ("🇵🇾 Paraguai", 1), ("🇵🇪 Peru", 1), ("🇻🇪 Venezuela", 1), ("🇧🇴 Bolívia", 1)
]

posicoes = ["Goleiro", "Zagueiro", "Lateral Direito", "Lateral Esquerdo", "Volante", "Meia Central", "Meia Ofensivo",
            "Ponta Direita", "Ponta Esquerda", "Centroavante"]

comparacoes = [
    # Elite
    "Messi", "Neymar", "Luis Suárez", "James Rodríguez", "Di María", "Casemiro", "Marquinhos", "Éder Militão",
    "Alisson", "Otamendi", "Dibu Martínez", "Valverde", "Paquetá", "Enzo Fernández", "Gabigol",
    # Memes e médios
    "Carlos Sánchez", "Bolaños", "Luciano", "Romarinho", "Rodinei", "Renato Kayzer", "Soteldo", "Mendoza",
    "Germán Cano", "Pedro Raul", "Tiquinho Soares", "Andréas Pereira", "Matheus Fernandes", "Everton Ribeiro"
]

capacidade_atual = [
    "Reserva na National League", "Titular na National League",
    "Reserva na League Two", "Titular na League Two",
    "Reserva na League One", "Titular na League One",
    "Reserva na Championship", "Titular na Championship"
]

capacidade_potencial = [
    "Reserva na Championship", "Titular na Championship",
    "Reserva na Premier League", "Reserva na NLEDF",
    "Titular na Premier League", "Titular na NLEDF"
]

estrelas_pesos = [(2, 5), (3, 20), (4, 45), (5, 30)]

@app.route('/')
def gerar_jogador():
    nacionalidade = random.choices(nacionalidades, weights=[n[1] for n in nacionalidades])[0][0]
    if nacionalidade == "🇧🇷 Brasil":
        nome = f"{random.choice(nomes_br)} {random.choice(sobrenomes_br)}"
    else:
        nome = f"{random.choice(nomes_latam)} {random.choice(sobrenomes_latam)}"
    posicao = random.choice(posicoes)
    comparacao = random.choice(comparacoes)
    atual = random.choice(capacidade_atual)
    potencial = random.choice(capacidade_potencial)
    estrelas = random.choices([e[0] for e in estrelas_pesos], weights=[e[1] for e in estrelas_pesos])[0]
    estrelas_txt = "<:sstar:1214063700886036532>" * estrelas

    return jsonify({
        "nome": nome,
        "nacionalidade": nacionalidade,
        "posicao": posicao,
        "comparacao": comparacao,
        "cap_atual": atual,
        "cap_potencial": potencial,
        "estrelas": estrelas_txt 
    })

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()
