from resources.base_resource import BaseResource


class SongsResource(BaseResource):

    def __init__(self, config):
        super().__init__(config)
        self.data_service = None
        self.columns = ['song_id', 'song_name', 'artist_id', 'artist_name', 'album_id', 'album_name']

    def get_full_collection_name(self):
        return self.config.collection_name

    def get_data_service(self):
        if self.data_service is None:
            self.data_service = self.config.data_service
        return self.data_service

    def get_resource_by_id(self, id):
        template = {'song_id': id}
        response = self.get_by_template(template=template)
        if response['status'] == 200:
            response['links'] = []
        return response

    def get_by_template(self,
                        relative_path=None,
                        path_parameters=None,
                        template=None,
                        field_list=None,
                        limit=None,
                        offset=None,
                        order_by=None):
        # can store sql results in value to format
        response = {'status': '', 'text':'', 'body':{}, 'links':[]}
        rsp = super().get_by_template(relative_path, path_parameters, template, field_list,
                                         limit, offset, order_by)
        if rsp:
            response['status'] = 200
            response['text'] = 'OK'
            response['body'] = rsp
        else:
            response['status'] = 404
            response['text'] = 'Resource not found.'
        return response

    # should not be able to create/delete/update new songs
    def create_resource(self, resource_data):
      # check body keys are the same or ones required
        response = {'status': '', 'text':'', 'body':{}, 'links':[]}
        if not resource_data:
            response['status'] = 400
            response['text'] = 'Empty data'
        elif not all(columns in resource_data for columns in self.columns):
            response['status'] = 400
            response['text'] = 'Missing data required'
        else:
            # check structure of song
            values = {
                'song_id': resource_data['song_id'],
                'song_name': resource_data['song_name'],
                'artist_id': resource_data['artist_id'],
                'artist_name': resource_data['artist_name'],
                'album_id': resource_data['album_id'],
                'album_name': resource_data['album_name']
            }
            rsp = super().create_resource(values)
            if rsp['status'] == 201:
                response['status'] = rsp['status']
                response['text'] = 'Resource created.' 
                response['body'] = {}
                response['links'] = [
                    {
                        "href": f"api/songs/{values['song_id']}",
                        "rel": "self",
                        "type" : "GET"
                    }
                    ]
            else:
                response['status'] = rsp['status']
                response['text'] = rsp['text']

        return response

    def delete_resource(self, resource_data):
        pass

    def update_resource(self, id, resource_data):
        pass