import datetime
import glob
import os

publishables = glob.glob(os.path.join("drafts", "done", "*.rst"))

year = "%d" % datetime.datetime.now().year
month = "%02d" % datetime.datetime.now().month
day = "%02d" % datetime.datetime.now().day


def main():
    acc = []
    for i in ["articles", year, month, day]:
        acc.append(i)
        try:
            os.mkdir(os.path.join(*acc))
        except FileExistsError:
            pass

    for pub in publishables:
        bn = os.path.basename(pub)
        os.rename(pub,os.path.join(*acc, bn))
        print(".")


if __name__ == "__main__":
    main()
