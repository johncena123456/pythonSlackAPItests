from Base_Request import BaseApiOperations


class Slack_Channel_Operations(BaseApiOperations):
    CHANNEL_LIST = "channels.list"
    CHANNEL_CREATE = "channels.create"
    CHANNEL_RENAME = "channels.rename"
    CHANNEL_ARCHIVE = "channels.archive"
    CHANNEL_UNARCHIVE = "channels.unarchive"

    def get_channel_list(self):
        response = self.get_call(self.CHANNEL_LIST, {})
        assert response['ok'] is True
        return response

    def create_channel(self, name):
        response = self.post_call(self.CHANNEL_CREATE, {"name": name})
        return response

    def rename_channel(self, name, new_name):
        channel_id = self.__get_channel_id_from_name(name)
        response = self.post_call(self.CHANNEL_RENAME, {"channel": channel_id, "name": new_name})
        return response

    def archive_channel(self, name):
        channel_id = self.__get_channel_id_from_name(name)
        response = self.post_call(self.CHANNEL_ARCHIVE, {"channel": channel_id})
        return response

    def verify_is_channel_archived(self, name):
        return  self.__get_channel_archived_status_name(name)

    def unarchive_channel(self, name):
        channel_id = self.__get_channel_id_from_name(name)
        response = self.post_call(self.CHANNEL_UNARCHIVE, {"channel": channel_id})
        return response

# Private Methods
    # This function takes list of channels and return value of key searched for based on channel name
    def __get_value_from_channel_list(self, channel_list, name_of_channel):
        for channel in channel_list["channels"]:
            if channel["name"] == name_of_channel.lower():
                return channel

    def __get_channel_id_from_name(self, name):
        channel_list = self.get_channel_list()
        return self.__get_value_from_channel_list(channel_list, name)['id']

    def __get_channel_archived_status_name(self, name):
        channel_list = self.get_channel_list()
        return self.__get_value_from_channel_list(channel_list, name)['is_archived']
