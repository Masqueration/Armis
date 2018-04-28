import getopt
import sys

import Test as T

SLEEP = 5


def main(argv):
    page, password, user = '', '', ''
    h_str = 'Armis.py -u <username> -p <password> -w <url>'
    try:
        opts, args = getopt.getopt(argv, "hw:u:p:", ["help", "url=", "user=", "pass="])
    except getopt.GetoptError:
        print h_str
        sys.exit(2)
    if len(opts) != 3:
        print h_str
        sys.exit()
    for opt, arg in opts:
        if opt == '-h':
            print h_str
            sys.exit()
        elif opt in ("-u", "--user"):
            user = arg
        elif opt in ("-p", "--pass"):
            password = arg
        elif opt in ("-w", "--url"):
            page = arg
    test = T.Test(page, user, password)
    test.test_login()
    test.test_playlists()


if __name__ == "__main__":
    main(sys.argv[1:])
    #test = T.Test("https://www.orfium.com/", "Homework", "Armis1234")
    #test.test_login()
    #test.test_playlists()


# python Armis.py -p "Armis1234" -w "https://www.orfium.com/" -u "Homework"


