clc;
clear all;
close all;

s =tf('s');
g=(s)/[(s+2)*(s^2+s+8)]
ltiview(g)