math_score = float(input('Enter math score:'))
science_score = float(input('Enter science score:'))

if math_score> 85:
    if science_score> 90:
        print('You are eligible for the scholarship.')
        ict_score = float(input('Enter ICT score:'))
        if ict_score> 90:
            print('You are eligible as DOST scholarship.')
    else:
        print('You are not eligible for the scholarship.Science score is too low')
else:
    print('You are not eligible for the scholarship. Math score is too low')