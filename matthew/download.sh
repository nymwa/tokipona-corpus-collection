#!/bin/bash

set -ex

echo '' > prince.txt

for N in 01 02 03 04; do
	wget -q -O - "https://raw.githubusercontent.com/davidar/nltk-tp/master/Corpus/Derivative%20Works%20of%20(C)/Michael%20Freedman/LittlePrince/${N}%20LittlePrince.txt" | tondi >> prince.txt
done

for N in 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25; do
	wget -q -O - "https://raw.githubusercontent.com/davidar/nltk-tp/master/Corpus/Derivative%20Works%20of%20(C)/Michael%20Freedman/LittlePrince/${N}%20Little%20Prince.txt" | tondi >> prince.txt
done

echo '' > mika.txt
C1="https://raw.githubusercontent.com/matthewdeanmartin/tokipona.parser/master/TokiPonaTools/TokiPona/corpus/jan%20Mika/soweli%20nasa%20-%20pipi%20pi%20moli%20luka.txt"
C2="https://raw.githubusercontent.com/matthewdeanmartin/tokipona.parser/master/TokiPonaTools/TokiPona/corpus/jan%20Mika/soweli%20nasa%20-%20soweli%20pi%20uta%20waso.txt"
C3="https://raw.githubusercontent.com/matthewdeanmartin/tokipona.parser/master/TokiPonaTools/TokiPona/corpus/jan%20Mika/soweli%20nasa%20-%20waso%20soweli.txt"

for N in $C1 $C2 $C3; do
	wget -q -O - $N | tondi >> mika.txt
done

echo '' > ote.txt
C01="https://raw.githubusercontent.com/matthewdeanmartin/tokipona.parser/master/TokiPonaTools/TokiPona/corpus/jan%20Ote/advanced-%20jan%20Kikamesi.%20utala%20pi%20jan%20Kuwawa.txt"
C02="https://raw.githubusercontent.com/matthewdeanmartin/tokipona.parser/master/TokiPonaTools/TokiPona/corpus/jan%20Ote/easy%20%20-%20soweli%20suli%20li%20lape%20mute.txt"
C03="https://raw.githubusercontent.com/matthewdeanmartin/tokipona.parser/master/TokiPonaTools/TokiPona/corpus/jan%20Ote/easy%20-%20pipi%20musi%20en%20pipi%20pali.txt"
C04="https://raw.githubusercontent.com/matthewdeanmartin/tokipona.parser/master/TokiPonaTools/TokiPona/corpus/jan%20Ote/easy%20-%20soweli%20en%20kili.txt"
C05="https://raw.githubusercontent.com/matthewdeanmartin/tokipona.parser/master/TokiPonaTools/TokiPona/corpus/jan%20Ote/easy-%20sike%20wan%20orig%20Jan%20Pije%20(fair%20use).txt"
C06="https://raw.githubusercontent.com/matthewdeanmartin/tokipona.parser/master/TokiPonaTools/TokiPona/corpus/jan%20Ote/intermediate-%20ma%20tomo%20Pape%20(Babel).txt"
C06="https://raw.githubusercontent.com/matthewdeanmartin/tokipona.parser/master/TokiPonaTools/TokiPona/corpus/jan%20Ote/jan%20Eloto%20-%20pipi%20pali%20en%20kiwen%20suno.txt"
C07="https://raw.githubusercontent.com/matthewdeanmartin/tokipona.parser/master/TokiPonaTools/TokiPona/corpus/jan%20Ote/ma%20Alansi.txt"
C08="https://raw.githubusercontent.com/matthewdeanmartin/tokipona.parser/master/TokiPonaTools/TokiPona/corpus/jan%20Ote/meli%20pona%20(jan%20Pije).txt"
C09="https://raw.githubusercontent.com/matthewdeanmartin/tokipona.parser/master/TokiPonaTools/TokiPona/corpus/jan%20Ote/soweli%20nasa-%20kala%20akesi%20kiwen%20pi%20nimi%20Limulu.txt"
C10="https://raw.githubusercontent.com/matthewdeanmartin/tokipona.parser/master/TokiPonaTools/TokiPona/corpus/jan%20Ote/soweli%20nasa-%20soweli%20pi%20poki%20sinpin.txt"
C11="https://raw.githubusercontent.com/matthewdeanmartin/tokipona.parser/master/TokiPonaTools/TokiPona/corpus/jan%20Ote/soweli%20nasa-%20waso%20pi%20noka%20laso.txt"
C12="https://raw.githubusercontent.com/matthewdeanmartin/tokipona.parser/master/TokiPonaTools/TokiPona/corpus/jan%20Ote/tan%20jan%20Eloto.%20jan%20pi%20ma%20seme%20--.txt"

for N in $C01 $C02 $C03 $C04 $C05 $C06 $C07 $C08 $C09 $C10 $C11 $C12; do
	wget -q -O - $N | iconv -f iso-8859-1 -t utf8 | tondi >> ote.txt
done

