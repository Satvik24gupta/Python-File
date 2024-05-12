def convert_format(input_file, output_file):
    try:
        with open(input_file, 'r') as f_i:
            lines = f_i.readlines()
            with open(output_file, 'w') as f_o:
                for line in lines:
                    data = line.strip().split(',')
                    formatted_data = '\t\t'.join(data) + '\n'
                    f_o.write(formatted_data)
        print("Conversion successful!")
    except FileNotFoundError:
        print("Input file not found!")
    except Exception as e:
        print("An error occurred:", e)
 
input_file = "Prog14_input.csv"
output_file = "Prog14_output.xt"
print()
convert_format(input_file, output_file)
print()
print()