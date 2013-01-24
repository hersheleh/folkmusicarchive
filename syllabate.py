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
    'K':['k','c','qu'], 'F':['f','ph','gh'], 'ZH':['g','sio','su'], 'JH':['j','dg','g'], 'HH':['h'], 
    'SH':['sh','tio','sio','ch'], 'DH':['th'], 'Y':['u','y'], 'CH':['ch','tu'], 'W':['w','ou'],'Z':['z','s','x'],
    # vowels
    'AA':['o','a'], 'AE':['a'],'AH':['a','u','e'], 'AO':['o','a'], 'AW':['ow'],'AY':['ie','i','ay'],
    'EH':['a','e'], 'ER':['ar','er','ear'], 'EY':['a','ei'], 'IH':['i','e'],'IY':['ea','ee','e','i'],
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
                split_point = nucleus[0]
            else:
                split_point = onset[0]

            print split_point
            '''
            if the split_point is in the phoneme dictionary,
            iterate and find index of all letters corrosponding to the 
            phoneme and set split_point_index to the smallest index
            '''
            if (split_point in phoneme_dict):
                indices = []
                for spelling in phoneme_dict[split_point]:
                    index = word.find(spelling)
                    if (index != -1):
                        indices.append(index)
                indices.sort()
                split_point_index = indices[0]
                
            else:
                split_point_index = word.find(split_point.lower())


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
            
        

    
