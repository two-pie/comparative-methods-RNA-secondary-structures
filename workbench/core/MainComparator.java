
package it.unicam.cs.bdslab.aspralign;

import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.CommandLineParser;
import org.apache.commons.cli.DefaultParser;
import org.apache.commons.cli.HelpFormatter;
import org.apache.commons.cli.Option;
import org.apache.commons.cli.Options;
import org.apache.commons.cli.ParseException;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

/**
 * MainComparator class interacting with the user through command line options.
 *
 * @author Luca Tesei
 *
 */
public class MainComparator {

    public static void main(String[] args) throws IOException {
        // create Options object for Command Line Definition
        var options = new Options();
        defineCommandLineOptions(options);

        // Parse command line
        HelpFormatter formatter = new HelpFormatter();
        CommandLineParser commandLineParser = new DefaultParser();
        CommandLine cmd = null;

        try {
            cmd = commandLineParser.parse(options, args);
        } catch (ParseException e) {
            // oops, something went wrong
            System.err.println("ERROR: Command Line parsing failed.  Reason: "
                    + e.getMessage() + "\n");
            formatter.printHelp("java -jar cores_calculator.jar",
                    "Cores Calculator", options,
                    "accepted formats for molecules: db, ct, bpseq and aas",
                    true);
            System.exit(1);
        }
        // Manage Option h
        if (cmd.hasOption("h")) {
            formatter.printHelp("java -jar cores_calculator.jar",
                    "Cores Calculator", options,"accepted formats for molecules: db, ct, bpseq and aas",
                    true);
            return;
        }

        // Manage Option core1
        if (cmd.hasOption("core1")) {
            var input = cmd.getOptionValue("core1");
            var rnaSecondaryStructure = RNASecondaryStructureFileReader.readStructure(input, false);
            var core1 = new RNACore1(rnaSecondaryStructure);
            if (cmd.hasOption('o')){
                var fileName = cmd.getOptionValue('o');
                Files.write(Paths.get(fileName),core1.getBrackets().getBytes());
            }
            else {
                System.out.println(core1.getBrackets());
            }
        }
        // Manage Option core2
        if (cmd.hasOption("core2")) {
            var input = cmd.getOptionValue("core2");
            var rnaSecondaryStructure = RNASecondaryStructureFileReader.readStructure(input, false);
            var core2 = new RNACore2(rnaSecondaryStructure);
            if (cmd.hasOption('o')){
                var fileName = cmd.getOptionValue('o');
                Files.write(Paths.get(fileName),core2.getBrackets().getBytes());
            }
            else {
                System.out.println(core2.getBrackets());
            }
        }
    }

    private static void defineCommandLineOptions(Options options) {
        var outputOption = Option.builder("o").desc(
                        "Output result on the given file instead of standard output")
                .longOpt("out").hasArg().argName("output_file").build();
        options.addOption(outputOption);
        var helpOption = Option.builder("h").desc("Show usage information")
                .longOpt("help").build();
        options.addOption(helpOption);

        var core1Option = Option.builder("core1").desc(
                        "Calculate the core1 of the given molecule")
              .hasArg().argName("molecule file").build();
        options.addOption(core1Option);

        var core2Option = Option.builder("core2").desc(
                        "Calculate the core2 of the given molecule").hasArg().argName("molecule file").build();
        options.addOption(core2Option);
    }

}
