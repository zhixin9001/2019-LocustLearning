from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        print('on_start')
    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        print('on_stop')
    @task(1)
    def index(self):
        self.client.get("/")

    @task(1)
    def index(self):
        self.client.get("/")
    # @task(2)
    # def about(self):
    #     self.client.get("/about")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000