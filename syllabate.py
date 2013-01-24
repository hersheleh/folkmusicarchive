# Syllabator by Grisha Khachaturyan
'''
The syllabator uses the P2TK syllabifier script and hyphenates words based on it's syllabified output
Here's an example of how to run it
######################################
from syllabator import *

syl('orange')

output:
[(1, [], ['AO'], []), (0, ['R'], ['AH'], ['N', 'JH'])]
caught:  o
word:  range
parsed:  [['o']]
caught:  r
word:  ange
parsed:  [['o', ''], ['r', 'ange']]
['o', 'range']

#############################################
'''
import syllabifier
from nltk.corpus import cmudict

eng = syllabifier.English
cmu = cmudict.dict()

phoneme_dict = {
    # consonants
    'K':['k','c','que'], 'F':['f','ph','gh'], 'ZH':['g','sio','su'], 'JH':['j','dg','g'], 'HH':['h'], 
    'SH':['sh','tio','sio','ch'], 'DH':['th'], 'Y':['u'], 'CH':['ch','tu'],
    # vowels
    'AA':['a','o'], 'AE':['a'],'AH':['a','u'], 'AO':['o','a'], 'AW':['ow'],'AY':['ie','i','ay'],
    'EH':['e'], 'ER':['er','ear'], 'EY':['a','ei'], 'IH':['i'],'IY':['ea','ee','i'],
    'OW':['o'],'OY':['oy','oy'], 'UH':['ou'], 'UW':['ou','oo','ew','u']}



def pro_syl(word):
    pronounce = " ".join(cmu[word][0])
    return syllabifier.syllabify(eng, pronounce)


def syl(word):
    pronounce = " ".join(cmu[word][0])
    
    syl_pro = syllabifier.syllabify(eng, pronounce)
    print syl_pro
    
    if len(syl_pro) > 1:
        parsed_word = []

        for syllable, (stress, onset, nucleus, coda) in enumerate(syl_pro):
            if onset == []:
                split_point = "".join(nucleus)
            else:
                split_point = "".join(onset) # turns list into string

            '''
            if the onset is in the phoneme dictionary,
            iterate and find the letter corrosponding to the 
            phoneme and set split_point_index to that letter's index
            '''
            if (split_point in phoneme_dict):
                for spelling in phoneme_dict[split_point]:
                    index = word.find(spelling)
                    if (index != -1):

                        split_point_index = index
                        break
            else:
                split_point_index = word.find(split_point[0].lower())


            print "caught: ",word[split_point_index]

            '''
            If you've iterated passed the first syllable, 
            take every letter preceding the onset of the current syllable,
            and append it to the onset of the previous syllable
            '''
            if syllable > 0:
                parsed_word[syllable-1].append(word[:split_point_index])
                    
            syl_split = []
            syl_split.append(word[split_point_index])
            parsed_word.append(syl_split)

            word = word[split_point_index+1:]

            if syllable+1 == len(syl_pro):
                syl_split.append(word)
            
            print "word: ",word
            print "parsed: ",parsed_word

        return ["".join(a) for a in parsed_word]

    return word
            
        

    
