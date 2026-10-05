# Atividade em Sala - GUI com Padroes de Projeto
# Uma Biblioteca com Cadastro de Livros

# Plano
# Dominio: Biblioteca
# Classe: Livro
# Excecao: LivroInvalido
# Padrao 1: Fabrica
# Padrao 2: Observador
# Dados que serao validados: titulo e ano de publicacao
# IA utilizada para ajudar na organizacao do codigo: https://claude.ai/share/3b65ff80-ca90-4d6e-a540-42107a96eb67


import tkinter as tk #importar as ferramentas que vamos usar para criar a tela do programa
from tkinter import messagebox


# Criando a excecao para quando o livro tiver algum dado errado
class LivroInvalido(Exception):
    pass


# Criando a classe Livro
class Livro:

    def __init__(self, titulo, ano):

        # O titulo nao pode ficar vazio
        if titulo.strip() == "":
            raise LivroInvalido("O titulo do livro nao pode estar vazio.")

        # O ano precisa estar dentro desse intervalo
        if ano < 1000 or ano > 2026:
            raise LivroInvalido(
                "O ano de publicacao deve estar entre 1000 e 2026."
            )

        self.titulo = titulo
        self.ano = ano

    def mostrar_informacoes(self):
        return self.titulo + " (" + str(self.ano) + ")"


# ------------------------ FABRICA ------------------------

# Nome: Fabrica
# Problema: a tela nao precisa criar o livro diretamente.
# Solucao: a Fabrica fica responsavel por criar os livros.
# Consequencia: a criacao dos livros fica organizada em um so lugar.

class LivroFactory:

    def criar_livro(self, titulo, ano):
        return Livro(titulo, ano)


# ------------------------ OBSERVADOR ------------------------

# Nome: Observador
# Problema: a tela precisa saber quando um livro foi cadastrado.
# Solucao: o Controller avisa os observadores quando o cadastro acontece.
# Consequencia: a tela recebe o aviso sem precisar fazer todo o cadastro.

class BibliotecaController:

    def __init__(self):

        self.factory = LivroFactory()

        # Lista que guarda os observadores
        self.observadores = []

    # Adicionando um observador
    def adicionar_observador(self, observador):
        self.observadores.append(observador)

    # Funcao para cadastrar o livro
    def cadastrar_livro(self, titulo, ano):

        # A Fabrica cria o livro
        livro = self.factory.criar_livro(titulo, ano)

        # Avisando os observadores
        for observador in self.observadores:
            observador.livro_cadastrado(livro)


# ------------------------ TELA ------------------------

# Criando a classe da tela
class TelaBiblioteca:

    def __init__(self, janela):

        self.janela = janela

        # Criando o Controller
        self.controller = BibliotecaController()

        # A tela sera um observador
        self.controller.adicionar_observador(self)

        # Configurando a janela
        janela.title("Cadastro de Livros")
        janela.geometry("400x250")

        # Campo para colocar o titulo
        tk.Label(janela, text="Titulo do livro:").pack(pady=5)

        self.campo_titulo = tk.Entry(janela, width=35)
        self.campo_titulo.pack()

        # Campo para colocar o ano
        tk.Label(janela, text="Ano de publicacao:").pack(pady=5)

        self.campo_ano = tk.Entry(janela, width=35)
        self.campo_ano.pack()

        # Botao para cadastrar
        self.botao = tk.Button(
            janela,
            text="Cadastrar livro",
            command=self.cadastrar
        )
        self.botao.pack(pady=15)

        # Mensagem que aparece depois do cadastro
        self.mensagem = tk.Label(janela, text="")
        self.mensagem.pack()

    # Funcao chamada quando clicar no botao
    def cadastrar(self):

        try:

            titulo = self.campo_titulo.get()
            ano = int(self.campo_ano.get())

            # Mandando os dados para o Controller
            self.controller.cadastrar_livro(titulo, ano)

        # Caso o ano nao seja um numero
        except ValueError:

            messagebox.showerror(
                "Erro",
                "O ano deve ser um numero."
            )

        # Caso algum dado do livro esteja errado
        except LivroInvalido as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )

    # Funcao chamada quando o livro for cadastrado
    def livro_cadastrado(self, livro):

        self.mensagem.config(
            text="Livro cadastrado: " + livro.mostrar_informacoes()
        )

        messagebox.showinfo(
            "Sucesso",
            "Livro cadastrado com sucesso!"
        )

        # Limpando os campos depois do cadastro
        self.campo_titulo.delete(0, tk.END)
        self.campo_ano.delete(0, tk.END)


# ------------------------ PROGRAMA ------------------------

# Criando a janela
janela = tk.Tk()

# Criando a tela
tela = TelaBiblioteca(janela)

# Abrindo a janela
janela.mainloop()

# ------------------------ AUTOAVALIACAO ------------------------

# Criterios atingidos: Consegui fazer a janela com o formulario
# para cadastrar um livro. Tambem fiz a validacao dos dados
# usando uma excecao e utilizei os dois padroes de projeto,
# Fabrica e Observador.

# Criterios nao atingidos: Nao ficou nenhum criterio pendente.

# Parte que deu mais trabalho: A parte mais complicada foi
# entender como fazer a tela receber o aviso de que o livro
# foi cadastrado usando o Observador. Tambem tive que entender
# como usar a Fabrica para criar os livros.

# Como resolvi: Fui fazendo o codigo por partes e testando.
# Primeiro fiz a classe Livro e as validacoes. Depois fiz a
# Fabrica e o Controller. Por ultimo fiz a tela e testei
# os casos de cadastro.

# Uso de IA: Utilizei a IA para tirar duvidas sobre excecoes,
# interface grafica, Fabrica e Observador. Tambem usei
# como apoio na organizacao do codigo e depois fiz os testes
# para verificar se estava funcionando.