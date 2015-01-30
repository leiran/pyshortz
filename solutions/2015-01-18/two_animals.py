'''
Created on Jan 24, 2015

Name two animals, both mammals, one domestic, the other wild, 
put their letters together and rearrange to spell another 
mammal, this one wild and not seen in North America.

@author: John
'''


def main():
    wild_mammals = ['bison',
                   'fox',
                   'wolf',
                   'buffalo',
                   'hare',
                   'rabbit',
                   'squirrel',
                   'camel',
                   'moose']
    domestic_mammals = ['cow',
                        'cat',
                        'dog',
                        'pig',
                        'sheep',
                        'llama',
                        ]
    
    alpha = []
    for animal in wild_mammals:
        alpha.append("".join(sorted(animal)))
    
    
    for wild_mammal in wild_mammals:
        for domestic_mammal in domestic_mammals:
            candidate = sorted(wild_mammal.join(domestic_mammal))
            if candidate in alpha:
                print("{0} is a candidate")
    print("Done.")



if __name__ == '__main__':
    main()