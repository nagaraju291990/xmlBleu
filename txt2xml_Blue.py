#program to convert txt file to xml for calcalating Bleu score 

from argparse import ArgumentParser
import os
import sys
import pysrt

parser = ArgumentParser(description='Convert txt to xml for BLEU calculation \n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + "-t=src/tgt/ref -i=text_file.txt " + "-sl=English/Hindi/Telugu"
						)
parser.add_argument("-i", "--input", dest="inputfile",
                    help="provide a txt file name", required=True)

parser.add_argument("-t", "--type", dest="type",
                    help="provide type like src/tgt/ref", required=True)

parser.add_argument("-sl", "--srclang",
                    dest="src_lang", help="sl=English", required=True)

parser.add_argument("-tl", "--tgtlang",
                    dest="tgt_lang", help="sl=Hindi", required=False)

args = parser.parse_args()

inputfile = args.inputfile
src_lang = args.src_lang
xtype = args.type

if(inputfile is None or inputfile == ""):
	print("Please provide a inputfile")
	exit()

if(src_lang is None or src_lang == ""):
	print("Please provide source language")
	exit()

if(xtype is None or xtype == ""):
	print("Please provide type as src/mt/ref")
	exit()

if(xtype == "tgt" or xtype == "ref"):
	tgt_lang =  args.tgt_lang
	if(tgt_lang is None or tgt_lang == ""):
		print("Please provide target language")
		exit()


fp = open(inputfile) # Open file on read mode
lines = fp.read().split("\n") # Create a list containing all lines
fp.close() # Close file

print ('<?xml version="1.0" encoding="UTF-8"?>')
print ('<!DOCTYPE mteval SYSTEM "ftp://jaguar.ncsl.nist.gov/mt/resources/mteval-xml-v1.3.dtd">')

if(xtype == "src"):
	print ('<mteval>\n<srcset setid="example_set" srclang="', src_lang, '">',sep='')
elif(xtype == "tgt"):
	print ('<mteval>\n<tstset setid="example_set" srclang="' , src_lang, '" trglang="', tgt_lang,'" sysid="sample_system">',sep='')
elif(xtype == "ref"):
	print ('<mteval>\n<refset setid="example_set" srclang="' , src_lang, '" trglang="', tgt_lang,'" refid="ref1">',sep='')

print ('<doc docid="doc1" genre="nw">\n<p>')

i =0;
for line in lines:
	if(line != ""):
		i = i +1
		print ('<seg id="', i ,'">', line ,'</seg>', sep='')

print ("</p>\n</doc>")

if(xtype == "src"):
	print ("</srcset>")
if(xtype == "tgt"):
	print ("</tstset>")
if(xtype == "ref"):
	print ("</refset>")

print ("</mteval>")