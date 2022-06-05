from rest_framework import viewsets, mixins


class ReadCreateViewSet(viewsets.ReadOnlyModelViewSet,
                        mixins.CreateModelMixin):
    pass
