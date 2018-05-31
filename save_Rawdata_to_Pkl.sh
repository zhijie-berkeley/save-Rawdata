#!/bin/sh
# to give permission: chmod +x save_Rawdata_to_Pkl.sh
# to run this shell: ./save_Rawdata_to_Pkl.sh

echo start saving rawdata to pkl ...

echo start saving 180228 WT nucleosome 2.5KHz hopping data
python /Volumes/Zhijie_Chen/Fleezers-data/savedata_txt.py /Volumes/Zhijie_Chen/Fleezers-data/180228/180228-savedata.txt -e . pkl

echo start saving 180305 uH2A nucleosome 2.5KHz hopping data
python /Volumes/Zhijie_Chen/Fleezers-data/savedata_txt.py /Volumes/Zhijie_Chen/Fleezers-data/180305/180305-savedata.txt -e . pkl

echo start saving 180306 uH2B nucleosome 2.5KHz hopping data
python /Volumes/Zhijie_Chen/Fleezers-data/savedata_txt.py /Volumes/Zhijie_Chen/Fleezers-data/180306/180306-savedata.txt -e . pkl

echo start saving 180312 H2A.Z nucleosome 2.5KHz hopping data
python /Volumes/Zhijie_Chen/Fleezers-data/savedata_txt.py /Volumes/Zhijie_Chen/Fleezers-data/180312/180312-savedata.txt -e . pkl

echo start saving 180314 M3_M7 nucleosome 2.5KHzhopping data
python /Volumes/Zhijie_Chen/Fleezers-data/savedata_txt.py /Volumes/Zhijie_Chen/Fleezers-data/180314/180314-savedata.txt -e . pkl

echo start saving 180409 single NPS unzipping data
python /Volumes/Zhijie_Chen/Fleezers-data/savedata_txt.py /Volumes/Zhijie_Chen/Fleezers-data/180409/180409-savedata.txt -e . pkl

echo done