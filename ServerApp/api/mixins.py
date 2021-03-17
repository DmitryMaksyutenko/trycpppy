class RelatedMixin:
    """The class provides a retrieving of the related modeldata."""

    request = None,
    quesyset = None
    serializer = None

    def related_serialized_data(self) -> list:
        """Returns the data from the serialized."""
        serialized = self.serializer(
            self.queryset, many=True, context={"request": self.request}
        )
        return serialized.data
