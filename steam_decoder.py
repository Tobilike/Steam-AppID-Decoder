#!/usr/bin/env python3
import argparse
import os
import pathlib


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Die Steam appid mit den Spielenamen auslesen"
    )

    parser.add_argument(
        "-V", "--version",
        action="version",
        version="%(prog)s 1.0",
        help="Zeige Versionsinformationen"
    )

    parser.add_argument(
        "datapath",
        type=pathlib.Path,
        nargs="?",
        default=pathlib.Path.cwd(),
        help="Den Path benutzen"
    )

    return parser.parse_args()


def lese_Datein(abs_path):

    anzahl = 0

    print("\n--- DEINE STEAM SPIELE-LISTE ---")
    print(f"{'  ORDNER-NUMMER'}   |   {'SPIELNAME'}")
    print("-" * 50)

    for file in os.listdir(abs_path):
        if file.endswith(".acf"):
            selected_file = f"{abs_path}/{file}"
            current_open_file = open(selected_file)
            try:
                file_content = current_open_file.readlines()
                # Get file Information
                name_of_game = None
                appID = None
                check = file_content[0]

                for line in file_content:
                    parts = line.split('"')
                    if len(parts) >= 4:
                        key = parts[1]  # Das ist z.B. 'name' oder 'appid'
                        value = parts[3]  # Das ist der eigentliche Text dazwischen!

                        if key == "name":
                            name_of_game = value
                        elif key == "appid":
                            appID = value

                if "AppState" not in check:
                    print(f"Die Datei {file} ist ungültig")
                    print("")
                else:
                    print(f"        {appID:<9} ->    {name_of_game}")
                    anzahl = anzahl + 1


            except:
                print(f"Die Datei {file} ist ungültig")
                print("")
            finally:
                current_open_file.close()

    print("-" * 50)
    if anzahl == 0:
        print("Es wurden keine gültige .acf Dateien gefunden.")
        print("Versuche es mit den help command")
    else:
        print(f"Erfolgreich {anzahl} Spiele zugeordnet.\n")


def main(args):
    abs_path = args.datapath.resolve()
    lese_Datein(abs_path)


if __name__ == '__main__':
    args = parse_arguments()
    main(args)
