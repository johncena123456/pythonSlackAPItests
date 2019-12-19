from Base_Request import BaseApiOperations


class Slack_Channel_Operations(BaseApiOperations):

    # This function takes list of channels and return value of key searched for based on channel name
    def get_value_from_channel_list(self, channel_list, name_of_channel):
        for channel in channel_list["channels"]:
            if channel["name"] == name_of_channel.lower():
                return channel

    def get_channel_id_from_name(self, name):
        channel_list = self.get_channel_list()
        return self.get_value_from_channel_list(channel_list, name)['id']

    def get_channel_archived_status_name(self, name):
        channel_list = self.get_channel_list()
        return self.get_value_from_channel_list(channel_list, name)['is_archived']

    def get_channel_list(self):
        operation_name = "channels.list"
        response = self.get_call(operation_name, {})
        assert response['ok'] is True
        return response

    def create_channel(self, name):
        operation_name = "channels.create"
        self.post_call(operation_name, {"name": name})

    def rename_channel(self, name, new_name):
        operation_name = "channels.rename"
        channel_id = self.get_channel_id_from_name(name)
        self.post_call(operation_name, {"channel": channel_id, "name": new_name})

    def archive_channel(self, name):
        operation_name = "channels.archive"
        channel_id = self.get_channel_id_from_name(name)
        self.post_call(operation_name, {"channel": channel_id})

    def unarchive_channel(self, name):
        operation_name = "channels.unarchive"
        channel_id = self.get_channel_id_from_name(name)
        self.post_call(operation_name, {"channel": channel_id})
