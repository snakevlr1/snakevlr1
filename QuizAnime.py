import tkinter as tk
from tkinter import messagebox

# Perguntas e respostas
questions = [
  {
    'pergunta': 'Quem foi o rei dos piratas em one piece?',
    'opções': ['Naruto', 'Luffy', 'Zoro', 'Gold Roger'],
    'resposta': 'Gold Roger',
  },
  {
    'pergunta': 'Quem é Saitama?',
    'opções': ['Um herói', 'Um vilão', 'Um monstro', 'Um deus'],
    'resposta': 'Um herói',
  },
  {
    'pergunta': 'O que Sasuke fez?',
    'opções': ['Ele traiu a vila', 'Ele salvou a vila', 'Ele se tornou hokage', 'Ele se tornou um vilão'],
    'resposta': 'Ele traiu a vila',
  },
  {
    'pergunta': 'Quem é Dante?',
    'opções': ['Um demônio', 'Um herói', 'Um vilão', 'Um deus'],
    'resposta': 'Um herói',
  },
  {
    'pergunta': 'Em Bleach, em que ano se passa a guerra dos mil anos?',
    'opções': ['2000', '2005', '2009', '2030'],
    'resposta': '2009',
  },
  {
    'pergunta': 'Por que Frieren queria tanto buscar por mais magias?',
    'opções': ['Porque ela queria se tornar mais forte', 'Porque ela queria ajudar os outros', 'Porque ela queria se vingar', 'Porque ela queria se divertir'],
    'resposta': 'Porque ela queria ajudar os outros',
  },
  {
    'pergunta': 'Quem era o melhor amigo de Satoru Gojo?',
    'opções': ['Nanami', 'Sukuna', 'Geto', 'Megumi'],
    'resposta': 'Geto',
  },
  {
    'pergunta': 'Por que Gon procura pelo pai?',
    'opções': ['Ele queria conhecer o pai', 'Ele queria se vingar', 'Ele queria se tornar mais forte', 'Ele queria se divertir'],
    'resposta': 'Ele queria conhecer o pai',
  },
  {
    'pergunta': 'Qual o motivo dos gigantes em Attack on Titan?',
    'opções': ['Eles queriam se vingar', 'Eles queriam se divertir', 'Eles queriam conhecimento', 'Eles queriam liberdade'],
    'resposta': 'Eles queriam liberdade',
  },
  {
    'pergunta': 'Qual era o objetivo de Edward Elric?',
    'opções': ['Ele queria conhecimento sobre alquimia', 'Ele queria se tornar o melhor alquimista', 'Ele queria se vingar', 'Ele queria trazer sua mãe de volta'],
    'resposta': 'Ele queria trazer sua mãe de volta',
  },
  {
    'pergunta': 'Por que Kuroko era considerado uma sombra?',
    'opções': ['Ele era invisível', 'Ele era rápido', 'Ele era forte', 'Ele era habilidoso'],
    'resposta': 'Ele era invisível',
  },
  {
    'pergunta': 'Por que Asta não tinha nenhum poder mágico?',
    'opções': ['Ele era fraco', 'Ele era azarado', 'Ele foi amaldiçoado', 'Ele nasceu sem poder'],
    'resposta': 'Ele nasceu sem poder',
  },
  {
    'pergunta': 'Em Solo Leveling, Sung JinWoo não ajudou na raid das formigas por qual motivo?',
    'opções': ['Ele queria ficar com a família', 'Ele não queria ajudar', 'Ele queria testar os caçadores japoneses', 'Ele não tinha poder'],
    'resposta': 'Ele queria ficar com a família',
  },
]

current_question_index = 0
correct_answers = 0

# Função para carregar a pergunta
def load_question():
  global current_question_index
  question_data = questions[current_question_index]
  question_label.config(text=question_data["pergunta"])
  for i, option in enumerate(question_data["opções"]):
    option_buttons[i].config(text=option, command=lambda opt=option: select_option(opt))

# Função para selecionar uma opção
def select_option(selected_option):
  global current_question_index, correct_answers
  question_data = questions[current_question_index]
  if selected_option == question_data["resposta"]:
    correct_answers += 1
    messagebox.showinfo("Resposta", "Você acertou! 👍")
  else:
    messagebox.showinfo("Resposta", f"Você errou! ❌ A resposta correta é: {question_data['resposta']}")
  
  current_question_index += 1
  if current_question_index < len(questions):
    load_question()
  else:
    show_result()

# Função para mostrar o resultado
def show_result():
  question_label.pack_forget()
  for button in option_buttons:
    button.pack_forget()
  result_label.config(text=f"Você acertou {correct_answers} de {len(questions)} perguntas.")
  result_label.pack()
  restart_button.pack()

# Função para reiniciar o quiz
def restart_quiz():
  global current_question_index, correct_answers
  current_question_index = 0
  correct_answers = 0
  result_label.pack_forget()
  restart_button.pack_forget()
  question_label.pack()
  for button in option_buttons:
    button.pack_forget()
  load_question()

# Configuração da janela principal
root = tk.Tk()
root.title("Quiz de Animes")

# Widgets da interface
question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=400, justify="center")
question_label.pack(pady=50)

option_buttons = [tk.Button(root, text="", font=("Arial", 14), width=50) for _ in range(4)]
for button in option_buttons:
  button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 16))
restart_button = tk.Button(root, text="Reiniciar Quiz", font=("Arial", 14), command=restart_quiz)
exit_button = tk.Button(root, text="Sair do Quiz", font=("Arial", 14), command=root.quit)
exit_button.pack(pady=10)
# Carregar a primeira pergunta
load_question()
exit_button.pack(side="bottom", pady=20)

# Iniciar o loop principal
root.mainloop()
