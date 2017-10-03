class hoge(object):

    target = {}

    def __init__(self):

        #self.target = {}

        pass



    def append(self, val, key):

        if self.target.has_key(key):

            self.target[key] = self.target[key] + val

        else:

            self.target[key] = val



if __name__ == '__main__':

    key = "conflict"
    a = hoge()

    a.append(1, key)
    print("{0}".format(a.target[key]))

    b = hoge()

    b.append(1, key)

    print("{0}".format(b.target[key]))