# Import any dependencies needed to execute sql queries
# YOUR CODE HERE
from sql_execution import QueryMixin
from sqlite3 import connect
from pathlib import Path
from functools import wraps
import pandas as pd


# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
# YOUR CODE HERE
class QueryBase:
    # Create a class attribute called `name`
    # set the attribute to an empty string
    # YOUR CODE HERE
    name = ""
    # Define a `names` method that receives
    # no passed arguments
    # YOUR CODE HERE
    def names():
        return []
        # Return an empty list
        # YOUR CODE HERE


    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    # YOUR CODE HERE
    def event_counts(self, id):
        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        # YOUR CODE HERE
        tab = "employee_events"
        query1  = f"SELECT SUM({tab}.positive_events) SUM({tab}.negative_events) FROM {table} INNER JOIN employees_event ON {table}.{table}_id={tab}.{table}_id WHERE {tab}.{table}_id={id} ORDER BY {tab}.event_date"
        df_response = pandas_query(query1)
        return(df_response)

            
    

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    # YOUR CODE HERE
    def notes(self, id):

        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        # YOUR CODE HERE
        n = "note"
        nd = "note_date"
        tab = "notes"
        query2 = f"SELECT {tab}.{nd}, {tab}.{n} FROM {tab} WHERE {tab}.{name}_id={id}"
        df = pandas_query(query2)
        return(df)

