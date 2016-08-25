function [F2_pos, F1_pos] = screen2formant(x_pos, y_pos)

F2_pos = ((800 - 2500)/1920)*x_pos + 2500;
F1_pos = ((100 - 900)/1080)*y_pos + 900;