function [rbt_array, dist, cluster_array] = formant_stats(goalx, goaly, respx, respy, chunk)
%Calculates the distance (in mm) between the target and the response, a
%measure of accuracy
%Calculates the clustering coefficient, the euclidean distance (in mm) between
%all of the responses to the same target, a measure of precision
%Should also return median and standard deviation F1 and F2 Productions per cue
%Plot chuncked goals and responses

trials = 1:length(goalx);
chunked_trials = chunk:chunk:length(respx);

%%%%Distance%%%%

%Calculate the distance between each response and the target
dist = distance_from_target(1, goalx, goaly, respx, respy);
figure
plot(trials,dist,'.')
title('Discrete distance from target')
xlabel('Trial')
ylabel('Distance from target')

%smooth_dist = smooth(dist,30);
dist = distance_from_target(chunk, goalx, goaly, respx, respy);

% %Smoothed distance from target as a function of trial
% figure
% plot(trials,smooth_dist)
% title('Smoothed distance from target')
% xlabel('Trial')
% ylabel('Distance from target')

%chunked distance from target as a function of trial
figure
plot(chunked_trials,dist)
title('Chunked distance from target')
xlabel('Trial')
ylabel('Distance from target')


%%%%Map Plots%%%%

%returns in a form of {[cue1x; cue1y],[cue2x; cue2y],[cue3x; cue3y]}
rbt_array = split_by_target(respx,respy,goalx);

%Plot all responses and targets on one plot
plot_formant_cues(rbt_array);
title('All target cues and responses')

% %Plot each trial block's responses relative the the targets individually
% rbt_array_b1 = split_by_target(respx(1:120),respy(1:120),goalx(1:120));
% plot_formant_cues(rbt_array_b1);
% title('Block 1 cues and responses')
% 
% rbt_array_b2 = split_by_target(respx(121:240),respy(121:240),goalx(121:240));
% plot_formant_cues(rbt_array_b2);
% title('Block 2 cues and responses')
% 
% rbt_array_b3 = split_by_target(respx(241:360),respy(241:360),goalx(241:360));
% plot_formant_cues(rbt_array_b3);
% title('Block 3 cues and responses')
% 
% rbt_array_b4 = split_by_target(respx(361:480),respy(361:480),goalx(361:480));
% plot_formant_cues(rbt_array_b4);
% title('Block 4 cues and responses')

%%%%Clustering%%%%

%Calculate the tightness of the clustering (precistion) both continuously
%and chunked
cluster_array = return_cluster_tightness(chunk, respx, respy, goalx);

%Plotting the chunked clustering
figure
plot(chunked_trials,cluster_array)
title('Chunked tightness of clusters')
ylabel('Mean Euclidean distance between points (mm)')
xlabel('Trial')

        