from flask import Flask, render_template, request, session

import get_dollars_from_api
import the_guess_game
from time import sleep
import create_random_numbers
import random

app = Flask(__name__, template_folder='D:/repo_for_git/backend/flask_basic_server')
app.secret_key = 'my_secret_key'


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('index.html')


@app.route('/game.html')
def game():
    return render_template('game.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    difficulty = int(request.form['difficulty'])
    guess = int(request.form['guess'])
    score, random_number = the_guess_game.guess(difficulty, guess)
    if guess > difficulty or difficulty < 1:
        return render_template('game_finish_not_vaild.html', result=[guess, random_number])
    if score == 'ok':
        return render_template('game_finish_succeed.html', result=[guess, random_number])
    elif score == 'failed':
        return render_template('game_finish_failed.html', result=[guess, random_number])


@app.route('/game2.html', methods=['POST', 'GET'])
def game2():
    return render_template('game2.html')


@app.route('/show_numbers', methods=['POST', 'GET'])
def game2_show_randoms():
    sleep(3)
    amount_of_numbers = int(request.form['amount'])
    list_of_random_numbers = create_random_numbers.render(amount_of_numbers)
    session['list_of_random_numbers'] = list_of_random_numbers
    return render_template('game2_show_randoms.html', result=list_of_random_numbers)


@app.route('/game2_insert_result', methods=['POST', 'GET'])
def game2_insert_results():
    list_of_random_numbers = session.get('list_of_random_numbers', '')
    return render_template('game2_insert_result.html', result=list_of_random_numbers)


@app.route('/calculate_game_of_memory', methods=['POST', 'GET'])
def game2_insert_results_show():
    count = 0
    list_of_numbers_from_web = []
    list_of_random_numbers = session.get('list_of_random_numbers', '')
    for i in range(len(list_of_random_numbers)):
        list_of_numbers_from_web.append(int(request.form[f'num{list_of_random_numbers[i]}']))
    for i in range(1, len(list_of_random_numbers)+1):
        if list_of_numbers_from_web[i-1] != list_of_random_numbers[i-1]:
            count += 1
    if count == 0:
        return render_template('game2_finish_succeed.html')
    else:
        return render_template('game2_finish_failed.html')


@app.route('/game3.html', methods=['POST', 'GET'])
def game3():
    return render_template('game3.html')


@app.route('/game3_magic.html', methods=['POST', 'GET'])
def game3_magic():
    random_number = random.randint(0, 100)
    session['random_number'] = random_number
    return render_template('game3_magic.html', result=random_number)


@app.route('/roulette_results', methods=['POST', 'GET'])
def game3_roulette_results():
    user_input_amount = float(request.form['user_input_amount'])
    user_input_difficulty = float(request.form['user_input_difficulty'])
    usd_amount = session.get('random_number', '')
    one_dollar_worth_in_ils = get_dollars_from_api.dollar_to_ils(1)
    total_real_amount = usd_amount * one_dollar_worth_in_ils
    if (total_real_amount - (5 - user_input_difficulty)) < user_input_amount < (total_real_amount + (5 - user_input_difficulty)):
        return render_template('game3_finish_succeed.html', result=[user_input_amount, total_real_amount])
    else:
        return render_template('game3_finish_failed.html', result=[user_input_amount, total_real_amount])


if __name__ == '__main__':
    app.run()