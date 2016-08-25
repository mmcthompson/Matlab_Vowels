
function [ts, ts_sd, voice, voice_sd] = voice_screen_formant_stats(goalx, respx, respy, dataVals, goodfiles)

%Find the median F1 and F2 productions using the touchscreen
%For right now, we're only going to look at the final trial block just
%because it's the simplest way I can think of right now to determine the
%production that the subject has "settled on"

%Sort by cue
rbt_array_b4 = split_by_target(respx(361:480), respy(361:480), goalx(361:480));
ts_F1.cue1 = median(rbt_array_b4{1,1}(2,:));
ts_F2.cue1 = median(rbt_array_b4{1,1}(1,:));
ts_F1.cue2 = median(rbt_array_b4{1,2}(2,:));
ts_F2.cue2 = median(rbt_array_b4{1,2}(1,:));
ts_F1.cue3 = median(rbt_array_b4{1,3}(2,:));
ts_F2.cue3 = median(rbt_array_b4{1,3}(1,:));

ts = [ts_F2, ts_F1];

%Find the standard deviation for F1 and F2 productions using the
%touchscreen

%Standard deviation doesn't really make too much sense for a 2D metric.
%Perhaps we should do clustering? But that is so sensitive to outliers
%For now, just do sd for both F1 and F2 and check out Carrie's paper again
%when you get a chance

ts_sd_F1.cue1 = std(rbt_array_b4{1,1}(2,:));
ts_sd_F2.cue1 = std(rbt_array_b4{1,1}(1,:));
ts_sd_F1.cue2 = std(rbt_array_b4{1,2}(2,:));
ts_sd_F2.cue2 = std(rbt_array_b4{1,2}(1,:));
ts_sd_F1.cue3 = std(rbt_array_b4{1,3}(2,:));
ts_sd_F2.cue3 = std(rbt_array_b4{1,3}(1,:));

ts_sd = [ts_sd_F2, ts_sd_F1];

%Find some way to do this by block, or possible after responses have
%plateaued? I'm honestly not really sure how to do this. Fourth block only?
%After the average derivative or a trendline is below a certain slope?

%Find the median F1 and F2 productions for vocal productions

%First find the median per production so longer productions don't unfairly
%schew the data

m = 1;
n = 1;
p = 1;

%Sort the trials by cue
%Average over the first 50ms, best approximation of Carrie's analysis
for i=1:length(dataVals)
    if mod(goodfiles(i),3) == 1
        %Head 
        voice_array{1,2}(2,m) = mean_speech_onset(dataVals(i).f1,dataVals(i).ftrack_taxis,.050);
        voice_array{1,2}(1,m) = mean_speech_onset(dataVals(i).f2,dataVals(i).ftrack_taxis,.050);
        m = m+1;
    elseif mod(goodfiles(i),3) == 2
        %Heed
        voice_array{1,3}(2,n) = mean_speech_onset(dataVals(i).f1,dataVals(i).ftrack_taxis,.050);
        voice_array{1,3}(1,n) = mean_speech_onset(dataVals(i).f2,dataVals(i).ftrack_taxis,.050);
        n = n+1;
    elseif mod(goodfiles(i),3) == 0
        %Car
        voice_array{1,1}(2,p) = mean_speech_onset(dataVals(i).f1,dataVals(i).ftrack_taxis,.050);
        voice_array{1,1}(1,p) = mean_speech_onset(dataVals(i).f2,dataVals(i).ftrack_taxis,.050);
        p = p+1;
    end
end


%Find the median of the medians for each cue type
voice_F1.cue1 = median(voice_array{1,1}(2,:));
voice_F2.cue1 = median(voice_array{1,1}(1,:));
voice_F1.cue2 = median(voice_array{1,2}(2,:));
voice_F2.cue2 = median(voice_array{1,2}(1,:));
voice_F1.cue3 = median(voice_array{1,3}(2,:));
voice_F2.cue3 = median(voice_array{1,3}(1,:));

voice = [voice_F2, voice_F1];

%Find the standard deviation for F1 and F2 during vocal productions

voice_sd_F1.cue1 = std(voice_array{1,1}(2,:));
voice_sd_F2.cue1 = std(voice_array{1,1}(1,:));
voice_sd_F1.cue2 = std(voice_array{1,2}(2,:));
voice_sd_F2.cue2 = std(voice_array{1,2}(1,:));
voice_sd_F1.cue3 = std(voice_array{1,3}(2,:));
voice_sd_F2.cue3 = std(voice_array{1,3}(1,:));

voice_sd = [voice_sd_F2, voice_sd_F1];

%Find a way to compare the F1 and F2 productions for speakers to the
%productions they produced with the screen. Focus on inter-subject
%differences that are consistent across platforms
plot_voice_cues(ts, ts_sd, voiýÖ°?§IºØãÄ