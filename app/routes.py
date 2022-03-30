from turtle import title
from app import app
from flask import render_template

@app.route('/')
def index():
    title='Home'
    user= {'id': 1, 'username':'Marvel Fans', 'email':'keyurpatel1121@gmail.com'}
    posts = [
        {
            'id': 1,
            'title': 'Iron Man',
            'body': 'Tony Stark. Genius, billionaire, playboy, philanthropist. Iron Man possesses powered armor that gives him superhuman strength and durability, flight, and an array of weapons.',
            'author': 'Keyur P.'
        },
        {
            'id': 2,
            'title': 'Thor Odinson',
            'body': 'The God of Thunder and an Asgardian warrior. The one who beholds Mjølnir and Stormbreaker. Thor is extremely durable to physical injuries, He has even survived energy blasts from a Star.',
            'author': 'BuffMovieBuff123'
        },
        {
            'id': 3,
            'title': 'Steve Rogers aka Captain America',
            'body': 'Captain America is the alter ego of Steve Rogers, a young man enhanced by an experimental super-soldier serum which enhances his  physical performance. Captain America often uses his shield (made of Vibranium) as an offensive throwing weapon. ',
            'author': 'code_is_life'
        },
        {
            'id': 4,
            'title': "T'Challa",
            'body': "T'Challa is the King of Wakanda and the Black Panther. He gets his powers from a magicaal herb which grants him uperhumanly acute senses, enhanced strength, speed, agility, stamina, durability, healing, and reflexes. He also possessess a suit made of Vibraanium and has the most  advnaced tech.",
            'author': 'CodingTemple4L'
        },
        {
            'id': 5,
            'title': 'Bruce Banner',
            'body': 'Hulk is the alter ego of Bruce Banner. He was accidentaly exposed to gamma rays which transforms him into Hulk when subjected to emotional stress.',
            'author': 'CodingTemple4L'
        }
        
    ]
    return render_template('index.html', current_user=user, title=title, posts=posts)


@app.route('/signup')
def signup():
    return render_template('signup.html')
