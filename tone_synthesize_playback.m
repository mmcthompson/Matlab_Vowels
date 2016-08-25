%%Megan attempts to synthesize formants based on input from touchscreen location
%Based on code from Vowel_Synthesis_GUI25.m (source code on Matlab Central)
%http://www.mathworks.com/matlabcentral/fileexchange/45449-vowel-synthesis
%Credit Rabiner, Shafer
function tone_synthesize_playback()
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% R: Signal length
    R=.60;%Determines how long playback is, seemingly the time in centiseconds (100=1second)
    
% fs: signal sampling rate
    fs = 6000; 
        
% freq: pitch frequency
    freq = 1000;
    
% create array of pitch periods
    values = 0:1/fs:R;
    
% create pitch pulse contour
    amp = 10;
    a = amp*sin(2*pi*freq*values);
    
    soundsc(a,fs)