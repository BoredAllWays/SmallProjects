import time
Questions = {
    'Name this long running T.V show franchise that is best known for its card game called Pocket Monsters? ': 'pokemon',
    'What is the name of the first computer? ': 'eniac',
    'Name the main programming language made in Unity: ': 'c#' ,
    'Name this famous mathematician who solved the seven bridges of konigsburg problem? ' : 'leonhard euler',
    'What was the name given to the cell by Anton Von Leeuwenhoek? ' : 'animalcules',
    'Name the shortest possible distance in the universe: ' : 'planck length',
    'What company has a long history with creating CPU\'s for laptops? ' : 'intel'
}
score = 0
for question in Questions:
    ans = input(question).lower()
    if ans == Questions[question]:
        print('correct added 10 points')
        score += 10
    else:
        print('Your answer is incorrect - 0 points')
    time.sleep(1)
print('Grading .......')
time.sleep(2)
print('Your final score is ' + str(score))
print(f"you got a {int(score / 10)} out of {len(Questions)}")
time.sleep(2)
if score > 50:
    print('You are smart.')
else:
    print('You need to study more.')


