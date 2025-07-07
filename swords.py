import argparse
import tempfile
import os

    
def main():
    parser = argparse.ArgumentParser(description="Wordlist Generator")
    parser.add_argument("--wlist1",required=False, type=str, help="Wordlist 1")
    parser.add_argument("--wlist2",required=False, type=str, help="Wordlist 2")
    parser.add_argument("--wlist3",required=False, type=str, help="Wordlist 3")
    parser.add_argument("--separator1",required=False, type=str, help="First separator")
    parser.add_argument("--separator2",required=False, type=str, help="Second separator")


    args = parser.parse_args()

    wlists = []
    if args.wlist1:
        wlists.append(args.wlist1)
    if args.wlist2:
        wlists.append(args.wlist2)
    if args.wlist3:
        wlists.append(args.wlist3)

    separator1 = args.separator1 if args.separator1 else ""
    separator2 = args.separator2 if args.separator2 else ""
    if len(wlists)>=2:
        tfile = tempfile.TemporaryFile()
        f1 = open(wlists[0], 'r')
        f2 = open(wlists[1], 'r')
        f3 = open(tfile.name if len(wlists)==2 else wlists[2], 'r') #This is not ugly, you're ugly ok?
        wlist1_lines = f1.readlines()
        wlist2_lines = f2.readlines()
        wlist3_lines = f3.readlines()

        if not wlist3_lines:
            wlist3_lines.append("")
        for line_1 in wlist1_lines:
            for line_2 in wlist2_lines:
                    for line_3 in wlist3_lines:
                        print(f"{line_1.strip("\n")}{separator1}{line_2.strip("\n")}{separator2}{line_3.strip("\n")}")
               
        f1.close()
        f2.close()
        f3.close()

if __name__ == "__main__":
    main()