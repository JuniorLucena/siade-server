# -*- coding: utf-8 -*-
from django.apps import AppConfig, apps as djapps
from django.db.models.signals import post_migrate
from sitetree.utils import get_tree_model, get_tree_item_model


def create_main_tree(sender, **kwargs):
    Tree = get_tree_model()
    TreeItem = get_tree_item_model()
    main, c = Tree.objects.get_or_create(title='Menu principal', alias='main')
    TreeItem.objects.get_or_create(title='Início', url='home', alias='home',
                                   urlaspattern=True, inmenu=True,
                                   insitetree=True, tree=main)


class BaseConfig(AppConfig):
    name = 'siade.base'

    def ready(self):
        post_migrate.connect(create_main_tree,
                             sender=djapps.get_app_config('sitetree'),
                             dispatch_uid="siade.base.post_migrate")
