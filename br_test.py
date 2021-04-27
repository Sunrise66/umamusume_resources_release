import brotli as br


def do_compress():
    with open('master.mdb', 'rb') as mdb:
        strs = mdb.read()
        cstr = br.compress(strs)
        with open('master.mdb.br', 'wb+') as bmdb:
            bmdb.write(cstr)
            print('done')


def do_decompress():
    with open('master.mdb.br', 'rb') as f:
        ors = f.read()
        with open('test.mdb', 'wb+') as w:
            ss = br.decompress(ors)
            w.write(ss)
            print('done')


if __name__ == '__main__':
    # do_compress()
    do_decompress()
