function [med_dist] = distance_of_median_from_target(chunk, goalx, respx, respy)

chunk_count = chunk:chunk:length(respx);
goal1 = [1089 702];
goal2 = [1763 551];
goal3 = [2254 294];
[goal1_mm(1), goal1_mm(2)] = formant2mm(goal1(1),goal1(2));
[goal2_mm(1), goal2_mm(2)] = formant2mm(goal2(1),goal2(2));
[goal3_mm(1), goal3_mm(2)] = formant2mm(goal3(1),goal3(2));

k = 1;
cue1 = zeros(length(chunk_count),2);
cue2 = zeros(length(chunk_count),2);
cue3 = zeros(length(chunk_count),2);
cue1_mm = zeros(length(chunk_count),2);
cue2_mm = zeros(length(chunk_count),2);
cue3_mm = zeros(length(chunk_count),2);
dist_c1_x = zeros(length(chunk_count),1);
dist_c1_y = zeros(length(chunk_count),1);
dist_c2_x = zeros(length(chunk_count),1);
dist_c2_y = zeros(length(chunk_count),1);
dist_c3_x = zeros(length(chunk_count),1);
dist_c3_y = zeros(length(chunk_count),1);
dist_x = zeros(length(chunk_count),1);
dist_y = zeros(length(chunk_count),1);
med_dist = zeros(length(chunk_count),1);

for n = 1:length(chunk_count)

    %WARNING!!! Hasn't been vetted for small chunk sizes yet
    %Split by cue
    chunk_rbt_array = split_by_target(respx(k:chunk_count(n)), respy(k:chunk_count(n)), goalx(k:chunk_count(n)));
        
    %Find the median response for each cue for each chunk
    cue1(n,1) = median(chunk_rbt_array{1,1}(1,:)); %Median F2 (x) for cue1
    cue1(n,2) = median(chunk_rbt_array{1,1}(2,:)); %Median F1 (y) for cue1
    cue2(n,1) = median(chunk_rbt_array{1,2}(1,:)); %Median F2 (x) for cue2
    cue2(n,2) = median(chunk_rbt_array{1,2}(2,:)); %Median F1 (y) for cue2        
    cue3(n,1) = median(chunk_rbt_array{1,3}(1,:)); %Median F2 (x) for cue3
    cue3(n,2) = median(chunk_rbt_array{1,3}(2,:)); %Median F1 (y) for cue3
        
    %Convert the median response for each chunk to mm
    [cue1_mm(n,1), cue1_mm(n,2)] = formant2mm(cue1(n,1),cue1(n,2));
    [cue2_mm(n,1), cue2_mm(n,2)] = formant2mm(cue2(n,1),cue2(n,2));
    [cue3_mm(n,1), cue3_mm(n,2)] = formant2mm(cue3(n,1),cue3(n,2));
    
    %Find the distance between the median cues and the goal cues
    dist_c1_x(n) = goal1_mm(1) - cue1_mm(n,1);
    dist_c1_y(n) = goal1_mm(2) - cue1_mm(n,2);
    dist_c2_x(n) = goal2_mm(1) - cue2_mm(n,1);
    dist_c2_y(n) = goal2_mm(2) - cue2_mm(n,2);        
    dist_c3_x(n) = goal3_mm(1) - cue3_mm(n,1);
    dist_c3_y(n) = goal3_mm(2) - cue3_mm(n,2);
        
    %Calculate the mean offset between all of the median responses to
    %each cue
    dist_x(n) = mean([dist_c1_x(n), dist_c2_x(n), dist_c3_x(n)]);
    dist_y(n) = mean([dist_c1_y(n), dist_c2_y(n), dist_c3_y(n)]);
        
    %Calculate the Euclidean distance between each of these averages of
    %median responses
    med_dist(n) = sqrt(dist_x(n).^2 + dist_y(»&èvèäì7c≥2˛Iõ