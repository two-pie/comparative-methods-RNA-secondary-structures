
clc;
clear all;
fid = fopen('benchmark-processes.txt','r');
if fid == -1
  error('Author:Function:OpenFile', 'Cannot open file: %s', 'benchmark-processes.txt');
end
folder = fgetl(fid);
while ischar(folder)
    disp(folder)
    output = fgetl(fid);
    disp(output)
    % Open and Write first line in output file
    outputFileID = fopen(output,'w');
    fprintf(outputFileID,'%s, %s, %s\n', "Molecule", "ValueS", "ValueE");
    % process all files in the folder
    projectdir = folder;
    dinfo = dir(projectdir + "/*.txt");
    dinfo([dinfo.isdir]) = []; %get rid of all directories including . and ..
    nfiles = length(dinfo);
    for j = 1 : nfiles
        filename = fullfile(projectdir, dinfo(j).name);
            %f1 = fopen(filename, 'r');
            disp(filename);
            % compute quella cosa per il file 
            AdjM = readmatrix(filename); % input adjacency matrix
            %disp(AdjM);
            DegM = diag(sum(AdjM));
            LapM = DegM - AdjM;
            [V,D] = eig(LapM);
            eigenvalues = diag(D);
            [~,idx] = sort(eigenvalues);
            column = 0;
            for c = 1 : length(idx)
                if idx(c) == 2
                    column = c;
                end
            end
            FV = V(:,column); % get Fiedler vector
            FV = sort(FV); % sort
            N = size(FV, 1); % vertex number
            FV = FV*(N-1)/(FV(end)-FV(1)); % scale
            p = polyfit([1:N]', FV, 1); % least squares linear regression
            s = p(1);
            e = sum((polyval(p,[1:N]')-FV).^2);
            %disp(s);
            %disp(e);
            disp(filename);            
            filename2 = regexprep(filename,"benchmark-adjmatrices|/5S/|/16S/|/23S/|/|Archaea|Bacteria|Eukaryota|_nH.ct_AdjMat.txt", "");
            fprintf(outputFileID,'%s, %f, %f\n', filename2, s, e);
            %fclose(f1);
    end
    fclose(outputFileID);
    folder = fgetl(fid);
end
fclose(fid);






