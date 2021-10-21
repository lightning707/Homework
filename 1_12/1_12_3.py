CHANNELS = ["BBC", "Discovery", "TV1000"]


class TvController:
    def __init__(self, channels):
        self.channel_id = 0
        self.channels = channels
        self.channel = self.channels[self.channel_id]

    def update_channel(self):
        self.channel = self.channels[self.channel_id]

    def first_channel(self):
        self.channel_id = 0
        self.update_channel()
        return self.channel

    def last_channel(self):
        self.channel_id = len(self.channels) - 1
        self.update_channel()
        return self.channel

    def turn_channel(self, turn_id):
        if turn_id - 1 in range(len(self.channels)):
            self.channel_id = turn_id - 1
        else:
            print("Channel doesn't exist")
        self.update_channel()
        return self.channel

    def next_channel(self):
        if self.channel_id < len(self.channels) - 1:
            self.channel_id += 1
        else:
            self.channel_id = 0
        self.update_channel()
        return self.channel

    def previous_channel(self):
        if self.channel_id > 0:
            self.channel_id -= 1
        else:
            self.channel_id = len(self.channels) - 1
        self.update_channel()
        return self.channel

    def current_channel(self):
        return self.channel

    def is_exist_n(self, n):
        if n - 1 in range(len(self.channels)):
            return "Yes"
        else:
            return "No"

    def is_exist_name(self, name):
        if name in self.channels:
            return "Yes"
        else:
            return "No"


controller = TvController(CHANNELS)
print(controller.first_channel() == "BBC",
      controller.last_channel() == "TV1000",
      controller.turn_channel(1) == "BBC",
      controller.next_channel() == "Discovery",
      controller.previous_channel() == "BBC",
      controller.current_channel() == "BBC",
      controller.is_exist_n(4) == "No",
      controller.is_exist_name("BBC") == "Yes")
