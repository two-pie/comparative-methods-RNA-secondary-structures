package it.unicam.cs.hierro.corecalculator;

import org.apache.commons.cli.*;

import java.io.IOException;
import java.nio.file.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // create Options object for Command Line Definition
        var options = new Options();
        defineCommandLineOptions(options);

        // Parse command line
        HelpFormatter formatter = new HelpFormatter();
        CommandLineParser commandLineParser = new DefaultParser();
        CommandLine cmd = null;

        var name = "CoresCalculator";
        var footer = "Input molecules must be in extended dot-bracket notation and all parameters must be folders";
        if (args.length!=4 && args.length!=1) {
            System.err.println("Wrong number of parameters!");
            formatter.printHelp(name, name, options, footer, true);
            System.exit(1);
        }
        try {
            cmd = commandLineParser.parse(options, args);
        } catch (ParseException e) {
            // oops, something went wrong
            System.err.println("ERROR: Command Line parsing failed.  Reason: "
                    + e.getMessage() + "\n");
            formatter.printHelp(name, name, options, footer, true);
            System.exit(1);
        }
        // Manage Option h
        if (cmd.hasOption("h")) {
            formatter.printHelp(name, name, options, footer, true);
            return;
        }

        //manage Option csv and file
        Path inputFolder;
        Path corePlusOutputFolder;
        Path coreOutputFolder;
        if (cmd.hasOption("csv")) {
            inputFolder = Paths.get(cmd.getOptionValues("csv")[0]);
            corePlusOutputFolder = Paths.get(cmd.getOptionValues("csv")[1]);
            coreOutputFolder = Paths.get(cmd.getOptionValues("csv")[2]);
        } else {
            inputFolder = Paths.get(cmd.getOptionValues("file")[0]);
            corePlusOutputFolder = Paths.get(cmd.getOptionValues("file")[1]);
            coreOutputFolder = Paths.get(cmd.getOptionValues("file")[2]);
        }
        if (!Files.isDirectory(inputFolder)
                || !Files.isDirectory(corePlusOutputFolder)
                || !Files.isDirectory(coreOutputFolder)) {
            System.err.print("All parameters must be folders!");
        }
        // retrieve all files in the input folder
        var files = Files.walk(inputFolder).filter(Files::isRegularFile).toList();
        // create csv
        if (cmd.hasOption("csv")) {
            Files.write(corePlusOutputFolder.resolve("corePlus.csv"), "".getBytes());
            Files.write(coreOutputFolder.resolve("core.csv"), "".getBytes());
        }
        // iterate over files
        for (var f : files) {
            // read all lines and remove header
            var lines = Files.readAllLines(f).stream().filter(l -> !l.startsWith("#")).toList();
            if (lines.size() != 2)
                System.err.println("Only 2 no header lines are needed!");
            // write corePlus and core
            var corePlus = new RNACorePlus(lines.get(1));
            var core = new RNACore(lines.get(1));
            // remove extension
            var fileNameWithExtension = f.getFileName().toString();
            var fileName = fileNameWithExtension.substring(0, fileNameWithExtension.lastIndexOf('.'));
            // write the cores
            if (cmd.hasOption("csv")) {
                Files.write(corePlusOutputFolder.resolve("corePlus.csv"),
                        (fileName + "," + corePlus.getCorePlus() + "\n").getBytes(),
                        StandardOpenOption.APPEND);
                Files.write(coreOutputFolder.resolve("core.csv"),
                        (fileName + "," + core.getCore() + "\n").getBytes(),
                        StandardOpenOption.APPEND);
            } else {
                Files.write(corePlusOutputFolder.resolve(fileName + ".txt"), corePlus.getCorePlus().getBytes());
                Files.write(coreOutputFolder.resolve(fileName + ".txt"), core.getCore().getBytes());
            }
        }
    }


    private static void defineCommandLineOptions(Options options) {
       var helpOption = Option
                .builder("h")
                .desc("Show usage information")
                .longOpt("help")
                .build();
        options.addOption(helpOption);

        var csvOption = Option
                .builder("csv")
                .desc("create a csv as result")
                .hasArg()
                .numberOfArgs(3)
                .argName("input output_core_plus output_core")
                .build();
        options.addOption(csvOption);


        var fileOption = Option
                .builder("file")
                .desc("create one file for each core as result")
                .hasArg()
                .numberOfArgs(3)
                .argName("input output_core_plus output_core")
                .build();
        options.addOption(fileOption);
    }


}
