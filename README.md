# SumBasic-Implementation

An implementation of SumBasic as described in The Impact of Frequency on Summarization by Ani Nenkova and Lucy Vanderwende along with other custom versions of the algorithm. Done as part of an assignment for COMP 550: Natural Language Processing at McGill University. 

All example summaries from the program are in /summaries

All articles used are in /docs

There are 4 versions of the algorithm, namely orig, best-avg, simplified, and leading as outline in the assignment (a4.pdf in the repo)

The shell script run.sh will run all 4 versions of the SumBasic algorithm
on all 5 article clusters and output each file to the /summaries directory
as version-#.txt (ex. simplified-1.txt) which represents the simplified version
of the SumBasic algorithm on article cluster 1.

to run:

python sumbasic.py <method_name> <file_n>*
or
python sumbasic.py orig doc4*.txt
