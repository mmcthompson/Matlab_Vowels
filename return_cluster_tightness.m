function [cluster_array] = return_cluster_tightness(chunk, respx, respy, goalx)
%Calculate cluster tightness based on chunk size

%Generally, will calculate cluster size based on the n most recent
%responses, where n=chunk. However, in the case of n=1, this obviously will
%not work, so cluster tightness will be based on all previous responses.
%This in nonideal, as later metrics are schewed because they contain more
%data points than earlier metrics.

%Creating an array of cluster tightness with one point for each chunk
input_length = length(respx);
chunk_count = chunk:chunk:input_length;
cluster_array = zeros(1,length(chunk_count));
k = 1;

if chunk >= 10
    %Don't bother chunking less than ten because can't even be assured that
    %there is one of each type of cue in the batch
    for n = 1:length(chunk_count)
        chunk_rbt_array = split_by_target(respx(k:chunk_count(n)), respy(k:chunk_count(n)), goalx(k:chunk_count(n)));
        [chunk_rbt_array_mm{1,1}(1,:), chunk_rbt_array_mm{1,1}(2,:)] = formant2mm(chunk_rbt_array{1,1}(1,:),chunk_rbt_array{1,1}(2,:));
        [chunk_rbt_array_mm{1,2}(1,:), chunk_rbt_array_mm{1,2}(2,:)] = formant2mm(chunk_rbt_array{1,2}(1,:),chunk_rbt_array{1,2}(2,:));
        [chunk_rbt_array_mm{1,3}(1,:), chunk_rbt_array_mm{1,3}(2,:)] = formant2mm(chunk_rbt_array{1,3}(1,:),chunk_rbt_array{1,3}(2,:));
    
        %Setting up the sorted chunk into the right format to calculate the
        %Euclidean distances between all other responses to the same target
        cue1 = [chunk_rbt_array_mm{1,1}(1,:)', chunk_rbt_array_mm{1,1}(2,:)'];
        cue2 = [chunk_rbt_array_mm{1,2}(1,:)', chunk_rbt_array_mm{1,2}(2,:)'];
        cue3 = [chunk_rbt_array_mm{1,3}(1,:)', chunk_rbt_array_mm{1,3}(2,:)'];
    
        %The point in the cluster array that corresponds to the chunk we're looking at now
        %As such, there should be one point for every chunk, the length of the
        %array is the same as the number of chunks that will fit in a given
        %dataset
        cluster_array(n) = mean([pdist(cue1), pdist(cue2), pdist(cue3)]);
    
        %Remember to clear the sorted mm array at the end or else you'll
        %get a size mismatch error when you try to write a new variable to
        %it in the next itteration        
        chunk_rbt_array_mm = [];

        %Make sure that the start of the window keeps incrementing
        k = k + chunk;
    
     end
else
    %Special case, chunk = 1
    %Must calculate continuous clustering
    %Start at ten because otherwise the sort causes all kinds of problems
    for i=10:length(respx)
        %Sort all of the points that have come thus far into groups by cue
        cont_rbt_array = split_by_target(respx(1:i), respy(1:i), goalx(1:i));

        %Translate from formant space to mm space
        [cont_rbt_array_mm{1,1}(1,:), cont_rbt_array_mm{1,1}(2,:)] = formant2mm(cont_rbt_array{1,1}(1,:), cont_rbt_array{1,1}(2,:));
        [cont_rbt_array_mm{1,2}(1,:), cont_rbt_array_mm{1,2}(2,:)] = formant2mm(cont_rbt_array{1,2}(1,:), cont_rbt_array{1,2}(2,:));
        [cont_rbt_array_mm{1,3}(1,:), cont_rbt_array_mm{1,3}(2,:)] = formant2mm(cont_rbt_array{1,3}(1,:), cont_rbt_array{1,3}(2,:));
        
        %Setting up the sorted chunk into the right format to calculate the
        %Euclidean distances between all other responses to the same target
        cue1 = [cont_rbt_array_mm{1,1}(1,:)', cont_rbt_array_mm{1,1}(2,:)'];
        cue2 = [cont_rbt_array_mm{1,2}(1,:)', cont_rbt_array_mm{1,2}(2,:)'];
        cue3 = [cont_rbt_array_mm{1,3}(1,:)', cont_rbt_array_mm{1,3}(2,:)'];
    
        %The point in the cluster array that corresponds to the chunk we're looking at now
        %As such, there should be one point for every chunk, the length of the
        %array is the same as the number of chunks that will fit in a given
        %dataset
        cluster_array(i) = mean([pdist(cue1), pdist(cue2), pdist(cue3)]);
        
        %Remember to clear the sorted mm array at the end or else you'll
        %get a size mismatch error when you try to write a new variable to
        %it in the next itteration
        cont_rbt_array_mm = [];
    end
end