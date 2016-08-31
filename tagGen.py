# -*- coding:utf-8 -*-

def main():
    time = raw_input("Time:")
    while True:
        name = raw_input("Name:").strip()
        link = raw_input("Link:").strip()
        size = raw_input("Size:").strip()

        print """
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
          </div>""" % (name, link, size, time)

if __name__ == '__main__':
    main()