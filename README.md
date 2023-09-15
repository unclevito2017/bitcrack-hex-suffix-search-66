# bitcrack-hex-suffix-search-
Find private key with bitcrack stride and last 7 hex digits
Script assigns 7 random hex digits <br>
writes to and checks tried.txt so never repeats the same 7 hex digits in same order. <br>
no more that 2 adjacent identical hex characters. Limits the possible combinations to approx. 33 million<br>
Example to test this method can find private key of a specific public asddress.<br>
Test Address 1K2wh7bdCYgFeipT8fnCS3GknWLKHPgJq5 lies in keyspace 66 private key 000000000000000000000000000000000000000000000003E838B13505B26867 we know in this example last 7 hex 5B26867<BR>
 run BitCrack.exe -b 128 -t 256 -p 1380 --stride 100000000 --keyspace 20000000005b26867:3ffffffffffffffff -o FOUND.txt -c 1K2wh7bdCYgFeipT8fnCS3GknWLKHPgJq5<br>
the python script generates 7 random  hex digits and places them in the end of the keyspace example 20000000005b26867<br>
Tries for a match if no match writes the tried to tried.txt checks tried.txt so no repeats then generates a new unique 7 hex digits  continuously. <br>
To run program run adust  -b 128 -t 256 -p 1380 in script to match your gpu DO NOT ADJUST STRIDE adjust time.sleep(33)  # Wait for 33 seconds before restarting to match your gpu time to complete the total keyspace<br>
run python3 p66.py and have bitcrack.exe in same folder a tried.txt database will be formed so no duplicate tries. DO not use command line below. Use run python3 p66.py<br>
<br>
<br>Example<br>
BitCrack.exe -b 128 -t 256 -p 1380 --stride 100000000 --keyspace 20000000005b26867:3ffffffffffffffff -o FOUND.txt -c 1K2wh7bdCYgFeipT8fnCS3GknWLKHPgJq5<br>
[2023-09-15.16:56:32] [Info] Compression : compressed<br>
[2023-09-15.16:56:32] [Info] Starting at : 0000000000000000000000000000000000000000000000020000000005B26867 (66 bit)<br>
[2023-09-15.16:56:32] [Info] Ending at   : 000000000000000000000000000000000000000000000003FFFFFFFFFFFFFFFF (66 bit)<br>
[2023-09-15.16:56:32] [Info] Range       : 000000000000000000000000000000000000000000000001FFFFFFFFFA4D9798 (65 bit)<br>
[2023-09-15.16:56:32] [Info] Initializing NVIDIA GeForce RTX 3060 Ti<br>
[2023-09-15.16:56:33] [Info] Generating 45,219,840 starting points (1725.0MB)<br>
[2023-09-15.16:56:55] [Info] 10.0%  20.0%  30.0%  40.0%  50.0%  60.0%  70.0%  80.0%  90.0%  100.0%<br>
[2023-09-15.16:56:58] [Info] Done<br>
[DEV: NVIDIA GeForce R 7953/8191MB] [00000000000000000000000000000000000000000000000240B0000005B26867 (66 bit)] [INC: 0, 0] [TARGET: 1] [SPEED: 578.81 MKey/s] [TOTAL: 1,085,2[DEV: NVIDIA GeForce R 7953/8191MB] <br>[0000000000000000000000000000000000000000000000028160000005B26867 (66 bit)] [INC: 0, 0] [TARGET: 1] [SPEED: 578.81 MKey/s] [TOTAL: 2,170,5[DEV: NVIDIA GeForce R 7953/8191MB] <br>[000000000000000000000000000000000000000000000002C210000005B26867 (66 bit)] [INC: 0, 0] [TARGET: 1] [SPEED: 578.81 MKey/s] [TOTAL: 3,255,8[DEV: NVIDIA GeForce R 7953/8191MB] <br>[00000000000000000000000000000000000000000000000302C0000005B26867 (66 bit)] [INC: 0, 0] [TARGET: 1] [SPEED: 578.81 MKey/s] [TOTAL: 4,341,1[DEV: NVIDIA GeForce R 7953/8191MB] <br>[0000000000000000000000000000000000000000000000034370000005B26867 (66 bit)] [INC: 0, 0] [TARGET: 1] [SPEED: 578.81 MKey/s] [TOTAL: 5,426,3[DEV: NVIDIA GeForce R 7953/8191MB] <br>[000000000000000000000000000000000000000000000003816E000005B26867 (66 bit)] [INC: 0, 0] [TARGET: 1] [SPEED: 573.98 MKey/s] [TOTAL: 6,466,4[DEV: NVIDIA GeForce R 7953/8191MB] <br>[000000000000000000000000000000000000000000000003BF6C000005B26867 (66 bit)] [INC: 0, 0] [TARGET: 1] [SPEED: 568.96 MKey/s] [TOTAL: 7,506,493,440] [00:00:11]<br>
[2023-09-15.16:57:15] [Info] Found key for address '1K2wh7bdCYgFeipT8fnCS3GknWLKHPgJq5'. Written to 'FOUND.txt'<br>
<br>
[2023-09-15.16:57:15] [Info] No targets remaining<br>
