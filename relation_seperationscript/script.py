import re

lines = [
    "6.2.31;	Schwiegervater von oP J. Deer ( 6. 1. 74 )",
"0.0.70;	Schwiegervater von Professor Samuel Anton Wilhelmi ( Nr. 83 )",
"3.1.51;	Vater von aoP Kurt Amonn ( 3. 2. 59 )",
"7.1.39;	Sohn von oP Armin Baltzer ( 7. 1. 18 )	",
"7.1.18;	Vater von oP Friedrich Baltzer ( 7. 1. 39 )",
"6.4.59;	Gattin von HonP Moritz Tramer ( 4. 3. 10 )",
"0.0.8;	Vater von Professor Gabriel Blauner ( Nr. 16 )",
"0.0.16;	Sohn von Professor Adrian Blauner ( Nr. 8 )",
"1.2.4;	Schwiegervater: oP Gottlieb Studer ( 1. 1. 15 )",
"3.1.42;	Gattin: oP Irene Blumenstein-Steiner ( 3. 1. 73 )",
"3.1.73;	Gattin von oP Ernst Blumenstein ( 3. 1. 42 )	",
"7.2.6;	Sohn von oP Karl Brunner ( 7. 1. 5 )	",
"7.1.5;	Vater von aoP Karl Brunner ( 7. 2. 6 )	",
"6.4.50;	Schwiegersohn von aoP A. F. Flückiger ( 7. 2. 9 )",
"3.1.44;	Sohn von PD Gottlieb Burckhardt ( 4. 4. 33 )	",
"4.1.50;	Vater von HonP Sandro Bürgi ( 4. 3. 16 ) und PD W. F. Bürgi ( 3. 4. 34 ), Bruder von aoP Moritz Bürgi ( 5. 2. 3 )",
"5.2.3;	Bruder von oP Emil Bürgi ( 4. 1. 50 )	",
"4.3.16;	Sohn von oP Emil Bürgi ( 4. 1. 50 ), Bruder von PD Wolfhart Friedrich Bürgi ( 3. 4. 34 )",
"3.4.34;	Sohn von oP Emil Bürgi ( 4. 1. 50 ), Bruder von HonP Sandro Bürgi ( 4. 3. 16 )	",
"3.4.29;	Vater von aoP Wilhelm Buser ( 7. 2. 28 )	",
"7.2.28;	Sohn von PD Jakob Buser ( 3. 4. 29 )	",
"4.1.95;	Bruder von aoP Paul Cottier ( 4. 2. 55 )",
"4.2.55;	Bruder von oP Hans Cottier ( 4. 1. 95 )	",
"1.1.34;	Neffe von oP Johann Friedrich de Quervain ( 4. 1. 55 )",
"4.1.55;	Onkel von oP A. De Quervain ( 1. 1. 34 )	",
"6.1.74;	Schwiegersohn von aoP Andreas Alföldi ( 6. 2. 31 )",
"4.1.11;	Vater von oP Rudolf Demme ( 4. 1. 41 ) und PD Karl Hermann Demme ( 4. 4. 17 )",
"4.4.17;	Sohn von oP Hermann Askan Demme ( 4. 1. 11 ), Bruder von oP Rudolf Demme ( 4. 1. 41 )",
"4.1.41;	Sohn von oP Hermann Askan Demme ( 4. 1. 11 ), Bruder von PD Karl Hermann Demme ( 4. 4. 17 )",
"4.3.1;	Schwiegersohn von oP Gustav König ( 3. 1. 21 ), Vater von PD Fritz L. Dumont ( 4. 4. 78 )	",
"4.4.78;	Sohn von Titularprof. Fritz Ludwig Dumont ( 4. 3. 1 )	",
"0.0.27;	Schwiegervater von Professor Johannes Hasler ( Nr. 22 )	",
"4.1.1;	Bruder von oP Carl Friedrich Emmert ( 5. 1. 1 A )	",
"5.1.1;	Bruder von oP A. G. F. Emmert ( 4. 1. 1 A ), Vater von oP F. K. Emmert ( 4. 1. 20 ) und von PD W. Emmert ( 4. 4. 8 )",
"4.3.2;	Sohn von oP Friedrich Karl Emmert ( 4. 1. 20 )	",
"4.1.20;	Sohn von oP ( Akademie ) Ludwig Carl Friedrich Emmert ( 5. 1. 1 A ), Bruder von PD Wilhelm Emmert ( 4. 4. 8 ), Vater von HonP Emil Emmert ( 4. 3. 2 )",
"4.4.8;	Sohn von oP ( Akademie ) Ludwig Carl Friedrich Emmert ( 5. 1. 1 ), Bruder von oP Karl Emmert ( 4. 1. 20 )	",
"4.4.28;	Vater von oP H. Adolf Fehr ( 3. 1. 49 )	",
"3.1.49;	Sohn von PD Adolf Fehr ( 4. 4. 28 )	",
"7.1.23;	Sohn von oP Ludwig Fischer ( 7. 1. 12 ), Vater von PD Kurt von Fischer ( 6. 4. 69 )",
"7.1.12;	Vater von oP Eduard Fischer ( 7. 1. 23 )	",
"2.1.11;	Vater von HonP Peter Gilg ( 6. 3. 25 )	",
"6.3.25;	Sohn von oP Arnold Gilg ( 2. 1. 11 )	",
"3.1.40;	Vater von PD Rudolf Gmür ( 3. 4. 37 )	",
"3.4.37;	Sohn von oP Max Gmür ( 3. 1. 40 )	",
"7.4.60;	Vater von aoP Hans Beat Hadorn ( 4. 2. 70 )",
"1.1.29;	Vater von oP Walter Hadorn ( 4. 1. 87 )	",
"4.2.70;	Sohn von PD Ernst Hadorn ( 7. 4. 60 )	",
"4.1.87;	Sohn von oP Friedrich Wilhelm Hadorn ( 1. 1. 29 )",
"6.1.21;	Sohn von oP Karl Hagen ( 6. 1. 11 )	",
"6.1.11;	Vater von oP Hermann Hagen ( 6. 1. 21 )",
"0.0.22;	Schwiegersohn von Professor Hermann Dürholz ( Nr. 27 )",
"0.0.28;	Urgrossvater von Professor Samuel Henzi ( Nr. 46 )	",
"0.0.46;	Urenkel von Professor Niklaus Henzi ( Nr. 28 )	",
"4.2.4;	Vater von oP Theodor Hermann ( 4. 1. 21 )	",
"4.1.21;	Sohn von aoP Joh. Jak. Hermann ( 4. 2. 4 )	",
"0.0.63;	Schwiegersohn von Professor David Wyss ( Nr. 45 )",
"0.0.41;	Enkel von Professor Peter Hübner ( Nr. 21 )	",
"0.0.21;	Grossvater von Professor Johann Rudolf Hübner ( Nr. 41 )",
"4.1.6;	Sohn von Professor Johannes Samuel Ith ( Prof. Hohe Schule Nr. 88 )",
"0.0.88;	Vater von oP Johann Rudolf Friedrich Ith ( 4. 1. 006A ), Schwiegersohn von Professor Johann Rudolf Walt-hard ( Nr. 78 )",
"6.3.4;	Sohn von aoP Carl Christian Jahn ( 6. 2. 1 )	",
"6.2.1;	Vater von HonP Albert Jahn ( 6. 3. 4 )	",
"6.1.88;	Gatte von aoP Judith Janoska-Bendl ( 3. 2. 61 )",
"3.2.61;	Gattin von oP G. Jánoska ( 6. 1. 88 )	",
"4.1.22;	Vater von PD Georg Jonquiere ( 4. 4. 42 )",
"4.4.42;	Sohn von oP Daniel Jonquiere ( 4. 1. 22 )	",
"4.4.57;	Sohn von oP Theodor Kocher ( 4. 1. 29 )	",
"0.0.81;	Bruder von Professor Jakob Kocher ( Nr. 73 ) Vater von Professor Johann David Kocher ( Nr. 94 )",
"0.0.73;	Bruder von Professor David Kocher ( Nr. 81 )	",
"0.0.94;	Sohn von Professor David Kocher ( Nr. 81 )	",
"4.1.29;	Vater von PD Albert Kocher ( 4. 4. 57 )	",
"7.4.37;	Vater von aoP Hans König ( 7. 2. 24 )	",
"4.4.82;	Bruder von oP Richard König ( 3. 1. 52 )",
"7.2.24;	Sohn von PD Emil König ( 7. 4. 37 )	",
"3.1.21;	Schwiegervater von Titularprof. Fritz Dumont ( 4. 3. 1 )",
"3.1.52;	Bruder von PD Fritz König ( 4. 4. 82 )	",
"2.1.12;	Vater von oP Urs Küry ( 2. 1. 15 )	",
"2.1.15;	Sohn von oP Adolf Küry ( 2. 1. 12 )	",
"1.1.20;	Bruder von oP Friedrich Ernst Langhans ( 1. 1. 19 )",
"1.1.19;	Bruder von oP Eduard Langhans ( 1. 1. 20 )",
"3.1.56;	Vater von oP Ricarda Liver ( 6. 1. 128 )	",
"6.1.128;	Tochter von oP Peter Liver ( 3. 1. 56 )	",
"4.4.74;	Sohn von oP Philipp Lotmar ( 3. 1. 33 )	",
"3.1.33;	Vater von PD Fritz Lotmar ( 4. 4. 74 )	",
"4.2.22;	Sohn von oP Friedrich Lüscher ( 4. 1. 61 )",
"4.1.61;	Vater von aoP E. Lüscher ( 4. 2. 22 )	",
"3.2.29;	Bruder von oP Hermann Matti ( 4. 1. 70 )",
"4.1.70;	Bruder von aoP Hans Matti ( 3. 2. 29 )	",
"3.2.64;	Bruder von oP Christian Heinrich Maurer ( 1. 1. 39 )",
"1.1.39;	Bruder von aoP Alfred Walter Maurer ( 3. 2. 64 )	",
"5.3.1;	Bruder von PD Walter Morgenthaler ( 4. 4. 89 )	",
"4.4.89;	Bruder von HonP Otto Morgenthaler ( 5. 3. 1 )	",
"4.1.149;	Sohn von oP Max Müller ( 4. 1. 88 )	",
"4.1.88;	Vater von oP Christian Müller ( 4. 1. 149 ) ",
"0.0.11;	Schwiegervater von Professor Valentin Rebmann ( Nr. 14 )",
"1.1.18;	Vater von PD Otfried Nippold ( 3. 4. 22 )	",
"3.4.22;	Sohn von oP Friedrich Nippold ( 1. 1. 18 )	",
"4.2.15;	Schwiegersohn von aoP August Friedrich Flückiger ( 7. 2. 9 )",
"0.0.14;	Schwiegersohn von Professor Wolfgang Müslin ( Nr. 11 )	",
"0.0.90;	Schwiegersohn von Professor Daniel Ludwig Studer ( Nr. 85 )",
"0.0.62;	Sohn von Professor Johann Rudolph Rudolf ( Nr. 48 ), Vater von Professor Samuel Ludwig Rudolf ( Nr. 82 )",
"0.0.48;	Vater von Professor Daniel Rudolf ( Nr. 62 ), Grossvater von Professor Samuel Ludwig Rudolf ( Nr. 82 )	",
"0.0.82;	Enkel von Professor Johann Rudolph Rudolf ( Nr. 48 ), Sohn von Professor Daniel Rudolf ( Nr. 62 )	",
"7.4.93;	Sohn von PD Hans Ryffel ( 6. 4. 72 )	",
"6.4.72;	Vater von PD Gerhart U. Ryffel ( 7. 4. 94 )	",
"0.0.75;	Bruder von Professor Johann Rudolf Salchli ( Nr. 66 )",
"0.0.66;	Bruder von Professor Johann Jakob Salchli ( Nr. 75 )",
"6.1.19;	Sohn von aoP August ( e ) Schaffter ( 1. 2. 1 )",
"1.2.1;	Vater von oP Albert Schaffter ( 6. 1. 19 )",
"7.4.6;	Bruder von aoP M. Schiff ( 4. 2. 8 )",
"4.2.8;	Bruder von PD H. Schiff ( 7. 4. 6 )	",
"4.1.138;	Sohn von aoP Jakob Schindler ( 4. 2. 32 )	",
"4.2.32;	Vater von oP Richard Schindler ( 4. 1. 138 )	",
"6.2.4;	Sohn von oP Samuel Ludwig Schnell ( 3. 1. 2 )	",
"3.1.2;	Vater von aoP Albrecht Eduard Schnell ( 6. 2. 4 ), Schwager von Philipp Albert Stapfer, Prof. der Hohen Schule ( Nr. 91 ) und helvetischer Minister",
"4.4.56;	Gatte von PD Wilhelmine Schwenter-Trachsler ( 4. 4. 60 )",
"4.4.60;	Gattin von PD Jakob Schwenter ( 4. 4. 56 )",
"3.2.3;	Bruder von oP W. Snell ( 3. 1. 6 )	",
"3.1.6;	Bruder von aoP Ludwig Snell ( 3. 2. 3 )	",
"1.1.35;	Bruder von oP Rudolf Georg Stamm ( 6. 1. 81 )	",
"6.1.81;	Bruder von oP Johann Jakob Stamm ( 1. 1. 35 )	",
"0.0.95;	Bruder von Professor Philipp Albert Stapfer ( Nr. 91 ), Neffe von Professor Johannes Stapfer ( Nr. 79 )",
"0.0.79;	Onkel der Professoren Philipp Albert ( Nr. 91 ) und Johann Friedrich Stapfer ( Nr. 95 )	",
"0.0.91;	Bruder von Professor Johann Friedrich Stapfer ( Nr. 95 ), Neffe von Professor Johannes Stapfer ( Nr. 79 )",
"5.1.38;	Sohn von oP Fritz Werner Steck ( 5. 1. 23 )	",
"5.1.23;	Vater von oP Franz Thomas Steck ( 5. 1. 38 )	",
"6.1.65;	Sohn von oP Ludwig Stein ( 6. 1. 31 ), Bruder von aoP Wilhelm Stein ( 6. 2. 26 )",
"6.1.31;	Vater von aoP Wilhelm Stein ( 6. 2. 26 ) und oP Arthur Stein ( 6. 1. 65 )	",
"6.2.26;	Sohn von oP Ludwig Stein ( 6. 1. 31 ), Bruder von oP Arthur Stein ( 6. 1. 65 )	",
"4.2.40;	Sohn von aoP Fritz Steinmann ( 4. 2. 18 ) Vater von PD Matthias Steinmann ( 3. 4. 47 )",
"4.2.18;	Vater von aoP Bernhard Friedrich Steinmann ( 4. 2. 40 )	",
"3.4.47;	Sohn von aoP Bernhard Friedrich Steinmann ( 4. 2. 40 )	",
"3.2.5;	Sohn von Albrecht Friedrich Stettier, Professor am Politischen Institut Bern",
"3.1.36;	Bruder von oP Max Stooss ( 4. 1. 59 )	",
"4.1.59;	Bruder von oP Carl Stooss ( 3. 1. 36 )	",
"6.2.42;	Sohn von HonP Hans Strahm ( 6. 3. 12 )	",
"6.3.12;	Vater von aoP Christian Niklaus Ernst Strahm ( 6. 2. 43 )",
"1.4.10;	Neffe von oP H. Strasser ( 4. 1. 42 )	",
"7.1.8;	Sohn von oP Samuel Studer ( 1. 1. 2 A ), Bruder von oP Gottlieb Studer ( 1. 1. 15 ), Schwiegersohn von oP Samuel Gottlieb Hünerwa-del ( 1. 1. 5 A )",
"0.0.85;	Onkel von Professor Samuel Emanuel Studer ( Nr. 93 ), Schwiegervater von Professor Gottlieb Risold ( Nr. 90 )",
"1.1.15;	Bruder von oP Bernhard Studer ( 7. 1. 8 ), Sohn von oP Samuel Studer ( 1. 1. 2 A )	",
"0.0.93;	Vater von oP Bernhard Studer ( 7. 1. 8 ) und oP Gottlieb Studer ( 7. 1. 15 ), Neffe von Professor Daniel Ludwig Studer ( Nr. 85 )",
"7.1.17;	Sohn von oP Gottlieb Studer ( 1. 1. 15 )	",
"6.4.46;	Bruder von oP Philipp Thormann ( 3. 1. 43 )	",
"3.1.43;	Bruder von PD Franz Thormann ( 6. 4. 46 )	",
"6.4.23;	Bruder von aoP Ludwig Tobler ( 6. 2. 10 )",
"6.2.10;	Bruder von PD Adolf Tobler ( 6. 4. 23 )	",
"4.2.26;	Schwiegersohn von aoP Otto Oesterle ( 4. 2. 15 )	",
"4.3.10;	Gatte von HonP Franziska Baumgarten-Tramer ( 6. 4. 59 )	",
"4.2.1;	Vater von oP med. Samuel Albrecht Tribolet ( 4. 1. 3 A )	",
"4.2.5;	Sohn von Samuel Albrecht Tribolet, Professor der Akademie und Stadtarzt Bern ( 4. 1. 3 A )",
"4.1.3;	Vater von aoP Johann Friedrich Albrecht Tribolet ( 4. 2. 5 )	",
"4.2.10;	Sohn von oP Gabriel Gustav Valentin ( 4. 1. 13 ), Vater von PD Francis Valentin ( 4. 4. 85 )",
"4.4.85;	Sohn von aoP A. Valentin ( 4. 2. 10 )	",
"4.1.13;	Vater von aoP Adolf Valentin ( 4. 2. 10 )	",
"4.1.33;	Sohn von oP Wilhelm Philipp Friedrich Vogt ( 4. 1. 12 ), Bruder von oP Emil Vogt ( 3. 1. 19 ) und von oP Gustav Vogt ( 3. 1. 15 )	",
"3.1.19;	Sohn von oP Wilhelm Philipp Friedrich Vogt ( 4. 1. 12 ), Bruder von oP Adolf Vogt ( 4. 1. 33 ) und von oP Gustav Vogt ( 3. 1. 15 )",
"3.1.15;	Sohn von oP Wilhelm Philipp Friedrich Vogt ( 4. 1. 12 ), Bruder von oP Adolf Vogt ( 4. 1. 33 ) und von oP Emil Vogt ( 3. 1. 19 )",
"4.1.12;	Vater von oP Adolf Vogt ( 4. 1. 33 ), oP Emil Vogt ( 3. 1. 19 ) und oP Gustav Vogt ( 3. 1. 15 )",
"3.2.20;	Sohn von aoP Paul Volmar ( 6. 2. 14 )	",
"6.2.6;	Vater von aoP Paul Volmar ( 6. 2. 14 )	",
"6.2.14;	Vater von aoP Friedrich Volmar ( 3. 2. 20 ), Sohn von aoP Joseph Simeon Volmar ( 6. 2. 6 )",
"6.4.69;	Sohn von oP Eduard Fischer ( 7. 1. 23 )	",
"4.1.79;	Sohn von Titularprofessor Max Rudolf Robert Walthard ( 4. 3. 4 )",
"4.4.98;	Neffe von HonP Max Rudolf Robert Walthard ( 4. 3. 4 )	",
"0.0.78;	Schwiegervater von Professor Johannes Samuel Ith ( Nr. 88 )	",
"4.3.4;	Vater von oP Bernhard Walthard ( 4. 1. 79 ), Onkel von PD Hermann Walthard ( 4. 4. 98 )",
"4.1.53;	Schwager von oP Werner Näf ( 6. 1. 53 )	",
"4.2.36;	Sohn von oP Hans Wildbolz ( 4. 1. 72 )	",
"0.0.83;	Schwiegersohn von Professor Johann Georg Altmann ( Nr. 70 )",
"7.2.21;	Tochter von oP Philipp Woker ( 2. 1. 7 / 6. 1. 27 )",
"2.1.7;	Vater von aoP Gertrud Woker ( 7. 2. 21 )	",
"6.1.27;	Vater von aoP Gertrud Woker ( 7. 2. 21 )	",
"0.0.45;	Schwiegervater von Professor Jakob Hortin ( Nr. 63 )",
"4.1.85;	Vater von PD Klaus Zuppinger ( 4. 4. 156 )	",
"4.4.156;	Sohn von oP Adolf Zuppinger ( 4. 1. 85 )",
]

print("insert into relation (verwandtid, sentence, id_date) values")
for line in lines:
    # Extract the first ID before the semicolon
    first_id = line.split(";")[0]

    # Check if the first ID ends with an "a" and treat it as a valid ID if it does
    if re.match(r'^\d+(\.\d+)+a$', first_id):
        valid_first_id = f"'{first_id}'"  # Valid ID even if it ends with 'a'
    elif re.match(r'^\d+(\.\d+)+$', first_id):
        valid_first_id = f"'{first_id}'"  # Valid ID without the 'a'
    else:
        valid_first_id = "NULL"  # If it doesn't match, set to NULL

    # Extract the sentence after the semicolon
    sentence = line.split(";")[1]

    # Split the sentence by commas first
    sentence_parts = [part.strip() for part in sentence.split(",")]

    # Now, split the sentence parts by "und" as well
    final_parts = []
    for part in sentence_parts:
        final_parts.extend([subpart.strip() for subpart in part.split("und")])

    for part in final_parts:
        # Search for the date in the parentheses
        match = re.search(r'\(\s*(\d+)\.\s*(\d+)\.\s*(\d+)\s*\)', part)
        if match:
            id_date = f"'{match.group(1)}.{match.group(2)}.{match.group(3)}'"
        else:
            id_date = "NULL"

        # Print each value pair on a new line with the first ID, sentence part, and date
        print(f"({valid_first_id}, '{part}', {id_date}),")

# Remove the trailing comma and add the semicolon at the end
print(";")


