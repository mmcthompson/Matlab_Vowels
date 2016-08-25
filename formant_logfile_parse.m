function [testgoalx, testgoaly, testrespx, testrespy, traingoalx, traingoaly, trainrespx, trainrespy] = formant_logfile_parse(filename)

fid = fopen(filename);
i=1;
j=1;
te = 1;
tr = 1;
linenum=0;
lastgoalline=0;
goalx = zeros(529,1);
goaly = zeros(529,1);
respx = zeros(529,1);
respy = zeros(529,1);
testgoalx = zeros(49,1);
testgoaly = zeros(49,1);
testrespx = zeros(49,1);
testrespy = zeros(49,1);
traingoalx = zeros(480,1);
traingoaly = zeros(480,1);
trainrespx = zeros(480,1);
trainrespy = zeros(480,1);

while ~feof(fid) 
    %Get the next line of the text file
    tline = fgetl(fid);
    linenum = linenum + 1;
    string_index_goal = strfind(tline,'goal');
    string_index_response = strfind(tline,'-');
    string_index_test = strfind(tline,'Test');
    string_index_train = strfind(tline,'Training');
    if (string_index_goal) %If this was a goal cue statement
        string_index_x = strfind(tline,'F2:');
        string_index_y = strfind(tline,' F1:');
        char_x = tline(string_index_x+3:string_index_y);
        char_y = tline(string_index_y+4:string_index_y+6);
        goalx(i) = str2double(char_x);
        goaly(i) = str2double(char_y);
        lastgoalline = linenum;
        i = i+1;
    end
    if (string_index_response)
        if linenum == lastgoalline + 1
            %If this was a response statement immediately following a goal
            %statement- helps to filter out multiple responses
            string_index_F2 = strfind(tline,'F2:');
            string_index_F1 = strfind(tline,' F1:');
            char_x = tline(string_index_F2+3:string_index_F1);
            char_y = tline(string_index_F1+4:length(tline));
            respx(j) = str2double(char_x);
            respy(j) = str2double(char_y);
            j = j+1;
            if (string_index_test)
                %This was response was a silent test response
                testrespx(te) = respx(j-1);
                testrespy(te) = respy(j-1);
                %The last goal was a silent test goal
                testgoalx(te) = goalx(i-1);
                testgoaly(te) = goaly(i-1);
                te = te+1;
            elseif (string_index_train)
                %This was a train response with auditory feedback
                trainrespx(tr) = respx(j-1);
                trainrespy(tr) = respy(j-1);
                %the last goal was a train goal
                traingoalx(tr) = goalx(i-1);
                traingoaly(tr) = goaly(i-1);
                tr = tr+1;
            end
        end
    end
end

fclose(fid);

