import sqlite3
conn = sqlite3.connect('banco.db')

conn.execute('''CREATE TABLE Pessoa
             (cpf INTEGER NOT NULL,
                nome TEXT NOT NULL,
                nascimento DATE NOT NULL,
                oculos BOOLEAN NOT NULL,
                PRIMARY KEY (cpf))''')

conn.execute('''CREATE TABLE Marca
                (id INTEGER NOT NULL,
                nome TEXT NOT NULL,
                sigla CHARACTER(2) NOT NULL,
                PRIMARY KEY (id))''')

conn.execute('''CREATE TABLE Veiculo
             (placa CHARACTER(7) NOT NULL,
              ano INTEGER NOT NULL,
              cor TEXT NOT NULL,
              motor REAL NOT NULL,
              proprietario INTEGER NOT NULL,
              marca INTEGER NOT NULL,
              PRIMARY KEY (placa),
              FOREIGN KEY (proprietario) REFERENCES Pessoa(cpf),
              FOREIGN KEY (marca) REFERENCES Marca(id))''')

conn.commit()
conn.close()

def inserir_pessoa(cpf, nome, nascimento, oculos):
    conn = sqlite3.connect('banco.db')
    conn.execute("INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (?, ?, ?, ?)", (cpf, nome, nascimento, oculos))
    conn.commit()

pessoas = [(12345, 'asdf', '13/12/2000', 0),
           (99999, 'Alec', '02/19/1801', 1),]

for pessoa in pessoas:
    inserir_pessoa(*pessoa)


def inserir_marca(nome, sigla):
    conn = sqlite3.connect('banco.db')
    conn.execute("INSERT INTO Marca (nome, sigla) VALUES (?, ?)", (nome, sigla))
    conn.commit()

marcas= [('Dois Irmaos', 'DI'),
         ('Aab', 'AB') ]

for marca in marcas:
    inserir_marca(*marca)


def inserir_veiculo(placa, cor, motor, proprietario, marca, ano):
    conn = sqlite3.connect('banco.db')
    conn.execute("INSERT INTO Veiculo (placa, cor, motor, proprietario, marca, ano) VALUES (?, ?, ?, ?, ?, ?)", (placa, cor, motor, proprietario, marca,ano))
    conn.commit()
    conn.close()

veiculos=[('A2f32', 'branco', 1.0, 12345, 'Dois Irmaos', 2001 )]

for veiculo in veiculos:
    inserir_veiculo(*veiculo)


def excluir_pessoa(cpf):
    conn = sqlite3.connect('banco.db')
    conn.execute("DELETE FROM Pessoa WHERE cpf = ?", (cpf))
    conn.commit()
    conn.close()

pessoas = []

for pessoa in pessoas:
    inserir_pessoa(*pessoa)



def excluir_marca(id):
    conn = sqlite3.connect('banco.db')
    conn.execute("DELETE FROM Marca WHERE id = ?", (id))
    conn.commit()
    conn.close()

marcas= []

for marca in marcas:
    inserir_marca(*marca)



def excluir_veiculo(placa):
    conn = sqlite3.connect('banco.db')
    conn.execute("DELETE FROM Veiculo WHERE placa = ?", (placa))
    conn.commit()
    conn.close()

veiculos=[]

for veiculo in veiculos:
    excluir_veiculo(*veiculo)





def alterar_pessoa(cpf, nome, nascimento, oculos):
    conn = sqlite3.connect('banco.db')
    conn.execute("UPDATE Pessoa SET nome = ?, nascimento = ?, oculos = ? WHERE cpf = ?", (nome, nascimento, oculos, cpf))
    conn.commit()
    conn.close()

def alterar_marca(id, nome, sigla):
    conn = sqlite3.connect('banco.db')
    conn.execute("UPDATE Marca SET nome = ?, sigla = ? WHERE id = ?", (nome, sigla, id))
    conn.commit()
    conn.close()


def alterar_veiculo(placa, cor, motor, proprietario, marca):
    conn = sqlite3.connect('banco.db')
    conn.execute("UPDATE Veiculo SET cor = ?, motor = ? proprietario = ?, marca = ? WHERE placa = ?", (cor, motor, proprietario, marca, placa))
    conn.commit()
    conn.close()


conn = sqlite3.connect('banco.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM Pessoa")
print("Pessoa: " + str(cursor.fetchall()))

cursor.execute("SELECT * FROM Veiculo")
print("Veiculos: " + str(cursor.fetchall()))

cursor.execute("SELECT * FROM Marca")
print('Marca: ' + str(cursor.fetchall()))

cursor.close()
conn.close()










