class RelatedMixin:

    request = None,
    quesyset = None
    serializer = None

    def related_serialized_data(self) -> list:
        serialized = self.serializer(
            self.queryset, many=True, context={"request": self.request}
        )
        return serialized.data
