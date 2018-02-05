reset

set terminal svg noenhanced size 600,300 fname 'STIX Two Text,10'
#set terminal png size 600,400

set output '2p3v-diode.svg'
#set output '2p3v-diode.png'

set encoding utf8

set border 3 front lc "#000000"
set tics nomirror

set arrow from graph 1,0 to graph 1.025,0 size screen 0.025,15,60 filled lc "#000000"
set arrow from graph 0,1 to graph 0,1.05 size screen 0.025,15,60 filled lc "#000000"

set multiplot layout 2, 1
set grid lt 1 lc "#808080"
set xlabel "t (\\si{\\micro\\second})"

set yrange [-5:15]
#set xrange [0.8e-6:1.8e-6]
set xrange [1.15e-6:1.75e-6]

#set xtics 0.0000010/5.0
set xtics 0.00000060/10.0
set format x "%.2s"
#
unset key
unset ylabel
set ylabel "$U_{\\text{Б}}$ (В)"
plot "2p3v-diode-in" with lines
#
unset key
unset ylabel
set ylabel "$U_{\\text{К}}$ (В)"
plot "2p3v-diode-out" with lines
#
unset multiplot