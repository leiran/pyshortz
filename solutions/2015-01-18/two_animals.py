'''
Created on Jan 24, 2015

Name two animals, both mammals, one domestic, the other wild, 
put their letters together and rearrange to spell another 
mammal, this one wild and not seen in North America.

@author: John
'''


class main:
    wild_mammals = ['bison',
                   'fox',
                   'wolf',
                   'buffalo',
                   'hare',
                   'rabbit',
                   'squirrel',
                   'camel',
                   'moose',
                   'soomewoc' #ringer moose + cow = soomewoc
                   ]
    domestic_mammals = ['cow',
                        'cat',
                        'dog',
                        'pig',
                        'sheep',
                        'llama'
                        ]
    
    def __init__(self, DEBUG):
        self.DEBUG = DEBUG
        self.combine_and_compare()
    
    def combine_and_compare(self):
        alpha = ["".join(sorted(animal)) for animal in self.wild_mammals]
        if self.DEBUG: print(alpha)
        candidate_list = [] #contains tuples (wild_mammal, domestic_mammal, correlated alpha)
        for wild_mammal in self.wild_mammals:
            for domestic_mammal in self.domestic_mammals:
                candidate = "".join(sorted(wild_mammal + domestic_mammal))
                if self.DEBUG: print(wild_mammal, ":", domestic_mammal, ":", candidate)
                if candidate in alpha:
                    candidate_list.append((wild_mammal, domestic_mammal, self.wild_mammals[alpha.index(candidate)]))
                    print("candidate:")
                    print("    %s" % wild_mammal)
                    print("    %s" % domestic_mammal)
                    print("    %s" % self.wild_mammals[alpha.index(candidate)])
        print("Done.")

if __name__ == '__main__':
    main(DEBUG=False)
