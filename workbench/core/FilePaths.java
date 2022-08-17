import java.nio.file.Path;
import java.nio.file.Paths;

public interface FilePaths {

    Path root = Paths.get(System.getProperty("user.dir"));
    Path Archaea = Paths.get(root.toString(), "workbench", "Molecules-pseudoknotfree", "db", "Archaea", "5S");
    Path Bacteria = Paths.get(root.toString(), "workbench", "Molecules-pseudoknotfree", "db", "Bacteria", "5S");
    Path Eukaryota = Paths.get(root.toString(), "workbench", "Molecules-pseudoknotfree", "db", "Eukaryota", "5S");
    Path Archaea_output = Paths.get(root.toString(), "workbench", "workbench-results", "Archaea", "Archaea");
    Path Bacteria_output = Paths.get(root.toString(), "workbench", "workbench-results", "Bacteria", "Bacteria");
    Path Eukaryota_output = Paths.get(root.toString(), "workbench", "workbench-results", "Eukaryota", "Eukaryota");
}
