package it.unicam.cs.bdslab.aspralign;
import java.nio.file.Path;
import java.nio.file.Paths;

public interface FilePaths {

    Path root = Paths.get(System.getProperty("user.dir"));
    Path Archaea  = Paths.get( root.toString(),"Molecules-pseudoknotfree", "db-nH", "Archaea", "5S");
    Path Bacteria = Paths.get( root.toString(),"Molecules-pseudoknotfree", "db-nH", "Bacteria", "5S");
    Path Eukaryota = Paths.get( root.toString(),"Molecules-pseudoknotfree", "db-nH", "Eukaryota", "5S");
    Path Archaea_output = Paths.get( root.toString(),"Molecules-pseudoknotfree", "db-nH", "Archaea", "5S", "Archaea_cores.csv");
    Path Bacteria_output = Paths.get( root.toString(),"Molecules-pseudoknotfree", "db-nH", "Bacteria", "5S", "Bacteria_cores.csv");
    Path Eukaryota_output = Paths.get( root.toString(),"Molecules-pseudoknotfree", "db-nH", "Eukaryota", "5S", "Eukaryota_cores.csv");
}
