# BMAT Library

## BMAT library’s Structure

The library is divided into two different modules to make simple and clean adding new code and functionalities in the 
future. 

-	data_persistence: module for CRUD-ing functions, thinking in new possible DBs.
    - mongodb.py
        - MongoDB
        - insert_many(data)
        - get_by_iswc(data)

-	data_sources: module for extract and transform different data sources.
    - csv_source.py (for csv_files)
        - CsvSourceType1 (db_works_test.csv type)
            - transform_to_list_dict()
            - save_to_file_as_dict(path_output)
            - check_consistency()
    - aux_functions.py (auxiliary functions for all data sources)
        - clean_string_iswc(iswc)

Also, three main files have been created:
1.	main_etl: Extract, transform and load db_works_test.csv info into mongodb database 
      (db=bmat, collection=musicalworks, location=localhost:27017) as required.
2.	main_get_owners: get right owners according iswc data (from bmat db and musicalworks collection)
3.	main_flask_server: initialize a server (127.0.0.1:5001) for querying right owners data using HTTP GET requests 
      (from bmat db and musicalworks collection).


## Running the code

Pipenv library has been used to generate an environment.
0.	For installing pipenv: pip install pipenv
1.	pipenv install (inside bmat folder)
2.	pipenv shell (for activating the environment)
3.	python main_etl (for assignment part1)
4.	python main_get_owners (for assignment part2)
5.	python main_flask_server (for assignment part2)
