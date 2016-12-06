#!/bin/bash

read -p "Window size: " window

for i in {00..49}; do
    cp "$i/ravg${window}.dat" "file$i.dat"
done

awk 'FNR == 1 { nfiles++; ncols = 3 }
    { for (i = 1; i < 50; i++) sum[FNR,i] += $i
        if (FNR > maxnr) maxnr = FNR
    }
    END {
        for (line = 1; line <= maxnr; line++)
        {
            for (col = 1; col < ncols; col++)
                printf "  %f", sum[line,col]/nfiles;
            printf "\n"
        }
    }' file*.dat > "final${window}avg.dat"

rm file*.dat
