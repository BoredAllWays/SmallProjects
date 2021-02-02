def _Inches():   
    divid = float(39.37)
    inch = int(input('What is your height in inches?'))
    inch_m = inch/divid
    print('Computer is calculating:')
    print('Done!', 'Computer: You are', inch_m , 'meters!')
  
def _Hello():
    name = input('what is your name?')
    print('Computer: Hello', name)

def _Weight():

    divids =  2.205;
    weight = float(input('What is your weight in pounds/lbs?:'));
    weight_K = weight / divids;
    print('You\'re', weight_K , 'Kilograms!');


def _QuestionForMetric():
    ask1 = 'What Measurement do you want to know in the metric system, height or weight?'
    print(ask1)

_Hello();
_QuestionForMetric();
answer = 'None'
while answer not in ("Height, Weight"):
    answer = input('Height or Weight:')
    answer = answer.lower()
    if answer == 'height':
        _Inches();
        break
    elif answer == 'weight':
        _Weight();
        break
    else:
          print('please enter Height or Weight')








