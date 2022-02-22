{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 .SFNSMono-Regular;}
{\colortbl;\red255\green255\blue255;\red189\green198\blue208;}
{\*\expandedcolortbl;;\cssrgb\c78824\c81961\c85098;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl380\partightenfactor0

\f0\fs27\fsmilli13600 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 def main():\
    try:\
        configuration = open('config.txt')\
    except FileNotFoundError:\
        print("Couldn't find the config.txt file!")\
    except IsADirectoryError:\
        print("Found config.txt but it is a directory, couldn't read it")\
}