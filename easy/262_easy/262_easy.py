#
# /r/dailyprogrammer Challenge #262 [Easy] 
#            MaybeNumeric           
# 										   
# Short Summary: The scope of this problem is kind of specific, so please see
#                the provided link for an accurare description of this problem
# 										   
# Full Problem: https://www.reddit.com/r/dailyprogrammer/comments/3xdmtw/20151218_challenge_245_hard_guess_whois/
#  

def flatten(i):
    return sum(i, [])

def MaybeNumeric(input, delim = '`'):
    for word in flatten([x.split(delim) for x in input]):
        try:
            if( all(float(w) for w in word.split()) and delim == '`' ):
                yield list(MaybeNumeric([word], ' '))
                continue
            else:
                raise ArgumentError('Delimiter was not backtick')
        except Exception as e:
            try:
                float(word)
                yield '{} ({})'.format(word, 'number')
            except ValueError as e:
                yield '{} ({})'.format(word, 'string')
            except OverflowError as e:
                yield '{} ({})'.format(word, 'number')

# Example usage (looks funky, I know)
# print(list(
#        MaybeNumeric(['123','44.234','0x123N'])
#        ))
