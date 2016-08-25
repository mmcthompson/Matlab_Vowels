function [rbt_dist_sums] = distance_by_cue(goalx, goaly, respx, respy)

%Split the responses by goal

%Calculate the distance from each of the test funds from their respective
%targets
dist_array = distance_from_target(1, goalx, goaly, respx, respy);

%split the distances by their respective goal cues (putting in a dummy
%variable for the y variable, as only two dimmensions will be needed for
%the bar chart
[rbt_dist_array] = split_by_target(dist_array, respy, goalx);
dist_dims = size(rbt_dist_array);

if dist_dims(2) == 5
    %There are 5 targets represented
    rbt_dist_sums = [sum(rbt_dist_array{1,1}(1,:)), sum(rbt_dist_array{1,2}(1,:)), sum(rbt_dist_array{1,3}(1,:)), sum(rbt_dist_array{1,4}(1,:)), sum(rbt_dist_array{1,5}(1,:))];    
elseif dist_dims(2) == 3
    %There are 3 targets represented
    rbt_dist_sums = [sum(rbt_dist_array{1,1}(1,:)), sum(rbt_dist_array{1,2}(1,:)), sum(rbt_dist_array{1,3}(1,:))];
end

figure;
bar(rbt_dist_sums)