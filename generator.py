import datetime
from bitcoin import *

number_of_candidates = int(input('How many candidate addresses do you need? '))

def generate_candidate_addresses(n):
    
    candidate_addresses=[]
    
    while n > 0:
        candidate_privateKey = random_key()
        candidate_publicKey = privtopub(candidate_privateKey)
        candidate_address = pubtoaddr(candidate_publicKey)
        candidate_addresses.append(candidate_address)
        n -= 1
        
    counter = 1
        
    for i in range(0, len(candidate_addresses)):
        print(f'Address of candidate {counter}: {candidate_addresses[i]}')
        counter += 1
        
    
generate_candidate_addresses(number_of_candidates)

answer = input('Do you also want to generate a hash for the genesis block? (y/n) ')

def generate_genesis_block_hash():
    new_hash = sha256(f'{datetime.datetime.now()}')
    print(f'The hash of the genesis block: {new_hash}')
    
if answer == 'y' or answer == 'Y':
    generate_genesis_block_hash()
