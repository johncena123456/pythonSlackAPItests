from Slack_Channel_Operations import Slack_Channel_Operations
import random


class Test_Slack_Methods:
    slack = Slack_Channel_Operations()

    NEW_CHANNEL_NAME = ''.join(random.choice('ABCDSFGEHIJK123456') for i in range(5))
    RENAMED_CHANNEL_NAME = ''.join(random.choice('ABCDSFGEHIJK123456') for i in range(5))

    def test_slack_get_list(self):
        self._verify_response_ok(self.slack.get_channel_list())

    def test_slack_create(self):
        self._verify_response_ok(self.slack.create_channel(self.NEW_CHANNEL_NAME))

    def test_slack_rename(self):
        self._verify_response_ok(self.slack.rename_channel(self.NEW_CHANNEL_NAME, self.RENAMED_CHANNEL_NAME))

    def test_slack_archive(self):
        self._verify_response_ok(self.slack.archive_channel(self.RENAMED_CHANNEL_NAME))
        assert self.slack.verify_is_channel_archived(self.RENAMED_CHANNEL_NAME) is True, "Failed to archive Channel"

    def test_slack_unarchive(self):
        self._verify_response_ok(self.slack.unarchive_channel(self.RENAMED_CHANNEL_NAME))
        assert self.slack.verify_is_channel_archived(self.RENAMED_CHANNEL_NAME) is False, "Failed to Unarchive Channel"

    def _verify_response_ok(self, response):
        assert response['ok'] is True, "Request failed due to %s" % response['error'] 
