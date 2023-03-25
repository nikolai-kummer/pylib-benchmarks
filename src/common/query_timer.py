# class QueryTime that takes in a maximum time and a parameter n. 
# The class has a time_function that accepts a string and returns a list of times. 
# The function loops through from k = 10^1 to k = 10^n and replaces any instance of array1 in
# the string query with array values from 1 to k.

import timeit

class QueryTimer(object):
    def __init__(self, n: int = 5, num_runs:int =1000):
        self.n = n
        self.num_runs = num_runs

    def time_function(self, query):
        times = {}
        # Loop over the sizes and execute the code templates
        for k in range(self.n+1):
            size = 10**k+1
            arr_str = ",".join(str(x) for x in range(1, size+1))
            new_query = query.replace(query[query.index("[")+1:query.index("]")], arr_str)

            # Execute the first template
            total_time1 = timeit.timeit(stmt=new_query, number=self.num_runs)
            times[size] = total_time1 / self.num_runs

        # Return the dictionary of execution times
        return times
 
