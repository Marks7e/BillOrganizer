from datetime import datetime
import os
import time

class IOServices:

    def __init__(self,base_path_bill_holder ,base_path_saving ):
        self.base_path_saving = base_path_saving
        self.base_path_bill_holder = base_path_bill_holder
        self.bill_folder_name = ""
        self.datetime_format = "%d/%m/%Y %H:%M:%S"
        self.execution_datetime = datetime.now().strftime(self.datetime_format)
    
    def process_start_header(self):
        print()
        print("Bill Organizer - v 1.0.0.")
        print("Execution time: ",self.execution_datetime,".")
        print("Base PATH for organize bills: ", self.base_path_saving,".")
        print("Base PATH where bills will be holding: ",self.base_path_bill_holder,".")
        print()

    def get_count_of_new_files(self):
        print()
        self.files = os.listdir(self.base_path_bill_holder)
        print(len(self.files)," new file/s found/s.")
    
    def get_creation_date_for_each_bill(self):
        for file in self.files:
            absolute_path_for_file = os.path.join(self.base_path_bill_holder,file)
            creation_date_for_file = time.strftime(self.datetime_format, time.localtime(os.path.getctime(absolute_path_for_file)))
            print(file," || created at: ",creation_date_for_file)

