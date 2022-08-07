import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.List;
import java.util.stream.Collectors;

/**
 * MainComparator class interacting with the user through command line
 * options.
 *
 * @author Luca Tesei
 */
public class MainComparator {


    public static void main(String[] args) throws IOException {
        createCsv(Files.walk(FilePaths.ARCHAEA).filter(Files::isRegularFile).collect(Collectors.toList()), FilePaths.ARCHAEA_OUTPUT);
        createCsv(Files.walk(FilePaths.BACTERIA).filter(Files::isRegularFile).collect(Collectors.toList()), FilePaths.BACTERIA_OUTPUT);
        createCsv(Files.walk(FilePaths.EUKARYOTA).filter(Files::isRegularFile).collect(Collectors.toList()), FilePaths.EUKARYOTA_OUTPUT);
    }

    private static void createCsv(List<Path> filePaths, Path file_output) throws IOException {
        Files.write(file_output, "MOLECULE,CORE1,CORE2\n".getBytes());
        for (var f : filePaths) {
            var rnaSecondaryStructure = RNASecondaryStructureFileReader.readStructure(f.toString(), false);
            var fileName = f.getFileName().toString();
            String csvRow = fileName.substring(0,fileName.lastIndexOf('.')) +
                    "," +
                    new RNACore1(rnaSecondaryStructure).getBrackets() +
                    "," +
                    new RNACore2(rnaSecondaryStructure).getBrackets() +
                    "\n";
            Files.write(file_output, csvRow.getBytes(), StandardOpenOption.APPEND);
        }
    }

}
