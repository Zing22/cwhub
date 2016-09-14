# -*- coding:utf-8 -*-

def main():
    time = str(input("Time:"))
    while True:
        name = str(input("Name:").strip())
        link = str(input("Link:").strip())
        size = str(input("Size:").strip())

        print ("""
          <div class="item">
            <hr>
            <h3>
              %s
            </h3>
            <p>
              Download: <a href="%s" target="_blank">Click link</a><br>
              Size: %s<br>
              Update: %s
            </p>
          </div>""" % (name, link, size, time))

if __name__ == '__main__':
    main()