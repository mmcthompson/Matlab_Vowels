%%Megan attempts to synthesize formants based on input from touchscreen location
%Based on code from Vowel_Synthesis_GUI25.m (source code on Matlab Central)
%http://www.mathworks.com/matlabcentral/fileexchange/45449-vowel-synthesis
%Credit Rabiner, Shafer
function formant_synthesize_playback(f1,f2)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Initialize Variables

% fs: signal sampling rate
    %For now, sampling rate hard-coded. Will investigate latter what
    %exactly it does.
    fs = 6000; %sampling rate in Hz
    
    t = 0:1/fs:.3; %time in seconds
    
    f = 1000; %tone in Hz
    
    % convolve vowel response with glottal pulse and then with pitch excitation
    y = sin(2.*pi.*f.*t);
    
    
    % play out convolved sequence
    soundsc(y,fs);