function [rbt_array] = split_by_target(respx,respy,goalx)
%Splits the given responses into arrays based on the target they are a
%response to (Still in units of formants)

n = 0;
m = 0;
p = 0;
q = 0;
r = 0;

for i = 1:length(goalx)
    if goalx(i) == 1089
        n = n+1;
        respx_cue1(n) = respx(i);
        respy_cue1(n) = respy(i);
    elseif goalx(i) == 1763 
        m = m+1;
        respx_cue2(m) = respx(i);
        respy_cue2(m) = respy(i);
    elseif goalx(i) == 2254
        p = p+1;
        respx_cue3(p) = respx(i);
        respy_cue3(p) = respy(i);
    elseif goalx(i) == 1917
        q = q+1;
        respx_cue4(q) = respx(i);
        respy_cue4(q) = respy(i);
    elseif goalx(i) == 1030
        r = r+1;
        respx_cue5(r) = respx(i);
        respy_cue5(r) = respy(i);
    end
end


if ~exist('respx_cue1','var') && ~exist('respx_cue2','var')
    fprintf('Missing 1 and 2.\n')
    respx_cue1(1) = 0;
    respy_cue1(1) = 0;
    respx_cue2(1) = 0;
    respy_cue2(1) = 0;
elseif ~exist('respx_cue1','var') && ~exist('respx_cue3','var')
    fprintf('Missing 1 and 3.\n')
    respx_cue1(1) = 0;
    respy_cue1(1) = 0;
    respx_cue3(1) = 0;
    respy_cue3(1) = 0;
elseif ~exist('respx_cue2','var') && ~exist('respx_cue3','var')
    fprintf('Missing 2 and 3.\n')
    respx_cue2(1) = 0;
    respy_cue2(1) = 0;
    respx_cue3(1) = 0;
    respy_cue3(1) = 0;
elseif ~exist('respx_cue1','var')
    fprintf('Missing 1.\n')
    respx_cue1(1) = 0;
    respy_cue1(1) = 0;
elseif ~exist('respx_cue2','var')
    fprintf('Missing 2.\n')
    respx_cue2(1) = 0;
    respy_cue2(1) = 0;
elseif ~exist('respx_cue3','var')
    fprintf('Missing 3.\n')
    respx_cue3(1) = 0;
    respy_cue3(1) = 0;
end

if exist('respx_cue4','var') && exist('respx_cue5','var')
    %fprintf('There were goals 4 and 5\n')
    rbt_array = {[respx_cue1; respy_cue1], [respx_cue2; respy_cue2], [respx_cue3; respy_cue3], [respx_cue4; respy_cue4], [respx_cue5; respy_cue5]};
else
    rbt_array = {[respx_cue1; respy_cue1], [respx_cue2; respy_cue2], [respx_cue3; respy_cue3]};
end
