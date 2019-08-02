## Script to convert txt files into XML format for calculating bleu score


### How to run?

   python3 txt2xml_Blue.py --type=src -i=1-Cartilage-harvest-eng-source.txt -sl=english
   python3 txt2xml_Blue.py --type=tgt -i=1-Cartilage-harvest-hin-gmt.txt -sl=english -tl=hindi 
   python3 txt2xml_Blue.py --type=ref -i=1-Cartilage-harvest-hin-pe.txt -sl=english -tl=hindi 
