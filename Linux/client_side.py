from SshToServer import SshToServer
import pandas as pd
import os
import ast


def main():
    my_ssh = SshToServer(r"C:\Users\Max\Downloads\my-key-pair.pem", "13.53.182.127", "ubuntu")
    stdout,stderr = my_ssh.runRemoteCommand("python3 server_side.py")

    try:
        clean_output = stdout.strip()
        data_dict = ast.literal_eval(clean_output)

        append_to_csv(r"C:\Users\Max\PycharmProjects\OperatingSystems\Linux\log_results.csv", data_dict)
        print("Data successfully appended.")
    except(ValueError,SyntaxError):
        print("Error: The server output was not a valid dictionary.")
        print("Received: " + stdout)



def append_to_csv(file_path,data):
    new_file = pd.DataFrame([data])
    if os.path.exists(file_path):
        exist_file = pd.read_csv(file_path)
        combine_file = pd.concat([exist_file,new_file])
    else:
        combine_file = new_file
    combine_file.to_csv(file_path,index=False)

if __name__ == "__main__":
    main()