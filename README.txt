

All example summaries from the program are in /summaries

All articles used are in /docs

The shell script run.sh will run all 4 versions of the SumBasic algorithm
on all 5 article clusters and output each file to the /summaries directory
as version-#.txt (ex. simplified-1.txt) which represents the simplified version
of the SumBasic algorithm on article cluster 1.

All code for this project is in sumbasic.py including the main method, a Cluster,
Article, SBU (SumBasic Unit), and Sentence class used for performing the algorithms
and storing relevant information.

to run:

python sumbasic.py <method_name> <file_n>*
or
python sumbasic.py orig doc4*.txt
