import sys
import io
def hextostring(w_file,r_file):
    hex = ""
    trim_str = ""
    str = ""
    b_str = ""
    with open(r_file,'r+',4096) as f:
        for i in f.read():
            hex += i
    trim_str=hex.split(" ")
    print(trim_str)
    for i in trim_str:
        str +=chr(int(i,16))
    print(str)
    with open(w_file,'wb',4096) as f:
        buf=io.BufferedWriter(f)
        b_str=bytes(str,encoding='utf-8')
        buf.write(b_str)
        buf.flush()
if __name__ == '__main__':
    print(len(sys.argv))
    if len(sys.argv) != 3:
        sys.stderr.write("[-]Usage: python3 %s <read-file> <write-file>\n" % sys.argv[0])
        sys.exit(1)
    r_file = sys.argv[1]
    w_file = sys.argv[2]
    hextostring(w_file,r_file)
