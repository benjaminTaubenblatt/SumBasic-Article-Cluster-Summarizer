#!/bin/sh

python3 ./sumbasic.py orig ./docs/doc1*.txt > summaries/orig-1.txt
python3 ./sumbasic.py orig ./docs/doc2*.txt > summaries/orig-2.txt
python3 ./sumbasic.py orig ./docs/doc3*.txt > summaries/orig-3.txt
python3 ./sumbasic.py orig ./docs/doc4*.txt > summaries/orig-4.txt
python3 ./sumbasic.py orig ./docs/doc5*.txt > summaries/orig-5.txt

python3 ./sumbasic.py best-avg ./docs/doc1*.txt > summaries/best-avg-1.txt
python3 ./sumbasic.py best-avg ./docs/doc2*.txt > summaries/best-avg-2.txt
python3 ./sumbasic.py best-avg ./docs/doc3*.txt > summaries/best-avg-3.txt
python3 ./sumbasic.py best-avg ./docs/doc4*.txt > summaries/best-avg-4.txt
python3 ./sumbasic.py best-avg ./docs/doc5*.txt > summaries/best-avg-5.txt

python3 ./sumbasic.py simplified ./docs/doc1*.txt > summaries/simplified-1.txt
python3 ./sumbasic.py simplified ./docs/doc2*.txt > summaries/simplified-2.txt
python3 ./sumbasic.py simplified ./docs/doc3*.txt > summaries/simplified-3.txt
python3 ./sumbasic.py simplified ./docs/doc4*.txt > summaries/simplified-4.txt
python3 ./sumbasic.py simplified ./docs/doc5*.txt > summaries/simplified-5.txt

python3 ./sumbasic.py leading ./docs/doc1*.txt > summaries/leading-1.txt
python3 ./sumbasic.py leading ./docs/doc2*.txt > summaries/leading-2.txt
python3 ./sumbasic.py leading ./docs/doc3*.txt > summaries/leading-3.txt
python3 ./sumbasic.py leading ./docs/doc4*.txt > summaries/leading-4.txt
python3 ./sumbasic.py leading ./docs/doc5*.txt > summaries/leading-5.txt
