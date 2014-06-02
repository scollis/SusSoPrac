#!/usr/bin/env python
import sys

if __name__=='__main__':
  infile = sys.argv[1]
  filehnd = open(infile, 'r')
  all_lines = filehnd.readlines()
  filehnd.close()
  emails = []
  for this_line in all_lines:
    entries = this_line.split('|')
    for entry in entries:
      if '@' in entry:
        emails.append(entry)
  for email in emails:
    print email 
