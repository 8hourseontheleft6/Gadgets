from extract_music import course
import time


def main():
    time.sleep(1)
    print("-Welcome Using Gadgets 0.1!-")
    time.sleep(1)
    print("-One Service-")
    print("-1.Extract Music-")
    a = input("Be Ready To Enter The Program?\n(Y=Yes   Other Key=No):")
    a = a.upper()
    if a == 'Y':
        course()
    else:
        print("-Thanks For Using-")

if __name__ == "__main__":
    main()
