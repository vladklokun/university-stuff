reset

set terminal svg noenhanced size 600,300 fname 'STIX Two Text,10'
#set terminal png size 600,400

set output '1p5v-nodiode.svg'
#set output '1p5v-nodiode.png'

set encoding utf8

set border 3 front lc "#000000"
set tics nomirror

set arrow from graph 1,0 to graph 1.025,0 size screen 0.025,15,60 filled lc "#000000"
set arrow from graph 0,1 to graph 0,1.05 size screen 0.025,15,60 filled lc "#000000"

set multiplot layout 2, 1
set grid lt 1 lc "#808080"
set xlabel "t (\\si{\\micro\\second})"

set yrange [-5:15]
set xrange [1.13e-6:1.5e-6]

set xtics 0.00000037/10.0
set format x "%.2s"
#
unset key
unset ylabel
set ylabel "$U_{\\text{ВХ}}$ (В)"
plot "1p5v-nodiode-in" with lines
#
unset key
unset ylabel
set ylabel "$U_{\\text{ВИХ}}$ (В)"
plot "1p5v-nodiode-out" with lines
#
unset multiplot