function [] = plot_formant_cues(rbt_array)

goal1 = [1089 702];
goal2 = [1763 551];
goal3 = [2254 294];
goal4 = [1030 450];
goal5 = [1917 400];

%Plot the different goals and cues, color-coordinated, all on one plot
figure
hold on

%Goal cue 1
plot(goal1(1),goal1(2),'*k')
plot(rbt_array{1,1}(1,:),rbt_array{1,1}(2,:),'.b')

%Goal cue 2
plot(goal2(1),goal2(2),'*g')
plot(rbt_array{1,2}(1,:),rbt_array{1,2}(2,:),'.c')
    
%Goal cue 3
if exist('respx_cue3','var')
    plot(goal3(1),goal3(2),'or','MarkerFaceColor','r')
    plot(respx_cue3,respy_cue3,'.m')
    xlabel('F2')
    ylabel('F1')
    axis([800,2500,100,900])    
end
    
%Goal cue 4
if exist('resp_cue4','var')
    plot(goal4(1),goal4(2),'ok')
    plot(respx_cue4,respy_cue4,'.g')
    xlabel('F2')
    ylabel('F1')
    axis([800,2500,100,900])
end

%Goal cue 5
if exist('resp_cue5','var')
    plot(goal5(1),goal5(1),'ok')
    plot(respx_cue5,respy_cue5,'.m')
end

xlabel('F2')
ylabel('F1')
axis([800,2500,100,900])
set(gca,'xaxislocation','bottom','yaxislocation','right','xdir','reverse')
    
hold off