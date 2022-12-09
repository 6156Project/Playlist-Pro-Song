from resources.base_resource import BaseResource


class SongsResource(BaseResource):

    def __init__(self, config):
        super().__init__(config)
        self.data_service = None

    def get_full_collection_name(self):
        return self.config.collection_name

    def get_data_service(self):
        if self.data_service is None:
            self.data_service = self.config.data_service
        return self.data_service

    def get_resource_by_id(self, id):
        pass

    def get_by_template(self,
                        relative_path=None,
                        path_parameters=None,
                        template=None,
                        field_list=None,
                        limit=None,
                        offset=None,
                        order_by=None):
        # can store sql results in value to format
        return super().get_by_template(relative_path, path_parameters, template, field_list,
                                         limit, offset, order_by)

    # should not be able to create/delete/update new songs
    def create_resource(self, resource_data):
      # check body keys are the same or ones required
        return super.create_resource(resource_data)

    def delete_resource(self, resource_data):
        pass

    def update_resource(self, id, resource_data):
        pass