import timeit
from random import randint

############Creating a class for each song
class SongNode:
    def __init__(self,trackid,songid,artistname,songtitle):
        self.trackid = trackid
        self.songid = songid
        self.artistname = artistname
        self.songtitle = songtitle

    def __lt__(self,other): #when using class1 < class2, I want it to check if the artistname in class1 is smaller the class2
        x = self.artistname
        y = other.artistname
        return x < y


def readfile( filename, amount = 1000000): #My own code
    #amount will be set to 1000000 if nothing else is given. Amount is used to check how many lines i want to read
    file = open(filename,"r")
    content = file.readlines()
    
    mylista = []
    mydictionary = {}

    for line in content[:amount]:
        vector = line.strip().split("<SEP>")    #4 elements in the vector which are: 1)trackid 2)songid 3)artistname 4)songname
        mylista.append( SongNode( vector[0], vector[1], vector[2], vector[3] ) )   #Add the node containing songdata into the list
        mydictionary[ vector[2] ] = vector[3] #Enter into dictionary, artistname as key, songname as data
        
    return mylista, mydictionary


def linsok(lista, desiredArtist):  #My own code /search for something else
    for i in range( len( lista ) ): #For each element, check if the artist name is the desired artistname
        currentNode = lista[i]
        if currentNode.artistname == desiredArtist:
            return

def mergesort(data):    #Lecture 12-13 Notes
    if len(data) > 1:   #This just makes it divide the list until you have a bunch of mini lists that only have one element
        mitten = len(data)//2
        vensterHalva = data[:mitten]    #Next two lives divide each list into a left and right side
        hogerHalva = data[mitten:]

        mergesort(vensterHalva) #Next two lines make it repeat until all your mini lists are only one element
        mergesort(hogerHalva)

        i, j, k = 0, 0, 0

        while i < len(vensterHalva) and j < len(hogerHalva):    #for each element in each list check which one is larger and it into data
            if vensterHalva[i] < hogerHalva[j]:            
                data[k] = vensterHalva[i]
                i = i + 1
            else:
                data[k] = hogerHalva[j]
                j = j + 1
            k = k + 1

        #The previous loop will always put ONE of the left/right lists into data. The next two while loops inserts the rest of the other list
        while i < len(vensterHalva):
            data[k] = vensterHalva[i]
            i = i + 1
            k = k + 1

        while j < len(hogerHalva):
            data[k] = hogerHalva[j]
            j = j + 1
            k = k + 1


def binsok(listan, nyckel):     #Lecture 8 notes
#The function checks if the middle element is the key, if not it finds out if middle element is larger/smaller than key and searches the proper half of the list    
    if len(listan) == 0:
        return False
    else:
        mitten = len(listan)//2
        if listan[mitten] == nyckel:
            return True
        else:
            if nyckel < listan[mitten].artistname:
                return binsok(listan[:mitten], nyckel)
            else:
                return binsok(listan[mitten+1:], nyckel)

def findinDict( dictionary, key):
    return dictionary[key]

def main():

    ###################Opening the file and entering data
    filename = "unique_tracks.txt"
    testmengd = 1000000        #Max is 1 000 000 (only 1 000 000 songs)
    mylist, mydictionary = readfile(filename,testmengd)   #Enter each node into mylist and enter  artistname and songname into mydictionary
    
    antal_element = len(mylist)

    
    #################### Söker efter nästsista  elementet med linjärsökning i osorterade listor.
    sista = mylist[antal_element-2]
    testartist = sista.artistname

    linjtid = timeit.timeit( stmt = lambda: linsok(mylist, testartist), number = 100 )    #Calculate the time it takes to run "lambda" function "number" amount of times
    print( "Linjärsökningen i osorterade lista tog", round( linjtid, 4 ) , "sekunder" )
    '''########################################################################################################################################################################################################'''

    #################### Sorterar listor med mergesort, (quicksort eller heapsort) som du kopierar
    # mergetime = timeit.timeit( stmt = lambda: mergesort(mylist), number = 100 )
    # print( "Mergesort tog", round( mergetime, 4 ), "seconds")
    '''########################################################################################################################################################################################################'''

    #################### Söker efter nästsista  elementet med linjärsökning i sorterade listor.
    # mergesort(mylist)   #Sort my list first

    # sista = mylist[antal_element-2]
    # testartist = sista.artistname

    # linjtid = timeit.timeit( stmt = lambda: linsok(mylist, testartist), number = 100 )    #Calculate the time it takes to run "lambda" function "number" amount of time
    # print( "Linjärsökningen i sorterade lista tog", round( linjtid, 4 ) , "sekunder" )
    '''########################################################################################################################################################################################################'''

    #################### Söker efter RANDOM  elementet med linjärsökning i osorterade listor.
    #################### When calculating a time, i insert mylist[ randint(0,antal_element) ].artistname which chooses a random artist all 1000 times
    # randomlinjtid = timeit.timeit( stmt = lambda: linsok(mylist, mylist[ randint(0,antal_element-1) ].artistname), number = 1000 )    #Calculate the time it takes to run "lambda" function "number" amount of times
    # print( "Random linjärsökningen i osorterade lista tog", round( randomlinjtid, 4 ) , "sekunder" )
    '''########################################################################################################################################################################################################'''
    
    #################### Söker med binärsökning i sorterade listor.
    # mergesort(mylist)   #Sort my list first

    # bintid = timeit.timeit( stmt = lambda: binsok(mylist, mylist[ randint(0, antal_element-1) ].artistname), number = 100 )    #Calculate the time it takes to run "lambda" function "number" amount of times
    # print( "Binärsökningen i sorterade lista tog", round( bintid, 4 ) , "sekunder" )
    '''########################################################################################################################################################################################################'''
    
    #################### Slår upp element i Pythons inbyggda dictionary
    dictid = timeit.timeit( stmt = lambda: findinDict(mydictionary, mylist[randint( 0,antal_element-1) ].artistname), number = 1000 )    #Calculate the time it takes to run "lambda" function "number" amount of times
    print(testmengd, round(dictid,4) )
    # print( "Binärsökningen i sorterade lista tog", round( dictid, 4 ) , "sekunder" )
    '''########################################################################################################################################################################################################'''


main()