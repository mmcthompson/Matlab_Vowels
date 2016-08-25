function chunked_array = chunk_data(chunk, inputdata)
%Chunking input according to the chunk size
input_length = length(inputdata);
chunk_count = chunk:chunk:input_length;
k = 1;
chunked_array = zeros(1,length(chunk_count));

for n = 1:length(chunk_count)
    chunked_array(n) = mean(inputdata(k:chunk_count(n)));
    k = k + chunk;
end