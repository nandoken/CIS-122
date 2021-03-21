__author__ = 'Fernando Ames'


# This program changes backwards a txt file

# Input Lists: input_file
# Output Lists: output_file

#  Function read_and_write_file(Integer input_file, Integer output_file)
#       Declare Integer input_file
#       Declare Integer Array input_lists []
#       Declare Integer Array output_lists []
#
#       for line in input_file:
#           Set input_list.append(line)
#       input_file.close()
#       End Loop
#
#      for i in range(0, len(input_list)):
#          if i == 0:
#             Set output_list.append(input_list[len(input_list) - 1 - i] + "\n")
#          else:
#              Set output_list.append(input_list[len(input_list) - 1 - i])
#      output_file = open(output_file, "w+")
#      End Loop
#
#      for i in range(0, len(output_list)):
#          Set output_file.write(output_list[i])
#      output_file.close()
#      End Loop
#
#  Module main():
#   input_file = "Lorem_Ipsum.txt"
#   output_file = "Lorem_Ipsum_Backward.txt"
#   read_and_write_file(input_file, output_file)


def read_and_write_file(input_file, output_file):
    input_file = open(input_file)
    input_list = []
    output_list = []

    for line in input_file:
        input_list.append(line)
    input_file.close()

    for i in range(0, len(input_list)):
        if i == 0:
            output_list.append(input_list[len(input_list) - 1 - i] + "\n")
        else:
            output_list.append(input_list[len(input_list) - 1 - i])

    output_file = open(output_file, "w+")

    for i in range(0, len(output_list)):
        output_file.write(output_list[i])
    output_file.close()


def main():
    input_file = "Lorem_Ipsum.txt"
    output_file = "Lorem_Ipsum_Backward.txt"
    read_and_write_file(input_file, output_file)


if __name__ == "__main__":
    main()
