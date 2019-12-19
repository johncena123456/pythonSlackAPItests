from Slack_Channel_Operations import Slack_Channel_Operations
import random
class Test_Slack_Methods:
    slack = Slack_Channel_Operations()

    @classmethod
    def _get_random_alphanumeric_string(self):
        return ''.join(random.choice('ABCDSFGEHIJK123456') for i in range(5))

    def test_slack_methods(self):
        NEW_CHANNEL_NAME = self._get_random_alphanumeric_string()
        RENAMED_CHANNEL_NAME = self._get_random_alphanumeric_string()

        self.slack.get_channel_list()
        self.slack.create_channel(NEW_CHANNEL_NAME)
        self.slack.rename_channel(NEW_CHANNEL_NAME, RENAMED_CHANNEL_NAME)
        self.slack.archive_channel(RENAMED_CHANNEL_NAME)
        self.slack.unarchive_channel(RENAMED_CHANNEL_NAME)


