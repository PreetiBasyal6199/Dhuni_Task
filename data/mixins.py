class DynamicSerializerClassMixin(object):
    serializer_action_classes = {}
    """

    the child classinheriting this mixin should have variable 'serializer_action_classes'
    with the data type dictionary i.e.{'key': 'value'}
    key => actions (list, retrieve, etc)
    value => serializer class

    """

    def get_serializer_class(self):
        return self.serializer_action_classes.get(self.request.method, super().get_serializer_class())