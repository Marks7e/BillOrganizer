import IOServices

Test = IOServices.IOServices("/home/marks/Documents/BaseBill","/home/marks/Documents/BillOrganizer")
Test.process_start_header()
Test.get_count_of_new_files()
Test.get_creation_date_for_each_bill()