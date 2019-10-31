

class GraphJobs(object):

    def __init__(self, nodes):
        self.nodes = nodes

    def jobtime_recursively_on_offspring(self, node, path=[], total_job_time=0):
        """This function will return job_time of children of node recursively"""
        if node is None:
            return 0
        path += [node['id']]
        total_job_time += node['job_time']
        for child_id in node['childJobIDs']:
            if child_id not in path:
                total_job_time =\
                    self.jobtime_recursively_on_offspring(self.nodes[child_id],
                                                          path, total_job_time)

        return total_job_time


    def job_time_id(self, id):
        """Function will check if id exist in structure of nodes"""
        if self.nodes and id in self.nodes:
            return self.jobtime_recursively_on_offspring(self.nodes[id])

        return None


