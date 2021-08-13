#!/bin/bash

set -ex

wget https://downloads.tatoeba.org/exports/per_language/toki/toki_sentences.tsv.bz2
bunzip2 toki_sentences.tsv.bz2 
cut -f 3 toki_sentences.tsv > tatoeba.txt

