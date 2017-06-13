from st2actions.runners.pythonrunner import Action


class GetConfig(Action):

    def __init__(self, config):
        super(GetConfig, self).__init__(config)

    def run(self, **kwargs):
        key = kwargs['key']
        return self.config[key]
