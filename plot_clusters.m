function [] = plot_clusters(respx, respy)

goal1 = [1089 702];
goal2 = [1763 551];
goal3 = [2254 294];
%goal4 = [1030 450];
%goal5 = [1917 400];

dat_to_cluster = [respx, respy];
clusterdesignation = kmeans(dat_to_cluster,3);

%Plot the different goals and cues, color-coordinated, all on one plot
figure
hold on

for i = 1:length(clusterdesignation)
    %respx(i)
    
    if clusterdesignation(i) == 2
        %Goal cue 1
        plot(respx(i),respy(i),'.b')

    elseif clusterdesignation(i) == 1
        %Goal cue 2
        plot(respx(i),respy(i),'.c')
        
    elseif clusterdesignation(i) == 3    
        %Goal cue 3
        plot(respx(i),respy(i),'.m')
        
    end
end

%Goal targets
plot(goal1(1),goal1(2),'*k')
plot(goal2(1),goal2(2),'*g')
plot(goal3(1),goal3(2),'*r')


xlabel('F2')
ylabel('F1')
axis([800,2500,100,900])
set(gca,'xaxislocation','bottom','yaxislocation','right','xdir','reverse')
hold off