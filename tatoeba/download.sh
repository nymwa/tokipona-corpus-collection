#!/bin/bash

set -ex

wget https://downloads.tatoeba.org/exports/per_language/tok/tok_sentences.tsv.bz2
bunzip2 tok_sentences.tsv.bz2
cut -f 3 tok_sentences.tsv > tatoeba.txt

