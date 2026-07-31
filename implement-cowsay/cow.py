import argparse
import sys
import cowsay

def main():
    available_chars = sorted(cowsay.char_names)

    parser = argparse.ArgumentParser(
        description = "A CLI tool that makes ASCII characters speak!"
    )

    parser.add_argument(
        "message",
        help = "The message for the character to speak."
    )

    parser.add_argument(
        "-c","--character",
        choices= available_chars,
        default = "cow",
        help ="Choose a character (default:cow)"

    )

    args = parser.parse_args()

    try:
        print(cowsay.get_output_string(args.character, args.message))
    except KeyError:
        print (f"Error : Character '{args.character}' not found.")

if __name__ == "__main__":
    main()