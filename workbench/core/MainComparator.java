/**
 * ASPRAlign - Algebraic Structural Pseudoknot RNA Alignment
 * <p>
 * Copyright (C) 2020 Luca Tesei, Michela Quadrini, Emanuela Merelli -
 * BioShape and Data Science Lab at the University of Camerino, Italy -
 * http://www.emanuelamerelli.eu/bigdata/
 * <p>
 * This file is part of ASPRAlign.
 * <p>
 * ASPRAlign is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * any later version.
 * <p>
 * ASPRAlign is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * <p>
 * You should have received a copy of the GNU General Public License
 * along with ASPRAlign. If not, see <http://www.gnu.org/licenses/>.
 */
package it.unicam.cs.bdslab.aspralign;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * MainComparator class interacting with the user through command line
 * options.
 *
 * @author Luca Tesei
 */
public class MainComparator {



    public static void main(String[] args) throws IOException {
        var filePaths = Files.walk(FilePaths.Archaea).filter(Files::isRegularFile).collect(Collectors.toList());
        //create a csv file with the header MOLECULE CORE1 CORE2
        var file =Files.createFile(Paths.get(args[1], "cores.csv"));
        Files.write(file, "MOLECULE,CORE1,CORE2\n".getBytes());

    }
}
