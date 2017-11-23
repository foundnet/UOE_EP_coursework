#!/usr/bin/python

import sys
import math
import getopt


# After comparing the string hash functions, do select
# the BKDRHash due to its good performance, balanced 
# distribution and easy implementation
def BKDRHash(in_bit,str_in):
    key = 0
    seed = 131

    for index in range(0 , len(str_in)):
        key = key * seed + ord(str_in[index])
    key = key % in_bit

    return key
# Check the particular position of biti vector, the bit_offset is from 0 to m-1
# return 1 represent this bit is setted, 0 represent not yet.
def check_vector(bit_offset,vector):
    if bit_offset < 0:
        raise Exception("Wrong bit offset value when check, should be a positive number!")

    index = int(bit_offset / 8)
    shift = bit_offset % 8
    item = vector[index]
    mask = 1 << shift
    item = item & mask
    if item > 0 :  return 1
    else:
        return 0
# Set the particular position of the bit vector
def set_vector(bit_offset,vector):
    if bit_offset < 0:
        raise Exception("Wrong bit offset value when set, should be a positive number!")

    index = int(bit_offset / 8)
    shift = bit_offset % 8
    item = vector[index]
    mask = 1 << shift
    item = item | mask
    vector[index] = item
 
# The main function to finish the bloom filter by the input
# parameters 
def main(argv):
    src_file = ""
    dest_file = ""
    src_io = sys.stdin
    dest_io = sys.stdout

    opt = ""
    in_opt = ""
    n_lines = 0
 
# Read parameters from command line
    try:
        opts, args = getopt.getopt(argv,"i:n:o:")
        for opt, arg in opts:
            if opt == "-i":
                src_file = arg
                src_io = open(src_file)
                n_lines = len(src_io.readlines())
                src_io.seek(0)
                in_opt = opt
            elif opt == "-n":
                n_lines = int(arg)
                if in_opt == "-i" : src_io.close()
                src_io = sys.stdin
                in_opt = opt
            elif opt == "-o":
                dest_file = arg
                dest_io = open(dest_file,"w")
            else:
                raise Exception("Invalid parameter!")
        
        if in_opt == "":  raise Exception("Should input -i or -n.")

# Calculate the suitable number of hash functions and suitable 
# cnumber of vecter bits
        p_falsepos = 0.01
        m_bitscnt = int(math.ceil(n_lines * math.log10(1/p_falsepos) / math.log10(2) / math.log(2)))
        k_hashcnt = int(math.ceil(math.log(2) * m_bitscnt / n_lines ))

        bit_vector = bytearray(int(math.ceil(m_bitscnt/8)) + 1)
        cur_line = ""

        dup_cnt = 0
        val_cnt = 1
        total_cnt = 1
        seq_num = 0

        for line in src_io:
            line = line.strip()
            cur_line = line
            if line == "":  
                total_cnt += 1
                continue

            if val_cnt > n_lines:  
                break

            is_newline = False
            for index in range(0,k_hashcnt):
                line = line + "LOVE EXC COURSE!"
                hash_key = BKDRHash(m_bitscnt,line)
                if is_newline == False:
                    if check_vector(hash_key , bit_vector) == 0:
                        is_newline = True
                if is_newline == True:
                    set_vector(hash_key , bit_vector)

            if is_newline :
                seq_num += 1
                dest_io.write(cur_line + "\n")
            else :
                dup_cnt += 1

            sys.stdout.write("[" + ">"*int(50*val_cnt/n_lines)    + ">"      \
                                 + " "*int(50-50*val_cnt/n_lines) + "]["     \
                                 +     str(val_cnt)               + "/"      \
                                 +     str(n_lines)               + "]\r")
            val_cnt += 1
            total_cnt += 1

#       print "\n\n--------------------VECTOR:----------------------------\n--0x%x"%(bit_vector)
        print "\n----K HASH_COUNT: " + str(k_hashcnt)   + \
              "   M VECTOR_BITS_CNT: " + str(m_bitscnt)   + \
              "  N EXPECTED_LINE_CNT: "+ str(n_lines)
        print "\n----CHECKED LINES: "  + str(total_cnt-1) + \
              "  VALID_LINES: "        + str(val_cnt-1)   + \
              "  DUP LINES: "          + str(dup_cnt)

        return 1

    except Exception as e:
        print "Error: " + e.message
        print "Usage: ./bloomfilter_old.py -i <inputfile> -n number_of_lines -o <outputfile>"
        print "    -i:Read the given input file, count the number of lines automatically."
        print "    -n:Read the top n lines from stdin."
        print "    -o:Identify the output file or the lines will be printed to stdout."
        print "If both -i and -n parameters are inputed, the last one will be effective."
        return 0
    finally :
        src_io.close()

# Calculate the suitable bit vector length and the number
# of hash functions. 
if __name__ == "__main__":
   main(sys.argv[1:])    

