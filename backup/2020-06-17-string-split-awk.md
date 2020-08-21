---
layout: post
title: "Simple string manipulations (splits/replaces) with awk"
location: "Japan"
tags: [awk, commandline, string, split]
---

_For personal reference:_

Lately, I've been doing loads of CSV processing on the terminal with lots of string replacing/splitting. There are probably better (shorter) ways to do this but I've been leaning on `awk` a lot recently.

Some examples.

{% highlight shell %}
# One-line separator replace:
$ echo "1,2,3,4,5" | awk '{gsub(/,/," ");print}'
1 2 3 4 5

# Then I can use it with something like:
for v in $(echo "1,2,3,4,5" | awk '{gsub(/,/," ");print}'); do echo "val=$v"; done
val=1
val=2
val=3
val=4
val=5

# Another separator:
$ echo "1|2|3|4|5" | awk '{gsub(/\|/,",");print}'
1,2,3,4,5

# Join multiple lines with a separator...
# Ref: https://www.baeldung.com/linux/join-multiple-lines
$ cat file.txt
one
two
three
four
five
five

# ...while removing duplicates:
$ cat file.txt | uniq | awk -v d="," '{s=(NR==1?s:s d)$0}END{print s}'
one,two,three,four,five
{% endhighlight %}
