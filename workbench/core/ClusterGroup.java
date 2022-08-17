import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.List;

/**
 * Removes the "taxon" column from a csv file and substitute it with calculated core (1 or 2).
 */
public class ClusterGroup {

    private ClusterGroup() {
    }

    /**
     * Creates two files called <code>file_output</code>_core1.csv and <code>file_output</code>_core2.csv
     * that contain for each {@link Path} in <code>filePaths</code> respectively 'Id;Organism;Core1' and 'Id;Organism;Core1' values.
     *
     * @param filePaths   the list of all files which to create thw two csv files.
     * @param file_output the output folder where to create the all csv cores files.
     */
    public static void createCsvCores(List<Path> filePaths, Path file_output) throws IOException {
        Path core1 = Files.write(Paths.get(file_output + "_core1.csv"), "Id;Organism;Core1\n".getBytes());
        Path core2 = Files.write(Paths.get(file_output + "_core2.csv"), "Id;Organism;Core2\n".getBytes());
        for (var f : filePaths) {
            var rnaSecondaryStructure = RNASecondaryStructureFileReader.readStructure(f.toString(), false);
            var fileName = f.getFileName().toString().substring(0, f.getFileName().toString().lastIndexOf('.'));
            String csvRowCore1 = fileName + ";" + getOrganism(f) + ";" + new RNACore1(rnaSecondaryStructure).getBrackets() + "\n";
            String csvRowCore2 = fileName + ";" + getOrganism(f) + ";" + new RNACore2(rnaSecondaryStructure).getBrackets() + "\n";
            Files.write(core1, csvRowCore1.getBytes(), StandardOpenOption.APPEND);
            Files.write(core2, csvRowCore2.getBytes(), StandardOpenOption.APPEND);
        }
    }

    private static String getOrganism(Path path) throws IOException {
        List<String> lines = Files.readAllLines(path);
        return lines.stream().filter(l -> l.contains("Organism")).findFirst().get().split(":")[1].trim();
    }
}