#User has to complete 20 questions, and the elapsed time is returned
import random
import time
note_positions = {
    '1': ['f', 'a#', 'd#', 'g#', 'c', 'f'],
    '2': ['f#', 'b', 'e', 'a', 'c#', 'f#'],
    '3': ['g', 'c#', 'f', 'a#', 'd', 'g'],
    '4': ['g#', 'c#', 'f#', 'b', 'd#', 'g#'],
    '5': ['a', 'd', 'g', 'c', 'e', 'a'],
    '6': ['a#', 'd#', 'g#', 'c#', 'f', 'a#'],
    '7': ['b', 'e', 'a', 'd', 'f#', 'b'],
    '8': ['c', 'f', 'a#', 'd#', 'g', 'c'],
    '9': ['c#', 'f#', 'b', 'e', 'g#', 'c#'],
    '10': ['d', 'g', 'c', 'f', 'a', 'd'],
    '11': ['d#', 'g#', 'c#', 'f#', 'a#', 'd#'],
    '12': ['e', 'a', 'd', 'g', 'b', 'e']
    }

print('Note: string 1 is the thickest string, and string 6 the thinnest!')
print('Note: Only sharps are considered here!')

total = 0
start_time = time.time()

for i in range(0,10):
    randint1 = str(random.randint(1,12))
    randint2 = random.randint(0,5)

    answer = note_positions[randint1][randint2]
    response = input('What is the note on fret {}, string {}?'.format(randint1, randint2+1))

    if response == answer:
        print('Well done!')
        total += 1
    else:
        print('Incorrect, the answer was {}'.format(answer))    

if total == 10:
    print('Well done, a perfect score: 10/10')

elif total >= 7:
    print('Well done, a score of {}/10'.format(total))

else:  
    print('You could do with some more practice! {}/10'.format(total))

print('You took approximately {} seconds'.format(time.time()-start_time))