%In which Megan attempts to write a basic mouse hook in Matlab
%The coordinate parameters will then be immediately passed on to
%formant_synthesis_playback to produce the vowel based on the coordinates

function formant_mouse_hook()

%Simplest solution, attempt to use ginput for the mouse hook
%[x y] = ginput(4)
%ginput has multiple problems, primarily that it does not cover the entire
%screen, meaning that the edges will get missed

%Attempting to make a full-screened figure
figure('units','normalized','outerposition',[0 0 1 1])
%Still doesn't take full screen, leaves toolbars open for clicking on



%%Attempting mouse hook callback from http://www.mathworks.com/matlabcentral/answers/97563-how-do-i-continuously-read-the-mouse-position-as-the-mouse-is-moving-without-a-click-event
%Not a straight-up variable return, doesn't work outside of window either
%set(gcf, 'WindowButtonMotionFcn', @mouseMove);

%function mouseMove (object, eventdata)

%C = get(gca, 'CurrentPoint');
%title(gca, ['(X,Y) = (', num2str(C(1,1)), ', ',num2str(C(1,2)), ')']);
