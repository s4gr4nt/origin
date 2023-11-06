#!/usr/bin/env python3
"""Alta3 Research | SGrant
   List Challenge - complex lists"""

def main():

    #create a new list of at least five animals with three-lettered names.
    animals = ['Fox', 'Fly', 'Ant', 'Bee', 'Cod', 'Cat', 'Dog']

    #display list of animals
    print(animals)

    #create a second list of three animals
    animals1 = ['Yak', 'Cow', 'Hen']

    #print second list of animals
    print(animals1)

    #append second list to first list
    animals.append(animals1)

    #display the first list again to see changes
    print(animals)

    #create another list
    animals2 = ['Koi', 'Hog', 'Jay']

    #display new list
    print(animals2)

    #extend animals1 list with animals2 list
    animals1.extend(animals2)

    #display animals1 to show changes
    print(animals1)

main()
