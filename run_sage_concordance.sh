# sage-ipython doesn't seem to use its --quiet or --no-banner flags, so just delete non-STDOUT console messages with grep

# Uncomment out the last line to overwrite the saved output file

sage-ipython concordance.py | grep -v "Exiting Sage" | grep -v "─" | grep -v "│"
#sage-ipython concordance.py | grep -v "Exiting Sage" | grep -v "─" | grep -v "│" > sage_concordance.stdout.txt
