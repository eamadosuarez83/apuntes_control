clc;
clear all;
close all;

s =tf('s');
g=(s+3)/[(s+2)*(s^2+s+8)]
k = 386
Td = 1000;
Ti = 900;

gc = k*[1+(1/Ti)*(1/s)+Td*s]
T=feedback(gc*g,1)
ltiview(T)