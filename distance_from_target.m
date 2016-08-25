function [distance_array_mm] = distance_from_target(chunk, goalx, goaly, respx, respy)

%Creating a continuous array of distances

%Convert from screen units to mm 
[goalx_mm, goaly_mm] = formant2mm(goalx, goaly);
[respx_mm, respy_mm] = formant2mm(respx, respy);

%Distance between goal and response
difx = goalx_mm - respx_mm;
dify = goaly_mm - respy_mm;
dist =  sqrt(difx.^2 + dify.^2);

% %For good measure, scatterplot the distance
% figure
% trials = 1:length(goalx);
% hold on
% difx_formant = goalx - respx;
% dify_formant = goaly - respy;
% plot(trials,difx_formant,'.')
% plot(trials,dify_formant,'.')
% title('Response distance (in formants) from the target')
% xlabel('Trial')
% ylabel('Distance from target')
% legend('F2','F1')

%Chunk it according to the chunk input
distance_array_mm = chunk_data(chunk,dist);