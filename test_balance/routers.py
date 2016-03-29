class MasterRouter(object):
    def __init__(self, app_label):
        super(MasterRouter, self).__init__()
        self.app_label = app_label

    def db_for_read(self, model, **hints):
        if model._meta.app_label == self.app_label:
            return self.app_label
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == self.app_label:
            return self.app_label
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == self.app_label or obj2._meta.app_label == self.app_label:
            return True
        return None

    def allow_syncdb(self, db, model):
        if db == 'default':
            return model._meta.app_label == self.app_label
        elif model._meta.app_label == self.app_label:
            return False
        return None


class TBRouter(MasterRouter):
    def __init__(self):
        super(TBRouter, self).__init__('test_balance')

