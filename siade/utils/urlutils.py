from django.conf.urls import url

actions_urls = {
    'listar': r'^$',
    'adicionar': r'^adicionar/$',
    'detalhes': r'^(?P<pk>\d+)/$',
    'editar': r'^(?P<pk>\d+)/editar$',
    'excluir': r'^(?P<pk>\d+)/excluir$',
}


def get_view_urls(actions, model_name):
    sub_urls = []
    for action, view in actions.iteritems():
        if action in actions_urls.keys():
            sub_urls += [url(actions_urls[action], view,
                             name='%s-%s' % (model_name, action))]
    return sub_urls
