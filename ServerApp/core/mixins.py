class CollectionResourceMixine:
    """Mixin class provides a method for combining
        the list of data and the number of data counts.
    """

    model_name = None

    def resource_as_collection(self, obj) -> dict:
        """The data combining."""
        return {
            "count": len(obj.data),
            self.model_name: obj.data
        }
