import unittest
from graph_jobs import GraphJobs

# Structure gave
nodes = {
    1: {'id': 1, 'job_time': 30, 'childJobIDs': [2, 4]},
    2: {'id': 2, 'job_time': 10, 'childJobIDs': [3]},
    4: {'id': 4, 'job_time': 60, 'childJobIDs': []},
    3: {'id': 3, 'job_time': 20, 'childJobIDs': []},

}
# Structure modified to test
nodes_2 = {
    1: {'id': 1, 'job_time': 30, 'childJobIDs': [2, 4, 5]},
    2: {'id': 2, 'job_time': 10, 'childJobIDs': [3]},
    4: {'id': 4, 'job_time': 60, 'childJobIDs': []},
    3: {'id': 3, 'job_time': 20, 'childJobIDs': []},
    5: {'id': 5, 'job_time': 12, 'childJobIDs': []},

}

class TestJobTime(unittest.TestCase):


    def setUp(self):
        self.GraphJobs = GraphJobs(nodes)


    def test_return_job_duration_single_job(self):
        """
        Test just a single job's duration without any dependencies
        """
        result = self.GraphJobs.job_time_id(4)
        self.assertEqual(result, 60)

    def test_return_job_duration_single_job(self):
        """
        Test just a single job's duration without any dependencies
        """
        result = self.GraphJobs.jobtime_recursively_on_offspring(nodes[4], [], 0)
        self.assertEqual(result, 60)

    def test_return_job_duration_dependencies(self):
        """
        Test job's duration with some children dependencies
        """
        result = self.GraphJobs.jobtime_recursively_on_offspring(nodes[2], [], 0)
        self.assertEqual(result, 30)


    def test_return_job_duration_dependencies_of_head(self):
        """
        Test job's duration with some children dependencies
        """
        result = self.GraphJobs.jobtime_recursively_on_offspring(nodes[1], [], 0)
        self.assertEqual(result, 120)

    def test_return_job_time_of_children(self):
        """
        Test that it can job's duration of children recursively of nodes if
        it has 3 children
        """
        self.GraphJobs = GraphJobs(nodes_2)
        result = self.GraphJobs.jobtime_recursively_on_offspring(nodes_2[1], [], 0)
        self.assertEqual(result, 132)

    def test_node_is_none(self):
        """
        Test  if function will return None if node is None
        """
        self.GraphJobs = GraphJobs(None)
        result = self.GraphJobs.job_time_id(1)
        self.assertEqual(result, None)

    def test_if_id_is_node(self):
        """
        Test if function will return None if id is node
        3 children
        """
        result = self.GraphJobs.job_time_id(None)
        self.assertEqual(result, None)


    def test_if_job_doesnt_exist(self):
        """
        Test if function will return None id doesn't exist
        """
        result = self.GraphJobs.job_time_id(9)
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()