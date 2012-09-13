#! usr/bin/env/python



def compress(a_string):
    previous_char   = None
    count           = 0
    pair_count      = 0
    final           = ''
    
    for character in a_string:
        #If we have a new character
        if character != previous_char:
            #Then inspect the string - do we need a number
            if count > 1:
                final += str(pair_count)
            count = 1
            final += character
            
        else:
            count += 1
        
        #If we are on the second one    
        if count == 2:
            final += character
        
        #Set/re-set the pair counter    
        pair_count = count - 2
        
        #But it can't be negative, so fix that
        if pair_count < 0:
            pair_count == 0
        #We also want to reset if its greater than 9
        if pair_count == 9:
            #Add and reset
            final += str(pair_count)
            count = 0
            pair_count = 0
            previous_char = None
        else:
            #Reset the previous character
            previous_char = character
        
    #If we are on the last one, add the count
    if count > 1:
        final += str(pair_count)
    
    return final
    
    
def decompress(compressed_string):
    
    previous_character = None
    final = ''
    
    for character in compressed_string:
        try:
            value = int(character)
            #If there is an integer value
            #Then there should be a previous character
            new = previous_character * value
            final += new
            
            
        except:
            final += character
            previous_character = character
        
        
    return final
        
        
