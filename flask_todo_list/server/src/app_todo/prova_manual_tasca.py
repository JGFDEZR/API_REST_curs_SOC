#!usr/bin/python3

import tasca

def main():
    tasca_1 = tasca.Tasca(None, "Tasca nova 1") # donde None es persistencia i "tasca nova 1" el nou titol
    tasca_2 = tasca.Tasca(None, "Tasca nova_2")
    tasca_3 = tasca.Tasca(None, "Tasca nova_3")

    print(f"{tasca_1.titol}, {tasca_1.done}")
    print(f"{tasca_2.titol}, {tasca_2.done}")
    print(f"{tasca_3.titol}, {tasca_3.done}")

if __name__ == "__main__":
    main()