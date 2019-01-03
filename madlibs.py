def getKeys(formatString):
    '''formatString is a format string with embedded dictionary keys.
    Return a set containing all the keys from the format string.'''

    keyList = list()
    end = 0
    repetitions = formatString.count('{')
    for i in range(repetitions):
        start = formatString.find('{', end) + 1
        # pass the '{'
        end = formatString.find('}', start)
        key = formatString[start: end]
        keyList.append(key)

    return set(keyList)
    # removes duplicates: no duplicates in a set

def addPick(cue, dictionary):
    '''Prompt for a user response using the cue string,
    and place the cue-response pair in the dictionary.
    '''
    promptFormat = "\nEnter {name}: "
    prompt = promptFormat.format(name=cue)
    response = input(prompt)
    dictionary[cue] = response                                                             


def getUserPicks(cues):
    '''Loop through the collection of cue keys and get user choices.
    Return the resulting dictionary.
    '''
    userPicks = dict()
    for cue in cues:
        addPick(cue, userPicks)
    return userPicks   

def tellStory(storyFormat):
    '''storyFormat is a string with Python dictionary references embedded,
    in the form {cue}.  Prompt the user for the mad lib substitutions
    and then print the resulting story with the substitutions.
    '''
    cues = getKeys(storyFormat)
    userPicks = getUserPicks(cues)
    story = storyFormat.format(**userPicks)
    print(story)

def main():
    originalStoryFormat = '''
My Love,\n

If the tears could explain how {Pronoun for large amount} I love you, I could never stop {synonym for shading tears} because,
I love you more {Adverb of time1} than {Adverb of time2} and I will love you more {Adverb of time2} than {Adverb of time1}.\n
So, here is what I’m {Verb to Go in Countinous Tense} to do:
I am {Verb to Go in Countinous Tense} to start all over {Adverb for repeating}.
I will turn heartbreak Valley into Acres of Hopes.
{Adjective for time}, I will give you bouquets of roses, because you mean a world to me.
If I could give you a hug now, you could understand how special you are to me.\n
To finish, I want you to know that, you are {Adjective for Great Value} in my eyes and 
I also believe that in time you will be able build a better life for yourself.
Just remember that I am thinking and believe in you and pray for you {Adjective for time}.\n

With Love,\n
{Your name}

'''
    tellStory(originalStoryFormat)
    # input("Press Enter to end the program.")


main()
