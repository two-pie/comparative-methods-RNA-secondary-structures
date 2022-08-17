import java.io.IOException;
import java.nio.file.Files;
import java.util.stream.Collectors;

/**
 * MainComparator class interacting with the user through command line options.
 *
 * @author Luca Tesei
 *
 */
public class MainComparator {

    public static void main(String[] args) throws IOException {
        ClusterGroup.createCsvCores(Files.walk(FilePaths.Archaea).filter(Files::isRegularFile).collect(Collectors.toList()), FilePaths.Archaea_output);
        ClusterGroup.createCsvCores(Files.walk(FilePaths.Bacteria).filter(Files::isRegularFile).collect(Collectors.toList()), FilePaths.Bacteria_output);
        ClusterGroup.createCsvCores(Files.walk(FilePaths.Eukaryota).filter(Files::isRegularFile).collect(Collectors.toList()), FilePaths.Eukaryota_output);
    }
}
