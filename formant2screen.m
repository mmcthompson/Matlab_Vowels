function [x_pos, y_pos] = formant2screen(F2_pos, F1_pos)

x_pos = (F2_pos - 2500).*1920./(800 - 2500);
y_pos = (F1_pos - 900).*1080./(100 - 900);