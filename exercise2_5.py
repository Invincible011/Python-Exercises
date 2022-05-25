def get_grade():
    '''
    hours = input('Enter hours? ')
    rate = input('Enter rate? ')
    try:
        hours = int(hours)
        rate = float(rate)
        if hours >= 40:
            pay = (hours * rate) + 25
            return('Payment with overtime work =', pay)
        else:
            pay = hours * rate
            return('Payment without Overtime work =', pay)
        return()
    except:
        return('Please enter a number')
    '''

    if (score >= 0.9) and (score <= 0.99):
        return f'with {score} score.\nYour Grade = A'
    elif (score >= 0.8) and (score <= 0.89):
        return f'with {score} score.\nYour Grade = B'
    elif (score >= 0.7) and (score <= 0.79):
        return f'with {score} score.\nYour Grade = C'
    elif (score >= 0.6) and (score <= 0.69):
        return f'with {score} score.\nYour Grade = D'
    elif score < 0.6:
        return f'with {score} score.\nYour Grade = F'
    else:
        return f'{score} is a Bad score'

score = input('Enter score? ')
try:
    score = float(score)
except:
    print(f'{score} is a Bad score')
    quit()

print(get_grade())