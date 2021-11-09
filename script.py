#!/usr/bin/python3
import sys,os
print ("\n\nImported sys, os\n\n")

while True:
	input = input("What's the input sequence?\n\t") or "ATGTTCGGT"
	break
	
file = open('output.txt', 'a')
sys.stdout = file

# Translation table
gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
	
def tripkey(input, trip_start):
	trip_key = []
	for base in trip_start:
		if (base+3) < len(input)+1:
			triple = input[base:base+3]
			print("Now generating the triple: ", triple)
			trip_key = trip_key + [triple]
	print("Generated all triples: ", trip_key)
	return trip_key

def allkey(input):
	trip_start1 = list(range(0,len(input),3))
	trip_start2 = list(range(1,len(input)-1,3))
	trip_start3 = list(range(2,len(input)-2,3))
	all_keys = [tripkey(input, trip_start1)] + [tripkey(input, trip_start2)] + [tripkey(input, trip_start3)]
	print("All three frames generated: ", all_keys)
	return all_keys

# allkey(input)

def trans(keys):
	aa_list = []
	for frame in keys:
		aa = ""
		for key in frame:
			aa = aa + gencode.get(key,"X")
		aa_list = aa_list + [aa]
		print("Generated translation {0} for frame {1}.".format(aa,frame))
	print("All three translation generated: ", aa_list)
	return aa_list
	
# trans(allkey(input))

def main(input):
	reversed = input[::-1]
	print(">>> For FORWARD frames: ", trans(allkey(input)))
	print(">>> For REVERSED frames: ", trans(allkey(reversed)))
	result = [trans(allkey(input))] + [trans(allkey(reversed))]
	print(">>>>> Final result of translation of both FORWARD and REVERSED frames: ", result)
	return result

main(input)
file.close()

