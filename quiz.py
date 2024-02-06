import random

def quiz():

    while True:

        score = 0
        questions = None

        # Define quiz questions by category and difficulty
        questions_easy = {
            'Matematica': ['Quanto é 1+1?', 'Quanto é 1-1?'],
            'Artes': ['Qual cor fica se misturtar azul e amarelo?', 'Qual cor fica se misturtar vermelho e amarelo?'],
            'Conhecimentos gerais': ['Qual a capital de São Paulo?', 'Qual a capital do Rio de Janeiro?']
        }

        questions_medium = {
            'Matematica': ['Quanto é 3²?', 'Quanto é 2.(1+1)?'],
            'Artes': ['Quem pintou a Mona Lisa?', 'Qual o estilo fundado por Pablo Picasso?'],
            'Conhecimentos gerais': ['Qual o diretor de "Shark"?', 'Quem escreveu "O Hobbit"?']

        }

        questions_hard = {
            'Matematica': ['Qual é a raiz quadrada de 9?', 'Quanto é 7x8?'],
            'Artes': ['A "Grande Onda de Kanagawa" é de qual artista?', 'O "Lago das Ninfeias" é de qual artista?'],
            'Conhecimentos gerais': ['Se o Bruno beber muito ele dorme aonde?', 'Neném mais daora é o?']
        }

        # Define answers to the questions
        answers = {
            #Awnsers for questions_easy:
            'Quanto é 1+1?': '2',
            'Quanto é 1-1?': '0',
            'Qual cor fica se misturtar azul e amarelo?': 'verde',
            'Qual cor fica se misturtar vermelho e amarelo?': 'laranja',
            'Qual a capital de São Paulo?': 'São Paulo',
            'Qual a capital do Rio de Janeiro?': 'Rio de Janeiro',

            #Awnsers for questions_medium:
            'Quanto é 3²?': '9',
            'Quanto é 2.(1+1)?': '4',
            'Quem pintou a Mona Lisa?': 'Leonardo da Vinci',
            'Qual o estilo fundado por Pablo Picasso?': 'Cubismo',
            'Qual o diretor de "Shark"?': 'Spielberg',
            'Quem escreveu "O Hobbit"?' : 'Tolkien',

            #Awnsers for questions_hard:
            'Qual é a raiz quadrada de 9?': '3',
            'Quanto é 7x8?': '56',
            'A "Grande Onda de Kanagawa" é de qual artista?': 'Hokusai',
            'O "Lago das Ninfeias" é de qual artista?': 'Monet',
            'Se o Bruno beber muito ele dorme aonde?': 'chão',
            'Neném mais daora é o?': 'Ethan'
        }

        
        difficulty = input('Digite a dificuldade (fácil, médio, difícil): ')

        if difficulty == 'fácil':
            questions = questions_easy
        elif difficulty == 'médio':
            questions = questions_medium
        elif difficulty == 'difícil':
            questions = questions_hard
        else:
            print( 'Opção incorreta!') 
            continue
        

        categories = list(questions.keys())

        for _ in range(5):  # Asking 5 random questions
            
            category = random.choice(categories)
            question = random.choice(questions[category])

            print(f'\nCategoria: {category}')
            print(f'Questão: {question}')

            user_answer = input('Sua resposta é: ')

            if user_answer.lower() == answers[question].lower():
                print('Correta!')
                score += 1
            else:
                print(f'Incorreto! A resposta certa é: {answers[question]}')

            questions[category].remove(question)

            # Remove the category if all questions in that category have been asked
            if not questions[category]:
                categories.remove(category)

        print(f'\nQuiz Completado! A sua pontuação final é: {score}/5')

        newgame = input( 'Deseja jogar novamente? ')
        if newgame == 'não':
            print( 'Obrigado por jogar!')
            break
        elif newgame == 'sim':
            continue
        else:
            print( 'Opção inválida! Fim de jogo!')
            break

if __name__ == "__main__":
    print("Bem vindo ao Quiz Game!")
    quiz()