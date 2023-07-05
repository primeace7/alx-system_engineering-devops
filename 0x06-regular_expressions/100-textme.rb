#!/usr/bin/env ruby
print ARGV[0].scan(/[\w\W]+\[from:(\S+)\][\w\W]+\[to:\S+\][\w\W]\[flags:\S+\]\
[\w\W]+/).join
print (',')
print ARGV[0].scan(/[\w\W]+\[from:\S+\][\w\W]+\[to:(\S+)\][\w\W]\[flags:\S+\]\
[\w\W]+/).join
print (',')
print ARGV[0].scan(/[\w\W]+\[from:\S+\][\w\W]+\[to:\S+\][\w\W]\[flags:(\S+)\]\
[\w\W]+/).join
puts ''
