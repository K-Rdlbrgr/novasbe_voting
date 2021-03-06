# Online Voting System of Nova SBE, Lisbon 
This repository contains all and solely the code for the blockchain-based online voting application, in use by Nova SBE, Lisbon.
The application allows you to hold elections in a secure, anonymous and fully transparent manner leveraging blockchain technology. 
Technically, every casted vote means an additional block on the blockchain, encrypted with SHA-256 cryptographic hash algorithm. It contains the voter's choice, hash and previous hash, the nonce and a timestamp. The election administrators are not able to see individual voter's choices since blocks can only be decrypted with the associated Voter Key (Private Key). The only person who temporarily gets access to this Key is the respective voter.
The Frontend consists of two main parts. First, the voting page which allows voters to select a candidate and confirm their choice. Second, the verification page, which provides the user with the aforementioned individual Voter Key (Private Key). It enables users to verify their vote afterwards. The database does not store Voter Keys manifesting the system's autonomous and anonoymous character.

## Powered by the Data Science Knowledge Center DSKC
This project originated as a Master Thesis of three Nova SBE students and their responsible supervisor and is now handled by the Data Science Knowledge Center of Nova SBE.
