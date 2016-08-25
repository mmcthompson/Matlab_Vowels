function [mean_dist, mean_cluster, mean_med_dist] = groupstats(logfile_list,chunk)

logfile_fid = fopen(logfile_list);

k=1;

%reads a list of paths to logfiles
while ~feof(logfile_fid) 
    %opens them and parses them with formant_logfile_parse
    tline = fgetl(logfile_fid); %should be the address to another logfile
    
    %runs formant parsing (and by extention, subject-specific stats) on
    %each of the listed subjects
    [subject(k).goalx, subject(k).goaly, subject(k).respx, subject(k).respy] = formant_logfile_parse(tline);
    k = k+1;
end

fclose(logfile_fid);

chunked_trials = chunk:chunk:length(subject(1).respx);
dist_sum = 0;
cluster_sum = 0;
med_dist_sum = 0;

for i = 1:length(subject)
    
    %Collect all of the formant stats from each subject
    [subject(i).rbt_array, subject(i).dist, subject(i).cluster_array] = formant_stats(subject(i).goalx, subject(i).goaly, subject(i).respx, subject(i).respy, chunk);
    [subject(i).med_dist] = distance_of_median_from_target(chunk, subject(i).goalx, subject(i).respx, subject(i).respy);
    
    %Find the average distance from target and the average clustering tightness
    %for all subjects including SEM accross subjects
    
    %Keep track of all values for the purposes of a sem plot
    if exist('distance_matrix','var')
        distance_matrix = [distance_matrix; subject(i).dist];
    else
        distance_matrix = subject(i).dist;
    end
    dist_sum = dist_sum + subject(i).dist;
    
    %Find the average clustering tightness of chunks for all subjects
    %including SEM accross subjects
    
    %Keep track of all values for the purposes of a sem plot
    if exist('cluster_matrix','var')
        cluster_matrix = [cluster_matrix; subject(i).cluster_array];
    else
        cluster_matrix = subject(i).cluster_array;
    end   
    cluster_sum = cluster_sum + subject(i).cluster_array;

    %Find the average distance between the median response and target for
    %all subjects including SEM across subjects
    if exist('med_dist_matrix','var')
        med_dist_matrix = [med_dist_matrix; subject(i).med_dist'];
    else
        med_dist_matrix = subject(i).med_dist';
    end
    med_dist_sum = med_dist_sum + subject(i).med_dist';
    
end

%Calculating the mean and sem for distance across subjects
mean_dist = dist_sum./i;
fprintf('sd of the mean distance is %d\n',std(distance_matrix))
sem_mean_dist = std(distance_matrix)./sqrt(i);

%Calculating the mean and sem for cluster tightness across subjects
mean_cluster = cluster_sum./i;
fprintf('sd of the mean cluster tightness is %d\n',std(cluster_matrix))
sem_mean_cluster = std(cluster_matrix)./sqrt(i);

%Calculating the mean and sem for distance from median responses across
%subjects
mean_med_dist = med_dist_sum./i;
sem_mean_med_dist = std(med_dist_matrix)./sqrt(i);

%Plotting the distance with sem bars
figure(1001);
shadedErrorBar(chunked_trials,mean_dist',sem_mean_dist);
title('Average response distance across all subjects over time')
%axis([-2,480,0,max_smooth])
xlabel('Trial')
ylabel('Distance from target (mm)')

%Plotting the cluster tightness with sem bars 
figure(1002);
shadedErrorBar(chunked_trials,mean_cluster,sem_mean_cluster);
title('Average cluster tightness across all subjects over time')
xlabel('Trial')
ylabel('Average euclidean distance between points (mm)')

%Plotting the distance of median response to target 
figure(1003);
shadedErrorBar(chunked_trials,mean_med_dist,sem_mean_med_dist);
title('Average distance from median response to target across subjects')
xlabel('Trial')
ylabel('Distance from target(mm)')