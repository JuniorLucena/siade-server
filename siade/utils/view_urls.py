from django.conf.urls import url, include

default_actions_urls = {
    'listar': r'^$',
    'adicionar': r'^adicionar/$',
    'detalhes': r'^(?P<pk>\d+)/$',
    'editar': r'^(?P<pk>\d+)/editar$',
    'excluir': r'^(?P<pk>\d+)/excluir$',
}


class ViewUrlRegistry(object):
    def __init__(self):
        self._registry = {}

    def register_action(self, model, action, view, url=None):
        if not url and action in default_actions_urls.keys():
            url = default_actions_urls[action]
        if url:
            if model in self._registry.keys():
                self._registry[model] += [(action, view, url)]
            else:
                self._registry[model] = [(action, view, url)]

    def register_actions(self, *args):
        model = args[0]
        actions = args[1:]
        for arg in actions:
            if len(arg) > 2:
                action, view, map_url = arg
            else:
                action, view = arg
                map_url = None
            self.register_action(model, action, view, map_url)

    def get_urls_for_model(self, model_name):
        model_name = model_name.lower()
        actions = self._registry[model_name]
        sub_urls = []
        for action, view, urls in actions:
            if isinstance(urls, basestring):
                urls = [urls]

            for map_url in urls:
                sub_urls += [url(map_url, view,
                                 name='%s-%s' % (model_name, action))]
        return sub_urls

registry = ViewUrlRegistry()
