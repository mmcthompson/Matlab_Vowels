function [av_onset] = mean_speech_onset(input_y, t, av_length)
%function which takes as input the array of y values for a y(t) function,
%the array of t values associated with this y(t), and the length of time
%after speech onset that you want to average the y(t) value over

%In most cases, input_y will be f1 or f2, t will be ftrack_taxis, and 
%av_length will be .050 (50 ms), as per Carrie's paper

%the last timepoint we want (50 ms after onset)
target_index = t(1) + av_length;

%Find the point in the time array closest to 50ms after onset
last_index = dsearchn(t,target_index);

%t should be the same length (and therefore have compatible indexes with)
%input_y
av_onset = mean(input_y(1:last_ind]×•@N@­