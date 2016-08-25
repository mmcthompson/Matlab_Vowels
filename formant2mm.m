function [x_mm, y_mm] = formant2mm(F2_pos, F1_pos)

x_pos = (F2_pos - 2500).*1920./(800 - 2500);
y_pos = (F1_pos - 900).*1080./(100 - 900);

x_mm = x_pos.*(418/1920);
y_mm = y_pos.*(236/1080);